#The Combat Game 
import random 
import warnings 
warnings.filterwarnings("ignore") 
#Player class to Add Units , View Units 
class Player: 
  commander1 = [] #List of units purchased by Commander1 
  #Method for adding Units for the Player 
  def addUnit(self,commander,c_total): 
    units = { 1:"Archer", 2:"Soldier", 3:"Knight"} 
    print("\n Press Unit Number to purchase the Unit\n\n1\tArcher\n2\tSoldier\n3\tKnight\n4\tComplete the Purchase\n") 
    while (True): 
      try: 
        Selection = int(input("Select an unit to be inserted: ")) 
      except: 
        print("SELECT VALID INPUT") 
        continue 
      #Adding Units 
      if (Selection > 0) and (Selection < 4): 
        if(len(commander)>9): 
          print("OUT OF MONEY TO BUY AN UNIT") 
          break; 
        commander1=commander 
        commander1.append(units[Selection]) 
        c_total = c_total-1 
      #Complete Purchase 
      elif (Selection ==4): 
        break 
      else: 
        print("Invalid Option. Select from the options available!") 
      # print(commander) 
    return c_total 

#Instruction Class to display on How the game works 
class Instruction: 
 #Method for listing intructions on How to Play 
  def instruction(self): 
 #print("***Instructions of the Game***\nArchers are good against Soldiers but are terrible against Knights. \nSoldiers are good against Knights but can’t win against Archers. \nKnights beat Archers, but fall short against Soldiers. \nIf a unit comes up against a unit of the same type, both lose") 
    print("***Instructions of the Game***") 
    print("Type of Unit\tArcher\t\tSoldier\t\tKnight\nArcher\t\t\tTie\t\t\tArcher\t\tKnight\nSoldier\t\t\tArcher\t\tTie\t\t\tSoldier\nKnight\t\t\tKnight\t\tSoldier\t\tTie") 

#Play class to execute the game 
class Play: 
  instance1 = Player() 
  instance2 = Instruction() 
 #Get User's Option for the player 
  def playerOptions(self,commander,c_total): 
    while True: 
      try: 
        print("\n Press any of the below Options for PLAYER\n\nP\tPurchase Army\nV\tView Clan\nR\tReturn to Menu") 
        player1Options = input() 
      except: 
        print("INVALID INPUT") 
        continue 
      #Method to add Units for Commander 
      if(player1Options.upper()=="P"): 
        c_total = instance1.addUnit(commander,c_total) 
      #Print the commander's clan 
      elif(player1Options.upper()=="V"): 
        print("\n",commander) 
      #To start the Game 
      elif(player1Options.upper()=="R"): 
        break 
      else: 
        print("Invalid Option. Select from the options available!") 
    return c_total 

#Method for starting the game 
  def startGame(self,commander1,commander2,c_total=0): 
    #Dictionary to Maintain Player Points 
    playerPoints={ 
    "Player1":0, 
    "Player2":0 
    } 
    print("\t\t\t***Lets Play!!!***") 
    print("\nYour Players:") 
    print("Archers\t\tKnights\t\tSoldiers") 
    print(commander1.count("Archer"),"\t\t\t",commander1.count("Knight"),"\t\t\t",commander1.count("Soldier"),"\t") 
    print("\nComputer's Players:") 
    print("Archers\t\tKnights\t\tSoldiers") 
    print(commander2.count("Archer"),"\t\t\t",commander2.count("Knight"),"\t\t\t",commander2.count("Soldier"),"\t") 
    while(len(commander1)!=0 and len(commander2)!=0): 
      if(commander1[0] is commander2[0]): 
        commander1.pop(0) 
        commander2.pop(0) 
      elif(commander1[0] == "Archer" and commander2[0] == "Soldier" or commander1[0] == "Soldier" and commander2[0] == "Knight" or commander1[0] == "Knight" and commander2[0] == "Archer" ): 
 #COMMANDER 2 POP IS LIST WHICH HOLDS ALL THE ITEMS WHICH LOST IN THE BATTLE IN COMMANDER 2 
        commander2.pop(0) 
        playerPoints["Player1"]+=1 
      elif(commander1[0] == "Archer" and commander2[0] == "Knight" or commander1[0] == "Soldier" and commander2[0] == "Archer" or commander1[0] == "Knight" and commander2[0] == "Soldier"): 
 #COMMANDER 1 POP IS LIST WHICH HOLDS ALL THE ITEMS WHICH LOST IN THE BATTLE IN COMMANDER 1 
        commander1.pop(0) 
        playerPoints["Player2"]+=1 
      else: 
        break 
    print ("Points table") 
    print ("You\tComputer\n",playerPoints["Player1"],"\t",playerPoints["Player2"]) 
 #Displays winner of the match 
    print("\n***Points Table***\nPlayer1",playerPoints["Player1"],"\nPlayer2",playerPoints["Player2"]) 
    if(commander1 == [] and commander2 != []): 
      print("\n\t\t\t!!!COMPUTER WINS!!!") 
    elif(commander1!= [] and commander2 == []): 
      print("\n\t\t\t!!!!!YOU WIN!!!!!") 
    else: 
      print("MATCH DRAW") 
    print("\nYour Players:") 
    print("Archers\t\tKnights\t\tSoldiers") 
    print(commander1.count("Archer"),"\t\t\t",commander1.count("Knight"),"\t\t\t",commander1.count("Soldier"),"\t") 
    print("\nComputer's Players:") 
    print("Archers\t\tKnights\t\tSoldiers") 
    print(commander2.count("Archer"),"\t\t\t",commander2.count("Knight"),"\t\t\t",commander2.count("Soldier"),"\t") 
    print("------------------------------------------------------------------------------------------") 
    print("AT THE END OF THE GAME UNITS LEFT IN COMMANDER1 AND COMMANDER2 ARE ") 
    print("Your's:") 
    print("Archers\t\tKnights\t\tSoldiers")  
    print(commander1.count("Archer"),"\t\t\t",commander1.count("Knight"),"\t\t\t",commander1.count("Soldier"),"\t\t") 
    print("-------------------------------------------------------------------------------------------") 
    print("Computer's:") 
    print("Archers\t\tKnights\t\tSoldiers") 
    print(commander2.count("Archer"),"\t\t\t",commander2.count("Knight"),"\t\t\t",commander2.count("Soldier"),"\t") 
    print("-------------------------------------------------------------------------------------------") 
    print("Wanna Play Again? ") 
    print("Y\tYES\nN\tNO") 
    play_again=input() 
    return play_again 

if __name__ == '__main__': 
  #Creating Objects for the above classes 
  instance1 = Player() 
  instance2 = Play() 
  instance3 = Instruction() 
  commander1 = []#List of Player1 Units 
  commander2 = []#List of Player2 Units 
  c1_total=10 # Total Units for commander1 
  choices=["Archer","Soldier","Knight"] 
 
  while(True): 
  #Get users's Option to start the game(to purchase clan,view clan) 
    try: 
      userOptions = int(input("***THE COMBAT GAME***\n Press any of the below Options\n\n1\tChoose your Players\n2\tStart Game\n3\tHow to Play\n4\tExit Game\n")) 
    except: 
      print("ENTER VALID INPUT") 
      continue 
    #Options for Player1 
    if (userOptions==1): 
      try: 
        c1_total = instance2.playerOptions(commander1,c1_total) 
      except: 
        print("NOT ENOUGH UNITS IN COMMANDER 1") 
      else: 
        for i in range(10-c1_total): 
          computer_guess=random.choice(choices) 
          commander2.append(computer_guess) 
      print("-----------------------------------------") 
      print("Available money for Purchase: " , c1_total) 
      print("-----------------------------------------") 
    #Game Play 
    elif (userOptions==2): 
    #Game does not progress if Commander1 has no units 
      if(len(commander1) == 0): 
        print("No units for select1ed for Player1") 
      #Game starts 
      else: 
        play_again=instance2.startGame(commander1,commander2) 
        if play_again in "Yy": 
          continue 
        else: 
          break 
    #Intructions on How the Game Works 
    elif(userOptions==3): 
      instance3.instruction() 
      #Exit Game 
    elif(userOptions==4): 
      print("***EXITING GAME...!***") 
      break 
    else: 
      print("Invalid Option. Select from the options available!") 