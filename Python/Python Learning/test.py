class test:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def LastnName(self):
        return self.name.split()[-1]
    def GiveRaise(self, percent):
        percent.split('%')
        percent = percent / 100
        self.pay *= (1.0 + percent)
