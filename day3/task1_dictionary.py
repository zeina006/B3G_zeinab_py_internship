product={"pen": 8, "pencil": 15, "notebook": 40,"bag": 550,"scale": 10}
exp_product={product:price
             for product,price in product.items() 
             if price>100}
print(exp_product)