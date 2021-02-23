import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = '2466543.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

highs = []
for row in reader:
    try:
        high = row.lstrip(')