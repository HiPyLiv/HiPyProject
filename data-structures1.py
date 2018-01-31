# 1. Import the data.
# 2. Extract the first names
# 3. Count frequencies of first names
# 4. Find the name with the most occurrences.
# 5. Give an output.

with open("Directory.txt", "r") as f:
    splitlines = [line.partition("\t") for line in f]

firstnames = [line[0] for line in splitlines]

countingdict = {}
for name in firstnames:
    if name in countingdict:
        countingdict[name] += 1
    else:
        countingdict[name] = 1

mostcommon = max(countingdict, key=countingdict.get)

print("The most common name is: ", mostcommon)
print("The number of occurrences is: ", countingdict[mostcommon])
