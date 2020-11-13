from behave import given, when, then
import requests

request_bodies = {}
response_codes = {}
api_url = None


@given('que o sistema deseja captar dados dos sensores')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-indicator-stg.herokuapp.com/indicators'
    print('url :'+api_url)


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
    statuscode = response.status_code
    response_codes['POST'] = statuscode


@then('os dados captados devem ser persistidos no banco de dados da aplicacao')
def step_impl_then(context):
    print('Post rep code ;'+str(response_codes['POST']))
    assert response_codes['POST'] == 200
