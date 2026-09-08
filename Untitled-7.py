products = ["bag"]
prices = ["900"]

while True:
    print("\n===== PRODUCT MENU =====")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Update Product Price")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add product
    if choice == 1:
        product = input("Enter product name: ")
        price = float(input("Enter product price: "))

        products.append(product)
        prices.append(price)

        print("Product added successfully!")

    # Display products
    elif choice == 2:
        if len(products) == 0:
            print("No products available.")
        else:
            print("\n--- Product List ---")
            for i in range(len(products)):
                print( products[i],prices[i])

    # Update product price
    elif choice == 3:
        if len(products) == 0:
            print("No products available.")
        else:
            print("\n--- Product List ---")
            for i in range(len(products)):
                print(products[i], prices[i])

            number = int(input("Enter product number to update: "))

            if 1 <= number <= len(products):
                new_price = float(input("Enter new price: "))
                prices[number - 1] = new_price
                print("Product price updated successfully!")
            else:
                print("Invalid product number.")
    
    # Serach Product            
    elif choice == 5:
         product = input("Enter product name to search: ")
         if product in product:
              print("Product is founded")
              index=products.index(product)
              print(products[index],prices[index])
   
                
         else:
            print("Product not available")
