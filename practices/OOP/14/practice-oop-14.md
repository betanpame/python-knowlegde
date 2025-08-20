# Encapsulation and Access Control - Practice 14

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn Python's approach to encapsulation using naming conventions and property decorators to control access to class attributes.

## Objectives

- Understand public, protected, and private attributes
- Use naming conventions (_protected, __private)
- Create getter and setter methods
- Implement data validation and access control

## Your Tasks

1. **create_encapsulated_class()** - Create class with different access levels
2. **implement_getters_setters()** - Control attribute access
3. **add_validation()** - Validate data in setters
4. **demonstrate_name_mangling()** - Show private attribute behavior

## Example

```python
import re
from datetime import datetime, date

class BankAccount:
    """Bank account class demonstrating encapsulation."""
    
    # Class variable (public)
    bank_name = "Python Bank"
    
    def __init__(self, account_holder, initial_balance=0, account_type="checking"):
        """Initialize bank account."""
        # Public attributes
        self.account_holder = account_holder
        self.account_type = account_type
        self.created_date = date.today()
        
        # Protected attributes (single underscore - convention only)
        self._account_number = self._generate_account_number()
        self._transaction_history = []
        
        # Private attributes (double underscore - name mangling)
        self.__balance = 0
        self.__pin = None
        self.__is_frozen = False
        
        # Use setter for validation
        self.balance = initial_balance
    
    def _generate_account_number(self):
        """Generate account number (protected method)."""
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    def __log_transaction(self, transaction_type, amount, description=""):
        """Log transaction (private method)."""
        transaction = {
            'date': datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'description': description,
            'balance_after': self.__balance
        }
        self._transaction_history.append(transaction)
    
    # Property for balance (read-only from outside)
    @property
    def balance(self):
        """Get current balance."""
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        """Set balance with validation."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Balance must be a number")
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        
        old_balance = self.__balance
        self.__balance = amount
        
        if old_balance != amount:
            self.__log_transaction("balance_set", amount, "Balance updated")
    
    # Property for account number (read-only)
    @property
    def account_number(self):
        """Get account number (read-only)."""
        return self._account_number
    
    # Property for PIN with validation
    @property
    def pin(self):
        """PIN is write-only (cannot be read)."""
        raise AttributeError("PIN cannot be read for security reasons")
    
    @pin.setter
    def pin(self, new_pin):
        """Set PIN with validation."""
        if not isinstance(new_pin, str):
            raise TypeError("PIN must be a string")
        if not re.match(r'^\d{4}$', new_pin):
            raise ValueError("PIN must be exactly 4 digits")
        
        self.__pin = new_pin
        self.__log_transaction("pin_change", 0, "PIN changed")
    
    def _verify_pin(self, pin):
        """Verify PIN (protected method)."""
        return self.__pin is not None and self.__pin == pin
    
    def deposit(self, amount, description="Deposit"):
        """Deposit money to account."""
        if self.__is_frozen:
            raise RuntimeError("Account is frozen")
        
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.__balance += amount
        self.__log_transaction("deposit", amount, description)
        return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"
    
    def withdraw(self, amount, pin, description="Withdrawal"):
        """Withdraw money from account."""
        if self.__is_frozen:
            raise RuntimeError("Account is frozen")
        
        if not self._verify_pin(pin):
            raise ValueError("Invalid PIN")
        
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        
        self.__balance -= amount
        self.__log_transaction("withdrawal", amount, description)
        return f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}"
    
    def transfer(self, amount, target_account, pin, description="Transfer"):
        """Transfer money to another account."""
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount")
        
        # Withdraw from this account
        withdrawal_msg = self.withdraw(amount, pin, f"Transfer to {target_account.account_number}")
        
        # Deposit to target account
        target_account.deposit(amount, f"Transfer from {self.account_number}")
        
        return f"Transferred ${amount:.2f} to account {target_account.account_number}"
    
    def freeze_account(self, admin_code="ADMIN123"):
        """Freeze account (admin function)."""
        if admin_code != "ADMIN123":
            raise ValueError("Invalid admin code")
        
        self.__is_frozen = True
        self.__log_transaction("freeze", 0, "Account frozen by admin")
        return "Account frozen"
    
    def unfreeze_account(self, admin_code="ADMIN123"):
        """Unfreeze account (admin function)."""
        if admin_code != "ADMIN123":
            raise ValueError("Invalid admin code")
        
        self.__is_frozen = False
        self.__log_transaction("unfreeze", 0, "Account unfrozen by admin")
        return "Account unfrozen"
    
    def get_transaction_history(self, pin):
        """Get transaction history (requires PIN)."""
        if not self._verify_pin(pin):
            raise ValueError("Invalid PIN")
        
        return self._transaction_history.copy()  # Return copy to prevent modification
    
    def get_account_info(self):
        """Get basic account information (public method)."""
        status = "frozen" if self.__is_frozen else "active"
        return {
            'holder': self.account_holder,
            'account_number': self._account_number,
            'type': self.account_type,
            'balance': self.__balance,
            'status': status,
            'created': self.created_date.strftime('%Y-%m-%d'),
            'has_pin': self.__pin is not None
        }
    
    def __str__(self):
        """String representation."""
        status = " (FROZEN)" if self.__is_frozen else ""
        return f"{self.account_holder}'s {self.account_type} account: ${self.__balance:.2f}{status}"
    
    def __repr__(self):
        """Developer representation."""
        return f"BankAccount(holder='{self.account_holder}', balance={self.__balance}, type='{self.account_type}')"

# Example usage
def create_encapsulated_class():
    """Demonstrate encapsulation with BankAccount."""
    print("=== Encapsulation Demo ===")
    
    # Create accounts
    alice_account = BankAccount("Alice Smith", 1000, "checking")
    bob_account = BankAccount("Bob Johnson", 500, "savings")
    
    print(f"Created accounts:")
    print(f"  {alice_account}")
    print(f"  {bob_account}")
    
    # Set PINs
    alice_account.pin = "1234"
    bob_account.pin = "5678"
    print(f"\nPINs set for both accounts")
    
    # Practice public access
    print(f"\n=== Public Access ===")
    print(f"Alice's balance: ${alice_account.balance:.2f}")
    print(f"Alice's account number: {alice_account.account_number}")
    print(f"Bank name: {BankAccount.bank_name}")
    
    # Practice protected access (works but discouraged)
    print(f"\n=== Protected Access (discouraged) ===")
    print(f"Alice's account number (protected): {alice_account._account_number}")
    print(f"Transaction count: {len(alice_account._transaction_history)}")
    
    # Practice private access (fails with name mangling)
    print(f"\n=== Private Access Attempts ===")
    try:
        print(f"Alice's balance (direct): {alice_account.__balance}")
    except AttributeError as e:
        print(f"Direct private access failed: {e}")
    
    try:
        print(f"Alice's PIN: {alice_account.pin}")
    except AttributeError as e:
        print(f"PIN access failed: {e}")
    
    # Show name mangling (advanced)
    try:
        # This actually works due to name mangling
        mangled_balance = alice_account._BankAccount__balance
        print(f"Balance via name mangling: ${mangled_balance:.2f}")
        print("(Note: This is not recommended and breaks encapsulation)")
    except AttributeError:
        print("Name mangling access failed")
    
    return alice_account, bob_account

def test_validation_and_methods(alice_account, bob_account):
    """Practice validation and method access control."""
    print(f"\n=== Validation and Method Practices ===")
    
    # Practice deposit
    print(alice_account.deposit(200, "Paycheck"))
    
    # Practice withdrawal with correct PIN
    print(alice_account.withdraw(50, "1234", "Coffee"))
    
    # Practice withdrawal with wrong PIN
    try:
        alice_account.withdraw(50, "0000", "Unauthorized")
    except ValueError as e:
        print(f"Wrong PIN error: {e}")
    
    # Practice transfer
    print(alice_account.transfer(100, bob_account, "1234", "Loan payment"))
    
    # Practice validation errors
    print(f"\n=== Validation Error Practices ===")
    
    try:
        alice_account.deposit(-50)
    except ValueError as e:
        print(f"Negative deposit error: {e}")
    
    try:
        alice_account.withdraw(10000, "1234")
    except ValueError as e:
        print(f"Insufficient funds error: {e}")
    
    try:
        alice_account.pin = "123"  # Too short
    except ValueError as e:
        print(f"Invalid PIN error: {e}")
    
    try:
        alice_account.pin = "abcd"  # Not digits
    except ValueError as e:
        print(f"Non-digit PIN error: {e}")

def test_admin_functions(alice_account):
    """Practice admin functions and frozen account behavior."""
    print(f"\n=== Admin Functions Practice ===")
    
    # Freeze account
    print(alice_account.freeze_account())
    
    # Try operations on frozen account
    try:
        alice_account.deposit(100)
    except RuntimeError as e:
        print(f"Frozen account deposit error: {e}")
    
    try:
        alice_account.withdraw(50, "1234")
    except RuntimeError as e:
        print(f"Frozen account withdrawal error: {e}")
    
    # Unfreeze account
    print(alice_account.unfreeze_account())
    
    # Operations work again
    print(alice_account.deposit(100, "After unfreeze"))

def show_transaction_history(alice_account):
    """Show transaction history with PIN verification."""
    print(f"\n=== Transaction History ===")
    
    try:
        history = alice_account.get_transaction_history("1234")
        print(f"Transaction history for {alice_account.account_holder}:")
        for i, transaction in enumerate(history[-5:], 1):  # Show last 5 transactions
            date_str = transaction['date'].strftime('%Y-%m-%d %H:%M:%S')
            print(f"  {i}. {date_str} - {transaction['type']}: ${transaction['amount']:.2f}")
            print(f"     {transaction['description']} (Balance: ${transaction['balance_after']:.2f})")
    except ValueError as e:
        print(f"History access error: {e}")

# Practice the implementation
if __name__ == "__main__":
    # Create and test encapsulated classes
    alice, bob = create_encapsulated_class()
    
    # Practice validation and methods
    test_validation_and_methods(alice, bob)
    
    # Practice admin functions
    test_admin_functions(alice)
    
    # Show transaction history
    show_transaction_history(alice)
    
    # Final account info
    print(f"\n=== Final Account Information ===")
    alice_info = alice.get_account_info()
    bob_info = bob.get_account_info()
    
    print(f"Alice's account:")
    for key, value in alice_info.items():
        print(f"  {key}: {value}")
    
    print(f"\nBob's account:")
    for key, value in bob_info.items():
        print(f"  {key}: {value}")
    
    print(f"\nFinal balances:")
    print(f"  {alice}")
    print(f"  {bob}")
```

## Hints

- Use single underscore `_` for protected attributes (convention)
- Use double underscore `__` for private attributes (name mangling)
- Create properties for controlled access to private attributes
- Validate data in setter methods
- Use protected methods for internal operations

## Practice Cases

Your encapsulated class should:

- Prevent direct access to private attributes
- Validate data through setter methods
- Allow controlled access through properties
- Protect sensitive operations with authentication
- Maintain data integrity through encapsulation

## Bonus Challenge

Create a `SecureDocument` class with different access levels for reading, editing, and admin operations, using encryption for sensitive data!