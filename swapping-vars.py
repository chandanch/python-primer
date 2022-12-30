# swapping of variables is done via tuple unpacking
score1 = 200
score2 = 500

score1, score2 = score2, score1
# the above statement is equivalent to score1, score2 = (score2, score1)
# which means that the tuple is unpacked to score1 and score2 i.e. score1, score2 = (500, 200)

print(score1, score2)
