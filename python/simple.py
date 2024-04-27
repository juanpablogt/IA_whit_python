line1 = input().split()
A=int(line1[0])
B=int(line1[1])
C=float(line1[2])
line2 = input().split()
D=int(line2[0])
E=int(line2[1])
F=float(line2[2])

VALOR=(B*C)+(E*F)

print("VALOR A PAGAR: R$ {0:.2f}".format(VALOR))