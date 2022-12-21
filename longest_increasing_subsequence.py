def lis(input):
    dp = [1 for i in range(len(input))]
    for i in range(1, len(input)):
        for j in range(0, i):
            if input[j] < input[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    ans = -1
    for elem in dp:
        ans = max(ans, elem)
    return ans

def main():
    input = [10,8,1,2,11,3,5]
    print(lis(input))

if __name__ == "__main__":
    main()