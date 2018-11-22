def asdf():

    word = str(input("Please a greeting or question:"))
    word = word.lower()

    for i in word.split(" "):    
        if i in ["hello","hi"]:
            print("Hello!")
            break
        elif i in ["how are", "are", "you"]:
            print("I am good!")
            break
        pass
    else:
        print("Sorry, I do not understand")
       
    
asdf()
