from datetime import datetime


class IncorrectTime(Exception):
    def __init__(self, message):
        super().__init__(self, message)
        self.message = message


class IncorrectHour(IncorrectTime):
    pass


class IncorrectMinute(IncorrectTime):
    pass


class IncorrectSecond(IncorrectTime):
    pass


class Time:
    def __init__(self, hour, minute, second):
        self.hour = 0
        self.minute = 0
        self.second = 0
        # check hour
        # check minute
        # check second
        self.change_hour(hour)
        self.change_minutse(minute)
        self.change_second(second)




    def __str__(self):
        return f'часы:{self.hour}, минуты:{self.minute}, секунды:{self.second}'

    def change_hour(self, hour):
        if hour > 23 or hour < 0:
            raise IncorrectHour("Incorrect hour value")
        self.hour = hour

    def change_minutse(self, minutse):
        if minutse > 59 or minutse < 0:
            raise IncorrectMinute("Incorrect minute value")
        self.minutse = minutse

    def change_second(self, second):
        if second > 59 or second < 0:
            raise IncorrectSecond("Incorrect second value")
        self.second = second

    @staticmethod
    def now():
        n = datetime.now()
        # d = datetime.replace(hour=14, minute=25, second= 45)
        return Time(hour=n.hour,
                    minute=n.minute,
                    second=n.second)


try:
    time1 = Time(hour=13, minute=44, second=12)
    time2 = Time(hour=78, minute=56, second=45)
    time3 = Time(hour=23, minute=46, second=45)
    print(time3)
    print(time2)
    print(time1)
except IncorrectHour as e:
    print(e)
except IncorrectMinute as r:
    print(r)
except IncorrectSecond as f:
    print(f)
