def find_largest_no():
    numbers = [12, 45, 67, 23,]
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print (largest)


def no_of_letters_in_string():
    name = "Banana"
    a = 0
    for no_a in name:
        if no_a == "a":
            a = a + 1
    print(a)


def find_samllest_no():
    numbers = [34, 12, 67, 89, 21, 1, 100]
    smallest_no = numbers[0]
    for n in numbers:
        if smallest_no > n:
            smallest_no = n
    print(smallest_no)


def marks():
    marks = int(input("What is Your Marks: "))
    if marks >= 40:
        print("PASS")
    else:
        print("FAIL")


def name_list():
    list = []
    for n in range(5):
        list.append(input(f"Write Your {n+1} name: "))
    print(list)


def table():
    n = int(input("Write Your Number: "))
    for m in range(1,11):
        print(n, "X", m, "=", n*m )


def FACT():
    n = int(input("Write Your Number: "))
    result = 1
    for m in range(1,n+1):
        result = result*m
    print(result)


def fib(x):
    a = 0
    b = 1
    for n in range(x):
        print(a, end="")
        next_term = a + b
        a = b
        b = next_term


def swap(a,b):
    a,b = b,a
    print(f"a = {a}, b = {b}")
def prime():


    a = int(input("What IS The Number: "))
    for m in range(2,a):
        if a%m == 0:
            print("It Is Not a Prime Number: ")
            break
        else:
            print("It is a Prime Number: ")


def wrdcount():
    word = input("Enter Your Sentence: ")
    word_count = word.split()
    result = len(word_count)
    print(result)


def word_present_or_not():
    string = input("Enter Your Sentence: ")
    word = input("Which Word Do You Want To Find: ")
     
    if word in string:
        print(f"{word} is present in the string")
    else:
        print(f"{word} is not present in the string")


def no_divided():
    for m in range(1,100+1):
        if m%3 == 0:
            print(m,end=" ")


def sum_of_no(x):
    sum = 0
    while x > 0:
        digit = x % 10
        sum += digit
        x = x//10
    print(sum)
        



