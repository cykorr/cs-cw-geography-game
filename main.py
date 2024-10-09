import time
total_score = 1
cntrl_panel = "********69"

print('''
----------------------------
welcome to geography quiz!!!

????? why would u want to play this game?????
----------------------------
''')
user = str(input('''what do u want ur username to be?
'''))
username = "@" + user # creates usernameVAR to hide true user and hidden ids
# admin debug panel, ignore
if user.lower() == "admin123":
    debug_mode = input('''administrator detected.
engage debug mode? (y/n)''')
    if debug_mode.lower() == "y":
        #adding this in future lol
        print("DEBUG MODE ENABLED.")
        username = "@admin"
        #hiding free points generator...
        user = cntrl_panel
# patching admin loophole
elif user.lower() == "super_secret_admin_password":
    print("loophole detected...")
    user = "clown"
    username = "@clown"

print("welcome", username,"to GEOGRAPHY GAME!!!!")
print("created by the mighty heydon")

print("----------------------------") # this is to make a new line

time.sleep(2.0) # waiting makes it more dramatic
# q1-q10 q = questions

# q1
q1 = str(input('''how old is the earth rounded to 1 number in the billions?
answer : '''))
if q1 == "5" or user == cntrl_panel:
    print("answer is correct", username,"! your current score is : 1")
    total_score = 1
else:
    print("womp womp, that's incorrect")

time.sleep(2.0)

# q2
print("----------------------------") # this is to make a new line
q2 = str(input('''how many continents are there? : '''))
if q2 == "7" or user == cntrl_panel:
    print("answer is correct! your current score is :", str(total_score))
    total_score = total_score + 1
else:
    print("womp womp, that's incorrect") 

time.sleep(2.0)

# q3
print("----------------------------") # this is to make a new line
q3 = str(input("what's the hardest material on earth? : "))
if q3.lower() == "diamond" or user == cntrl_panel:
    print("answer is correct! your current score is :", str(total_score))
    total_score = total_score + 1
else:
    print("womp womp, that's incorrect")  

time.sleep(2.0)

# q4
print("----------------------------") # this is to make a new line
q4 = str(input("which continent is russia located in? : "))
if q4.lower() == "asia" or q4.lower() == "europe" or user == cntrl_panel:
    print("answer is correct! your current score is :", str(total_score))
    total_score = total_score + 1
else:
    print("womp womp, that's incorrect") 

time.sleep(2.0)

# q5
print("----------------------------") # this is to make a new line
q5 = str(input('''What is the name of the tallest mountain in the world?
a) mount everest
b) mount K2
c) mount tai 
answer : '''))
if q5.lower() == "a" or user == cntrl_panel:
    print("answer is correct! your current score is :", str(total_score))
    total_score = total_score + 1
else:
    print("womp womp, that's incorrect")   

time.sleep(2.0)

# q6
print("----------------------------") # this is to make a new line
q6 = str(input('''What's the name of the longest river in Africa?
a) amazon river
b) nile river
c) sink
answer : '''))
if q6.lower() == "b" or user == cntrl_panel:
    print("answer is correct! your current score is :", str(total_score))
    total_score = total_score + 1
elif q6.lower() == "c":
    print("nah bruda r u dumb :skull: deducting a point for that")
    total_score = total_score - 1
    print("your current score is :", str(total_score))
else:
    print("womp womp, that's incorrect")   

time.sleep(2.0)

# q7
print("----------------------------") # this is to make a new line
q7 = str(input('''question?
a) test
b) test
c) test
answer : '''))
if q7.lower() == "b" or user == cntrl_panel:
    print("answer is correct! your current score is :", str(total_score))
    total_score = total_score + 1
else:
    print("womp womp, that's incorrect")   

time.sleep(2.0)

# q8
print("----------------------------") # this is to make a new line
q8 = str(input('''test
a) test
b) test
c) test
answer : '''))
if q8.lower() == "b" or user == cntrl_panel:
    print("answer is correct! your current score is :", str(total_score))
    total_score = total_score + 1
else:
    print("womp womp, that's incorrect")   

time.sleep(2.0)

# q9
print("----------------------------") # this is to make a new line
q9 = str(input('''qyesution
a) test
b) test
c) test
answer : '''))
if q9.lower() == "b" or user == cntrl_panel:
    print("answer is correct! your current score is :", str(total_score))
    total_score = total_score + 1
else:
    print("womp womp, that's incorrect")   

time.sleep(2.0)

# q10
print("----------------------------") # this is to make a new line
q10 = str(input('''qyesution
a) test
b) test
c) test
answer : '''))
if q10.lower() == "b" or user == cntrl_panel:
    print("answer is correct! your current score is :", str(total_score))
    total_score = total_score + 1
else:
    print("womp womp, that's incorrect")   

time.sleep(2.0)
