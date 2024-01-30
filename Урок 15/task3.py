# 1-й четверг ноября, 3-я среда мая
import sys
import datetime

WEEKDAYS = """понедельник вторник среда четверг пятница суббота воскресенье""".split()
WEEKDAYS = {str(WEEKDAYS[n]):n+1 for n in range(len(WEEKDAYS))}

MONTHS = """января февраля марта апреля мая июня июля августа сентября октября ноября декабря""".split()
MONTHS = {str(MONTHS[n]):n+1 for n in range(len(MONTHS))}

def correct_date(text: str) -> datetime.datetime:
    week_count, weekday, month = text.split()
    week_count = int(week_count[0])
    weekday = WEEKDAYS[weekday]
    month = MONTHS[month]

    # print(f"{week_count = }, \n{weekday = }, \n{month = }")
    weeks_passed = 0
    for day in range(1,31):
        tempdate = datetime.datetime(
            year=datetime.datetime.now().year,
            month=month,
            day=day
        )
        if tempdate.weekday() + 1 == weekday:
            weeks_passed += 1
            if weeks_passed == week_count:
                return  tempdate
    raise ValueError(f"Талкой даты не существует: {text}")








if __name__ == "__main__":
    print(sys.argv)
    path, date, *_ = sys.argv
    print(path, date)
    print(correct_date(date))
    print(correct_date("1-ый четверг ноября"))
    print(correct_date("3-я среда мая"))

    # print(correct_date("2-я среда января"))
    # print(correct_date("5-ый четверг января"))








