from behave import given, when, then
import requests

request_bodies = {}
response_codes = {}
api_url = None
bff_url = None
user = None


@given('que o sistema deseja captar dados dos sensores')
def step_impl_given(context):
    global api_url
    global user
    user = '5fac6984fb4a09e30d599bf7'
    api_url = 'https://smartvit-indicator-stg.herokuapp.com/indicators'
    print('url :'+api_url + '/'+user)


@when('captar dados dos sensores')
def step_impl_when(context):
    request_bodies['POST'] = {"sensor": "78as7as78as",
                              "ph": "3.5",
                              "wind": "10",
                              "humidity": "25",
                              "temperature": "31"}
    response = requests.post(
                            api_url,
                            json=request_bodies['POST']
                            )
    assert response.status_code == 200


@then('o bff requisita o microsservico indicator')
def step_impl_then(context):
    global bff_url
    bff_url = 'https://smartvit-user-bff-stg.herokuapp.com/indicators'
    response = requests.get(bff_url + '/'+user)
    assert response.status_code == 200
