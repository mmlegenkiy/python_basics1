num = int(input())
fourth_num = int(str(num)[-1])
third_num = int(str(num)[-2]) 
second_num = int(str(num)[-3])
first_num = int(str(num)[-4])
message = f'{first_num} + {second_num} + {third_num} + {fourth_num} = \
{first_num + second_num + third_num + fourth_num}'
print(message)
