def C_to_F(temp):
    F=temp*9/5+32
    return F

# Celsius=input("Temperature in Celsius to be converted: ")

Celsius_list=[10,-20,-289,100]

for Celsius in Celsius_list:
    if Celsius < -273.15:
        print ("Such temperature does not exist")
    else:
        print(str(Celsius) + " in Celsius degrees" +" is " + str(C_to_F(Celsius))+ " degrees Fahrenheit")


