from validate import *
def main():

    user = input("PLease enter username: ")
    
    
    valid = False
    while not valid:

        passwd = input("Please enter password: ")

        if not passcheck(passwd):

            print("Password does not meet requrements!\nPlease enter again: ")

        elif len(passwd) < 8:
            print("your password is too short")
                  
        else:
            passwd2 = input("Please re-enter password: ")
            if passwd == passwd2:

                valid = True

            else:
                print ('passwords do not match please enter again')

main()