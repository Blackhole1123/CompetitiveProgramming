def high(x):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    alpha_scores = {'a': 1}
    counter = 1
    for letter in alpha:
        alpha_scores[letter] = counter
        counter += 1
    x = x.lower().split(' ')
    wordscores = {}
    for i in x:
        score = 0
        for char in i:
            score += alpha_scores[char]
        wordscores[i] = score
    return max(wordscores, key=wordscores.get)