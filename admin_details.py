#Admin Functions

from admin import Admin_Cred
from food_items import Food_Items
import random
import re
admin_info = dict()
food_info = dict()
class Admin_Details:
    admin_list = []
    food_list = []
    def add_admin(self):
        admin_username = input("Enter your Username :")
        while len(admin_username) <=5 :
            if len(admin_username) <= 5:
                print("Please enter a Username minimum of 6 characters :")
                admin_username = input("Enter your Username :")
            else:
                break
        print("*********************************")
        admin_password = input("Enter your Password :")
        while len(admin_password) <=7 :
            if len(admin_password) <= 7:
                print("Please enter a Password minimum of 8 characters :")
                admin_password = input("Enter your Password :")
            else:
                break
        print("*********************************")
        admin_name = input("Enter Your Name :")
        print("*********************************")
        
        admin_email = input("Enter your email :")
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        while True:
            if re.fullmatch(email_regex, admin_email):
                print("***********************************")
                break
            else:
                print("Please enter a valid email address !")
                admin_email = input("Enter your email :")
            
        admin_mobileno = input("Enter your mobile number :")
        mobileno_regex =r'\b^[7-9]\d{9}$\b'
        while True:
            if re.fullmatch(mobileno_regex, admin_mobileno):
                print("***********************************")
                break
            else:
                print("Please enter a valid mobile number !")
                admin_mobileno = input("Enter your mobile number :")
        print("Admin successfully created")
        admin_obj = Admin_Cred(admin_username ,admin_password,admin_name,admin_email,admin_mobileno)
        self.admin_list.append(admin_obj)
        admin_info[admin_username] = admin_obj
        
    def add_food_item(self):
        counter = 1
        no_of_items = int(input("Enter Number of Items to be added :"))
        for i in range(no_of_items):
            print("***********************************")
            print("Item",counter)
            food_id = random.randint(1111,9999)
            print("***********************************")
            food_name = input("Enter Item Name :")
            print("***********************************")
            food_price = float(input("Enter item Price :"))
            print("***********************************")
            food_qty = input("Enter the Quantity :")
            print("***********************************")
            discount = (input("Enter the Discount in percentage :"))
            print("***********************************")
            food_stock = input("Enter available Stock :")
            print("***********************************")
            food_obj = Food_Items(food_id,food_name,food_price,food_qty,discount,food_stock)
            self.food_list.append(food_obj)
            food_info[food_id] = food_obj
            counter = counter + 1
    
        return food_info
    def edit_food_item(self):
        for k,v in food_info.items():
            print("Item ID:",v.food_id,"|","Item Name:",v.food_name,"|","Item Price:",v.food_price,"|","Item Quantity:",v.food_qty,"|","Item Discount:",v.discount,"|","Item Stock:",v.food_stock)
        print("***********************************")
        edit_food_item_id = int(input("Enter the Item ID :"))
        if edit_food_item_id == v.food_id:
            pass
        else:
            print("***********************************")
            print("Item with this ID does not exist.")
            return False
        print("***********************************")
        while True:
            print("Select... \n1.UpItem Name \n2.Update Price \n3.Update Quantity \n4.Update Discount \n5.Update Stock\n6.Press 0 to return to the main menu")
            print("***********************************")
            choice_edit_food_item_id = int(input("Enter your choice :"))
            print("***********************************")
            if choice_edit_food_item_id == 1:
                for k,v in food_info.items():
                    if v.food_id == edit_food_item_id:
                        v.food_name = input("Enter new Item Name :")
                        print("***********************************")
                        print("Name Updated Successfully !")
                        print("***********************************")
            elif choice_edit_food_item_id == 2:
                for k,v in food_info.items():
                    if v.food_id == edit_food_item_id:
                        v.food_price = float(input("Enter new Item Price :"))
                        print("***********************************")
                        print("Price Updated Successfully !")
                        print("***********************************")
            elif choice_edit_food_item_id == 3:
                for k,v in food_info.items():
                    if v.food_id == edit_food_item_id:
                        v.food_qty = input("Enter new Quantity :")
                        print("***********************************")
                        print("Quantity Updated Successfully !")
                        print("***********************************")

            elif choice_edit_food_item_id == 4:
                for k,v in food_info.items():
                    if v.food_id == edit_food_item_id:
                        v.discount = input("Enter new Discount in percentage :")
                        print("***********************************")
                        print("Discount Updated Successfully !")
                        print("***********************************")

            elif choice_edit_food_item_id == 5:
                for k,v in food_info.items():
                    if v.food_id == edit_food_item_id:
                        v.food_stock = input("Enter new available Stock :")
                        print("***********************************")
                        print("Stock Updated Successfully !")
                        print("***********************************")
            elif choice_edit_food_item_id == 0:
                print("Redirecting to Main Menu...")
                break
            else:
                print("Wrong Choice, Please Try Again!")
                print("Redirecting.....")
                print("***********************************")
        return food_info

    def view_food_item(self):
        if len(food_info) == 0:
            print("Nothing to see here")
            print("***********************************")
        else:
            for k,v in food_info.items():
                print("Item ID:",v.food_id,"|","Item Name:",v.food_name,"|","Item Price:",v.food_price,"|","Item Quantity:",v.food_qty,"|","Item Discount:",v.discount,"|","Item Stock:",v.food_stock)

    def delete_food_item(self):
        for k,v in food_info.items():
            print("Item ID:",v.food_id,"|","Item Name:",v.food_name,"|","Item Price:",v.food_price,"|","Item Quantity:",v.food_qty,"|","Item Discount:",v.discount,"|","Item Stock:",v.food_stock)
        delete_food_item_id = int(input("Enter the Item ID :"))
        for k,v in food_info.items():
            if v.food_id == delete_food_item_id:
                del food_info[k]
                print("Item Deleted Successfully !")
            break