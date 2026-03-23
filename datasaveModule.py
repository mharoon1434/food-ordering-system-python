def storeOrder(order,name):
    filename =str(name+".txt")
    print(filename)
    if not order:
        return
    with open(filename,'a')as f:
        f.write(str(order.id))
        f.write("\n")
        f.write(order.status)
        f.write("\n")
        f.write(order.itemsName)
        f.write("\n")
        f.write(order.prices)
        f.write("\n")
        f.write(order.address)
        f.write("\n")
def putdataInfile(Ad1,f):
    f.write(Ad1.name)
    f.write("\n")
    f.write(Ad1.gmail)
    f.write("\n")
    f.write(Ad1.username)
    f.write("\n")
    f.write(Ad1.password)
    f.write("\n")
def saveData(Ad1, role):
        if role=="admin":
            with open("Admin.txt", 'a') as f:
                putdataInfile(Ad1,f)
        elif(role=="wrk"):
            with open("worker.txt",'a') as f:
                putdataInfile(Ad1,f)
        elif(role=="cust"):
            with open("customer.txt",'a')as f:
                putdataInfile(Ad1,f)
                f.write(Ad1.address)
                f.write("\n")
                storeOrder(Ad1.order_list, Ad1.name)
        elif(role=="delivery"):
            with open("Delivery.txt",'a') as f:
                putdataInfile(Ad1,f)
def savefooditem(fd):
    with open("foodItem.txt",'a')as f:
        f.write(fd.name)
        f.write("\n")
        f.write(fd.prices)
        f.write("\n")
def saveOrder(order):
    with open("Order.txt",'a')as f:
        f.write(str(order.id))
        f.write("\n")
        f.write(order.status)
        f.write("\n")
        f.write(order.itemsName)
        f.write("\n")
        f.write(order.prices)
        f.write("\n")
        f.write(order.address)
        f.write("\n")
