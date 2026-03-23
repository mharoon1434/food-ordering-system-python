from classModule import Admin,Worker,DeliveryBoy,Customer,FoodItem,Person,Order
import random
def print_main(Ad1,role):
    print("\n--- LOGIN/SIGNIN MENU ---")
    print('1- login \n2- create account ')
    choice = int(input("\nYour choice: "))

    if choice == 1:
        if role=="admin":
            el=Admin.login(Ad1)
        elif role=="wrk":
            el=Worker.login(Ad1)
        elif role=="cust":
            el=Customer.login(Ad1)
        elif role =="delivery":
            el=DeliveryBoy.login(Ad1)
    elif choice == 2:
        if role=="admin":
            Admin.createAdmin(Ad1)
        elif role=="wrk":
            Worker.createworker(Ad1)
        elif role=="delivery":
            DeliveryBoy.createdelivery(Ad1)
        elif role=="cust":
            Customer.createcustomer(Ad1)
        print('Now login to your account ')
        el = Person.login(Ad1)
    else:
        return False
    return el


#  Admin Menu 

def adminRelated(current, Ad1, food, wrk, delivery, cust, order):
    print("\n--- ADMIN MENU ---")
    print(f"Welcom {current.name} as Admin\n")
    print("Add and delivery fodd items\n1- check order \n2- add food items\n3- check the available food items\n0- employee manu\n")
    ch = int(input('Your choice: '))
    if ch == 1:
        Order.print_order_list(order)
        print_back_track(current, Ad1, wrk, delivery, cust, food, order)
    elif ch == 2:
        FoodItem.addFoodItems(food)
        print_back_track(current, Ad1, wrk, delivery, cust, food, order)
    elif ch == 3:
        print("Name\t\tPrices")
        FoodItem.printFood(food)
        print_back_track(current, Ad1, wrk, delivery, cust, food, order)
    elif ch == 0:
        mainManu(Ad1, wrk, delivery, cust, food, order)
    else:
        adminRelated(current, Ad1, food, wrk, delivery, cust, order)


#  Worker Menu 

def workRelated(current, Ad1, food, wrk, delivery, cust, order):
    print("\n--- Worker MENU ---")
    print(f"Welcom {current.name} as worker\n")
    print("Add and check fodd items\n1- add food items\n2- check the available food items\n0- employee manu\n")
    ch = int(input('Your choice: '))
    if ch == 1:
        FoodItem.addFoodItems(food)
        print_back_track_wrk(current, Ad1, wrk, delivery, cust, food, order)
    elif ch == 2:
        print("Name\t\tPrices")
        FoodItem.printFood(food)
        print_back_track_wrk(current, Ad1, wrk, delivery, cust, food, order)
    elif ch == 0:
        mainManu(Ad1, wrk, delivery, cust, food, order)
    else:
        workRelated(current, Ad1, food, wrk, delivery, cust, order)


#  Delivery Menu 

def deliveryRelated(current, Ad1, food, wrk, delivery, cust, order):
    print("\n--- Delivery Boy MENU ---")
    print(f"Welcom {current.name} as delivery boy\n")
    print("Check pending order and deliver fodd items\n1- pending orders\n2- deliver food items\n0- employee manu\n")
    ch = int(input('Your choice: '))
    if ch == 1:
        j = 0
        for i in range(len(order)):
            if order[i].status == 'Pending':
                j += 1
                print(order[i].id, "\t", order[i].itemsName, "\t", order[i].status)
        if j == 0:
            print("All food item are deliver")
        else:
            print_back_track_delivery(current, Ad1, cust, food, order, wrk, delivery)
    elif ch == 2:
        Order.print_order_list(order)
        id = int(input("Enter the id of food item your going to deliver: "))
        Customer.findItem(id, cust)
        for i in range(len(order)):
            if order[i].id == id:
                order[i].status = "Delivered"
        print_back_track_delivery(current, Ad1, cust, food, order, wrk, delivery)
    elif ch == 0:
        mainManu(Ad1, wrk, delivery, cust, food, order)
    else:
        deliveryRelated(current, Ad1, food, wrk, delivery, cust, order)

#  Backtrack Functions 

def print_back_track(current, Ad1, wrk, delivery, cust, food, order):
    print("\nWhere your go\n1- remain in Admin manu\n2- employee manu\n0- main manu\n")
    choice = int(input("Your choice: "))
    if choice == 1:
        adminRelated(current, Ad1, food, wrk, delivery, cust, order)
    elif choice == 0:
        mainManu(Ad1, wrk, delivery, cust, food, order)
    elif choice == 2:
        main_manu_emp(Ad1, food, wrk, delivery, cust, order)
    else:
        print_back_track(current, Ad1, wrk, delivery, cust, food, order)


def print_back_track_wrk(current, Ad1, wrk, delivery, cust, food, order):
    print("\nWhere your go\n1- remain in worker manu\n2- employee manu\n0- main manu\n")
    choice = int(input("Your choice: "))
    if choice == 1:
        workRelated(current, Ad1, food, wrk, delivery, cust, order)
    elif choice == 0:
        mainManu(Ad1, wrk, delivery, cust, food, order)
    elif choice == 2:
        main_manu_emp(Ad1, food, wrk, delivery, cust, order)
    else:
        print_back_track(current, Ad1, wrk, delivery, cust, food, order)


def print_back_track_delivery(current, Ad1, cust, food, order, wrk, delivery):
    print("\nWhere you go\n1- remain delivery manu\n0- main manu")
    choice = int(input("Your choice: "))
    if choice == 1:
        deliveryRelated(current, Ad1, food, wrk, delivery, cust, order)
    elif choice == 0:
        mainManu(Ad1, wrk, delivery, cust, food, order)
    else:
        print_back_track_delivery(current, Ad1, cust, food, order, wrk, delivery)


#  Customer Menu 

def customerRelated(current, Ad1, cust, food, order, wrk, delivery):
    print(f"\nHi {current.name} order your favorite dash ")
    print('1- order food items\n2- order details\n3- change order\n0- main manu')
    choice = int(input("\nYour choice: "))
    if choice == 0:
        mainManu(Ad1, wrk, delivery, cust, food, order)
    elif choice == 1:
        orderitm = current.orderItem(food, order)
        if orderitm:
            print_back_track_customer(current, Ad1, cust, food, order, wrk, delivery)
        else:
            print("Sorry no food items exist ")
            customerRelated(current, Ad1, cust, food, order, wrk, delivery)
    elif choice == 2:
        print("\nId\tFood-Name\tStatus")
        current.print_order()
        print_back_track_customer(current, Ad1, cust, food, order, wrk, delivery)
    elif choice == 3:
        current.changeOrder(food, order)
        print_back_track_customer(current, Ad1, cust, food, order, wrk, delivery)


def print_back_track_customer(current, Ad1, cust, food, order, wrk, delivery):
    print("\nWhere you go\n1- remain in customer manu\n0- main manu")
    choice = int(input("Your choice: "))
    if choice == 1:
        customerRelated(current, Ad1, cust, food, order, wrk, delivery)
    elif choice == 0:
        mainManu(Ad1, wrk, delivery, cust, food, order)
    else:
        print_back_track_customer(current, Ad1, cust, food, order, wrk, delivery)


#  Main Employee Menu 

def main_manu_emp(Ad1, food, wrk, delivery, cust, order):
    print("\n---- Employee Manu ----")
    print("1- Admin\n2- worker \n3- delivery person\n0- main manu")
    choice = int(input("\nYour choice: "))
    if choice == 1:
        current_Admin = print_main(Ad1,role="admin")
        if current_Admin:
            adminRelated(current_Admin, Ad1, food, wrk, delivery, cust, order)
        else:
            main_manu_emp(Ad1, food, wrk, delivery, cust, order)
    elif choice == 2:
        current_wrk = print_main(wrk,role="wrk")
        if current_wrk:
            workRelated(current_wrk, Ad1, food, wrk, delivery, cust, order)
        else:
            main_manu_emp(Ad1, food, wrk, delivery, cust, order)
    elif choice == 3:
        current_delivery = print_main(delivery,role="delivery")
        if current_delivery:
            deliveryRelated(current_delivery, Ad1, food, wrk, delivery, cust, order)
        else:
            main_manu_emp(Ad1, food, wrk, delivery, cust, order)
    elif choice == 0:
        mainManu(Ad1, wrk, delivery, cust, food, order)
    else:
        mainManu(Ad1, wrk, delivery, cust, food, order)


#  Main Menu 

def mainManu(Ad1, wrk, delivery, cust, food, order):
    print("\n--- MAIN MENU ---")
    print('Select your categorizes\n1- employee\n2- customer\n0- return')
    num = int(input("\nYour choice: "))
    if num == 1:
        main_manu_emp(Ad1, food, wrk, delivery, cust, order)
    elif num == 2:
        current_customer = print_main(cust,role="cust")
        if current_customer:
            customerRelated(current_customer, Ad1, cust, food, order, wrk, delivery)
        else:
            mainManu(Ad1, wrk, delivery, cust, food, order)
    elif num==0:
        return
    else:
        mainManu(Ad1, wrk, delivery, cust, food, order)
