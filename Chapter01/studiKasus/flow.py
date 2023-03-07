
# IF

# In this program, we check if the number is positive or negative or zero and 
# display an appropriate message

# Flow Control

x=7
if x >10: 
    print("x is the value is big.") 
elif x > 0: 
        print("x the value is small.")
else:
            print("x is not positive.")

# Array

# Variabel array
genap = [14,24,56,80]
ganjil = [13,55,73,23]

nap = 0
jil = 0

# Buat looping for menggunakanvariable dari array  yang udah dibuat
for val in genap:
    nap = nap+val
    for val in ganjil:
        jil = jil+val

print("Ini adalah bilangan Genap", nap )
print("Ini adalah bilangan Ganjil", jil )