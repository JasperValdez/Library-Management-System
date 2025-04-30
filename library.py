from abc import ABC, abstractmethod
from datetime import datetime, timedelta

#------------JASPER VALDEZ------------#
# Abstract class: LibraryItem
class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title
        self.borrower = None
        self.due_date = None
        self.borrow_date = None
        self.is_borrowed = False

    @abstractmethod
    def get_type(self):
        pass

#------------LIU ARBY GARCIA------------#
    def borrow(self, borrower_name, borrow_date=None):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
        else:
            self.borrower = borrower_name
            self.borrow_date = borrow_date if borrow_date else datetime.now()
            self.due_date = self.borrow_date + timedelta(days=14)
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed by {borrower_name}.")
            print(f"Borrowed on: {self.borrow_date.date()}, Due on: {self.due_date.date()}.")

    def return_item(self, return_date=None):
        if not self.is_borrowed:
            print(f"'{self.title}' is not borrowed.")
        else:
            if return_date is None:
                return_date = datetime.now()
            late_days = (return_date - self.due_date).days
            if late_days > 0:
                fee = late_days * 2  # 2 pesos per late day
                print(f"'{self.title}' returned by {self.borrower} on {return_date.date()}. Late fee: {fee} pesos")
            else:
                print(f"'{self.title}' returned by {self.borrower} on {return_date.date()}. No late fee.")
            # Reset item status
            self.borrower = None
            self.due_date = None
            self.borrow_date = None
            self.is_borrowed = False
            
#------------RON CACHOLA------------#

    def status(self):
        if self.is_borrowed:
            return (f"{self.title} ({self.get_type()}): Borrowed by {self.borrower}, "
                    f"Borrowed on {self.borrow_date.date()}, Due {self.due_date.date()}")
        else:
            return f"{self.title} ({self.get_type()}): Available"

# Subclasses
class Book(LibraryItem):
    def get_type(self):
        return "Book"

class Magazine(LibraryItem):
    def get_type(self):
        return "Magazine"

class DVD(LibraryItem):
    def get_type(self):
        return "DVD"
    
    
#------------KEN REYES------------#
# Library class
class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_inventory(self):
        for item in self.items:
            print(item.status())


#------------ARSENIO LARANANG------------#
lib = Library()
lib.add_item(Book("Python Programming"))
lib.add_item(Magazine("Tech Monthly"))
lib.add_item(DVD("Inception"))

print("------ INITIAL INVENTORY ------")
lib.show_inventory()
print()

# Borrow items
print("------ BORROWING ITEMS ------")
lib.items[0].borrow("Liu", datetime(2025, 4, 20))
lib.items[1].borrow("Ron", datetime(2025, 4, 25))
print()

# Inventory after borrowing
print("------ INVENTORY AFTER BORROWING ------")
lib.show_inventory()
print()

#------------KHRYZ ALABADO------------#
# Return items
print("------ RETURNING ITEMS ------")
lib.items[0].return_item(datetime(2025, 5, 10))  
lib.items[1].return_item(datetime(2025, 5, 7))  
print()

# Final inventory
print("------ FINAL INVENTORY ------")
lib.show_inventory()
