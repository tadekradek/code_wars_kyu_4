"""
We want to generate all the numbers of three digits where:

    the sum of their digits is equal to 10
    their digits are in increasing order (the numbers may have two or more equal contiguous digits)

The numbers that fulfill these constraints are: [118, 127, 136, 145, 226, 235, 244, 334]. There're 8 numbers in total with 118 being the lowest and 334 being the greatest.
Task

Implement a function which receives two arguments:

    the sum of digits (sum)
    the number of digits (count)

This function should return three values:

    the total number of values which have count digits that add up to sum and are in increasing order
    the lowest such value
    the greatest such value

Note: if there're no values which satisfy these constaints, you should return an empty value (refer to the examples to see what exactly is expected).
Examples

find_all(10, 3)  =>  [8, 118, 334]
find_all(27, 3)  =>  [1, 999, 999]
find_all(84, 4)  =>  []

Features of the random tests:

    Number of tests: 112
    Sum of digits value between 20 and 65
    Amount of digits between 2 and 17


"""


#my solutions
#solution1, good, but too inefficient
def find_all_1(sum_dig, digs):
    if sum_dig  > digs*9:
        return []
    else:
        values = []
        for i in range(int("1"+"0"*(digs-1)), int("9"*digs)+1):
            if sum([ int(j) for j in (str(i))]) == sum_dig and all(int(str(i)[j]) <= int(str(i)[j+1]) for j in range (0, digs-1)):
                values.append(i)
    return [len(values), min(values), max(values)]


#my solutions
#solution2, still too inefficient

def find_all(sum_dig, digs):

    def counter():
        counter = 0
        for i in range (int("1"+"0"*(digs-1)), int("9"*digs)+1):
            if sum([ int(j) for j in (str(i))]) == sum_dig and all(int(str(i)[j]) <= int(str(i)[j+1]) for j in range (0, digs-1)):
                counter += 1
        return counter        
    
    def min():
        min = 0
        for i in range (int("1"+"0"*(digs-1)), int("9"*digs)+1):
            if sum([ int(j) for j in (str(i))]) == sum_dig and all(int(str(i)[j]) <= int(str(i)[j+1]) for j in range (0, digs-1)):
                min = i
                break
        return min        

    def max():
        max = 0
        for i in range (int("9"*digs), int("1"+"0"*(digs-1)),-1):
            if sum([ int(j) for j in (str(i))]) == sum_dig and all(int(str(i)[j]) <= int(str(i)[j+1]) for j in range (0, digs-1)):
                max = i
                break
        return max

    if sum_dig  > digs*9:
        return []
    else:
        return [counter(), min(), max()]

