import sys
import csv

number_of_indices = int(sys.argv[1])
index = str(sys.argv[2])
historical_prices = str(sys.argv[3])

indice_count = 0
chosen_index_values = []
selected_index_values = {}
weighted_values = {}

with open(historical_prices) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] == 'Symbol':
            continue
        elif row[0] == index:
            chosen_index_values.append(float(row[2]))
        else:
            if row[0] not in selected_index_values.keys():
                indice_count += 1
                if indice_count > number_of_indices:
                    continue
                selected_index_values[row[0]] = []
                weighted_values[row[0]] = []
            selected_index_values[row[0]].append(float(row[2]))

for i in range(0,len(chosen_index_values)):
    current_val = chosen_index_values[i]/number_of_indices
    for key in selected_index_values.keys():
        weighted_value = current_val/(selected_index_values[key][i])
        weighted_values[key].append(weighted_value)

print('Symbol, Weight')
for key in weighted_values.keys():
    sum = 0
    for num in weighted_values[key]:
        sum += num
    print(key+",", round(sum/len(chosen_index_values),3))

