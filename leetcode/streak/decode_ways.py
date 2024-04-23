def numDecodings(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1  # Base case: empty string is one valid decoding

    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
            if i + 1 < n and int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]

    return dp[0]

def numDecodings2(s): # Bottom Up Approach
    if len(s) == 0 or s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    count1, count2 = 1,1 # where count2 is the previous value and count1 is the previous to previous value
    for i in range(1,len(s)): # starting from second character onwards as for 1 character we are already returning 1 way
        single_digit = int(s[i])
        double_digit = int(s[i-1])*10+single_digit
        count = 0
        if single_digit>0:
            count+=count2
        if double_digit>=10 and double_digit<=26:
            count+=count1
        count1 = count2
        count2 = count
    return count




s = input()
print(numDecodings(s))
print(numDecodings2(s))