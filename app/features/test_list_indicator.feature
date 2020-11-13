Feature: aptar requisicao feita no frontend e enviar dados dos  indicadores ao microsservico indicator atraves do BFF 
  Como Sistema, quero pegar os dados dos indicadores e visualiza-los no meu servico.

  Context: O usuario ver os indicadores
    Dado que os dados que foram resgistrados utilizem o servico atraves do BFF

    Scenario: Usuario visualiza os indicadores cadastrados na aplicacao
        Given a pagina de visualizar indicadores
        When a pagina de visualizar indicadores
        Then os dados captados devem ser persistidos no banco de dados da aplicacao