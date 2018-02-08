def convert(number):
    ten_e0 = number[-1]
    
    if len(number) == 1:
        return(ten_e0)
    elif len(number) == 2:
        return(number[-2] + ten_e0)
    elif len(number) == 3:
        return(hundreds_function(number))
    elif len(number) == 4:
        return(thousands_function(number))
    elif len(number) == 5:
        return(tens_of_thousands_function(number))
    elif len(number) == 6:
        return(hundreds_of_thousands_function(number))
    elif len(number) == 7:
        return(millions_function(number))
    else:
        return "Beyond scope"
           
def hundreds_function(number):
    number = str(number)
    ten_e0 = number[-1]
    ten_e1 = number[-2]
    ten_e2 = number[-3]
    
    if ten_e2 == str(0):
        if ten_e1 == str(0):
            return("and " + ten_e0)
        else:
            return("and " + ten_e1 + ten_e0)
    
    elif ten_e1 == str(0) and ten_e0 == str(0):
        return(ten_e2 + " hundred")
    elif ten_e1 == str(0):
        return(ten_e2 + " hundred and " + ten_e0)
    else:
        return(ten_e2 +" hundred and " + ten_e1 + ten_e0)
    
def thousands_function(number):
    number = str(number)
    ten_e0 = number[-1]
    ten_e1 = number[-2]
    ten_e2 = number[-3]
    ten_e3 = number[-4]
        
    if ten_e2 == str(0) and ten_e1 == str(0) and ten_e0 == str(0):
        return(ten_e3 + " thousand")
    else:
        return(ten_e3 + " thousand " + hundreds_function(number))
    
def tens_of_thousands_function(number):
    number = str(number)
    ten_e0 = number[-1]
    ten_e1 = number[-2]
    ten_e2 = number[-3]
    ten_e3 = number[-4]
    ten_e4 = number[-5]

    if ten_e2 == str(0) and ten_e1 == str(0) and ten_e0 == str(0):
        return(ten_e4 + ten_e3 + " thousand")
    else:
        return(ten_e4 + ten_e3 + " thousand " + hundreds_function(number))
    
def hundreds_of_thousands_function(number):
    number = str(number)
    ten_e0 = number[-1]
    ten_e1 = number[-2]
    ten_e2 = number[-3]
    ten_e3 = number[-4]
    ten_e4 = number[-5]
    ten_e5 = number[-6]

    if ten_e4 == str(0) and ten_e3 == str(0) and ten_e2 == str(0) and ten_e1 == str(0) and ten_e0 == str(0):
        return(ten_e5 + " hundred thousand")
    elif ten_e4 == str(0) and ten_e3 == str(0):
        return(ten_e5 + " hundred thousand " + hundreds_function(number))
    elif ten_e4 == str(0):
        return(ten_e5 + " hundred and " + thousands_function(number))
    else:
        return(ten_e5 + " hundred and " + tens_of_thousands_function(number))

def millions_function(number):
    number = str(number)
    ten_e0 = number[-1]
    ten_e1 = number[-2]
    ten_e2 = number[-3]
    ten_e3 = number[-4]
    ten_e4 = number[-5]
    ten_e5 = number[-6]
    ten_e6 = number[-7]

    if ten_e5 == str(0) and ten_e4 == str(0) and ten_e3 == str(0) and ten_e2 == str(0) and ten_e1 == str(0) and ten_e0 == str(0):
        return(ten_e6 + " million")
    else:
        return "Beyond scope"
def main():
    
    input_number = input("Enter a number: ")
    input_number = input_number.replace(",","") #replace comma, e.g. 1,000 becomes 1000
    print(convert(input_number))
    input()
    
 ##TEST RUN
##    for input_number in range(0,1000000 +1):
##        print(input_number ,":", convert(str(input_number)))

main()
