from time import sleep

total = 0 #cost total
c = 0 #num of the products over the R$1000
name_p = "" #name of the more cheap product
price_p = 100000000 #price of the more cheap product

print("-----"*20)
print("")
print("THE MIGUEL SUPERMARKET")
print("")
print("-----"*20)

while True:
    name = input("Write the name of the product: ")
    price = float(input("Write the price of the product: "))
    
    if price > 1000:
        c += 1
    if price < price_p:
        name_p = name
        price_p = price
    
    total += price
    
    while True:
        cont = input("You want continue? [Y/N] ").strip()
        if cont == "Y" or cont == "N" or cont == "y" or cont == "n":
            break
        else:
            print("Write a valid answer.")
    
    if cont == "Y" or cont == "y":
        print("Ok! Renew!")
        sleep(0.5)
    else: 
        break

print(f"The cost total of this purchase is R${total}")
print(f"We have a {c} products costing more the R$1000")
print(f"The more cheap product is {name_p} costing R${price_p}")
