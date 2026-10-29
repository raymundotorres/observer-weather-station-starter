from .current_conditions_display import CurrentConditionsDisplay
from .statistics_display import StatisticsDisplay
from .forecast_display import ForecastDisplay

class WeatherData:
    def __init__(self,current: CurrentConditionsDisplay,statistics: StatisticsDisplay,forecast: ForecastDisplay):
        self.current=current; self.statistics=statistics; self.forecast=forecast
    def measurements_changed(self,t,h,p):
        self.current.update(t,h,p)
        self.statistics.update(t,h,p)
        self.forecast.update(t,h,p)
