Feature: Captar dados do modulo eletronico
  Como Sistema, quero captar os dados coletados pelo modulo
  eletronico para que seja possivel calcular indicadores,
  gerar alertas e indicacoes para o software como um todo.

  Context: O ambiente de captacao de dados esta preparado
    Dado que o servico de captacao de dados esteja ativo

  Scenario: Captar dado dos sensores
      Given que o sistema deseja captar dados dos sensores

       When captar dados dos sensores
       | sensor      | pH  | vento | umidade | temperatura |
       | 78as7as78as | 3.5 | 10    |  25     | 31          |
       Then o bff requisita o microsservico indicator
       | sensor      | pH  | vento | umidade | temperatura |
       | 78as7as78as | 3.5 | 10    |  25     | 31          |