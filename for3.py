school_scores = [
                {'school_class': '4a', 'scores': [3,4,4,5,2]},
                {'school_class': '7a', 'scores': [5,4,4,5,5]},
                {'school_class': '10b', 'scores': [5,3,2,5,2]},
                {'school_class': '5a', 'scores': [5,3,3,5,5]},
                 ]
scores_sum = 0
for score in school_scores:
		scores_sum += score
		print(scores_sum)

scores_avg = scores_sum / len(school_scores)
print(f"Средняя оценка {scores_avg}")