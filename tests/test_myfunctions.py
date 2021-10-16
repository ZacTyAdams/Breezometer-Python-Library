from breezometerlib import Breezometer

breezometer = Breezometer("33.222659", "-97.115009", "ce760ac41cab4da093ac45e653d99423")

def test_test_connection():
    assert  breezometer.test_connection() == 200

def test_get_current_aqi():
    breezometer.get_current_aqi()
    assert breezometer.current_aqi != None

def test_get_aqi_forecast():
    breezometer.get_aqi_forecast()
    assert breezometer.aqi_forecast != None

def test_get_pollen_forecast():
    breezometer.get_pollen_forecast()
    assert breezometer.aqi_forecast != None