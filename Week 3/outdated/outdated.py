def main():
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    while True:
        try:
            date = input("Date: ").strip()
            if date.count("/") == 2:
                m, d, y =  date.split("/")
                if len(m) == 1:
                    m = "0" + m
            else:
                m, d, y = date.split(" ")
                m = months.get(m)
                if "," not in d:
                    continue
                d = d.replace(",", "")
            if len(d) == 1:
                d = "0" + d
            if not 1 <= int(d) <= 31:
                continue
            if not 1 <= int(m) <= 12:
                continue
            print(f"{y}-{m}-{d}")
            break
        except:
            pass



main()
