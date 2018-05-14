name = "Teddy Minchin"

subject = ["English","History","Math","Spanish"]

print("My name is " + name)

for i in subject:
    print("I take " + i + " as one of my classes.")
    

nfl_teams = ["Giants", "Steelers", "Packers"]

for i in nfl_teams:
    if i == "Giants":
        print("Giants is the best team of the nfl teams 'Giants'")
    elif i == "Steelers":
        print("Steelers has the best wide reciever.")

    elif i == "Packers":
        print(i + " has one of the best Quaterbacks in the nfl.")
    else:
        print(i + " is one of the best teams in the nfl.")


teams = []

while True:
    print("What are your favorite teams? Type 'end' to stop program")
    answer = input()
    if answer == "end":
        break
    else:
        teams.append(answer)


for i in teams:
    print(i + " is one of your favorite teams.")
    









    
    
        
    
