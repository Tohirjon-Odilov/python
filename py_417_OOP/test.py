class Time:
    def __init__(self, hour: int, minute: int, second: int) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    def getHour(self):
        if self.hour < 0:
            return "The given number is small"
        elif self.hour > 23:
            return "The given number is hight"
        else:
            return self.hour

    def setHour(self, hour):
        self.hour = hour

    def getMinute(self):
        if self.minute < 0:
            return "The given number is small"
        elif self.minute > 59:
            return "The given number is hight"
        else:
            return self.minute

    def setMinute(self, minute):
        self.minute = minute

    def getSecond(self):
        if self.second < 0:
            return "The given number is small"
        elif self.second > 59:
            return "The given number is hight"
        else:
            return self.second

    def setSecond(self, second):
        self.second = second

    def setTime(self):
        self.setTime = f"{self.hour}, {self.minute}, {self.second}"

    def toString(self):
        return "%02d : %02d : %02d" % (
            self.getHour(),
            self.getMinute(),
            self.getSecond(),
        )

    def nextSecond(self):
        if self.second + 1 >= 60:
            self.second = 0
            self.minute = self.minute + 1
            if self.minute >= 60:
                self.minute = 0
                self.hour = self.hour + 1
            return self.hour, self.minute, self.second
        else:
            return self.hour, self.minute, self.second

    def previousSecond(self):
        return self.hour, self.minute, self.second

    def str(self) -> str:
        return f"{self.hour} {self.minute} {self.second}"


time = Time(23, 59, 59)
print(time.nextSecond())
print(time.nextSecond())
