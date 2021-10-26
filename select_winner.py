import csv
import hashlib
import sys


def get_md5_number(text):
	md5_hash = hashlib.md5(text.encode())
	md5_hex = md5_hash.hexdigest()
	return int(md5_hex, 16)


INPUT_FILE = sys.argv[1]
entries_handle = []
with open(INPUT_FILE) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		entries_handle.append(row[0])

length = len(entries_handle)

total = 0
for entry in entries_handle:
	hashValue = get_md5_number(entry)
	total += hashValue

winner = total % length
print(entries_handle[winner])
