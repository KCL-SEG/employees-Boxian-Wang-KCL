"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, m_money=None, c_time=None, h_money=None):
        self.name = name
        self.m_money = m_money
        self.h_money = h_money
        self.c_time = c_time


    def get_pay(self):
        if self.c_time:
            return self.c_time * self.h_money
        else:
            return self.m_money

    def __str__(self):
        if self.c_time:
            return f"{self.name} works on a contract of {self.c_time} hours at {self.h_money}/hour.  Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a monthly salary of {self.m_money}.  Their total pay is {self.get_pay()}."

class ComissionedEmployee(Employee):
    def __init__(self, name, m_money=None, c_time=None, h_money=None, c_id=None, cpc=None, bonus=None):
        super().__init__(name, m_money, c_time, h_money)
        self.c_id = c_id
        self.cpc = cpc
        self.bonus = bonus

    def get_bonus(self):
        if self.bonus:
            return self.bonus
        else:
            return self.cpc * self.c_id

    def get_pay(self): 
        return super().get_pay() + self.get_bonus()

    def __str__(self):
        explanatory_string = ""
        if self.c_time:
            explanatory_string += f"{self.name} works on a contract of {self.c_time} hours at {self.h_money}/hour"
        else:
            explanatory_string += f"{self.name} works on a monthly salary of {self.m_money}"
        if self.bonus:
            explanatory_string += f" and receives a bonus commission of {self.bonus}."
        else:
            explanatory_string += f" and receives a commission for {self.c_id} contract(s) at {self.cpc}/contract."
        explanatory_string += f"  Their total pay is {self.get_pay()}."
        return explanatory_string
