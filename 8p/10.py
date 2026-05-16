s = input()

words = s.split()
first_word = words[0]

for word in words[1:]:          
    if word != first_word:       
        
        check = False
        for i in range(len(word)):
            if word[i] in word[i+1:]:   
                check = True
                break
        
        if not check:       
            print(word)
