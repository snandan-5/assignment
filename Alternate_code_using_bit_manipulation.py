#Function to find No of possible ways to attend the class over N days
def check_consecutive(num,input_val):
    count_1=0
    for i in range(2,num):
        temp = str(format(i,"0"+str(input_val)+"b"))#representing Decimal in Binary form (1--> "00001")
        if(max(map(len,temp.split('1')))>=4):
            count_1+=1
            continue
    return count_1
#Function to determine the probability of attending the class
def check_absent(num):
    count_2=0
    for i in range(2,num):
        if not(i & (1 << (0))):
            count_2+=1
    return count_2

if __name__ == '__main__':
    input_val= 5
    num = (1<<input_val) #total number of possibilities
    rejected,probability = check_consecutive(num,input_val),check_absent(num)
    answer1,answer2 = (rejected+2),probability-rejected # No of >=4 Consecutive days

    print("The number of ways to attend classes over N days :",(num-answer1))
    print("The probability that will miss graduation :",f'{str(answer2)}/{str(num-answer1)}')
