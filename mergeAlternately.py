def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    res = ""
    extra = ""
    index1 = 0
    index2 = 0

    if len(word1) > len(word2):
        limit = len(word2)
        extra = word1[limit:]
    elif len(word1) < len(word2):
        limit = len(word1)
        extra = word2[limit:]
    else:
        limit = len(word1)
    
    for i in range(limit):
        res+=(word1[index1])
        index1 += 1
        for j in range(limit):
            res+=(word2[index2])
            index2 += 1
            break
    
    if extra != "": 
        res+=extra
    
    return res

word1 = "abc"
word2 = "pqrm"
print(mergeAlternately(word1, word2))


