import sys
import csv

number_of_indices = int(sys.argv[1])
index = str(sys.argv[2])
historical_prices = str(sys.argv[3])
# print('This message will be displayed on the screen.')
print("ok" + str(number_of_indices) + index + historical_prices)

indice_count = 1

with open(historical_prices) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        # print(row[0])
        print(indice_count)
        print(number_of_indices)
        if indice_count == number_of_indices:
            print("ending")
            break
        elif row[0] == index:
            # do something
            print("index")
        else:
            indice_count += 1
            print("!")

# original_stdout = sys.stdout # Save a reference to the original standard output

# with open('filename.txt', 'w') as f:
#     sys.stdout = f # Change the standard output to the file we created.
#     print('This message will be written to a file.')
#     sys.stdout = original_stdout # Reset the standard output to its original value