from behave import given, when, then
import requests

response_codes = {}
api_url = None
bff_url = None
user_id = None


@given('a pagina de visualizar indicadores')
def step_impl_given(context):
    global api_url
    global user_id
    user_id = '5fac6984fb4a09e30d599bf7'
    api_url = 'http://smartvit-indicator-stg.herokuapp.com/indicators'
    print('url :' +api_url + '/'+user_id)


@when('a pagina de visualizar indicadores')
def step_impl_when(context):
    response = requests.get(api_url + '/'+user_id)
    statuscode = response.status_code
    response_codes['GET'] = statuscode


@then('os dados captados devem ser persistidos no banco de dados da aplicacao')
def step_impl_then(context):
    print('Get rep code ;'+str(response_codes['GET']))
    assert response_codes['GET'] == 200

