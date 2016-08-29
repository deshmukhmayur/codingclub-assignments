'''FizzBuzz program
A program to print all the numbers between 1-100,
but print "Fizz" instead of the numbers divisible by 3,
"Buzz" instead of the numbers divisible by 5,
and "FizzBuzz" instead of the numbers divisible by both.'''

def fizzbuzz():
    for i in range(1,101):
        if i%3 == 0:
            print("Fizz")
        elif i%3 == 0:
            print("Buzz")
        elif i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        else:
            print(i)

if __name__ == '__main__':
    fizzbuzz()
