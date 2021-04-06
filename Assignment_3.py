#........ and shoot for the Sky in you getting a big promotion & opportunity
#Enter Full Names

fname = input("First Name") #First Name
lname = input("last Name") #last Name
fullnames = (fname + " " + lname)

#Enter phone, email
phone = input("Enter Customer's Phone Number: ")

email = input("Enter Customer's email aaddress: ")


#price of a used car
price = 10000

has_good_credit = float(input ("What is your current creditscore: ") )
has_good_credit = int(has_good_credit)


if has_good_credit > 600:
    down_payment = 0.1 * price
else:
        down_payment = 0.2 * price
         

print("")
print("Full Names:"+" " +fullnames)
print("Phone: " +phone)
print("Email: " + email)
print("Down Payment:"+ " "+str(down_payment))
