import csv

# https://data.gov.tw/dataset/11764
bwibbu_file = "BWIBBU_d_ALL.csv"

# https://data.gov.tw/dataset/11549
stock_day_file = "STOCK_DAY_ALL.csv"

subjects = []
subject_id_price = {}


with open(bwibbu_file, newline="", encoding="utf-8") as csvfile:

    rows = csv.reader(csvfile)

    # skip first two line in csv file which is not usable
    next(rows)
    next(rows)

    for row in rows:
        if not len(row) == 7 or "-" in row or "" in row:
            continue
        # print(row)
        yield_rate = float(row[2])
        pe = float(row[4])
        pb = float(row[5])
        if yield_rate > 6 and pe < 10 and pb < 5:
            subjects.append(row)

with open(stock_day_file, newline="", encoding="utf-8") as csv_file:
    rows = csv.reader(csv_file)
    next(rows)
    for row in rows:
        # print(row)
        if row:
            if row[0]:
                stock_id = row[0]
            if row[7]:
                stock_price = float(row[7])
            subject_id_price[stock_id] = stock_price

# print(subject_id_price)

for subject in subjects:

    title = subject[1]

    if "KY" in title:
        continue

    id = subject[0]

    price = float(subject_id_price[subject[0]])
    pbr = float(subject[5])
    book_price = price / pbr
    pe = float(subject[4])
    eps = price / pe
    years_taken = (price - book_price) / eps
    print(id, title, "years_taken", round(years_taken, 2))
