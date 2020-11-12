import numpy as np
# import os
import skfuzzy as fuzz
# import matplotlib.pyplot as plt
from datetime import datetime
from bson import ObjectId
from bson.json_util import dumps, loads
from models.indicator import MongoDB
import itertools
import json


# entradas
ph = np.arange(0, 15, 1)
wind = np.arange(0, 28, 1)
air_temp = np.arange(-16, 51, 1)
rain = np.arange(0, 351, 1)
soil_temp = np.arange(-16, 51, 1)
soil_humidity = np.arange(0, 101, 1)
air_humidity = np.arange(0, 101, 1)
# Qualidade (saída)
quality = np.arange(0, 101, 1)


# fig, (ax5) = plt.subplots(nrows=1, figsize=(8, 9))

# Funções de pertinência
low_ph = fuzz.trimf(ph, [0, 0, 4])
high_ph = fuzz.trimf(ph, [8, 15, 15])
acceptable_ph = fuzz.trimf(ph, [4, 5, 6])
good_ph = fuzz.trapmf(ph, [5, 6, 7, 9])

# ax0.plot(ph, low_ph, 'b', linewidth=1.5, label='low')
# ax0.plot(ph, high_ph, 'b', linewidth=1.5, label='high')
# ax0.plot(ph, acceptable_ph, 'g', linewidth=1.5, label='acceptable')
# ax0.plot(ph, good_ph, 'r', linewidth=1.5, label='Good')
# ax0.set_title('ph')
# ax0.legend()

# ax0.spines['top'].set_visible(False)
# ax0.spines['right'].set_visible(False)
# ax0.get_xaxis().tick_bottom()
# ax0.get_yaxis().tick_left()

# plt.savefig('name1.png')
# os.system('eog name1.png &')

bad_wind = fuzz.trimf(wind, [5, 27, 27])
acceptable_wind = fuzz.trapmf(wind, [2, 3, 4, 6])
good_wind = fuzz.trapmf(wind, [0, 0, 2, 3])

# ax1.plot(wind, bad_wind, 'b', linewidth=1.5, label='Bad')
# ax1.plot(wind, acceptable_wind, 'g', linewidth=1.5, label='acceptable')
# ax1.plot(wind, good_wind, 'r', linewidth=1.5, label='Good')
# ax1.set_title('wind')
# ax1.legend()

# ax1.spines['top'].set_visible(False)
# ax1.spines['right'].set_visible(False)
# ax1.get_xaxis().tick_bottom()
# ax1.get_yaxis().tick_left()

# plt.savefig('name2.png')
# os.system('eog name2.png &')

low_air_temp = fuzz.trimf(air_temp, [0, 14, 14])
high_air_temp = fuzz.trimf(air_temp, [36, 50, 50])
acceptable_air_temp = fuzz.trapmf(air_temp, [13, 15, 20, 22])
good_air_temp = fuzz.trapmf(air_temp, [18, 21, 35, 37])

# ax2.plot(air_temp, low_air_temp, 'b', linewidth=1.5, label='low')
# ax2.plot(air_temp, high_air_temp, 'b', linewidth=1.5, label='high')
# ax2.plot(air_temp, acceptable_air_temp, 'g', linewidth=1.5, label='acceptable') # noqa
# ax2.plot(air_temp, good_air_temp, 'r', linewidth=1.5, label='Good')
# ax2.set_title('air_temp')
# ax2.legend()

# ax2.spines['top'].set_visible(False)
# ax2.spines['right'].set_visible(False)
# ax2.get_xaxis().tick_bottom()
# ax2.get_yaxis().tick_left()

# plt.savefig('name4.png')
# os.system('eog name4.png &')

low_rain = fuzz.trimf(rain, [0, 50, 52])
high_rain = fuzz.trimf(rain, [245, 350, 350])
acceptable_rain = fuzz.trapmf(rain, [48, 60, 148, 152])
good_rain = fuzz.trapmf(rain, [148, 160, 242, 252])

# ax3.plot(rain, low_rain, 'b', linewidth=1.5, label='low')
# ax3.plot(rain, high_rain, 'b', linewidth=1.5, label='high')
# ax3.plot(rain, acceptable_rain, 'g', linewidth=1.5, label='acceptable')
# ax3.plot(rain, good_rain, 'r', linewidth=1.5, label='Good')
# ax3.set_title('rain')
# ax3.legend()

# ax3.spines['top'].set_visible(False)
# ax3.spines['right'].set_visible(False)
# ax3.get_xaxis().tick_bottom()
# ax3.get_yaxis().tick_left()

# plt.savefig('fuzzy2.png')
# os.system('eog fuzzy2.png &')

low_soil_temp = fuzz.trimf(soil_temp, [0, 15, 15])
high_soil_temp = fuzz.trimf(soil_temp, [32, 100, 100])
acceptable_soil_temp = fuzz.trapmf(soil_temp, [12, 16, 20, 22])
good_soil_temp = fuzz.trapmf(soil_temp, [21, 22, 35, 37])

# ax4.plot(soil_temp, low_soil_temp, 'b', linewidth=1.5, label='low')
# ax4.plot(soil_temp, high_soil_temp, 'b', linewidth=1.5, label='high')
# ax4.plot(soil_temp, acceptable_soil_temp, 'g', linewidth=1.5, label='acceptable') # noqa
# ax4.plot(soil_temp, good_soil_temp, 'r', linewidth=1.5, label='Good')
# ax4.set_title('soil_temp')
# ax4.legend()

# ax4.spines['top'].set_visible(False)
# ax4.spines['right'].set_visible(False)
# ax4.get_xaxis().tick_bottom()
# ax4.get_yaxis().tick_left()

# plt.savefig('name6.png')
# os.system('eog name6.png &')

low_soil_humidity = fuzz.trimf(soil_humidity, [0, 30, 30])
high_soil_humidity = fuzz.trimf(soil_humidity, [49, 100, 100])
acceptable_soil_humidity = fuzz.trapmf(soil_humidity, [29, 31, 39, 40])
good_soil_humidity = fuzz.trapmf(soil_humidity, [39, 41, 50, 50])

# ax5.plot(soil_humidity, low_soil_humidity, 'b', linewidth=1.5, label='low')
# ax5.plot(soil_humidity, high_soil_humidity, 'b', linewidth=1.5, label='high')
# ax5.plot(soil_humidity, acceptable_soil_humidity, 'g', linewidth=1.5, label='acceptable') # noqa
# ax5.plot(soil_humidity, good_soil_humidity, 'r', linewidth=1.5, label='Good')
# ax5.set_title('soil_humidity')
# ax5.legend()

# ax5.spines['top'].set_visible(False)
# ax5.spines['right'].set_visible(False)
# ax5.get_xaxis().tick_bottom()
# ax5.get_yaxis().tick_left()

# plt.savefig('fuzzy3.png')
# os.system('eog fuzzy3.png &')

low_air_humidity = fuzz.trimf(air_humidity, [0, 10, 10])
high_air_humidity = fuzz.trimf(air_humidity, [68, 100, 100])
acceptable_air_humidity = fuzz.trapmf(air_humidity, [8, 12, 15, 17])
good_air_humidity = fuzz.trapmf(air_humidity, [16, 19, 70, 72])

# ax6.plot(air_humidity, low_air_humidity, 'b', linewidth=1.5, label='low')
# ax6.plot(air_humidity, high_air_humidity, 'b', linewidth=1.5, label='high')
# ax6.plot(air_humidity, acceptable_air_humidity, 'g', linewidth=1.5, label='acceptable') # noqa
# ax6.plot(air_humidity, good_air_humidity, 'r', linewidth=1.5, label='Good')
# ax6.set_title('air_humidity')
# ax6.legend()

# ax6.spines['top'].set_visible(False)
# ax6.spines['right'].set_visible(False)
# ax6.get_xaxis().tick_bottom()
# ax6.get_yaxis().tick_left()

# plt.savefig('name8.png')
# os.system('eog name8.png &')

quality_L = fuzz.trapmf(quality, [0, 0, 15, 35])
quality_A = fuzz.trapmf(quality, [30, 40, 60, 70])
quality_H = fuzz.trapmf(quality, [65, 80, 100, 100])

# ax7.plot(quality, quality_L, 'b', linewidth=1.5, label='Bad')
# ax7.plot(quality, quality_A, 'g', linewidth=1.5, label='acceptable')
# ax7.plot(quality, quality_H, 'r', linewidth=1.5, label='Good')
# ax7.set_title('quality')
# ax7.legend()

# ax7.spines['top'].set_visible(False)
# ax7.spines['right'].set_visible(False)
# ax7.get_xaxis().tick_bottom()
# ax7.get_yaxis().tick_left()

# plt.savefig('fuzzy4.png')
# os.system('eog fuzzy4.png &')


def retrieve_indicators_request(winery_id):
    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        winery_obj_id = ObjectId(winery_id)
        winery = db.get_one(winery_obj_id, 'winery')
        if winery:
            indicator = db.get_fuzzy_by_winery_id(winery_id)
            fuzzy = indicator
            fuzzy = [item['value'] for item in fuzzy]
            systems = []
            general_indicators = dict()
            general_indicators["sensor_ph"] = 0
            general_indicators["temp_celsius"] = 0
            general_indicators["vento_MS"] = 0
            general_indicators["humidity_percent"] = 0
            general_count = 0

            for system in winery['systems']:
                sys_gen = dict()
                sys_gen["sensor_ph"] = 0
                sys_gen["temp_celsius"] = 0
                sys_gen["vento_MS"] = 0
                sys_gen["humidity_percent"] = 0
                
                system_ind = dict()
                system_ind["vento_MS"] = []
                system_ind["vento_direcao"] = []
                system_ind["qtd_chuva"] = []
                system_ind["temp_celsius"] = []
                system_ind["humidity_percent"] = []
                system_ind["pressure_hPa"] = []
                system_ind["sensor_ph"] = []
                system_ind["moist_percent_1"] = []
                system_ind["moist_percent_2"] = []
                system_ind["moist_percent_3"] = []
                for sensor in system['sensors']:
                    measurements = db.get_measurement_from_sensor(
                                sensor['identifier']
                            )

                    for measurement in measurements:
                        system_ind[measurement['type']].append(
                            measurement['value']
                        )
                is_valid = False
                gen_keys = sys_gen.keys()
                for indicator in system_ind.keys():
                    if system_ind[indicator]:
                        is_valid = True
                        sys_gen_indicator = list(
                            itertools.islice(
                                system_ind[indicator], 10
                            )
                        )
                        system_ind[indicator] = sys_gen_indicator
                        if indicator in gen_keys:
                            sys_gen[indicator] = sum(sys_gen_indicator)/len(sys_gen_indicator)
                
                if is_valid:
                    general_count += 1
                    general_indicators["sensor_ph"] += sys_gen["sensor_ph"]
                    general_indicators["temp_celsius"] += sys_gen["temp_celsius"]
                    general_indicators["vento_MS"] += sys_gen["vento_MS"]
                    general_indicators["humidity_percent"] += sys_gen["humidity_percent"]

                system_ind["sys_gen"] = sys_gen
                systems.append(system_ind)

                if general_count > 0:
                    general_indicators["sensor_ph"] /= general_count 
                    general_indicators["temp_celsius"] /= general_count 
                    general_indicators["vento_MS"] /= general_count 
                    general_indicators["humidity_percent"] /= general_count 

                return {
                    "fuzzy": fuzzy,
                    "systems": systems,
                    "general_indicators": general_indicators
                }, 200

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

        #     final = 0
        #     count = 0
        #     for system in winery['systems']:
        #         phVal = 0
        #         windVal = 0
        #         airTemVal = 0
        #         rainVal = 0
        #         soilTempVal = 0
        #         soilHumidityVal = 0
        #         airHumidityVal = 0
        #         for sensor in system['sensors']:
        #             try:
        #                 agFunc = aggMemberFunc(
        #                     phVal,
        #                     windVal,
        #                     airTemVal,
        #                     rainVal,
        #                     soilTempVal,
        #                     soilHumidityVal,
        #                     airHumidityVal
        #                 )
        #                 final += fuzz.defuzz(quality, agFunc, 'centroid')
        #             except Exception as e:
        #                 print(e)
                
        #         count += 1

        #     if count > 1:
        #         final /= count

            # indicator['value'] = final
            indicator['value'] = 20
            db.insert_one(indicator)

        return {"message": "Indicadores salvos"}, 200

    db.close_connection()
    return {'error': 'Something gone wrong'}, 500


def aggMemberFunc(
    phVal,
    windVal,
    airTemVal,
    rainVal,
    soilTempVal,
    soilHumidityVal,
    airHumidityVal
):
    # Interpola as variáveis (adiciona as variáveis ao universo de dados)
    ph_bl = fuzz.interp_membership(ph, low_ph, phVal)
    ph_hl = fuzz.interp_membership(ph, high_ph, phVal)
    ph_md = fuzz.interp_membership(ph, acceptable_ph, phVal)
    ph_hi = fuzz.interp_membership(ph, good_ph, phVal)

    wind_lo = fuzz.interp_membership(wind, bad_wind, windVal)
    wind_md = fuzz.interp_membership(wind, acceptable_wind, windVal)
    wind_hi = fuzz.interp_membership(wind, good_wind, windVal)

    air_temp_bl = fuzz.interp_membership(air_temp, low_air_temp, airTemVal)
    air_temp_hl = fuzz.interp_membership(air_temp, high_air_temp, airTemVal)
    air_temp_md = fuzz.interp_membership(
        air_temp,
        acceptable_air_temp,
        airTemVal
    )
    air_temp_hi = fuzz.interp_membership(air_temp, good_air_temp, airTemVal)

    rain_bl = fuzz.interp_membership(rain, low_rain, rainVal)
    rain_hl = fuzz.interp_membership(rain, high_rain, rainVal)
    rain_md = fuzz.interp_membership(rain, acceptable_rain, rainVal)
    rain_hi = fuzz.interp_membership(rain, good_rain, rainVal)

    soil_temp_bl = fuzz.interp_membership(
        soil_temp,
        low_soil_temp,
        soilTempVal
    )
    soil_temp_hl = fuzz.interp_membership(
        soil_temp,
        high_soil_temp,
        soilTempVal
    )
    soil_temp_md = fuzz.interp_membership(
        soil_temp,
        acceptable_soil_temp,
        soilTempVal
    )
    soil_temp_hi = fuzz.interp_membership(
        soil_temp,
        good_soil_temp,
        soilTempVal
    )

    soil_humidity_bl = fuzz.interp_membership(
        soil_humidity,
        low_soil_humidity,
        soilHumidityVal
    )
    soil_humidity_hl = fuzz.interp_membership(
        soil_humidity,
        high_soil_humidity,
        soilHumidityVal
    )
    soil_humidity_md = fuzz.interp_membership(
        soil_humidity,
        acceptable_soil_humidity,
        soilHumidityVal
    )
    soil_humidity_hi = fuzz.interp_membership(
        soil_humidity,
        good_soil_humidity,
        soilHumidityVal
    )

    air_humidity_bl = fuzz.interp_membership(
        air_humidity,
        low_air_humidity,
        airHumidityVal
    )
    air_humidity_hl = fuzz.interp_membership(
        air_humidity,
        high_air_humidity,
        airHumidityVal
    )
    air_humidity_md = fuzz.interp_membership(
        air_humidity,
        acceptable_air_humidity,
        airHumidityVal
    )
    air_humidity_hi = fuzz.interp_membership(
        air_humidity,
        good_air_humidity,
        airHumidityVal
    )

    # Determina os pesos para cada antecedência
    bad_ph = np.fmax(ph_bl, ph_hl)
    bad_air_temp = np.fmax(air_temp_bl, air_temp_hl)
    bad_rain = np.fmax(rain_bl, rain_hl)
    bad_soil_temp = np.fmax(soil_temp_bl, soil_temp_hl)
    bad_soil_humidity = np.fmax(soil_humidity_bl, soil_humidity_hl)
    bad_air_humidity = np.fmax(air_humidity_bl, air_humidity_hl)

    rule1 = np.fmax(
        ph_hi, np.fmax(
            wind_hi, np.fmax(
                air_temp_hi, np.fmax(
                    rain_hi, np.fmax(
                        soil_temp_hi, np.fmax(
                            soil_humidity_hi, air_humidity_hi
                        )
                    )
                )
            )
        )
    )

    rule2 = np.fmax(
        ph_md, np.fmax(
            wind_md, np.fmax(
                air_temp_md, np.fmax(
                    rain_md, np.fmax(
                        soil_temp_md, np.fmax(
                            soil_humidity_md, air_humidity_md
                        )
                    )
                )
            )
        )
    )

    rule3 = np.fmax(
        bad_ph, np.fmax(
            wind_lo, np.fmax(
                bad_air_temp, np.fmax(
                    bad_rain, np.fmax(
                        bad_soil_temp, np.fmax(
                            bad_soil_humidity, bad_air_humidity
                        )
                    )
                )
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
