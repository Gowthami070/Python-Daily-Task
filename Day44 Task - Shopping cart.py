cart={
    "item1":{
        "name":"Laptop"
        "price":50000
        "quantity":1
        "catagory":"Electronics"
    }
    "item2":{
        "name":"Mouse"
        "price":1000
        "quantity":2
        "catagory":"Accessories"
    }
    "item3":{
        "name":"Keyboard"
        "price":2000
        "quantity":1
        "catagory":"Accessories"
    }
}
total=0
highest_total=0
highest_product=""

for item in cart.values():
    subtotal=item["price"]*item["quantity"]
    print(item["name"],"Subtotal:",subtotal)
    total=total+subtotal
    if subtotal>highest_subtotal:
        highest_subtotal=subtotal
        hightest_product=itam["name"]

print("Total cost:",total)
print("Hightest subtotal Product:",hightest_product)
if total>50000:
    discount=total*10/100
else:
    discount=0
final_amount=total-discount
print("Discount:",int(discount))
print("Final amount:",int(final_amount))
