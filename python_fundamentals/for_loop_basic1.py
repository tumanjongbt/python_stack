# Basic - Print all the numbers/integers from 0 to 150.
number = 151
for i in range(number):
    print("number: ", i)


# Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
for i in range(5, 1000000, 5):
    print(i)


# Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for i in range(1, 105):
    if i % 5 == 0:
        print("Coding: ", i )
    if i % 10 == 0:
        print("Dojo: ", i)


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for num in range(500001):
    if num % 3 == 0:
        sum +=num
print(sum)


# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).

for i in range(2018, 1, -4):
        print(i)

# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR 

lowNum = 1
highNum = 10
mult = 2
for i in range(lowNum, highNum, mult):
        print("I is: ", i, "multiple of mult: ", i*mult)
