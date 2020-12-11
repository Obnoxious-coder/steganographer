def text_to_binary(text):
    print("The original string is : " + str(text)) 
    text=text.replace(" ", "")
    res = ''.join(format(ord(x), 'b') for x in text)
    print(res)
    return res

def BinaryToDecimal(binary):   
    decimal, i = 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return (decimal)


def binary_to_text(text):
    print("The binary value is:", text) 
    str_data =''
    for i in range(0, len(text), 7): 
        temp_data = int(text[i:i + 7]) 
        decimal_data = BinaryToDecimal(temp_data) 
        str_data = str_data + chr(decimal_data) 
    
    return str_data
   
