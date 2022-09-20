# 算课程平均成绩
# 1、输入课程学分
xuefen = [3,1,2,2,2,2,2,2,2,1,1,2,1,1]
# 2、输入课程分数，分数要和学分对应
fenshu = [86.2,92,90,85.3,88,92.2,79.7,73.9,87.4,87,87,85.8,85.7,94]
scores = []
for (i, j) in zip(xuefen, fenshu):
    score = i * j
    scores.append(score)
all_score = sum(scores)
final_score = all_score/sum(xuefen)
print('课程平均成绩：{}'.format(final_score))
