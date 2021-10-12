# Functions with outputs

# defining function that take two argumetns
def format_name(f_name, l_name):
    if f_name == "" or l_name == "": #Cheking if either first or last name is empty
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title() # converting to title case
    formated_l_name = l_name.title() # converting to title case
    return f"{formated_f_name} {formated_l_name}" #returning 


print(format_name(input("What is your first name? "),input("what is your last name? ")))
