class Shop:

    def __init__(self, name):
        self.name = name
        self.exit_id = []
        self.info_id = []

    def welcome(self, stock, bike_name, cost):
        welcome_message = f"WELCOME TO {self.name} BIKE SHOP".upper()
        print(welcome_message)
        print("-" * len(welcome_message))
        print("You can choose a perfect bike that you want")
        print("-" * 45)

        latest_i = []
        for i in range(len(bike_name)):
            # bike_name is list like ['Thunder','Sun','Bear']
            print(f"{i + 1} - {bike_name[i]} is {cost[i]} TRY (Current stock is {stock[i]})")
            print("-" * 45)
            latest_i = i + 1

        print(f"{latest_i + 1} - Exit")
        print("-" * 45)

        self.exit_id = latest_i + 1


class MenuItem:
    # Models each bike

    def __init__(self, order_id, name, speed, typ, cost, stock):
        self.id = order_id
        self.name = name
        self.speed = speed
        self.type = typ
        self.cost = cost
        self.stock = stock


class BikeMenu:
    # Models the Menu with bike.

    def __init__(self, total_stock1, total_stock2, total_stock3):
        self.total_stock1 = total_stock1
        self.total_stock2 = total_stock2
        self.total_stock3 = total_stock3
        self.menu = [
            MenuItem(order_id=1, name="Thunder", speed="High", typ="Race", cost=7834, stock=self.total_stock1),
            MenuItem(order_id=2, name="Sun", speed="Medium", typ="Daily Life", cost=3899, stock=self.total_stock2),
            MenuItem(order_id=3, name="Bear", speed="High", typ="Mountain", cost=5789, stock=self.total_stock3)
        ]

    def get_name_info(self):
        # Returns all the names of the available menu items
        options = []
        for item in self.menu:
            options.append(item.name)
            # Output will be like : Thunder/Sun/Bear
        return options

    def get_cost_info(self):
        # Returns all the costs of the available menu items
        options = []
        for item in self.menu:
            options.append(item.cost)
            # Output will be like : Thunder/Sun/Bear
        return options

    def get_stock_info(self):
        # Returns all the stock information of the available menu items
        options = []
        for item in self.menu:
            options.append(item.stock)
            # if item.name == order_name:
        return options

    def get_speed_info(self):
        # Returns all the speed values of the available menu items
        options = []
        for item in self.menu:
            options.append(item.speed)

        return options

    def get_type_info(self):
        # Returns all the type of the available menu items
        options = []
        for item in self.menu:
            options.append(item.type)

        return options

    def find_bike(self, order_id):
        # Searches the menu for a specific bike by name
        # Returns that bike if it exists
        # Otherwise returns None
        for item in self.menu:
            if item.id == order_id:
                return item
        # print("Sorry that bike is not available. Please try again later.")

    def sell_bike(self, order_id, number, order_name):
        # CODES BETWEEN THESE LINES ARE NOT EFFECTIVE RIGHT NOW
        for item in self.menu:
            if item.id == order_id:
                item.stock -= number

                return item.stock
        # CODES BETWEEN THESE LINES ARE NOT EFFECTIVE RIGHT NOW

        print(f"You succesfully bought {number} '{order_name}'")

    @staticmethod
    def report(order_name, total_orders, amount, order_type, order_speed):
        # prints sale summary
        print("-" * 19)
        print("Your order summary:")
        print("-" * 19)
        total_amount = f"Total amount: {total_orders} x {amount} = {total_orders * amount} TRY"
        print("-" * len(total_amount))
        print(f"Order name: {order_name}")
        print(f"Order type: {order_type}")
        print(f"Order speed level: {order_speed}")
        print(f"Total orders: {total_orders}")
        print(total_amount)
        print("-" * len(total_amount))


class MoneyMachine:
    CURRENCY = "TRY"

    TRY_BANKNOTE_VALUES = {
        "200 TRY": 200,
        "100 TRY": 100,
        "50 TRY": 50,
        "20 TRY": 20,
        "10 TRY": 10,
        "5 TRY": 5,
        "1 TRY": 1
    }

    # TRY_COIN_VALUES = {
    #     "0.50 TRY": 0.50,
    #     "0.25 TRY": 0.25,
    #     "0.10 TRY": 0.10,
    # }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        # let's see current profit
        print(f"Money: {self.profit} {self.CURRENCY}")

    def process_coins(self, cost):

        # returns the total calculated from banknotes and coins inserted
        # if amount of inserted coins or banknotes is equal to cost during loop
        # it stops the loop, so user doesn't need to insert more coins.

        # while True:
        # print("How would you like to pay it ? (Banknote/Coin)")
        # choice = input("Enter your choice: ")
        # if choice.lower().capitalize() == "Coin":
        #     for coin in self.TRY_COIN_VALUES:
        #         self.money_received += int(input(f"How many {coin} ?: ")) * self.TRY_COIN_VALUES[coin]
        #         if self.money_received >= cost:
        #             print("That's enough")
        #             break
        #     return self.money_received
        #
        # if choice.lower().capitalize() == "Banknote":
        #     for banknote in self.TRY_BANKNOTE_VALUES:
        #         self.money_received += int(input(f"How many {banknote} ?: ")) * self.TRY_BANKNOTE_VALUES[banknote]
        #         if self.money_received >= cost:
        #             print("That's enough")
        #             break
        #     return self.money_received
        # else:
        #     print("\033[31mError! You entered invalid value. Please choose one of options.\033[m")
        #     continue

        for banknote in self.TRY_BANKNOTE_VALUES:
            self.money_received += int(input(f"How many {banknote} ?: ")) * self.TRY_BANKNOTE_VALUES[banknote]
            if self.money_received >= cost:
                print("That's enough")
                break
        return self.money_received

    def make_payment(self, cost):
        self.process_coins(cost=cost)
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {change} {self.CURRENCY} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False


is_active = True
while is_active:

    bike_shop = Shop("Gurur's")
    bike_menu = BikeMenu(total_stock1=15, total_stock2=120, total_stock3=30)
    money_machine = MoneyMachine()

    bike_names = bike_menu.get_name_info()
    bike_costs = bike_menu.get_cost_info()
    bike_stocks = bike_menu.get_stock_info()
    bike_speeds = bike_menu.get_speed_info()
    bike_types = bike_menu.get_type_info()

    # while True:

    bike_shop.welcome(stock=bike_stocks, bike_name=bike_names,
                      cost=bike_costs)

    print("What would you like to do ?")

    try:
        choice = int(input("Enter your choice: "))

        if choice == bike_shop.exit_id:
            print('\033[32mYou have succesfully exited the program.\033[m')
            is_active = False
            break

        how_many = int(input("How many bikes would you like to buy ?: "))

        if bike_menu.find_bike(choice) is None or how_many > bike_stocks[choice - 1]:
            print('\033[31mError. Please choose an available option.\033[m')

        print(
            f"Total cost of {how_many} '{bike_names[choice - 1]}' is {bike_costs[choice - 1] * how_many} TRY.")
        bike_item = bike_menu.find_bike(choice)
        sufficient_stock = bike_menu.get_stock_info()
        sufficient_money = money_machine.make_payment(bike_item.cost * how_many)
        if sufficient_money and sufficient_stock[choice - 1] >= how_many:
            print("-" * 35)
            print("\033[32mDone! We are preparing your order now.\033[m")
            print("-" * 35)
            # stock_after_purchase = bike_menu.sell_bike(order_id=bike_item.id, number=how_many,
            #                                            order_name=bike_names[choice - 1])
            # bike_menu.total_stock1 = stock_after_purchase
            print("Would you like to see your order summary ? (Yes/No)")
            choice2 = input("Enter your choice: ")
            if choice2.lower().capitalize() == "Yes":
                bike_menu.report(
                    order_name=bike_names[choice - 1],
                    total_orders=how_many,
                    amount=bike_item.cost,
                    order_type=bike_types[choice - 1],
                    order_speed=bike_speeds[choice - 1]
                )
                print("\033[32mThank you for choosing us\033[m")
                break
            elif choice2.lower().capitalize() == "No":
                print("\033[32mThank you for choosing us\033[m")
                continue
    except ValueError:
        print("Please enter integer number")
