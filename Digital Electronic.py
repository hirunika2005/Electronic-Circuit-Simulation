A=int(input("Enter A(0 or 1): "))
B=int(input("Enter B(0 or 1): "))
C=int(input("Enter C(0 or 1): "))

D=int(not bool(A))
E=int(bool(B) and bool(C))
Z=int(bool(D) or bool(E))

print("D : ",D)
print("E : ",E)
print("Z : ",Z)
