class test:
    
    def __init__(self, rng):
        self.rng = rng 

    def is_prime(self, i):
        p_num = []
        n_p_num = []
        if i > 1:
            if i == 2 or i == 3 or i == 5 or i == 7:
                p_num.append(i)
            elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                n_p_num.append(i)
            else:
                p_num.append(i)
        else:
            n_p_num.append(i)
        
        return p_num
    
    def match(self):
        r = []
        for i in range(self.rng[0], self.rng[1] + 1):
            x = self.is_prime(i)
            if x != []:
                r.append(x[0])
        return r
        
    def final_r(self, p_num):
        if len(p_num) == 1: 
            return 0
        if p_num == []:
            return -1
        else:
            return (max(p_num) - min(p_num))

n = int(input())
for _ in range(n):
    i = list(map(int, input().split()))
    t = test(i)
    x = t.match()
    print(t.final_r(x))
