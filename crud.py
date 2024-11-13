class ShoppingCart:
    purchase_id = 0
    product_name_list = ["Urad dal", "Salt", "Almond", "Cashew", "Chilli Powder", "Sunflower Oil"]
    product_price_list = [120, 85, 250, 267, 52, 190]

    def __init__(self, name):
        ShoppingCart.purchase_id += 1
        self.purchase_id = ShoppingCart.purchase_id
        self.name = name
        self.cart = []

    def count_cart_item(self):
        return len(self.cart)

    @classmethod
    def show_product(cls):
        print("\n--- Available Products ---")
        for i in range(len(cls.product_name_list)):
            print(f"{i + 1}. {cls.product_name_list[i]} - ₹{cls.product_price_list[i]}")

    def add_product(self, product_id, quantity):
        self.cart.append([
            ShoppingCart.product_name_list[product_id-1],
            ShoppingCart.product_price_list[product_id-1],
            quantity
        ])
        print("Product Added Successfully.....")

    def view_cart(self):
        cart_item_count = self.count_cart_item()
        total_price = 0
        print("\n--- Products in Cart ---")
        print("-----------------------------------------------------------")
        print(f"{'S.N0':<5} {'Product':<20} {'Price':<10} {'Quantity':<10}")
        print("-----------------------------------------------------------")
        for i in range(cart_item_count):
            price = self.cart[i][1]
            quantity = self.cart[i][2]
            total_price = price * quantity
            print(f"{i + 1:<5} {self.cart[i][0]:<20} ₹{price:<10} {quantity:<10}")
        print("-----------------------------------------------------------")
        print(f"Total Price: ₹{total_price}")

    def update_product_quantity(self, cart_id, quantity):
        self.cart[cart_id-1][2] = self.cart[cart_id-1][2]+quantity
        print("Quantity Updated Successfully.....")

    def remove_product(self, cart_id):
        self.cart.pop(cart_id-1)
        print("Product Removed from Cart Successfully.....")

    @staticmethod
    def shopping_cart_menu():
        name = input("Enter Customer Name: ").capitalize()
        purchase1 = ShoppingCart(name)
        while True:
            print("\n--- Shopping Cart Menu ---")
            print("1. Add Product to Cart")
            print("2. View Cart")
            print("3. Update Product Quantity")
            print("4. Remove Product from Cart")
            print("5. Exit")
            choice = int(input("Enter your Choice: "))
            if choice == 1:
                purchase1.show_product()
                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity: "))
                purchase1.add_product(product_id, quantity)

            elif choice == 2:
                if purchase1.count_cart_item() == 0:
                    print("*** Empty Cart ***")
                    continue
                purchase1.view_cart()

            elif choice == 3:
                if purchase1.count_cart_item() == 0:
                    print("*** Empty Cart ***")
                    continue
                purchase1.view_cart()
                cart_id = int(input("Enter S.No to update: "))
                quantity = int(input("Enter the new quantity: "))
                purchase1.update_product_quantity(cart_id, quantity)

            elif choice == 4:
                if purchase1.count_cart_item() == 0:
                    print("*** Empty Cart ***")
                    continue
                purchase1.view_cart()
                s_no = int(input("Enter S.No to remove from Cart: "))
                purchase1.remove_product(s_no)

            else:
                print(f"--- Thank You for Shopping, {name} ---\n--- Visit Us Again ---")
                break


ShoppingCart.shopping_cart_menu()
