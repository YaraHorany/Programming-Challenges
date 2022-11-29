# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

def nthUglyNumber(n):
    ugly_nums_list = [1]
    
    two_position = 0
    three_position = 0
    five_position = 0
    
    while len(ugly_nums_list) < n:

        by2 = ugly_nums_list[two_position] * 2;
        by3 = ugly_nums_list[three_position] * 3;
        by5 = ugly_nums_list[five_position] * 5;

        minimum = min(by2, by3, by5)

        ugly_nums_list.append(minimum)
        
        if minimum == by2:
            two_position += 1

        if minimum == by3:
            three_position += 1

        if minimum == by5:
            five_position += 1

    return ugly_nums_list[-1]
    
    # Time Limit Exceeded:
    # i = 0
    # x = 1
    # while i < n:
    #     num = x
    #     while num % 5 == 0:
    #         num /= 5
    #     while num % 3 == 0:
    #         num /= 3
    #     while num % 2 == 0:
    #         num /= 2
    #     if num == 1:
    #         i += 1
    #     x += 1
    # return x - 1


print(nthUglyNumber(10)) # output: 12, Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
print(nthUglyNumber(1)) # output: 1, Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
print(nthUglyNumber(345))