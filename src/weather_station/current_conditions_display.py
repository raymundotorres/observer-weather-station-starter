class CurrentConditionsDisplay:
    def __init__(self): self.last=None
    def update(self,t,h,p): self.last=(t,h,p)
