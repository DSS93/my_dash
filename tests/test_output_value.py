from app import *
state = 'Uttar Pradesh'


def test_total_india():
  response = total_india()
  assert 'total' in list(response.keys()), 'Failed'
  print('Successfully response')


def test_state_loc():
  response = state_loc()
  assert state in response, 'Failed'
  print('Successfully response')


def test_state_total_confirmed():
  response = state_total_confirmed()
  assert len(response) != 0, 'Failed'
  print('Successfully response')


def test_state_total_discharge():
  response = state_total_discharge()
  assert len(response) != 0, 'Failed'
  print('Successfully response')


def test_state_total_death():
  response = state_total_death()
  assert len(response) != 0, 'Failed'
  print('Successfully response')


def test_state_total_confirmed_foreign():
  response = state_total_confirmed_foreign()
  assert len(response) != 0, 'Failed'
  print('Successfully response')


def test_pie_county_total():
  response = pie_county_total()
  assert isinstance(response, int) and response != 0, 'Failed'
  print('Successfully response')


def test_pie_county_recovered():
  response = pie_county_recovered()
  assert isinstance(response, int) and response != 0, 'Failed'
  print('Successfully response')


def test_pie_county_death():
  response = pie_county_death()
  assert isinstance(response, int) and response != 0, 'Failed'
  print('Successfully response')
