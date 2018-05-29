nums = input("숫자 5개를 , 로 구분하여 입력하세요 > ")

num_list = nums.split(',')
summary = 0
for i in num_list:
    summary += int(i)

avg = summary/len(num_list)
print("평균은 {0} 입니다.".format(avg))