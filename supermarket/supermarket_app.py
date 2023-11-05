# Date: June 2023
# author: Selam Mitike

import tkinter as tk
from tkinter import ttk
from grocery_product import GroceryProduct
from dairy_product import DairyProduct
from beverage import Beverage
from enums import SugarLevel, Fat

class SupermarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket")
        self.cart = []
        self.budget = 0

        self.product_name_label = ttk.Label(root, text="Product Name:")
        self.product_name_label.grid(row=0, column=0)
        self.product_name_entry = ttk.Entry(root)
        self.product_name_entry.grid(row=0, column=1)

        self.product_price_label = ttk.Label(root, text="Product Price:")
        self.product_price_label.grid(row=1, column=0)
        self.product_price_entry = ttk.Entry(root)
        self.product_price_entry.grid(row=1, column=1)

        self.shop_discount_label = ttk.Label(root, text="Shop Discount (%):")
        self.shop_discount_label.grid(row=2, column=0)
        self.shop_discount_entry = ttk.Entry(root)
        self.shop_discount_entry.grid(row=2, column=1)

        self.budget_label = ttk.Label(root, text="Budget:")
        self.budget_label.grid(row=3, column=0)
        self.budget_entry = ttk.Entry(root)
        self.budget_entry.grid(row=3, column=1)

        self.add_to_cart_button = ttk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.grid(row=4, columnspan=2)

        self.cart_tree = ttk.Treeview(root, columns=("Product Name", "Price", "Discount", "Budget", "Quantity"))
        self.cart_tree.grid(row=5, columnspan=2)
        self.cart_tree.heading("#1", text="Product Name")
        self.cart_tree.heading("#2", text="Price")
        self.cart_tree.heading("#3", text="Discount")
        self.cart_tree.heading("#4", text="Budget")
        self.cart_tree.heading("#5", text="Quantity")

        self.error_label = ttk.Label(root, text="")
        self.error_label.grid(row=6, columnspan=2)

    def add_to_cart(self):
        product_name = self.product_name_entry.get()
        product_price = self.product_price_entry.get()
        shop_discount = self.shop_discount_entry.get()
        budget = self.budget_entry.get()

        try:
            product_price = float(product_price)
            shop_discount = float(shop_discount)
            budget = float(budget)
        except ValueError:
            self.error_label.config(text="Please provide valid product details.")
            return

        if product_name and product_price > 0:
            if shop_discount > 0:
                product_price *= (1 - shop_discount / 100)

            if self.budget == 0:
                self.budget = budget
            if product_price <= self.budget:
                product = GroceryProduct(product_name, product_price, shop_discount)

                # Calculate quantity based on remaining budget
                quantity = int(self.budget // product_price)

                self.cart.append((product, quantity))
                self.update_cart_display()
                self.budget -= product_price * quantity
                self.budget_entry.delete(0, tk.END)
                self.budget_entry.insert(0, self.budget)
                self.error_label.config(text="The item's price does not exceed your budget.")
            else:
                self.error_label.config(text="The item's price exceeds your budget.")
        else:
            self.error_label.config(text="Please provide valid product details.")

    def update_cart_display(self):
        self.cart_tree.delete(*self.cart_tree.get_children())

        for item, quantity in self.cart:
            self.cart_tree.insert("", "end", values=(item.name, item.price, item.discount, self.budget, quantity))

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketApp(root)
    root.mainloop()
