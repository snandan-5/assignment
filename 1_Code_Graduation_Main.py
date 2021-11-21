import itertools
#Check whether given combination has 4 consecutive absence
def check_consecutive(allowed):
    consecutive = 0
    temp = set()
    for i in allowed:
        if i not in temp:
            temp = set()
            temp.add(i)
            if i == 1:continue
            else:consecutive = 1
        else:
            if i == 1:continue
            else:
                consecutive += 1
                if consecutive>= 4:
                    return False
    return True

def check_probability(days, abs_limit):
    choices = [0, 1] #Each day there is two choices
    #total number of combinations that can be considered
    total_ways = [i for i in itertools.product(choices, repeat=days)]
    #Total number of combinations allowed for attending the class
    allowed_ways = [j for j in total_ways if check_consecutive(j)]
    #Check the prob of missing the graduation day
    missing_probability = [k for k in allowed_ways if k[-1] == 0]
    print("The number of ways to attend classes over N days :",len(allowed_ways))
    print("The probability you will miss graduation ceremony:",f'{len(missing_probability)}/{len(allowed_ways)}')

if __name__ == '__main__':
    num = 5
    check_probability(num,4)