class Time:
    def __init__(self, hour: int, minute: int, second: int) -> None:
        self.hour = hour % 24
        self.minute = minute % 60
        self.second = second % 60

    def get_hour(self) -> int:
        return self.hour

    def get_minute(self) -> int:
        return self.minute

    def get_second(self) -> int:
        return self.second

    def set_hour(self, hour: int) -> None:
        self.hour = hour

    def set_minute(self, minute: int) -> None:
        self.minute = minute

    def set_second(self, second: int) -> None:
        self.second = second

    def set_time(self, hour: int, minute: int, second: int) -> None:
        self.hour = hour % 24
        self.minute = minute % 60
        self.second = second % 60

    def to_string(self) -> str:
        return "%02d:%02d:%02d" % (self.hour, self.minute, self.second)

    def next_second(self) -> str:
        if self.second + 1 > 59:
            self.second = 0
            if self.minute + 1 > 59:
                self.minute = 0
                if self.hour + 1 > 23:
                    self.hour = 0
                else:
                    self.hour += 1
            else:
                self.minute += 1
        else:
            self.second += 1
        return self.to_string()

    def previus_second(self) -> str:
        if self.second - 1 < 0:
            self.second = 59
            if self.minute - 1 < 0:
                self.minute = 59
                if self.hour - 1 < 0:
                    self.hour = 23
                else:
                    self.hour -= 1
            else:
                self.minute -= 1
        else:
            self.second -= 1
        return self.to_string()


date1 = Time(500, 59, 59)
print(date1.to_string())
print(date1.next_second())
print(date1.next_second())
print(date1.previus_second())
