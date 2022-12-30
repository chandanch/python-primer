from collections import deque

scores_list = deque([])

scores_list.append(23)
scores_list.append(223)
scores_list.append(123)
scores_list.append(203)

scores_list.popleft()

print(scores_list)

print(f"{'Emptpy' if not scores_list else 'Not Empty'}")
