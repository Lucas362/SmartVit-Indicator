from behave import given, when, then
import requests

api_url = None
bff_url = None
user_id = None


@given('a pagina de visualizar indicadores')
def step_impl_given(context):
    global api_url
    global user_id
    user_id = '5fa06810b79fd9c15a9a6c51'
    api_url = 'https://smartvit-indicator-dev.herokuapp.com/indicators'
    print('url :' +api_url+'/'+user_id)


@when('a pagina de visualizar indicadores')
def step_impl_when(context):
    response = requests.get(api_url+'/'+user_id)
    assert response.status_code == 200


@then('o bff requisita o microsservico indicator')
def step_impl_then(context):
    global bff_url
    bff_url = 'https://smartvit-user-bff-dev.herokuapp.com/indicators'
    response = requests.get(bff_url+'/'+user_id)
    assert response.status_code == 200
