# 1. Create a new file called data_presenter.py.
# 2. Open the CupcakeInvoices.csv.
# 3. Loop through all the data and print each row.
# 4. Loop through all the data and print the type of cupcakes purchased.
# 5. Loop through all the data and print out the total for each invoice 
#    (Note: this data is not provided by the csv, you will need to calculate it. 
#     Also, keep in mind the data from the csv comes back as a string, 
#     you will need to convert it to a float. Research how to do this.).
# 6. Loop through all the data, and print out the total for all invoices combined.
# 7. Close your open file.
# 8. Challenge: Do some research and see if you can limit your floats to 
#   　never exceed to characters after the decimal point.

# 2.
open_file = open("CupcakeInvoices.csv")

# 3.
# for line in open_file:
#     print(line)

# 4.
# for line in open_file:
#     line = line.rstrip('\n').split(',')
#     print(line[2])

# 5.
# for line in open_file:
#     line = line.rstrip('\n').split(',')
#     number_of_cakes = float(line[3])
#     cake_price = float(line[4])
#     total_price = number_of_cakes * cake_price
#     print(total_price)

# 6.
# total_price = 0
# for line in open_file:
#     line = line.rstrip('\n').split(',')
#     number_of_cakes = float(line[3])
#     cake_price = float(line[4])
#     each_invoice = number_of_cakes * cake_price
#     total_price += each_invoice

# print(total_price)

# 7.
# open_file.close()

# 8.
# x = 9.55555
# print(round(x))

# Going Further
# Explore the graphing tools covered in today’s lecture. 
# See if you can implement one of them to display 
# the total income of chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.
# python3 --version
# python3 -m pip install -U matplotlib

# import matplotlib.pyplot as plt
# import numpy as np

# total_income_chocolate = 0
# total_income_vanilla = 0
# total_income_strawberry = 0

# for line in open_file:
#     line = line.rstrip('\n').split(',')
#     name_of_cake = line[2]
#     number_of_cakes = float(line[3])
#     cake_price = float(line[4])
#     each_invoice = number_of_cakes * cake_price
#     if name_of_cake == 'Chocolate':
#         total_income_chocolate += each_invoice
#     elif name_of_cake == 'Vanilla':
#         total_income_vanilla += each_invoice
#     elif name_of_cake == 'Strawberry':
#         total_income_strawberry += each_invoice

# x = np.array(["Chocolate", "Vanilla", "Strawberry"])
# y = np.array([round(total_income_chocolate), round(total_income_vanilla), round(total_income_strawberry)])

# plt.bar(x,y)
# plt.show()