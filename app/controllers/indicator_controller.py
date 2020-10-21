import numpy as np
import skfuzzy as fuzz


# entradas
mem = np.arange(0, 101, 1)
cpu = np.arange(0, 101, 1)
# kpi de desempenho
kpi = np.arange(0, 101, 1)

# Funções de pertinência - Memória disponível
mem_L = fuzz.gaussmf(mem, 0, 10)  # Baixa memória
mem_A = fuzz.gaussmf(mem, 50, 20)  # Média memória
mem_H = fuzz.gaussmf(mem, 100, 15)  # Alta memória

# Funções de pertinência - CPU disponível
cpu_LL = fuzz.trapmf(cpu, [0, 0, 5, 10])  # Muito baixa cpu
cpu_L = fuzz.gaussmf(cpu, 15, 20)  # Baixa cpu
cpu_A = fuzz.gaussmf(cpu, 45, 18)  # Média cpu
cpu_H = fuzz.trimf(kpi, [60, 100, 100])  # Alta cpu

# Funções de pertinência - kpi
kpi_L = fuzz.trapmf(kpi, [0, 0, 15, 35])  # Baixo kpi
kpi_A = fuzz.trapmf(kpi, [30, 40, 60, 70])  # Médio kpi
kpi_H = fuzz.trapmf(kpi, [60, 80, 100, 100])  # Alto kpi


def aggMemberFunc(memVal, cpuVal):
    # Interpola as variáveis
    mem1 = fuzz.interp_membership(mem, mem_L, memVal)
    mem2 = fuzz.interp_membership(mem, mem_A, memVal)
    mem3 = fuzz.interp_membership(mem, mem_H, memVal)
    cpu0 = fuzz.interp_membership(cpu, cpu_L, cpuVal)
    cpu1 = fuzz.interp_membership(cpu, cpu_L, cpuVal)
    cpu2 = fuzz.interp_membership(cpu, cpu_A, cpuVal)
    cpu3 = fuzz.interp_membership(cpu, cpu_H, cpuVal)

    # Determina os pesos para cada antecedência
    rule0 = np.fmax(mem3, cpu0)  # 0 - muita memória disponível e muito pouco uso de cpu # noqa
    rule1 = np.fmax(mem1, cpu3)  # 1 - pouca memória disponível e muito uso de cpu # noqa
    rule2 = np.fmax(mem2, cpu1)  # 2 - media memoria disponivel e pouco uso de cpu # noqa
    rule3 = np.fmax(mem2, cpu2)  # 3 - media memoria disponivel e medio uso de cpu # noqa
    rule4 = np.fmax(mem3, cpu3)  # 4 - muita memoria disponível e muito uso de cpu # noqa

    # Determina os valores de cada relação de kpi
    kpi0 = rule0 * kpi_L
    kpi1 = rule1 * kpi_L
    kpi2 = rule2 * kpi_A
    kpi3 = rule3 * kpi_H
    kpi4 = rule4 * kpi_L

    aggregate_membership = np.fmax(
        kpi0, np.fmax(
            kpi1, np.fmax(
                kpi2, np.fmax(
                    kpi3, kpi4
                )
            )
        )
    )
    return aggregate_membership


# Testando
agFunc = aggMemberFunc(100, 100)
final = fuzz.defuzz(kpi, agFunc, 'centroid')
print(agFunc)
print(final)
