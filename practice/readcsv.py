import csv
with open('a.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("ID Department Name")
 print("---------------------------------")

 for row in data:
     if row['department_name']=="Sales":
         print("hello")

with open("a.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
      print(lines[1])


