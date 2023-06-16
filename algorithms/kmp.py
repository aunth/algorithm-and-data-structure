
def p_func(pattern):
    n = len(pattern)
    p = [0] * n
    for i in range(1, n):
        j = p[i-1]
        while j > 0 and pattern[i] != pattern[j]:
            j = p[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        p[i] = j
    return p

def knp(str, pattern):
    new_str = str+" "+pattern
    p = p_func(new_str)
    print(p)
    lenght = len(str)
    for i,j  in enumerate(p):
        if j == lenght:
            return i - 2 * lenght
    else:
        return False
          
string = "This is my haystack!"
find = "is my"
print(knp(find, string))