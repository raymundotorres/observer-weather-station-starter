from weather_station.current_conditions_display import CurrentConditionsDisplay
from weather_station.statistics_display import StatisticsDisplay
from weather_station.forecast_display import ForecastDisplay
from weather_station.weather_data import WeatherData

def test_hard_coded_receivers():
    c=CurrentConditionsDisplay(); s=StatisticsDisplay(); f=ForecastDisplay()
    w=WeatherData(c,s,f); w.measurements_changed(24,55,1012)
    assert c.last==(24,55,1012)
    assert s.temperatures==[24]
    assert f.last_pressure==1012
