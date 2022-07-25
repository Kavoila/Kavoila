# The Online psychiatrist.
################################
# This is just  a beginning  of what is to become an application dubbed "The only psychiatrist" to help mothers in the more remote and unaccessible areas to be able diagnose their children by their own.
# I am a begginner, I still have so much to learn 
#I'll all the critics, suggestions and advises.
#################################

from email.headerregistry import Address


while True:
    name = input("Please enter your name:")
    if name != "":
        break
Location = input("Enter your current location :")
phone = input(" Enter your phone number:")
while len(phone)!=10 :
    phone = input(" ooops! please Check and Enter ur phone number again:")
Temperature =int(input("What's the temperature of the child?:"))
if Temperature > 37:
    print("That's fever make the kid drink more water and rest:")
elif Temperature <=0 or Temperature <= 29:
    print("The kid is freezing:")
else:
    print("The kid is okay no need to worry")
Further_Assistance= input(" what other signs does the child show?:")
Address= input ("Incase of emergency please dial 911 or whatsapp us 0792572728,Okay?:")

Age = int(input(" How old is the baby: "))
try: 
  if Age >= 3:
    print("The kid would enjoy a walk in the park:")
  else:
   pass
except:
    Age =int.Age[0]
    if Age >= 3:
       print("The kid would enjoy a walk in the park:")
    elif Age <=4:
       print(" Keep the baby indoors, he/she is too young to be out here, end="")
    else:
     print ("for any further assistance, please reach us @ Kavoi_a or whatsapp us @ 0792572728",end="")




