def solution(words, word):
    count = 0
    for w in words:
        for i in range(len(word)):
            if (w[i]!=word[i]):
                count+=1
    return count
words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)
print(ret)
