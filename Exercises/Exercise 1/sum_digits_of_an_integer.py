# sum the digits of an integer using recursion

# optimal solution
def sum_digits(num):
    if(num == 0):
        return 0
    else:
        print(num)
        return num % 10 + sum_digits(num // 10)
        
print(sum_digits(1234))

# attempt solution
# def sum_digits(num, sum = 0):
#     if(num != 0):
#         digit = num % 10
#         num = num // 10
#         print("Digit: ", digit, "Num: ", num)
#         sum += digit
#         sum_digits(num,sum)
        
#         return digit
#     else:
#         print("Finished")
#         return sum
    

# total = sum_digits(1234)
# print("Total is: ", total)
