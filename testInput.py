from datetime import date

data = []
currweek = []
for x in open("input.txt"):
    dateStr = x.split(" ")[0].split(".")
    currDate = date(int(dateStr[2]),int(dateStr[1]),int(dateStr[0]))
    if currDate.weekday() == 6:
        data.append(currweek)
        currweek = []
    times = x.split(" ")[1].rstrip()
    currweek.append("_" if times == "1" else "X")

for x in data:
    print("".join(x))