class ForecastDisplay:
    def __init__(self): self.last_pressure=None
    def update(self,t,h,p): self.last_pressure=p
