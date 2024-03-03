name = input("enter your name: ")
print(f"welcome {name} to this adventure game")


answer = input("انت في طريق ويوجد ممران تذهب (يمين او يسار)").lower()

if answer =="يمين":
    answer=input("فوجدت جسرا هل تريد العبور من عليه (نعم او لا)").lower()
    if answer == "نعم":
        answer = input("لقد قابلت رجما هل تريد التحدث معه (نعم او لا)").lower()
        if answer== "نعم":
            print("لقد اعطاك هذا الرجل كنزا لقد ربحت")
        elif answer == "لا" :
            print("لقد انزعج الرجل لقد خسرت!")
        else:
            print("Not valid option. you lose! ")
    elif answer== "لا":
        print("اذن انت جبان وقد خسرت!")
    else:
        print("Not valid option. you lose! ")
elif answer =="يسار":
    print("لقد قابلت اسد وقام بقتلك لقد خسرت!")
else:
    print("Not valid option. you lose! ")

print(f"thanks for playing {name}")
# my adventure game OA