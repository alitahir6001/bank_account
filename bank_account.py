class BankAccount:
    def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
        self.int_rate = int_rate
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount  # why do you hate me
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        # self.balance *=self.int_rate 
        self.balance = self.balance*self.int_rate + self.balance
        return self


account_1 = BankAccount(0.025, 1000) # these are numbers and don't need to be strings.
account_2 = BankAccount(0.125, 2000) # the default values for the Class parameters

print(account_1.balance)
print(account_2.balance)  # Checking to see if the account balances are running properly

account_1.deposit(50).deposit(100).deposit(200).withdraw(25).yield_interest().display_account_info()
account_2.deposit(150).deposit(500).withdraw(300).withdraw(200).withdraw(10).withdraw(20).yield_interest().display_account_info()


# Had to ask for help from Chris
# What I want -- to chain 3 deposits, 2 withdrawls, and yielded interest, and then display it.
# What I've tried -- to emulate my previous assignment display attributes/methods

# What I was doing wrong: i was manually passing a yield_interest rate in the function call, when I didn't need to
    # my yield_interest attributes were also a little screwy - You can see where I commented out what was incomplete. I just multiplied my exisisting balance with the interest rate I set when I instantiated the two accounts, but what i needed to do was add that yielded interest amount, back into my exisiting balance. 

    # Thanks Chris!!