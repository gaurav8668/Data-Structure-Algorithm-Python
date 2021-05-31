def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)

def fib(n):
    if n == 0 or n == 1:
        return n 
    return fib(n - 1) + fib(n - 2)

def sum_list(l):
    sum = 0
    # if len(l) == 1:
    #     return l[0]
    # else:
    #     return l[0] + sum_list(l[1:])
    for i in l:
        if isinstance(i, int):
            sum += i
        elif isinstance(i, list):
            sum += sum_list(i)
    return sum

def fac(n):
    # 4 = 4 * 3 * 2 * 1
    if n >= 0:
        if n == 0 or n == 1:
            return n
        else:
            return n * fac(n - 1)

def sum_num(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_num(int(n / 10))
    
def sum_series(n):
    if n < 1:
        return n
    else:
        return n + sum_series(n - 2)
    # return f

def power():
    # n = str(number)
    # n = int(n[-1:0:-1])
    # return "-" + str(n)
    if 1534236469 < 2 ** 31:
        return True
    else:
        return False

def s(lst, t):
    x = 0
    # for index, i in enumerate(lst):
    while x <= (len(lst) - 1):
        j = x + 1
        while j <= (len(lst) - 1):
            s = lst[x] + lst[j]
            if s == t:
                a = [x, j]
            j = j + 1
        x = x + 1
    return a
    

if __name__ == '__main__':
    # print(find_sum(5))
    # print(fib(4))
    # print(sum_list([1, 2, [3, 4], [5, 6]]))
    # print(fac(4))
    # print(sum_num(45))
    # print(sum_series(10))
    print(power())
    # power(3, 4)
    # print(s([2, 7 , 11, 15], 9))