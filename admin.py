

class Admin_Cred:
    def __init__(self,admin_username,admin_password,admin_name,admin_email,admin_mobileno):
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.admin_name = admin_name
        self.admin_email = admin_email
        self.admin_mobileno = admin_mobileno

    
    def __str__(self):
        return "Admin Username :{self.admin_username}\nAdmin Password :{self.admin_password}\nAdmin First Name :{self.admin_name} \nAdmin Email :{self.admin_email}\nAdmin Mobile :{self.admin_mobileno}"
    
    def get_admin_username(self):
        return self.admin_username

    def set_admin_username(self,admin_username):
        self.admin_username = admin_username

    def get_admin_password(self):
        return self.admin_password

    def set_admin_password(self,admin_password):
        self.admin_password = admin_password

    def get_admin_name(self):
        return self.admin_name

    def set_admin_name(self,admin_name):
        self.admin_name = admin_name

    def get_admin_email(self):
        return self.admin_email

    def set_admin_email(self,admin_email):
        self.admin_email = admin_email

    def get_admin_mobileno(self):
        return self.admin_mobileno

    def set_admin_mobileno(self,admin_mobileno):
        self.admin_mobileno = admin_mobileno