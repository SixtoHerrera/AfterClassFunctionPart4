# Function 1
def max_num(num1, num2, num3):
    print(max([num1, num2, num3]))
max_num(5,6,7)

# Function 2


def mult_list(num_list):
    if len(num_list) == 0:
        return 0
    
    else:
        result = num_list[0]
        if len(num_list)>1:
            for num in num_list[1:]:
                result = result * num
                return result

# Function 3
def rev_string(reverse_string):
    return reverse_string[::-1]
print(reverse_string("ReversedString"))

# Function 4
def num_within(num, str_range, end_range):
    return num in range (str_range,end_range+1)

# Function 5

def pascal(n):
  
#  I don't have an idea not even how to start this one and dont want to use the AI or solution codes I got, ill keep
#trying to understand it