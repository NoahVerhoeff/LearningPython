import math

print("Cosine Law Calculator")
#Single Comment
#Assignment Statement:
#   x=4
#   x=2+3*3
#   x=input()

#Input
a = float(input("Side A: "))
b = float(input("Side B: "))
c = float(input("Side C: "))

sum=a+b+c
print(sum)

#Process
angleA = (a*a - b*b - c*c)/(-2*b*c)
angleA = math.acos(angleA)
angleA = math.degrees(angleA)
angleA = round(angleA,3)

angleB = (b*b - a*a - c*c)/(-2*a*c)
angleB = math.acos(angleB)
angleB = math.degrees(angleB)
angleB = round(angleB,3)

angleC = (c*c - b*b - a*a)/(-2*b*a)
angleC = math.acos(angleC)
angleC = math.degrees(angleC)
angleC = round(angleC,3)

print("Angle A: "+str(angleA)+"degrees.")
print("Angle B: "+str(angleB)+"degrees.")
print("Angle C: "+str(angleC)+"degrees.")

check = angleA+angleB+angleC
print(check)

#Output