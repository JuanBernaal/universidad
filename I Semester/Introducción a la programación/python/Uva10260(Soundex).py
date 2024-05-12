def soundex(): 
    word = input() 
    soundexCoding = {'B': '1', 'F' : '1', 'P' : '1', 'V' : '1', 'C' : '2','G' : '2', 'J' : '2', 'K' : '2', 'Q' : '2', 'S' : '2', 
                     'X' : '2', 'Z' : '2', 'D' : '3', 'T' : '3', 'L' : '4', 'M' : '5', 'N' : '5', 'R': '5'} 
    while word != "": 
        ans = "" 
        before = None 
        for i in range(len(word)): 
            if word[i] in soundexCoding: 
                if before != soundexCoding[word[i]]:
                    ans += soundexCoding[word[i]] 
                    before = soundexCoding[word[i]] 
            else: 
                before = None 
        print(ans) 
        word = input() 
soundex() 