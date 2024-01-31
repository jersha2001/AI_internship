# a=10
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)


# weight_kg=50
# height_m=7
# BMI=weight_kg/(height_m*height_m)
# print(BMI)


# str="python"
# print(str[0])
# print(str[5])



# a="Python programming is fun"
# print(a[19:25])



# z=123
# print(int(z))


# year=int(input("Enter the year:"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("The year is leap year !")
# else:
#    print(" The year is not a leap year !")


# num=11
# if num > 1:
#     for i in range(2, int(num/2)+1):
#         if(num % i)==0:
#             print(num,"is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")







# def isPalindrome(s):
#     return s == s[::-1]
 
 
# # Driver code
# s = "radar"
# ans = isPalindrome(s)
 
# if ans:
#     print("Yes")
# else:
#     print("No")


# i = 1
# while i <= 100:
#     print(i, end=" ")
#     i += 1
# for i in range(1,101):
#     print(i, end=" ")


# number = int(input("Enter number: "))

# print("The multiples are: ")
# for i in range(1,6):
#     print(number*i, end =" ")


# print("Enter the Number: ")
# num = int(input())

# fact = 1
# i = 1
# while i<=num:
#     fact = fact*i
#     i = i+1

# print("\nFactorial =", fact)



# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum)


# rows=5
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("")



num = int(input('Enter a number: '))
sum = 0
for i in range(0, num+1):
    if i % 2 == 0:
        print(i)
        sum+=i
print("Sum of all the even numbers is:",sum)


























