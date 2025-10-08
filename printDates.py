from datetime import date, timedelta

# Starting from today
start_date = date(2027, 2, 28)
# Ending on the last day of February 2027
end_date = date(2027, 3, 20)

current_date = start_date
while current_date <= end_date:
    formatted_date = current_date.strftime("%d.%m.%Y")
    if current_date.weekday() in [5,6]:
        formatted_date += "1"
    print(formatted_date)
    current_date += timedelta(days=1)
