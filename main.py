# 算算数平均成绩
xuefen = [3,1,2,2,2,2,2,2,2,1,1,2,1,1]
fenshu = [86.2,92,90,85.3,88,92.2,79.7,73.9,87.4,87,87,85.8,85.7,94]
zongfen = []
for (i, j) in zip(xuefen, fenshu):
    score = i * j
    zongfen.append(score)
all_score = sum(zongfen)
final_score = all_score/sum(xuefen)
print('课程平均成绩：{}'.format(final_score))
