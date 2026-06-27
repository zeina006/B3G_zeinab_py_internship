inventory={
    "pen":10,
    "pencil":15,
}
inventory["pen"]=inventory["pen"]+5
product="pencil"

if product in inventory:
    inventory[product]-=2
    print(product,"sold successfully")
else:
    print("Product not found:")
product="Keyboard"
if product in inventory:
    inventory[product]-=1
else:
    print("product not found")
print("Final inventory:",inventory)