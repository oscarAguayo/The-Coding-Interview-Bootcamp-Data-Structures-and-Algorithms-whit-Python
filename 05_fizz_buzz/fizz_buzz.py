## --- Directions
## Write a program that ~~console logs~~ put in list the numbers
## from 1 to n. But for multiples of three print
## “fizz” instead of the number and for the multiples
## of five print “buzz”. For numbers which are multiples
## of both three and five print “fizzbuzz”.
## --- Example
##   fizzBuzz(5);
##   1
##   2
##   fizz
##   4
##   buzz

def fizz_buzz(number: int) -> list:
    for i in range(1, number+1):
        if i % 3 == 0 and not i % 5 == 0:
            print('fizz')
        elif i % 5 == 0 and not i % 3 == 0:
            print('buzz')
        elif i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        else:
            print(i)

if __name__ == "__main__":
    fizz_buzz(int(input("Give a number: ")))