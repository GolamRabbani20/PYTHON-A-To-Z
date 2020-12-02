#if the three sides are the same size, write the message: TRIANGULO EQUILATERO
#if only two sides are the same and the third one is different, write the message:


A=float(input())
B=float(input())
C=float(input())


if A>=B+C:
    print("NAO FORMA TRIANGULO")

    if A==B or B==C or C==A:
        print("TRIANGULO ISOSCELES")
    elif A==B==C:
        print("TRIANGULO EQUILATERO")

elif (A*A)==(B*B+C*C):
    print("TRIANGULO RETANGULO")

    if A==B or B==C or C==A:
        print("TRIANGULO ISOSCELES")
    elif A==B==C:
        print("TRIANGULO EQUILATERO")

elif A*A > B*B + C*C:
    print("TRIANGULO OBTUSANGULO")

    if A==B or B==C or C==A:
        print("TRIANGULO ISOSCELES")
    elif A==B==C:
        print("TRIANGULO EQUILATERO")

elif A*A < B*B + C*C:
    print("TRIANGULO ACUTANGULO")

    if A==B or B==C or C==A:
        print("TRIANGULO ISOSCELES")
    elif A==B==C:
        print("TRIANGULO EQUILATERO")

