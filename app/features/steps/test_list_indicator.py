from behave import given, when, then
import requests

api_url = None
bff_url = None

@given('a pagina de visualizar indicadores')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-indicator-dev.herokuapp.com/indicators/5fa06810b79fd9c15a9a6c51'
    print('url :'+api_url)


@when('a pagina de visualizar indicadores')
def step_impl_when(context):
    response = requests.get(api_url)
    assert response.status_code == 200


@then('o bff requisita o microsservico indicator')
def step_impl_then(context):
    global bff_url
    bff_url = 'https://smartvit-user-bff-dev.herokuapp.com/indicators/5fa06810b79fd9c15a9a6c51'
    response = requests.get(bff_url)
    assert response.status_code == 200