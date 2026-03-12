import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def show_menu():
    print("\n\tStore Menu\n"
          "\t----------\n"
          "1.\tList all products in store\n"
          "2.\tShow total amount in store\n"
          "3.\tMake an order\n"
          "4.\tQuit")


def get_choice_by_user():
    while True:
        try:
            user_choice = int(input("Please choose a number: "))
        except ValueError:
            print("Invalid choice\n")
            show_menu()
            continue
        if user_choice not in range(1, 5):
            print("Invalid choice\n")
            show_menu()
        else:
            return user_choice


def list_products_in_store(store):
    products = store.get_all_products()
    print("------")
    for index, product in enumerate(products, start=1):
        print(f"{index}. ", end="")
        product.show()
    print("------\n")


def show_total_amount_in_store(store):
    total_amount = store.get_total_quantity()
    print(f"Total of {total_amount} items in store\n")


def make_order(store):
    list_products_in_store(store)
    available_products = store.get_all_products()
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    while True:
        product_choice = input("Which product # do you want? ")
        product_amount = input("What amount do you want? ")
        if not product_choice:
            if shopping_list:
                total = store.order(shopping_list)
                if total:
                    print("********")
                    print(f"Order made! Total payment: ${int(total)}")
            break
        try:
            int(product_choice)
        except ValueError:
            print("Error adding product!\n")
            continue
        if int(product_choice) > len(available_products):
            print("Error adding product!\n")
            continue
        else:
            chosen_product = available_products[int(product_choice) - 1]
            shopping_list.append((chosen_product, product_amount))
            print("Product added to list!\n")


def start(store):
    while True:
        show_menu()
        menu_choice = get_choice_by_user()
        dispatch = {
            1: list_products_in_store,
            2: show_total_amount_in_store,
            3: make_order
        }
        if menu_choice == 4:
            exit()
        else:
            dispatch[menu_choice](store)


def main():
    start(best_buy)


if __name__ == "__main__":
    main()

