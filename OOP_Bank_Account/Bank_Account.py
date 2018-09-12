# class:

class Account:

    def __init__(self,file_path):
        self.file_path=file_path
        with open(file_path, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self, amount):
        self.balance=self.balance+amount

    def write_to_file(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.balance))

account=Account("balance.txt")

class Checking(Account):

    """this is doc string - this class generates checking account object"""

    # class variable - rarely used
    type="checking"

    def __init__(self, file_path,fee):
        Account.__init__(self,file_path)
        #  or super().__init__(file_path)

        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance-amount-self.fee

checking=Checking("balance.txt",1)
checking.transfer(200)
print(checking.balance)
checking.write_to_file()
print(checking.__doc__)

# instantiation - creating object instance