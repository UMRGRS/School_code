temp = float input("ingresa la temperatura:")

escala = input("Farenheit (F) o Celsius (C)").lower()

if escala == "f":
    cel = (temp-32)*5/9
    print (cel)
elif escala = "c":
    far = temp * 1.8 + 32
    print (far)
else :
    print ("Escala incorrecta")