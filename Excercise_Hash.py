import pandas as pd 

df = pd.read_csv('nyc_whether.csv')
# print(df.head(7))
# df.tem
def avg_temp(df):
    sum = 0
    for idx, value in enumerate(df['temperature(F)']):
        if idx <= 6:    
            sum += value
    avg = sum / 7
    print(avg)

# avg_temp(df)
# print(max(df['temperature(F)']))


# print(df.iloc[3, 1])

# count = {'diverged':0,
        # 'in': 0,
        # 'I':0}
count = {}
l = ['diverged', 'in', 'I']

f = open('poem.txt', 'r') 

li = list(f)
for x in li:
    lines = x.split('\n')[0]
    for i in l:
        if i in lines:

            if i not in count:
                count[i] = 1
            elif i in count:
        # if i in lines:
                count[i] += 1 
    # break
# print(li)

    
print(count)


print('Code Completed')