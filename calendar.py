import datetime

class Calendar:
    def __init__(self):
        self.current_date = datetime.date.today()
        
    def today_date(self):
        print(f"Today is {self.current_date}")
        
        
class Time:
    def __init__(self):
        self.current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
    def display_time(self):
        print(f"Current time is {self.current_time}")
        
        
class CalendarTime(Calendar, Time):
    def __init__(self):
        Calendar.__init__(self)
        Time.__init__(self)
        
    def display_current(self):
        print(f"Date : {self.current_date} Time : {self.current_time}")
        
def main():
    t1 = CalendarTime()
    t1.display_current()

d1 = Calendar()
d1.today_date()
if __name__ == "__main__":
    main()
