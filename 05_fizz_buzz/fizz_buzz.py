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
    print(1)

if __name__ == "__main__":
    fizz_buzz(int(input("Give a number: ")))