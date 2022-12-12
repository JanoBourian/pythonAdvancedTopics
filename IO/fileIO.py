import os 

file_to_open = os.path.dirname(os.path.abspath(__file__)) + "/test.txt"
f = open(file_to_open, "r", encoding="utf-8")
print(f)
f.close()

## Read all data
with open(file_to_open, "r", encoding="utf-8") as f:
    read_data = f.read()
    print(read_data)

## Data per line
with open(file_to_open, "r", encoding="utf-8") as f:
    for line in f:
        print(line)
