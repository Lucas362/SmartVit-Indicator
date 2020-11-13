from behave import given, when, then
import requests

api_url = None
bff_url = None
user_id = None


@given('a pagina de visualizar indicadores')
def step_impl_given(context):
    global api_url
    global user_id
    user_id = '5fadb6f1dbce533b02338e59'
    api_url = 'https://smartvit-indicator-stg.herokuapp.com/indicators'
    print('url :' +api_url + '/'+user_id)


@when('a pagina de visualizar indicadores')
def step_impl_when(context):
    response = requests.get(api_url + '/'+user_id)
    assert response.status_code == 200


@then('o bff requisita o microsservico indicator')
def step_impl_then(context):
    global bff_url
    bff_url = 'https://smartvit-user-bff-stg.herokuapp.com/indicators'
    response = requests.get(bff_url + '/'+user_id)
    assert response.status_code != 200
