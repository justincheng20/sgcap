import sys
import csv

number_of_indices = int(sys.argv[1])
index = str(sys.argv[2])
historical_prices = str(sys.argv[3])
# print('This message will be displayed on the screen.')
print("ok" + str(number_of_indices) + index + historical_prices)

indice_count = 1
# use a dictionary?
chosen_index_values = [5,3]
selected_index_values = {}

with open(historical_prices) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row[-1])
        # print(row[0])
        print(indice_count)
        print(number_of_indices)
        if row[0] == 'Symbol':
            continue
        if indice_count == number_of_indices:
            continue
        elif row[0] == index:
            # do something
            # print("index")
            chosen_index_values[row[0]].append(row[2])
        else:
            if row[0] not in selected_index_values.keys():
                selected_index_values[row[0]] = []
                indice_count += 1
            selected_index_values[row[0]].append(row[2])
      

chosen_slope = (chosen_index_values[-1] - chosen_index_values[0])/len(chosen_index_values) 
print(chosen_index_values)
print('symbol', 'weight')
for key in selected_index_values.keys():
    val = (float(selected_index_values[key][-1]) - float(selected_index_values[key][0]))/len(selected_index_values[key]) 
    print(key, val/chosen_slope)

# original_stdout = sys.stdout # Save a reference to the original standard output

# with open('filename.txt', 'w') as f:
#     sys.stdout = f # Change the standard output to the file we created.
#     print('This message will be written to a file.')
#     sys.stdout = original_stdout # Reset the standard output to its original value