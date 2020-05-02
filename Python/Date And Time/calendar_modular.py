
import calendar 
if __name__ == "__main__":
    month, day, year = map(int,input().split())
    week_day = calendar.weekday(year, month, day)
    print(str(calendar.day_name[week_day]).upper())

