from classModule import Admin,Worker,DeliveryBoy,Customer,FoodItem,Order
def restoredData(file_name, role):
    with open(file_name,'r') as file:
        Ad1=[]
        while True:
            name=file.readline().strip()
            if not name:
                break     
            gmail=file.readline().strip()
            username=file.readline().strip()
            password=file.readline().strip()
            if role=="cust":
                address=file.readline().strip()
                Ad1.insert(0,Customer(name,gmail,username,password,address))
                Ad1[0].order_list=restoredSelf(Ad1[0].username)
            elif role=="admin":
                Ad1.insert(0,Admin(name,gmail,username,password))
            elif role=="wrk":
                Ad1.insert(0,Worker(name,gmail,username,password))
            elif role=="delivery":
                Ad1.insert(0,DeliveryBoy(name,gmail,username,password))
    return Ad1
def restoredFood():
    with open("fooditem.txt",'r') as file:
        food=[]
        while True:
            name=file.readline().strip()
            if not name:
                break     
            prices=file.readline().strip()
            food.append(FoodItem(name,prices))
    return food
def restoredSelf(username):
    filename = username + ".txt"
    if not filename:
        return
    with open(filename, 'r') as file:
        orders = []
        while True:
            id_str = file.readline().replace("\n", '').strip()
            
            if not id_str:  
                break
            ide = int(id_str)
            status = file.readline().strip()
            name = file.readline().strip()
            prices = file.readline().strip()
            address = file.readline().strip()
            
            orders.insert(0, Order(ide, name, prices, address))
    return orders
def restoredOrder():
    with open("Order.txt", 'r') as file:
        orders = []
        while True:
            id_str = file.readline().replace("\n", '').strip()
            
            if not id_str:  
                break
            
            ide = int(id_str)
            status = file.readline().strip()
            name = file.readline().strip()
            prices = file.readline().strip()
            address = file.readline().strip()
            
            orders.insert(0, Order(ide, name, prices, address))
    return orders

Ad1=restoredData("Admin.txt","admin")
wrk=restoredData("worker.txt", "wrk")
delivery=restoredData("Delivery.txt","delivery")
customer=restoredData("customer.txt", "cust")
orders =restoredOrder()
food=restoredFood()