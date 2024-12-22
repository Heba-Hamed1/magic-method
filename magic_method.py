class Customer:
    
    def __init__(self, name, balance):  
        self.name = name
        self.balance = balance
        print("")
        
    def __str__(self):
        return 'Customer: ' + str(self.name) + ', balance: ' + str(self.balance)
    
    def __repr__(self):
        return f"Customer(name={self.name}, balance={self.balance})"
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    def __le__(self, other):
        return self.balance <= other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance
 
    def __ge__(self, other):
        return self.balance >= other.balance
    

    

customer1 = Customer("Ali", 10)
customer2 = Customer("Mona", 25)
customer3 = Customer("Amr", 10)


print(str(customer1))  


print(repr(customer2))  

print(customer1 == customer2)  
print(customer1 == customer3)  

print(customer2 < customer1)   
print(customer1 < customer3)   

print(customer2 <= customer1) 
print(customer1 <= customer3)  

print(customer1 > customer2)   
print(customer2 > customer3)  

print(customer1 >= customer2)  
print(customer1 >= customer3)  




