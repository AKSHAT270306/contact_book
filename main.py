class Contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    def str_conv(self):
        return f"{self.name},{self.phone},{self.email}"
    def display(self):
        print (f"name:{self.name}")
        print (f"phone:{self.phone}")
        print (f"email:{self.email}")

contacts=[]   
def add_contacts():                         #to add contact
    name=input("enter name:")
    phone=input("enter phone no.:")
    email=input("enter email id:")
    c=Contact(name,phone,email)
    contacts.append(c)
    print("Contact Added Succesfully!!")

def view_all():                             #to view contact
    if len(contacts)==0:
        print("no contacts")
    else:
        for c in contacts:
            c.display()
            print("######################")

def search_contact(name):
    n=name.lower()
    if len(contacts)==0:
        print("no contacts")
    else:
        for c in contacts:
            if c.name.lower()==n :
                print("contact found")
                break
        else:
            print("contact not found")

def find(n):
        if len(contacts)==0:
            return None
        else:
            for c in contacts:
                if c.name.lower()==n:
                    return c
                    
            else:
                return None

def delete_contact(name):
    n=name.lower() 
    ans=find(n)
    if ans== None:
        print("no contact to delete!")
    else:
        contacts.remove(ans)
        print(ans.str_conv(),"deleted")

def update_contact(name):
    n=name.lower()
    ans=find(n)
    if ans== None:
        print("no contact to update!")
    else:
        print("what to change?")
        print("1)phone no.")
        print("2)email")
        print("3)both")
        x=int(input("enter a no.:"))
        if x==1:
            new_phone=input("enter phone:")
            ans.phone=new_phone
            print("updated!!")
        elif x==2:
            new_email=input("enter email:")
            ans.email=new_email
            print("updated!!")
        elif x==3:
            new_phone=input("enter phone:")
            ans.phone=new_phone
            new_email=input("enter email:")
            ans.email=new_email
            print("updated!!")
        else:
            print("choose valid no.")
def save_to_file():
    with open("contact.txt","w") as f:
        for c in contacts:
            f.write(c.str_conv())
            f.write("\n")

def load_from_file():
    try:
        with open("contact.txt","r") as f:  
            lines=f.readlines()
            for line in lines:
                line=line.strip("\n")
                l=line.split(",")
                name,phone,email=l
                c=Contact(name,phone,email)
                contacts.append(c)
    except FileNotFoundError:
        print("no file found")

load_from_file()
while True:
    print("1) Add Contact")
    print("2) View All")
    print("3) Search Contact")
    print("4) Delete Contact")
    print("5) Update Contact")
    print("6) Exit")
    option=int(input("Choose what You Want To Do:"))
    if option==1:
        add_contacts()
    elif option==2:
        view_all()
    elif option==3:
        name=input("enter the name")
        search_contact(name)
    elif option==4:
        name=input("enter the name")       
        delete_contact(name)
    elif option==5:
        name=input("enter name of person whose details you want to update:")
        update_contact(name)
    elif option==6:
        save_to_file()
        exit()
    else:
        print("invalid option")