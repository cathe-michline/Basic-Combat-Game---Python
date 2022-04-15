# Python--BasicGame
A simple game of combat without GUI. The basic game of the combat simulator comprises two commanders, where you choose your units namely Archer, Knight&amp; Soldier and the computer chooses its units for its army respectively to start the game.

**✔ LIBRARY:**

Random:
The random module provides random.choice() which is used to create
computer’s units by giving the list choices[“Archer”,”Knight”,”Soldier”]

Warning:
This module is used to remove all the warnings shown in output for the sake of
presentation.

**✔ CLASS:**
Three classes namely Player class, Instruction class, Play class is used

    i. Player Class: Includes function addUnit to add units (Archer, Soldier,
    Knight) to the commander’s respective armies upon each function call
    by the commanders.
    
    ii. Instruction Class: Includes function instruction to display how the
    game works(i.e.) unit’s weakness and strength.
    
    iii. Play Class: This class includes two functions
    - playerOptions which has options for the commander to
    Purchase Units,View Clan and an option to start the game.
    - startGame to start the combat once the commanders have
    purchased their units.

**✔ MAIN PROGRAM**
Here the instances for the classes are created. Two lists are created for
Commander1 and Commander2 to store their units purchased in the respective
order and each commander is allotted with a total of $10 each to buy units for
their respective army. The user is provided with 5 options namely:

    i. Commander1
    Here the functional call is made to playerOptions function of the Play
    class with Commander1’s list and Commander1 total units as arguments
    
    ii. Commander2
    
    iii. Ready to Play
    The functional call to startGame function of the Play with arguments
    Commander1’s list and Commander2’s list is made.
    
    iv. How to Play
    The function call to instructions function of the Instruction class is made
    to view how the game works
    
    v. Exit the Game
    This option exits the game

**✔ LIST**
    Two lists are maintained in this program:
    
    i. Commander1 List
    To add, remove, modify, append units for Commander1
    
    ii. Commander2 List
    The add, remove, modify, append units for Commander2 which is done by
    random.choice().
    
    iii. Choices List
    This list contains the three different units [“Archer”,”Knight”,”Soldier”]
    
**✔ DICTIONARY**
    Two dictionaries are maintained in this program:
    
    i. Unit Dictionary:
    Key – Unit Name
    Value – Units Number
    
    ii. Player Points Dictionary
    Key – Commander Name
    Value – Commander’s Points
    
**✔ EXCEPTIONS**
Exceptions are caught to handle invalid input
