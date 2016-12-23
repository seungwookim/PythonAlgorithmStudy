

def count_friend(f_list):
    ans = 0
    n = len(f_list[0])

    for i in range(0, n) :
        cnt = 0
        for j in range(0, n) :
            if(i==j):
                continue

            if(f_list[i][i-n] == 'Y'):
                cnt = cnt + 1
            else :
                for k in range(0, n):

                    if(f_list[j][k-n] == 'Y' and f_list[k][i-n] == 'Y'):
                        cnt = cnt + 1
                        break

        ans = max(ans, cnt)

    return ans


friend = ["YYNNYNYN", "YYNNYNYN", "YYNNYNYN", "YYNNYNYN", "YYNNYNYN", "YYNNYNYN", "YYNNYNYN", "YYNNYNYN"]

print(count_friend(friend))