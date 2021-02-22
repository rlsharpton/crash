import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '2466543.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)
    
    # Get high temps
    
    dates, pre_clean_highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = row[9]
        dates.append(current_date)
        pre_clean_highs.append(high)

    post_clean_highs = []
    for row in pre_clean_highs:
        nhigh = int(row)
        post_clean_highs.append(nhigh)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, post_clean_highs, c='red')

# format plot.
plt.title("Daily high temperatures, Jan 2021", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

#print(post_clean_highs)