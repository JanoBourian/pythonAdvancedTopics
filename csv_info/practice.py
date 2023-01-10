import csv

print(csv.list_dialects())
print(csv.field_size_limit())

info_to_write = [
    ["Spam Spam Spam Spam Spam Baked Beans"],
    ["Spam Lovely Spam Wonderful Spam"]
]

with open("eggs.csv", "w", newline="") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = " ", quotechar = "|", quoting = csv.QUOTE_MINIMAL)
    for item in info_to_write:
        spamwriter.writerow(item)

with open("eggs.csv", newline ="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=" ", quotechar = "|")
    for row in spamreader:
        print(", ".join(row))

## Dictionars

with open("names.csv", "w", newline="") as csvfile:
    fieldnames = ["first_name", "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({"first_name": "Baked", "last_name": "Beans"})
    writer.writerow({"first_name": "Lovely", "last_name": "Spam"})
    writer.writerow({"first_name": "Wonderful", "last_name": "Spam"})
    
with open("names.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["first_name"], row["last_name"])