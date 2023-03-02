print("WELCOME TO THE SYSTEM")
customer=input("enter customer name?")
commodity=input("enter commodity name?")
price=int(input("enter commodity price?"))
date=input("enter date DD-MM-YY?")
cashier=input("enter cashier's name?")

print("thank you for your input",customer)




def VAT():
    vat = 0.18
    return vat

def poc(price):
    tpoc= price * (1-VAT())
    return tpoc



print("customer name:",customer)
print("commodity name:",commodity)
print("net sale of product:",poc(price))
print("cashier:",cashier)
print("customer name:",customer)
print("date:",date)


print("Software developed by loerich nasaba")
print("copyright refactory 2023")
    






# customer_name = input("Enter the name of the customer: ")
# commodity_name = input("Enter the name of the commodity: ")
# commodity_price = float(input("Enter the price of the commodity: "))
# cashier_name = input("Enter the name of the cashier: ")
# sale_date = input("Enter the name of the cashier: ")


# # Define a dynamic function to calculate the net sale price after VAT
# def calculate_net_sale(price):
#     vat = 0.18
#     net_sale = price * (1 - vat)
#     return net_sale



# # Calculate the net sale price after VAT
# net_sale_price = calculate_net_sale(commodity_price)

# # Print the sale details
# print(f"NET sale of {commodity_name} is: {net_sale_price:.2f}")
# print(f"Customer name: {customer_name}")
# print(f"Cashier name: {cashier_name}")
# print(f"Sale date: {sale_date.strftime('%Y-%m-%d %H:%M:%S')}")

# # Print the software developer's name and copyright
# print("Software developed by loerich nasaba")
# print("copyright refactory 2023")




