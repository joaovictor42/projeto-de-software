
class Date:
    
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year
        self.date = (year, month, day)

    def __str__(self) -> str:
        return f'{self.day:02}/{self.month:02}/{self.year}'
