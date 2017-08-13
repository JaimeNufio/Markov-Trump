from collections import defaultdict

data = [(2010,3),(2010,5),(2007,6),(2006,4)]
d = defaultdict(list)


for year, month in data:
    d[year].append(month);

print(d[2010])
