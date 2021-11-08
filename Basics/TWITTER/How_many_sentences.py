from collections import defaultdict
def countSentences(wordSet, sentences):
    wordList = set(wordSet)
    am = defaultdict(set)
    for word in wordSet:
        am[tuple(sorted(word))].add(word)
    result = []
    for sentence in sentences:
        cnt = 1
        words = sentence.split(" ")
        for word in words:
            if word not in wordList: continue
            cnt *= len(am[tuple(sorted(word))])
        result.append(cnt)
    # Write your code here
    return result