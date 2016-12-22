dictionary = {"a":2,"b":2,"c":2,"d":3,"e":3,"f":3,"g":4,"h":4,"i":4, \
              "j":5,"k":5,"l":5,"m":6,"n":6,"o":6,"p":7,"q":7,"r":7, \
              "s":7,"t":8,"u":8,"v":8,"w":9,"x":9,"y":9,"z":9}
             

number = input("Enter a telephone number: ")

while number != "":
    number = number.lower()
    blank_str = ""
    num = '1234567890'
    num_and_alph = "1234567890abcdefghijklmnopqrstuvwxyz"
    for i in number:
        if i in num_and_alph:
            blank_str += i
    if  len(str(blank_str)) != 7 and len(str(blank_str)) != 10:
            print("Invalid number. Reenter:")
    else:
        conversion = ""
        for i in blank_str:
            if i in num:
                conversion += str(i)
            else:
                if i in dictionary:
                    conversion += str(dictionary[i])
        if len(conversion) == 7:
            print("Numeric telephone number is:",conversion[0:3],"-",conversion[3:])
        if len(conversion) == 10:
            print("Numeric telephone number is:",conversion[0:3],"-",conversion[3:6],"-",conversion[6:])
    number = input("Enter a telephone number: ")
