print("""Fake Fan Finder"
     Do you like \033[33m'Avengers'\033[0m?
     Let's find out!""")
print("----------------")

while True:
    faveAvenger = input("Who is your favourite character from the original team, the founders? :\n").lower() #conver to lower case

    if faveAvenger == "iron man":
        name = input("What is his real name?  :\n")
        if name == "tony stark":
            print("Correct! You are a real Avenger's fan.")
            break
        else:
            print("""\nAre you really sure you know the Avengers fouders? 
        Try again, maybe using the correct name\n""")

    elif faveAvenger == "wasp":
        name = input("Wow! What is her real name?  :\n")
        if name == "Janet Van Dyne":
            print("Correct! You are a real Avenger's fan.")
            break
        elif name == "janet":
            print("You are a real fan, but the corect name is Janet Van Dyne")
            break
        else:
                print("""\nAre you really sure you know the Avengers fouders? 
            Try again, maybe using the correct name\n""")

    elif faveAvenger == "thor":
        name = input("wha is his real complete name?  :\n")
        if name == "thor odinson":
            print("Correct! You are a real Avenger's fan.")
            break
        else:
                print("""\nAre you really sure you know the Avengers fouders? 
            Try again, maybe using the correct name\n""")

    elif faveAvenger == "hulk":
        name = input("Hulk smash! What is his real name?  :\n")
        if name == "dr. banner" or name == "dr. bruce banner":
            print("Correct! You are a real Avenger's fan.")
            break
        elif name == "bruce banner":
            print("Doctor Bruce Banner, please")
            break
        else:
                print("""\nAre you really sure you know the Avengers fouders? 
            Try again, maybe using the correct name\n""")

    elif faveAvenger == "ant-man" or faveAvenger == "ant man":
        name = input("Now the decisive question! What is his real name?  :\n")
        if name == "dr. henry jonatthan pym":
            print("You are a real Avenger's fan!")
            break
        elif name == "dr. pym" or name == "dr pym" or name == "hank pym":
            print(
            "OK... You are a real Avenger's fan! The corect name is Dr. Henry Jonatthan Pym, but it's very difficult")
            break
        elif name == "scott lang" or faveAvenger == "scott edward harris lang":
            print("Correct hero, but wrong time. You might be an Avengers fan, but are you truly a 'big fan'?")
            break # break statement inside a loop
        else:
                print("""\nAre you really sure you know the Avengers fouders? 
            Try again, maybe using the correct name\n""")

    elif faveAvenger == "scarlet witch":
        print("Ok, maybe the most powerful, but she's not a founder of the team\n")
        break
    elif faveAvenger == "black widow":
        print("Ok Natasha is great, but shes' not a founder of the team\n")
    elif faveAvenger == "spider-man" or faveAvenger == "spider man":
        print("""He is the best ever...
        But he's not a founder of the team!\n""")
    elif faveAvenger == "black panther":
        print("My favorite, but he's not a founder of the team\n")
    elif faveAvenger == "doctor strange":
        print("Ok, but he's not a founder of the team\n")
    elif faveAvenger == "captain marvel":
        print("The beautiful Carol Danvers... But she's not a founder of the team\n")
    elif faveAvenger == "captain america":
        print("Ok, the oldest Avenger, but he's not a founder of the team\n")
    elif faveAvenger == "falcon":
        print("He's not a founder of the team, he's very young for this\n")
    elif faveAvenger == "groot":
        print("He's a wonderful hero, we love him. But he's a Guardian of the Galaxy...\n")

    else:
        print("""\nAre you really sure you know the Avengers fouders? 
        Try again, maybe using the correct hero or name\n""")
