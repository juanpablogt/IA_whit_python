with open(r"C:\Users\juapa\OneDrive\Escritorio\Programas\IA_whit_python\archivo\mno.txt") as file_object:
    for line in file_object:
        print(line)

with open(r"C:\Users\juapa\OneDrive\Escritorio\Programas\IA_whit_python\archivo\mno.txt", 'w') as file_object:
    file_object.write("\n:::::::::::::::::::")
    file_object.write("\nich bin Juan")
    file_object.write("\nich come aus kolumbien")
    file_object.write("\nSegunda prueba")
    file_object.write("\nTercera prueba")
    file_object.write("\ncuarta")

with open(r"C:\Users\juapa\OneDrive\Escritorio\Programas\IA_whit_python\archivo\mno.txt") as file_object:
    for line in file_object:
        print(line)
