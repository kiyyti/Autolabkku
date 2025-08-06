x1,x2,x3,x4 = map(float, input().split())
score = [x1, x2, x3, x4]
score.remove(max(score))
score.remove(min(score))
print(round(sum(score)/2, 2))