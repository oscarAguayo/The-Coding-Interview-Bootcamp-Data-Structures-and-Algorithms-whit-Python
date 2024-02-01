## --- Directions
## Write a program that ~~console logs~~ put in list the numbers
## from 1 to n. But for multiples of three print
## “fizz” instead of the number and for the multiples
## of five print “buzz”. For numbers which are multiples
## of both three and five print “fizzbuzz”.
## --- Example
##   fizz_buzz(5);
##   1
##   2
##   fizz
##   4
##   buzz

def fizz_buzz(number: int) -> list:
    data = []
    for i in range(1, number+1):
        if i % 3 == 0 and not i % 5 == 0:
            data.append('fizz')
        elif i % 5 == 0 and not i % 3 == 0:
            data.append('buzz')
        elif i % 3 == 0 and i % 5 == 0:
            data.append('fizzbuzz')
        else:
            data.append(i)
    return data

if __name__ == "__main__":
    for number in fizz_buzz(int(input("Give a number: "))):
        print(number)