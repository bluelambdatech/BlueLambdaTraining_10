def letters(sentence):
    up_num=0
    low_num=0
    for alp in sentence:
        if(alp.islower()):
            low_num = low_num + 1
        elif(alp.isupper()):
            up_num = up_num + 1
    print(f'The number of uppercase characters is: {up_num}')
    print(f'The number of lowercase characters is: {low_num}')