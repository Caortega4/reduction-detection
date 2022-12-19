import csv

annotation = [0, 1, 2]

with open('metadata.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    id = 234
    writer.writerow([annotation[0], 'Profession'])
    writer.writerow([annotation[0], 'Profession'])