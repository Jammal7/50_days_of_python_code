def tableOfContents(text):
    # Write your code here
    res = []
    cnt = 0
    sc = 0
    for sentence in text:
        if sentence[0:2] == '##':
            sc += 1
            curr = f"{cnt}.{sc}. {sentence[3:]}"
            res.append(curr)
        elif sentence[0] == '#':
            cnt += 1
            sc = 0
            curr = f"{cnt}. {sentence[2:]}"
            res.append(curr)
    return res