def caesarCipher(s, k):
    alpha = "_abcdefghijklmnopqrstuvwxyz"
    print(len(alpha))
    res_s = ""
    for char in s:
        if char.isalpha():
            for idx, a_char in enumerate(alpha):
                x = char.lower()
                if x == a_char:
                    if char.isupper():
                        res_s = res_s + alpha[idx%26 + k].upper()
                    else:
                        print(idx, idx%26 + 5)
                        res_s = res_s + alpha[idx%26 + k]
        else:
            res_s = res_s + char        
    return s, res_s

s, res = caesarCipher('covidz-19', 2)
print(s)
print(res)
s, res = caesarCipher('Always-Look-on-the-Bright-Side-of-Life',5)
print(s)
print(res)