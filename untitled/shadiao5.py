

def power(x, n):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s

print(power(5,2))

##
# 设置默认参数时
# 一。必选参数在前，默认参数在后，否则python会报错
#
# #
def power2(x, n = 2):

    return 2

































