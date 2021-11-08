from GymManager import GymManager
from Customer import Customer

print("^^^^^^Gym Manager Portal^^^^^^")
print("Hello admin,please select a option from menu")


def menu():
    print(" 1.create member")
    print(" 2.view member")
    print(" 3.delete member")
    print(" 4.update member")
    print(" 5.create regimen")
    print(" 6.view regimen")
    print(" 7.delete regimen")
    print(" 8.update regimen")
    print(" 9.logout")
    print("\nEnter your choice: ")

menu()

while(True):
    option = int(input())
    if option ==1:
            name = str(input("enter members name :"))
            age = str(input("enter members age :"))
            gender = str(input("enter your gender :"))
            phoneNo = str(input("enter your phoneNo :"))
            email = str(input("enter your email :"))
            bmi = str(input("enter your bmi :"))
            if bmi < '18.5':
                r = {'mon': 'chest','Tue': 'Biceps','Wed': 'Rest','Thu': 'Back','Fri': 'Triceps','sat': 'Rest','Sun': 'Rest'}
            elif bmi < '25':
                r ={'mon': 'chest','Tue': 'Biceps','Wed': 'cardio/Abs','Thu': 'Back','Fri': 'Triceps','sat': 'Legs','Sun': 'Rest'}
            elif bmi < '30':
                r = {'mon': 'chest','Tue': 'Biceps','Wed': 'Abs/Cardio','Thu': 'Back','Fri': 'Triceps','sat': 'Legs','Sun': 'cardio'}
            elif bmi >= '30':
                r = {'mon': 'chest','Tue': 'Biceps','Wed': 'Cardio','Thu': 'Back','Fri': 'Triceps','sat': 'Cardio','Sun': 'Cardio'}
            duration = str(input("enter your duration months :"))
            customer = Customer(name,age,gender,phoneNo,email,bmi,duration)
            GymManager.regimen[phoneNo] = r
            GymManager.addCustomer(customer)

    elif option == 2:
        check_num = input("enter phone number of member :")
        print("Name\tAge\tGender\tPhoneNo\tEmail\tBmi\tDuration")
        for cusid in GymManager.customers.keys():
            if cusid == check_num:
                customer = GymManager.customers[cusid]
                name = customer.getName()
                age = customer.getAge()
                gender = customer.getGender()
                phoneNo = customer.getPhoneNo()
                email = customer.getEmail()
                bmi = customer.getBmi()
                duration = customer.getDuration()
                print(name + "\t" +age+ "\t" +gender+ "\t" +phoneNo+ "\t" +email+ "\t" +bmi+ "\t" +duration)
        print("\n")

    elif option == 3:
        check_num = input("enter phone number of member you want to delete :")
        try:
            for cusid in GymManager.customers.keys():
                if cusid == check_num:
                    print("member deleted")
            GymManager.customers.pop(check_num)
        except:
            print("number doesn't exist\n")

    elif option == 4:
        check = input("enter your phone number :")
        exr = input("enter the number you want to extend or revoke :")
        if exr == "extend":
            for cusid in GymManager.customers.keys():
                customer = GymManager.customers[cusid]
                if cusid == check:
                    dur = customer.getDuration()
                    s = int(dur)+int(input("enter the number of month you want to extend :"))
                    res = str(s)
                    customer.setDuration(res)
        elif exr == "revoke":
            for cusid in GymManager.customers.keys():
                customer = GymManager.customers[cusid]
                if cusid == check:
                    customer.setDuration('0')
                    print("membership revoked")


    elif option == 5:
        phn = input("enter the phone number of a membeer you want to create regimen of :")
        for i in GymManager.regimen:
            if i == phn:
                for j in GymManager.regimen[i]:
                    GymManager.regimen[i][j]=input(j+":")

    elif option == 6:
        check_num = input("enter phone number of member")
        for i in GymManager.regimen:
            if i == check_num:
                for key,val in GymManager.regimen[i].items():
                    print(key,":",val)
        print("\n")
            
    elif option == 7:
        check_num = input("enter phone number of memeber :")
        for i in GymManager.regimen:
            if i == check_num:
                print("regimen deleted!!")
        GymManager.regimen.pop(check_num)
        print("\n")

    elif option == 8:
        check_num = input("enter the members phone number you want to update :")
        for i in GymManager.regimen:
            if i == check_num:
                d = input("enter the day which u want to update :")
                for j in GymManager.regimen[i]:
                    if j == d:
                        GymManager.regimen[i][j]=input("enter the workout :")
                        print("updated succcessfully!!")
        print("\n")

    elif option == 9:
        break

    else:
        print("please enter a valid number")
    menu()

def memmenu():
    print("\n*****Member portal*****\n")
    print("1. my regimen")
    print("2. my profile")
    print("3. exit")
    print("\nEnter your choice :")

memmenu()
while(True):
    option = int(input())
    if option == 1:
        p= input("enter your phone number :")
        print("^^ your regimen based on your bmi ^^")
        for i in GymManager.regimen:
            if i == p:
                for key,val in GymManager.regimen[i].items():
                    print(key,":",val)
        print("\n")

    elif option == 2:
        p = input("enter your phone number:")
        try:
            for cusid in GymManager.customers.keys():
                if cusid == p:
                    customer = GymManager.customers[cusid]
                    name = customer.getName()
                    age = customer.getAge()
                    gender = customer.getGender()
                    phoneNo = customer.getPhoneNo()
                    email = customer.getEmail()
                    bmi = customer.getBmi()
                    duration = customer.getDuration()
                    print("********your profile*******")
                    print("name:",name,"\nage:",age,"\ngender:",gender,"\nphoneNo:",phoneNo,"\nemail:",email,"\nbmi:",bmi,"\nduration:",duration)
            
        except:
            print("no user with this phone number exit")

    elif option == 3:
        break

    else:
        print("please enter a valid number")
    memmenu()















