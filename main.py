def passcheck(passwd):
    
    has_capital = False
    has_num = False
    has_special = False
    has_lower = False
    has_space = True
    
    for i in passwd:
        if i.isupper():
            has_capital = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_num = True
        elif not i.isalnum():
            has_special = True
        elif i.isspace():
            has_space = False 

def main():
    passwd = input("Please enter password: ")
        
    while not passcheck(passwd):
        passwd = input("Password does not meet requrements!\nPlease enter again: ")
    
    while len(passwd) < 8:
        passwd = input("Password is too short!\nPlease Re-enter password: ")
        break

    
        
    passwd2 = input("Please re-enter password: ")

    while passwd != passwd2:
        passwd2 = input("Passwords do not match\nPlease Re-enter: ")

main()