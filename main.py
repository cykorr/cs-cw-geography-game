import time
score = 1
win = 1
total_score = 0

print('''
----------------------------
welcome to geography quiz!!!

????? why would u want to play this game?????
----------------------------
''')
user = str(input('''what do u want ur username to be?
'''))
# creates usernameVAR to hide true user and hidden ids
username = "@" + user
# admin debug panel, ignore
if user.lower() == "admin123":
    debug_mode = input('''administrator detected.
engage debug mode? (y/n)''')
    if debug_mode.lower() == "y":
        #adding this in future lol
        print("DEBUG MODE ENABLED.")
        username = "@admin"
        #hiding free points generator...
        user = "super_secret_admin_password"
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
if q1 == "5" or user == "super_secret_admin_password":
    print("answer is correct", username,"! your current score is : 1")
    total_score = score + win
    score = total_score
else:
    print("womp womp, that's incorrect")
    core = total_score

time.sleep(2.0)

# q2
print("----------------------------") # this is to make a new line
q2 = str(input('''how many continents are there? : '''))
if q2 == "7" or user == "super_secret_admin_password":
    print("answer is correct! your current score is :", str(total_score))
    total_score = score + win
    score = total_score
else:
    print("womp womp, that's incorrect")
    score = total_score    

time.sleep(2.0)

# q3
print("----------------------------") # this is to make a new line
q3 = str(input("what's the hardest material on earth? : "))
if q3.lower() == "diamond" or user == "super_secret_admin_password":
    print("answer is correct! your current score is :", str(total_score))
    total_score = score + win
    score = total_score
else:
    print("womp womp, that's incorrect")
    score = total_score    

time.sleep(2.0)

# q4
print("----------------------------") # this is to make a new line
q3 = str(input("which continent is russia located in? : "))
if q3.lower() == "asia" or q3.lower() == "europe" or user == "super_secret_admin_password":
    print("answer is correct! your current score is :", str(total_score))
    total_score = score + win
    score = total_score
else:
    print("womp womp, that's incorrect")
    score = total_score    

time.sleep(2.0)