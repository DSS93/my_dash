from app import *
state = 'Delhi'


def test_total_india():
  response = total_india()
  assert response != None, 'Failed'
  print('Successfully response')


def test_state_loc():
  response = state_loc()
  assert response != None, 'Failed'
  print('Successfully response')


def test_state_total_confirmed():
  response = state_total_confirmed()
  assert response != None, 'Failed'
  print('Successfully response')


def test_state_total_discharge():
  response = state_total_discharge()
  assert response != None, 'Failed'
  print('Successfully response')


def test_state_total_death():
  response = state_total_death()
  assert response != None, 'Failed'
  print('Successfully response')


def test_state_total_confirmed_foreign():
  response = state_total_confirmed_foreign()
  assert response != None, 'Failed'
  print('Successfully response')


def test_pie_county_total():
  response = pie_county_total()
  assert response != None, 'Failed'
  print('Successfully response')


def test_pie_county_recovered():
  response = pie_county_recovered()
  assert response != None, 'Failed'
  print('Successfully response')


def test_pie_county_death():
  response = pie_county_death()
  assert response != None, 'Failed'
  print('Successfully response')


def test_state_loc_name():
  response = state_loc_name()
  assert response != None, 'Failed'
  print('Successfully response')


def test_pie_all_state_case():
  response = pie_all_state_case(state)
  assert response != None, 'Failed'
  print('Successfully response')


def test_pie_all_state_recovered():
  response = pie_all_state_recovered(state)
  assert response != None, 'Failed'
  print('Successfully response')


def test_pie_all_state_death():
  response = pie_all_state_death(state)
  assert response != None, 'Failed'
  print('Successfully response')
