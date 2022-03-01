class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s=="":
            return 0
        s = s.split(' ')[0]
        new_s = ""
        neg = False
        pos = False
        if s[0]=='-' or s[0]=='+' or s[0]>='0' and s[0]<='9':
            if s[0]=='-':
                neg = True
            if s[0]=='+':
                pos = True
            i = 0
            for s1 in s:
                if neg and i==0 or pos and i==0:
                    i+=1
                    continue
                if s1>='0' and s1<='9':
                    new_s+=s1
                else:
                    break
        if neg:
            new_s = "-"+new_s
        # print(new_s)
        try:
            i = int(float(new_s))
            if i < -2147483648:
                return -2147483648
            if i > 2147483647:
                return 2147483647
            return i
        except:
            return 0
        