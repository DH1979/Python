#Declaring and displaying variables
FirstName = input("Enter your First Name:")
LastName = input("Enter your Last Name:")
print(FirstName + " " + LastName)

#List of variable strings seperated by commas in one line
thislist = FirstName, LastName,
print(thislist)

#List of variable strings - one per line
thislist = [FirstName]
print(thislist)
thislist = [LastName]
print(thislist)

# Storing the variables as key value pairs and displaying the dictionary
thisdict =	{
  "FirstName": "Danielle",
  "LastName": "Harper",
}
print(thisdict)
