def pass_checker(S:str):
    special_chars = "-!@#$%^&*_+"

    hasNum= False
    hasAlpha= False
    lengthOkay = False
    lower_caseOkay = False
    upper_caseOkay = False
    hasSpecial = False
    
    
    if(len(S)) >= 10:
        lengthOkay = True
        #check 3
        for char in S:
            if char.lower() == char:
                lower_caseOkay = True
            else:
                upper_caseOkay = True
            
            if char in special_chars:
                hasSpecial = True
            elif char.isnumeric():
                hasNum = True
            else:
                hasAlpha = True
            #check 4
    if hasAlpha and hasNum and lengthOkay and lower_caseOkay and upper_caseOkay and hasSpecial:
        return "Your password is ingenious!"
    return "Password does not meet security standards."

password = input("Input: ")
print(pass_checker(password))

# Functionality: 5
# Performance: 5
# Quality: 3.5