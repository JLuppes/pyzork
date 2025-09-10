score = 0
def enterToContinue():
    input("<<<Press <Enter> to continue>>>")
def endScore():
    enterToContinue()
    print(f"\nYour final score:\n\t{score} points")
    print("\n\n\t\tGame Over!!!")
def badEnding():
    print("You miss out on your opportunity to gain incredibly useful skills.\nYou Lose!")
    endScore()
def declineEnding():
    print("You decide not to join the school, for now. Maybe you'll make better choices next time! ;)")
    endScore()
def goodEnding():
    print("You join the school as part of the Computer Technology Department. Great choice!\n\tYou Win!!!!!!")
    endScore()

print("You are standing alone in a room full of people. Around you are tables with chairs set behind them, and people with lanyards sit at the tables, smiling and patiently waiting for anyone to walk up and talk to them. You notice a person sitting at a table marked \"Computer Technology Department\" beckoning you to come towards them.")
goToTable = input("Do you go to the table? (y/n):")

if goToTable.casefold() == "n".casefold(): 
    print("You ignore the people at the table, and you miss out on your chance to gain important skills.")
    enterToContinue()
    badEnding()
elif goToTable.casefold() != "y".casefold():
    print("Not sure what you mean by that. Times up!")
    enterToContinue()
    badEnding()
else: 
    print("As you approach, you notice literature on the table that describes various degree options within the school of Computer Technology.")
    numLiteratureGrabbed = input("How many pieces of literature do you grab? (0-4):")
    grabNormal = True
    try:
        numLiteratureGrabbed = int(numLiteratureGrabbed)
    except ValueError:
        grabNormal = False
    if numLiteratureGrabbed < 0:
        grabNormal = False
    if not grabNormal:
        weirdGrabAward = 2
        score += weirdGrabAward
        print(f"Um, I'm not even sure how you would grab {str(numLiteratureGrabbed)} pamphlets, soooooo.....")
        enterToContinue()
        print(f"(Good effort for trying though, here's {weirdGrabAward} point(s) for doing something unexpected)")
        enterToContinue()
    elif numLiteratureGrabbed == 0:
        print("You don't feel like taking any literature.")
        enterToContinue()
    elif numLiteratureGrabbed > 0 and numLiteratureGrabbed < 5:
        pamphletValue = 10
        score += numLiteratureGrabbed * pamphletValue
        print(f"You pick up {numLiteratureGrabbed} pamphlets. Hey these things have some great information! You get {pamphletValue} points for each, bringing your score to {score}")
        enterToContinue()
    elif numLiteratureGrabbed > 4: 
        greedPenalty = 5
        score -= greedPenalty
        print(f"That's way too many! You lose {greedPenalty} points for being greedy, and your score is now {score}, but the people at the table still seem interested in talking to you.")
        enterToContinue()
    name = input("A person at the table asks you your name. What do you tell them? (name):")
    if not isinstance(name, str):
        print(f"\"Huh, well I'm not sure how I'll put that on the form, but it's nice to meet you {str(name)}")
        enterToContinue()
    else: 
        print(f"That sure does sound like a great name! Nice to meet you {name}") 
        enterToContinue()
    print(f"Hey so {str(name)}, we'd really like you to consider joining one of our Computer Technology programs.")
    enterToContinue()
    joinDecision = input("Would you like to join our school? (y/n):")
    if joinDecision.casefold() == "n".casefold():
        declineAward = 20
        score += declineAward
        print(f"Well, we're a little disappoined, but we appreciate you coming this far. Here, take {declineAward} points as a consolation prize.")
        enterToContinue()
        declineEnding()
    elif joinDecision.casefold() == "y".casefold():
        joinAward = 100
        score += joinAward
        print(f"That's wonderful! As a thank-you gift for joining, here's a special scholarship of {joinAward} points!")
        enterToContinue()
        goodEnding()