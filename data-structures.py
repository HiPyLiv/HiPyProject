with open("Directory.txt", 'r') as f:
    names = [line.partition("\t")[0] for line in f]

counting_dict = {}
for name in names:
    if name in counting_dict:
        counting_dict[name] += 1
    else:
        counting_dict[name] = 1

common_name = max(counting_dict, key=counting_dict.get)

print("Most common name: ", common_name)
print("Number of occurrences: ", counting_dict[common_name])
