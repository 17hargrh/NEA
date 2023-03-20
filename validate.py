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

    return all([has_capital, has_num, has_special, has_lower, has_space])