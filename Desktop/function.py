def get_summ(one, two, delimeter='&'):
    return (str(one) + str(delimeter)  + str(two)).upper()

sum_string = get_summ('Learn' , 'python')
print(sum_string)