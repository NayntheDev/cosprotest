def func_a(bundle, start):
    return bundle[start::2]
def func_b(score1, score2):
    if score1 > score2:
        return [1, score1]
    elif score2 > score1:
        return [2, score2]
    else:
        return [0, score1]
def func_c(bundle):
    answer = 0
    score_per_cards = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
    }
    for card in bundle:
        answer += score_per_cards[card]
    return answer
def solution(n, bundle):
    a = func_a(bundle, 0)[:n]
    b = func_a(bundle, 1)[:n]
    a_score = func_c(a)
    b_score = func_c(b)
    return func_b(a_score, b_score)
n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)
print(ret)
