import numpy as np
# import os
import skfuzzy as fuzz
# import matplotlib.pyplot as plt
from datetime import datetime
from bson.json_util import dumps
from models.indicator import MongoDB


# entradas
wind = np.arange(0, 101, 1)
pluviometric = np.arange(0, 101, 1)
temperature = np.arange(-16, 51, 1)
humidity = np.arange(0, 101, 1)
ph = np.arange(0, 15, 1)
# Qualidade
quality = np.arange(0, 101, 1)

# Funções de pertinência
bad_wind = fuzz.trimf(wind, [16, 100, 100])
acceptable_wind = fuzz.trapmf(wind, [10, 11, 13, 18])
good_wind = fuzz.trimf(wind, [0, 5, 11])

# fig, (ax0, ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=6, figsize=(8, 9))

# ax0.plot(wind, bad_wind, 'b', linewidth=1.5, label='Bad')
# ax0.plot(wind, acceptable_wind, 'g', linewidth=1.5, label='acceptable')
# ax0.plot(wind, good_wind, 'r', linewidth=1.5, label='Good')
# ax0.set_title('wind')
# ax0.legend()

# ax0.spines['top'].set_visible(False)
# ax0.spines['right'].set_visible(False)
# ax0.get_xaxis().tick_bottom()
# ax0.get_yaxis().tick_left()

bad_pluviometric = fuzz.trimf(pluviometric, [11, 100, 100])
acceptable_pluviometric = fuzz.trapmf(pluviometric, [2, 3, 10, 14])
good_pluviometric = fuzz.trimf(pluviometric, [0, 2, 3])

# ax1.plot(pluviometric, bad_pluviometric, 'b', linewidth=1.5, label='Bad')
# ax1.plot(
#     pluviometric,
#     acceptable_pluviometric,
#     'g',
#     linewidth=1.5,
#     label='acceptable'
# )
# ax1.plot(pluviometric, good_pluviometric, 'r', linewidth=1.5, label='Good')
# ax1.set_title('pluviometric')
# ax1.legend()

# ax1.spines['top'].set_visible(False)
# ax1.spines['right'].set_visible(False)
# ax1.get_xaxis().tick_bottom()
# ax1.get_yaxis().tick_left()

low_temperature = fuzz.trimf(temperature, [-15, -15, 10])
high_temperature = fuzz.trimf(temperature, [27, 50, 50])
acceptable_temperature = fuzz.trapmf(temperature, [8, 10, 16, 17])
good_temperature = fuzz.trapmf(temperature, [16, 18, 25, 28])

# ax2.plot(temperature, low_temperature, 'b', linewidth=1.5, label='Too Low')
# ax2.plot(temperature, high_temperature, 'b', linewidth=1.5, label='Too High')
# ax2.plot(
#     temperature,
#     acceptable_temperature,
#     'g',
#     linewidth=1.5,
#     label='acceptable'
# )
# ax2.plot(temperature, good_temperature, 'r', linewidth=1.5, label='Good')
# ax2.set_title('temperature')
# ax2.legend()

# ax2.spines['top'].set_visible(False)
# ax2.spines['right'].set_visible(False)
# ax2.get_xaxis().tick_bottom()
# ax2.get_yaxis().tick_left()

bad_humidity = fuzz.trimf(humidity, [11, 100, 100])
acceptable_humidity = fuzz.trapmf(humidity, [2, 4, 10, 12])
good_humidity = fuzz.trimf(humidity, [0, 2, 3])

# ax3.plot(humidity, bad_humidity, 'b', linewidth=1.5, label='Bad')
# ax3.plot(
#     humidity,
#     acceptable_humidity,
#     'g',
#     linewidth=1.5,
#     label='acceptable'
# )
# ax3.plot(humidity, good_humidity, 'r', linewidth=1.5, label='Good')
# ax3.set_title('humidity')
# ax3.legend()

# ax3.spines['top'].set_visible(False)
# ax3.spines['right'].set_visible(False)
# ax3.get_xaxis().tick_bottom()
# ax3.get_yaxis().tick_left()

low_ph = fuzz.trimf(ph, [0, 0, 5])
high_ph = fuzz.trimf(ph, [8, 15, 15])
acceptable_ph = fuzz.trapmf(ph, [6, 7, 8, 9])
good_ph = fuzz.trapmf(ph, [4, 5, 6, 7])

# ax4.plot(ph, low_ph, 'b', linewidth=1.5, label='Bad')
# ax4.plot(ph, high_ph, 'b', linewidth=1.5, label='Bad')
# ax4.plot(ph, acceptable_ph, 'g', linewidth=1.5, label='acceptable')
# ax4.plot(ph, good_ph, 'r', linewidth=1.5, label='Good')
# ax4.set_title('ph')
# ax4.legend()

# ax4.spines['top'].set_visible(False)
# ax4.spines['right'].set_visible(False)
# ax4.get_xaxis().tick_bottom()
# ax4.get_yaxis().tick_left()

quality_L = fuzz.trapmf(quality, [0, 0, 15, 35])
quality_A = fuzz.trapmf(quality, [30, 40, 60, 70])
quality_H = fuzz.trapmf(quality, [65, 80, 100, 100])

# ax5.plot(quality, quality_L, 'b', linewidth=1.5, label='Bad')
# ax5.plot(quality, quality_A, 'g', linewidth=1.5, label='acceptable')
# ax5.plot(quality, quality_H, 'r', linewidth=1.5, label='Good')
# ax5.set_title('quality')
# ax5.legend()

# ax5.spines['top'].set_visible(False)
# ax5.spines['right'].set_visible(False)
# ax5.get_xaxis().tick_bottom()
# ax5.get_yaxis().tick_left()

# plt.savefig('name4.png')
# os.system('eog name4.png &')


def retrieve_indicators_request(winery_id):
    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        indicator = db.get_indicators_by_winery_id(winery_id)
        return dumps(indicator), 200

    db.close_connection()
    return {'error': 'Something gone wrong'}, 500


def calculate_indicators():
    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        wineries = db.get_all_wineries()
        date = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
        for winery in wineries:
            indicator = dict()
            indicator['winery_id'] = str(winery['_id'])
            indicator['date'] = date
            try:
                agFunc = aggMemberFunc(5, 2, 19, 2, 5)
                final = fuzz.defuzz(quality, agFunc, 'centroid')
                indicator['value'] = final
            except Exception as e:
                print(e)
                indicator['value'] = 0

            db.insert_one(indicator)

        return {"message": "Indicadores salvos"}, 200

    db.close_connection()
    return {'error': 'Something gone wrong'}, 500


def aggMemberFunc(
    windVal, pluviometricVal, temperatureVal, humidityVal, phVal
):
    # Interpola as variáveis (adiciona as variáveis ao universo de dados)
    wind_lo = fuzz.interp_membership(wind, bad_wind, windVal)
    wind_md = fuzz.interp_membership(wind, acceptable_wind, windVal)
    wind_hi = fuzz.interp_membership(wind, good_wind, windVal)

    pluviometric_lo = fuzz.interp_membership(
        pluviometric,
        bad_pluviometric,
        pluviometricVal
    )
    pluviometric_md = fuzz.interp_membership(
        pluviometric,
        acceptable_pluviometric,
        pluviometricVal
    )
    pluviometric_hi = fuzz.interp_membership(
        pluviometric,
        good_pluviometric,
        pluviometricVal)

    temperature_bl = fuzz.interp_membership(
        temperature,
        low_temperature,
        temperatureVal
    )
    temperature_hl = fuzz.interp_membership(
        temperature,
        high_temperature,
        temperatureVal
    )
    temperature_md = fuzz.interp_membership(
        temperature,
        acceptable_temperature,
        temperatureVal
    )
    temperature_hi = fuzz.interp_membership(
        temperature,
        good_temperature,
        temperatureVal
    )

    humidity_lo = fuzz.interp_membership(
        humidity,
        bad_humidity,
        humidityVal
    )
    humidity_md = fuzz.interp_membership(
        humidity,
        acceptable_humidity,
        humidityVal
    )
    humidity_hi = fuzz.interp_membership(
        humidity,
        good_humidity,
        humidityVal
    )

    ph_bl = fuzz.interp_membership(ph, low_ph, phVal)
    ph_hl = fuzz.interp_membership(ph, high_ph, phVal)
    ph_md = fuzz.interp_membership(ph, acceptable_ph, phVal)
    ph_hi = fuzz.interp_membership(ph, good_ph, phVal)

    # Determina os pesos para cada antecedência
    bad_temperature = np.fmax(temperature_bl, temperature_hl)
    bad_ph = np.fmax(ph_bl, ph_hl)
    humidity_good = np.fmax(humidity_hi, humidity_md)
    temperature_good = np.fmax(temperature_hi, temperature_md)
    rule1 = np.fmax(
        wind_hi, np.fmax(
            pluviometric_hi, np.fmax(
                ph_hi, np.fmax(temperature_good, humidity_good)
            )
        )
    )
    rule2 = np.fmax(
        wind_md, np.fmax(
            pluviometric_md, np.fmax(
                ph_md, np.fmax(temperature_md, humidity_md)
            )
        )
    )
    rule3 = np.fmax(
        wind_lo, np.fmax(
            pluviometric_lo, np.fmax(
                humidity_lo, np.fmax(bad_ph, bad_temperature)
            )
        )
    )

    # Determina os valores de cada relação de quality
    quality1 = rule1 * quality_H
    quality2 = rule2 * quality_A
    quality3 = rule3 * quality_L

    aggregate_membership = np.fmax(
        quality1, np.fmax(
            quality2, quality3
        )
    )
    return aggregate_membership
