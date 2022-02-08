#Excercise 10 - part 2


#second attempt with loops- continue and break statements
attempts = ['2', '1', '0']
for attempts in attempts:
 pin = input("Enter your PIN")
 if pin != '1234':
    print('You have entered an incorrect pin. You have ' + attempts + ' attempts left.')
    continue
 elif pin == '1234':
    print('PIN accepted')
    break






#first attempt - without loops
#pin = input("Enter your PIN")
#if pin == '1234':
    #print("Success-continue with your withdrawl")
#elif:print('Incorrect pin. You have ' + attempt + ' attempts left.')
#else:
#pin = input("Enter your PIN")
#if pin == '1234':
    #print("Success-select amount of money you wish to withdraw")
#else: print("Incorrect PIN. Please try again - you have 2 attempts left")
#pin = input("Enter your PIN")
#if pin == '1234':
    #print("Success -select amount of money you wish to withdraw")
#else: print("Incorrect PIN. Please try again - you have 1 attempt left")
#pin = input("Enter your PIN")
#if pin == '1234':
    #print("Success - select amount of money you wish to withdraw")
#else: print("Incorrect PIN. You have used all your attempts. Your account is blocked. Please contact your bank")