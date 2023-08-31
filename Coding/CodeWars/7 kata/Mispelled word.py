



def mispelled(word1,word2):
    counter = 0
    if len(word1) == len(word2):
        for _, __ in enumerate(word1):
            if word1[_] != word2[_]:
                counter += 1
        if counter > 1:
            return False
        else:
            return True
    else:
        # longer = max(word1, word2, key=len)
        # shorter = min(word1, word2, key=len)
        if len(word1) > len(word2):
            max_word = word1
            min_word = word2
        else:
            max_word = word2
            min_word = word1
        if max_word[1:] == min_word or max_word[:-1] == min_word:
            return True
        else:
            return False



mispelled('versed','xersed')            #True
mispelled('versed','applb')             #False
mispelled('versed','v5rsed')            #True
mispelled('1versed','versed')           #True
mispelled('versed','versed')            #True


