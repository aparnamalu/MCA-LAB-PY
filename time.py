class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        # Add hours, minutes, seconds
        total_seconds = self.__second + other.__second
        total_minutes = self.__minute + other.__minute
        total_hours = self.__hour + other.__hour

        # Handle carry-over for seconds
        if total_seconds >= 60:
            total_minutes += total_seconds // 60
            total_seconds = total_seconds % 60

        # Handle carry-over for minutes
        if total_minutes >= 60:
            total_hours += total_minutes // 60
            total_minutes = total_minutes % 60

        return Time(total_hours, total_minutes, total_seconds)

    def display(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")


# --- Example Usage ---
t1 = Time(2, 45, 50)
t2 = Time(3, 20, 30)

t3 = t1 + t2   # operator overloading
t3.display()
