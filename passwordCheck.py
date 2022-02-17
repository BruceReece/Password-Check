#-------------------------------------------------------------
#  Programmed by: Bruce Reece
#  date:  10/03/2016
#--------------------------------------------------------------

#///////////////////////////////////////////////////////////////////////////////////// 
def userCheck():
    # These declarations are used to store the number of lower case, upper case and number of digits from the input.
    uuper = 0
    llower = 0
    digitt = 0
    countText = 0
    
    print("The password must have a minimum of 9 characters")    # Instructions - - tells the user the requirements for the passoword
    print("with at least one upper case and one lower case letter.")
    print("The password must also have at least one digit.")
    newPassword = input("Enter a new password\n")
    
    for n in newPassword:    # This for loop identify each characters from the input
        if n.isupper():
            uuper+=1
        elif n.islower():
            llower+=1
        elif n.isdigit():
            digitt+=1

    if uuper < 1:            # Checks for number of lower case, upper case, digits and length of password 
        userCheck()          # and if not found, function will recurse. 
    elif llower < 1:
        userCheck()
    elif digitt < 1:
        userCheck()
    elif len(newPassword) < 9:
        userCheck()
    confirmation(newPassword) # Pass password in frunction and call it
#/////////////////////////////////////////////////////////////////////////////////////
    
#////////////////////////////////////////////////////////////////////////////////////
    # This function ask the user to confirm his/her password  
def confirmation(password):
    confirm = False
    while confirm == False:
        confirmPassword = input("Please re-enter your password\n")
        if password == confirmPassword:
            print("Password successfully made")
            confirm = True
        else:
            print("Password doesn't match")
           
    '''if password == confirmPassword:
        print("Password successfully made")
    else:
        print("Password doesn't match")
        confirmation(password)'''
#////////////////////////////////////////////////////////////////////////////////////

# Main - -
def main():
    userCheck()
main()
