# Your code here
def sing():
    let_it_be_set = list()
    let_it_be = "let it be"
    words_of_wisdom = "whisper words of wisdom"
    there_will_be_an_answer = "there will be an answer"
    for x in range(3):
        let_it_be_set.append(let_it_be)
    print( ",\n".join(let_it_be_set) + ",\n" + let_it_be + "," )
    print( "{}, {}, {},".format(words_of_wisdom, let_it_be, let_it_be))
    print( ",\n".join(let_it_be_set) + "," )
    print( "{}, {}".format(there_will_be_an_answer, let_it_be) )
sing()





