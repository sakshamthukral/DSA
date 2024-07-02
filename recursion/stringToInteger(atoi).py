def myAtoi(s: str) -> int:
        number = '0123456789'
        res = ''
        for c in s:
            if res =='' and (c == '+' or c == '-'):
                res+=c
            elif res == '' and c == ' ':
                continue
            elif c in number:
                res+=c
            else:
                break
        if res == '' or res == '+' or res == '-':
            return 0 
        if int(res) > (2**31)-1:
            return (2**31)-1
        elif int(res) < -(2**31):
            return -(2**31)
        else:
            return int(res)
num = "42"
print(myAtoi(num))