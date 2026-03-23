from datasaveModule import saveData, savefooditem, saveOrder, storeOrder
import random
class Person:
    def __init__(self, name, gmail, username, password):
        self.name = name
        self.gmail = gmail
        self.username = username
        self.password = password

    @classmethod
    def login(cls, user_list):
        print("\nEnter your login info ")
        username = str(input("Enter your user name: "))
        password = str(input("Enter your password: "))
        for el in user_list:
            if el.username == username and el.password == password:
                print("\n--- login successfully ---")
                return el
        else:
            return -1



class Admin(Person):
    def __init__(self, name, gmail, username, password):
        super().__init__(name, gmail, username, password)
    
    @classmethod
    def createAdmin(cls, user_list):
        name = str(input("Enter your name: "))
        gmail = str(input("Enter your gmail: "))
        username = str(input("Enter your user name: "))
        password = str(input("Enter your password: "))
        adm = Admin(name, gmail, username, password)
        user_list.insert(0, adm)
        saveData(adm,"admin")
        print("\n--- Account Create ---")
    

class Employee(Person):
    def __init__(self, name, gmail, username, password):
        super().__init__(name, gmail, username, password)

class Worker(Employee):
    def __init__(self, name, gmail, username, password):
        super().__init__(name, gmail, username, password)

    @classmethod
    def createworker(cls, user_list):
        name = str(input("Enter your name: "))
        gmail = str(input("Enter your gmail: "))
        username = str(input("Enter your user name: "))
        password = str(input("Enter your password: "))
        adm = Worker(name, gmail, username, password)
        user_list.insert(0, adm)
        saveData(adm,"wrk")
        print("\n--- Account Create ---")
    
class DeliveryBoy(Employee):
    def __init__(self, name, gmail, username, password):
        super().__init__(name, gmail, username, password)

    @classmethod
    def createdelivery(cls, user_list):
        name = str(input("Enter your name: "))
        gmail = str(input("Enter your gmail: "))
        username = str(input("Enter your user name: "))
        password = str(input("Enter your password: "))
        adm = DeliveryBoy(name, gmail, username, password)
        saveData(adm,"delivery")
        user_list.insert(0, adm)
        print("\n--- Account Create ---")
    
#  FoodItem 



class FoodItem:
    def __init__(self, name, prices):
        self.name = name    
        self.prices = prices

    @classmethod
    def addFoodItems(cls, food):
        print("\nNow your going to add food items")
        name = str(input("Food item name: "))
        amount = int(input("Prices of food item: "))
        food.insert(0, FoodItem(name, amount))
        savefooditem(FoodItem(name,amount))
        print("\n--- add successfully ---")

    @classmethod
    def printFood(cls, food):
        print("Name\t\tPrices")
        k = 1
        for el in food:
            print(k, " ", el.name, "\t\t", el.prices)
            k += 1

    @classmethod
    def returnSingle(cls, food):
        cls.printFood(food)
        if not food:
            return -1
        ch = int(input("Select item: "))
        return food[ch - 1] if 1 <= ch <= len(food) else -1


#  Order 

class Order:
    def __init__(self, id, itemsName, prices, address):
        self.id = id
        self.status = 'Pending'
        self.itemsName = itemsName
        self.prices = prices
        self.address = address

    @classmethod
    def print_order_list(cls, orders):
        print("Id\tFood_Item\tAddress\t\tStatus")
        for el in orders:
            print(el.id, "\t", el.itemsName, "\t", el.address, "\t\t", el.status)


#  Customer 

class Customer(Person):
    def __init__(self, name, gmail, username, password, address):
        super().__init__(name, gmail, username, password)
        self.order_list = []
        self.address = address

    @classmethod
    def createcustomer(cls, user_list):
        name = str(input("Enter your name: "))
        gmail = str(input("Enter your gmail: "))
        username = str(input("Enter your user name: "))
        password = str(input("Enter your password: "))
        address=str(input("Enter your address: "))
        adm = Customer(name, gmail, username, password,address)
        user_list.insert(0, adm)
        saveData(adm,"cust")
        print("\n--- Account Create ---")

    def orderItem(self, food, Main_list):
        fi = FoodItem.returnSingle(food)
        if fi == -1:
            print("Invalid selection")
            return

        addr = input("Delivery address: ")
        oid = random.randint(1000, 9999)
        self.order_list.append(Order(oid, fi.name, fi.prices, addr))
        saveOrder(Order(oid,fi.name,fi.prices,addr))
        storeOrder(Order(oid,fi.name,fi.prices,addr), self.username)
        Main_list.append(Order(oid, fi.name, fi.prices, addr))
        print("Order placed successfully")
        return True

    def print_order(self):
        for i in range(len(self.order_list)):
            print(self.order_list[i].id, "\t", self.order_list[i].itemsName, "\t", self.order_list[i].status)

    def changeOrder(self, food, main_list):
        self.print_order()
        id = int(input("Type the id of order to it change"))
        i = -1
        for el in self.order_list:
            if el.id == id:
                i += 1
                break
            i += 1
        if i > -1:
            print("Which changing you make ")
            print('1- delete the order\n2- change the items\n3- changing address')
            choice = int(input("\nYour choice "))
            if choice == 1:
                del self.order_list[i]
            elif choice == 2:
                del self.order_list[i]
                self.orderItem(food, main_list)
            elif choice == 3:
                new_address = str(input("Enter the new address \n"))
                self.order_list[i].address = new_address
            else:
                self.changeOrder(food, main_list)
        else:
            print("Invalid id of items ")

    @classmethod
    def findItem(cls, id, cust):
        found = False
        for el in cust:
            for i in range(len(el.order_list)):
                if el.order_list[i].id == id:
                    el.order_list[i].status = "Delivered"
                    print(el.order_list[i].id, "  ", el.order_list[i].address, "  Delivered")
                    found = True
                    return
        if not found:
            print("Id does not exist")
