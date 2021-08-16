def is_palindrome(word):
    rev_word = word[::-1]

    if(rev_word == word):
        return True
    else:
        return False

def doubler(numbers):
    doubled = []

    for num in numbers:
        doubled.append(num*2)

    return doubled

def fizz_buzz(max):
    ans = []

    for num in range(1, max, 1):
        if(num % 4 == 0 and num % 6 != 0):
            ans.append(num)
        elif(num % 6 == 0 and num % 4 != 0):
            ans.append(num)
    
    return ans

def average_of_three(num1, num2, num3):
    return (num1 + num2 + num3)/3

def goodbye(name):
    return "Goodbye " + name

print(is_palindrome("hannah"))
print(doubler([1, 2, 3, 4, 5]))
print(fizz_buzz(15))
print(average_of_three(50, 75, 90))
print(goodbye("David"))