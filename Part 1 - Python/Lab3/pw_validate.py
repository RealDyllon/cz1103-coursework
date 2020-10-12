pw_len_pass = False
pw_upper_pass = False
pw_lower_pass = False
pw_digit_pass = False
pw_special_pass = True # disable for now
first_time_run = false

while (not pw_len_pass or not pw_upper_pass or not pw_lower_pass or not pw_digit_pass or not pw_special_pass):
    
    
    
    pw_len_pass = False
    pw_upper_pass = False
    pw_lower_pass = False
    pw_digit_pass = False
    pw_special_pass = True
    
    pw = input("enter your new password")
    if len(pw) > 8:
        pw_len_pass = True
    
    for char in pw:
        if char.isupper():
            pw_upper_pass = True
            
    for char in pw:
        if char.islower():
            pw_lower_pass = True
    
    for char in pw:
        if char.islower():
            pw_lower_pass = True
            
    for char in pw:
        if char.isnumeric():
            pw_digit_pass = True
            
    first_time_run = true
    
print("password has passed validation!!")
