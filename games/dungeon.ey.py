import Dungeon.html
from random import randint
import random
import winsound
import time
import threading


def gameover():
    global bosskills
    global playerhealth
    global gold
    global enemykills
    if playerhealth <= 0:
        print("Game over")
        print("had", gold, "gold")
        print("killed", enemykills, "enemies")
        print("killed", bosskills, "bosses")
        print("what is your adventures name")
        x = input()
        newdata = ("Name:", x, "Gold:", gold, "Enemies killed:", enemykills, "Bosses killed:", bosskills)
        file = open("leader_board.txt", "a")
        file.write(newdata)
        file.close()
        file = open("leader_board.txt", "r")
        filedata = file.read()
        print(filedata)
        file.close()


def thechoice():
    global fight
    fight = "END"
    print("the boss has been defeated.\n "
          "As you stand over him in victory you see before you two passages open")
    print("On your right you see a hallway back into the dungeon dark and wonder filled at what's next")
    print("but on your left you see sunlight, an opening to the surface, an END to this adventure")
    print("left or right")
    x = input()
    while x != "left" or "right":
        print("left or right")
        x = input()
        if x == "left":
            print("are you sure you want to end this adventure")
            print("yes or no")
            y = input()
            if y == "yes":
                print("As you walk to the exit you feel yourself warmed by the sun.")
                print("You feel the grass on your feet")
                print("wait didn't you have boots")
                print("you look down and realize you are completely naked")
                print("You look behind you and see that the dungeon entrance is now gone")
                print("as you turn back around you see your self in the middle of your village")
                print("everyone looking at you")
                print("Your welcome didn't want you to be lost now did ya haha")
                print("I'll be seeing you again, I know I will player, Bye Bye")
                print("Win?")
                print("oh wait I never caught you name")
                name = input()
                print("See you agian", name, "Oh and if we see eachother agian I will have mosltlikely have forgoten so tell me to 'remember' then your name")
                if name.lower == "markiplier":
                    print("What did you say", x, "well I have something for you left by a previous adventure ive been keeping it here for many years")
                if name.lower == "jacksepticeye":
                    print("What did you say", x, "well I have a something for you left by a previous adventure ive been keeping it here for many years")
            if y == "no":
                print("stop waisting my time")

        if x == "right":
            print("Are you sure you don't want to go home")
            print("yes or no")
            y = input()
            if y == "yes":
                print("you take one last glimpse at the exit as there could be no other way to leave this place")
                print("though you feel as if this place is your home")
                print("all the shop keepers you have met")
                print("the bodies that show your path")
                print("you walk through the door way")
                print("you find yourself in an underground village")
                print("tons of people cheering for you, thanking you from freeing them from the spell of the boss")
                print("The mayor of the town walks up to you and says\n"
                      " 'This town thanks you for everything you have done for us you can visit anytime,\n "
                      "shop, sleep, anything for you our great warrior'")
                print("(great job kid, I guess you got a new home )")
                print("The Mayor asks What is your name by the way "
                      "(I guess I never did get your name before throwing you in here)")
                name = input()
                print("Thank you", name)
                if name.lower == "markiplier":
                    print("What did you say", x, "well I have a letter for you ive been keeping it here for many years")
                if name.lower == "jacksepticeye":
                    print("What did you say", x, "well I have a letter for you ive been keeping it here for many years")
                village()


def player():  # need to set up mana abilities
    print("so what do you want to be, knight, rogue, or a mage")
    print("(by the way you get more info on each class before you are stuck with it)(classes don't do much yet)")
    print("(pick knight it works)")
    class1 = input()
    global fight
    fight = "normal"
    global playerhealth
    global gold
    global mana
    global basemana
    global spells
    spells = []
    global classes
    global enemykills
    global bosskills
    global equip
    equip = []
    global defence
    global inventory
    inventory = []
    global tpv
    tpv = 0
    if class1 == "knight":
        print("The Knight,")
        print("you start off with a long sword (3d6 A), a Chest piece (10 D) and 3 Strength Elixirs (+1 d6 A 2moves)")
        print("(y or n)")
        c = input()
        if c != "y":
            player()
        elif c == "y":
            classes = "Knight"
            equip.append("Long Sword")
            equip.append("Chest Piece")
            defence = 10
            inventory.append("Strength Elixir")
            inventory.append("Strength Elixir")
            inventory.append("Strength Elixir")
            playerhealth = 100
            gold = 100
            mana = 100
            basemana = mana
            enemykills = 0
            bosskills = 0
            print("You start with", playerhealth, "health and", gold, "gold")
    elif class1 == "rogue":
        print("The Rogue,")
        print("you start off with a Short Sword (4d4 A), a Chest Piece (10 D) and 3 Health Elixirs (+10 Health)")
        print("(y or n)")
        c = input()
        if c != "y":
            player()
        elif c == "y":
            classes = "Rogue"
            equip.append("Short Sword")
            equip.append("Chest Piece")
            defence = 10
            inventory.append("Health Elixir")
            inventory.append("Health Elixir")
            inventory.append("Health Elixir")
            playerhealth = 100
            gold = 100
            mana = 100
            basemana = mana
            enemykills = 0
            bosskills = 0
            print("You start with", playerhealth, "health and", gold, "gold")
    elif class1 == "mage":
        print("The mage,")
        print("you start off with a Staff (2d6 A) and (+50mana), a Robe (8 D) and 3 Mana Elixirs (+50 Mana), "
              "and the spell Fire Ball (20 Points of damage)")
        print("(y or n)")
        c = input()
        if c != "y":
            player()
        elif c == "y":
            classes = "Mage"
            equip.append("Staff")
            equip.append("Robe")
            defence = 8
            inventory.append("Mana Elixir")
            inventory.append("Mana Elixir")
            inventory.append("Mana Elixir")
            spells.append("Fire Ball")
            playerhealth = 100
            gold = 100
            mana = 150
            basemana = mana
            enemykills = 0
            bosskills = 0
            print("You start with", playerhealth, "health and", gold, "gold")
    else:
        player()


def manacounter():
    global mana
    global basemana
    print("your mana has been reset")
    mana = basemana


def inventory1():
    global spells
    global inventory
    print(inventory)
    global equip
    global strength
    global defence
    print("what would you like to select, or you can 'exit'")
    print("(by the way for any spell books just say the spell not the book part")
    x = input()
    if x.lower() == "healing elixir":
        if "Healing Elixir" in inventory:
            print("Healing Elixir adds 10 health to your player health"
                  "Would you like to activate the Healing Elixir(y,n)")
            e = input()
            if e == "y":
                healingelixir()
                inventory1()
            elif e == "n":
                inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "strength elixir":
        if "Strength Elixir" in inventory:
            print("Strength Elixir gives 1d6 dice of damage for 2 moves"
                  "Would you like to activate Strength Elixir(y,n)")
            e = input()
            if e == "y":
                equip.append("Strength Elixir")
                strength = 2
                inventory1()
                if strength <= 0:
                    equip.remove("Strength Elixir")
                    print("Strength Elixir as worn off")
            if e == "n":
                inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "mana elixir":
        if "Mana Elixir" in inventory:
            print("Mana Elixir gives 50 mana"
                  "Would you like to activate Strength Elixir(y,n)")
            e = input()
            if e == "y":
                manaelixir()
                inventory1()
            if e == "n":
                inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "long sword":
        if "Long Sword" in inventory:
            print("don't have any special abilities")
            inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "short sword":
        if "Short Sword" in inventory:
            print("don't have any special abilities")
            inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "staff":
        if "Staffs" in inventory:
            print("don't have any special abilities")
            inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "fire ball":
        if "Spell Book: Fire Ball" in inventory:
            global fbdamage
            global fbmana
            if "Fire Ball" not in spells and "Fire Ball II" not in spells and "Fire Ball III" not in spells and "Fire Ball IV" not in spells and "Fire Ball V" not in spells:
                print("adds the attack Fire ball"
                      " it does 30 points of damage"
                      " but depletes 10 points of mana"
                      " would you like to read it")
                e = input()
                if e == "y":
                    if "Fire Ball" not in spells:
                        spells.append("Fire Ball")
                        inventory.remove("Spell Book: Fire Ball")
                        print("You read through the first chapter of the book\n"
                              " but before you start the next chapter the book bursts into flames\n"
                              " You gain Fire Ball")
                        fbdamage = 30
                        fbmana = 10
                        inventory1()
                if e == "n":
                    inventory1()
            elif "Fire Ball" in spells:
                print("you already have this item equipped")
                print("Would you like to upgrade your Fire Ball")
                print("it would add 10 points of damage but increases the mana cost by 5")
                print("or you can add 0 points of damage and decreases the mana cost by 5")
                print("beware if you have 0 mana cost you can waist this book if you decrease the mana.")
                e = input()
                if e == "y":
                    print("Would you like to attack more'a', or use less mana'm'")
                    s = input()
                    if s == "a":
                        print("are you sure... nah im not gunna be that kinda game, you increase your attack")
                        spells.remove("Fire Ball")
                        inventory.remove("Spell Book: Fire Ball")
                        spells.append("Fire Ball II")
                        fbdamage = fbdamage + 10
                        fbmana = fbmana + 5
                        print("You first look at the table of context to see how many times this book is useful\n"
                              "you see this book has 5 chapters")
                    if s == "m":
                        print("are you sure... nah im not gunna be that kinda game, you decrease your mana")
                        spells.remove("Fire Ball")
                        inventory.remove("Spell Book: Fire Ball")
                        spells.append("Fire Ball II")
                        fbdamage = fbdamage + 0
                        fbmana = fbmana - 5
                        print("You first look at the table of context to see how many times this book is useful\n"
                              "you see this book has 5 chapters")
                inventory1()
                if e == "n":
                    print("your gunna change your mind I know you will")
                    inventory1()
            elif "Fire Ball II" in spells:
                print("you already have this item equipped")
                print("Would you like to upgrade your Fire Ball")
                print("it would add 10 points of damage but increases the mana cost by 5")
                print("or you can add 0 points of damage and decreases the mana cost by 5")
                e = input()
                if e == "y":
                    print("Would you like to attack more'a', or use less mana'm'")
                    s = input()
                    if s == "a":
                        print("are you sure... nah im not gunna be that kinda game, you increase your attack")
                        spells.remove("Fire Ball II")
                        inventory.remove("Spell Book: Fire Ball")
                        spells.append("Fire Ball III")
                        fbdamage = fbdamage + 10
                        fbmana = fbmana + 5
                    if s == "m":
                        print("are you sure... nah im not gunna be that kinda game, you decrease your mana")
                        spells.remove("Fire Ball II")
                        inventory.remove("Spell Book: Fire Ball")
                        spells.append("Fire Ball III")
                        fbdamage = fbdamage + 0
                        fbmana = fbmana - 5
                inventory1()
                if e == "n":
                    print("your gunna change your mind I know you will")
                    inventory1()
            elif "Fire Ball III" in spells:
                print("you already have this item equipped")
                print("Would you like to upgrade your Fire Ball")
                print("it would add 10 points of damage but increases the mana cost by 5")
                print("or you can add 0 points of damage and decreases the mana cost by 5")
                e = input()
                if e == "y":
                    print("Would you like to attack more'a', or use less mana'm'")
                    s = input()
                    if s == "a":
                        print("are you sure... nah im not gunna be that kinda game, you increase your attack")
                        spells.remove("Fire Ball III")
                        inventory.remove("Spell Book: Fire Ball")
                        spells.append("Fire Ball IV")
                        fbdamage = fbdamage + 10
                        fbmana = fbmana + 5
                    if s == "m":
                        print("are you sure... nah im not gunna be that kinda game, you decrease your mana")
                        spells.remove("Fire Ball III")
                        inventory.remove("Spell Book: Fire Ball")
                        spells.append("Fire Ball IV")
                        fbdamage = fbdamage + 0
                        fbmana = fbmana - 5
                        print("You first look at the table of context to see how many times this book is useful\n"
                              "you see this book has 5 chapters")
                inventory1()
                if e == "n":
                    print("your gunna change your mind I know you will")
                    inventory1()
            elif "Fire Ball IV" in spells:
                print("you already have this item equipped")
                print("Would you like to upgrade your Fire Ball")
                print("it would add 10 points of damage but increases the mana cost by 5")
                print("or you can add 0 points of damage and decreases the mana cost by 5")
                e = input()
                if e == "y":
                    print("Would you like to attack more'a', or use less mana'm'")
                    s = input()
                    if s == "a":
                        print("are you sure... nah im not gunna be that kinda game, you increase your attack")
                        spells.remove("Fire Ball IV")
                        inventory.remove("Spell Book: Fire Ball")
                        spells.append("Fire Ball V")
                        fbdamage = fbdamage + 10
                        fbmana = fbmana + 5
                        print("You first look at the table of context to see how many times this book is useful\n"
                              "you see this book has 5 chapters")
                    if s == "m":
                        print("are you sure... nah im not gunna be that kinda game, you decrease your mana")
                        spells.remove("Fire Ball IV")
                        inventory.remove("Spell Book: Fire Ball")
                        spells.append("Fire Ball V")
                        fbdamage = fbdamage + 0
                        fbmana = fbmana - 5
                        print("You first look at the table of context to see how many times this book is useful\n"
                              "you see this book has 5 chapters")
                inventory1()
                if e == "n":
                    print("your gunna change your mind I know you will")
                    inventory1()
                if "Fire Ball V" in spells:
                    print("You have maxed out your fireball there is no more to be learned")
                    print("(your still not a better mage than me)")
                    inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "heal":
        if "Spell Book:Heal" in inventory:
            print()
            inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "vinegrow":
        if "Spell Book:VineGrow" in inventory:
            print()
            inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "freeze":
        if "Spell Book:Freeze" in inventory:
            print()
            inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "chest piece":
        if "Chest Piece" in inventory:
            if "Chest Piece" not in equip and "Chest Piece II" not in equip and "Chest Piece III" not in equip and "Chest Piece IV" not in equip and "Chest Piece V" not in equip:
                print("Equipping this adds 10 defence"
                      "\nWould you like to equip it")
                e = input()
                if e == "y":
                        equip.append("Chest Piece")
                        inventory.remove("Chest Piece")
                        defence = defence + 10
                        inventory1()
                if e == "n":
                    inventory1()
            if "Chest Piece" in equip or "Chest Piece II" in equip or "Chest Piece III" in equip or "Chest Piece IV"  in equip or "Chest Piece V" in equip:
                print("You already have a Chest Piece equipped")
                inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "gloves":
        if "Gloves" in inventory:
            if "Gloves" not in equip and "Gloves II" not in equip and "Gloves III" not in equip and "Gloves IV" not in equip and "Gloves V" not in equip:
                print("adds 5 defence"
                      "\nWould you like to equip it")
                e = input()
                if e == "y":
                    if "Gloves" not in equip:
                        equip.append("Gloves")
                        inventory.remove("Gloves")
                        defence = defence + 5
                        inventory1()
                if e == "n":
                    inventory1()
            if "Gloves" in equip or "Gloves II" not in equip or "Gloves III" not in equip or "Gloves IV" not in equip or "Gloves V" not in equip:
                print("you already have Gloves equipped")
                inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "helm":
        if "Helm" in inventory:
            if "Helm" not in equip and "Helm II" not in equip and "Helm III" not in equip and "Helm IV" not in equip and "Helm V" not in equip:
                print("adds 5 defence"
                      "\nWould you like to equip it")
                e = input()
                if e == "y":
                    if "Helm" not in equip:
                        equip.append("Helm")
                        inventory.remove("Helm")
                        defence = defence + 5
                        inventory1()
                if e == "n":
                    inventory1()
            if "Helm" in equip or "Helm II"  in equip or "Helm III"  in equip or "Helm IV"  in equip or "Helm V"  in equip:
                print("you already have a Helm equipped")
                inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "robe":
        if "Robe" in inventory:
            if "Robe" not in equip and "Robe II" not in equip and "Robe III" not in equip and "Robe IV" not in equip and "Robe V" not in equip:
                print("adds 8 defence"
                      "\nWould you like to equip it")
                e = input()
                if e == "y":
                    if "Robe" not in equip:
                        equip.append("Robe")
                        inventory.remove("Robe")
                        defence = defence + 8
                        inventory1()
            if "Robe" in equip or "Robe II" in equip or "Robe III" in equip or "Robe IV" in equip or "Robe V" in equip:
                print("you already have a Robe equipped")
                inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "boots":
        if "Boots" in inventory:
            if "Boots" not in equip and "Boots II" not in equip and "Boots III" not in equip and "Boots IV" not in equip and "Boots V" not in equip:
                print("adds 5 defence"
                      "\nWould you like to equip it")
                e = input()
                if e == "y":
                    if "Boots" not in equip:
                        equip.append("Boots")
                        inventory.remove("Boots")
                        defence = defence + 5
                        inventory1()
            if "Boots" in equip or "Boots II" in equip or "Boots III" in equip or "Boots IV" in equip or "Boots V" in equip:
                print("you already have Boots equipped")
                inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "pants":
        if "Pants" in inventory:
            if "Pants" not in equip and "Pants II" not in equip and "Pants III" not in equip and "Pants IV" not in equip and "Pants V" not in equip:
                print("adds 5 defence "
                      "\nWould you like to equip it")
                e = input()
                if e == "y":
                    if "Pants" not in equip:
                        equip.append("Pants")
                        inventory.remove("Pants")
                        defence = defence + 5
                        inventory1()
            if "Pants" in equip or "Pants II" in equip or "Pants III" in equip or "Pants IV" in equip or "Pants V" in equip:
                print("you already have this item equipped")
                inventory1()
        else:
            print("N/A")
            inventory1()
    if x.lower() == "exit":
        if fight == "normal":
            crossroads()
        if fight == "end":
            village()


def inventory2():
    global spells
    global inventory
    print("inventory: ",inventory)
    print("spells: ", spells)
    global equip
    global strength
    global defence
    global fight
    print("what would you like to select, or you can 'exit'")
    x = input()
    if x.lower() == "healing elixir":
        if "Healing Elixir" in inventory:
            print("Healing Elixir adds 10 health to your player health"
                  "Would you like to activate the Healing Elixir(y,n)")
            e = input()
            if e == "y":
                healingelixir()
                if fight == "normal":
                    ediceroll()
                if fight == "Boss":
                    bossdiceroll()
            elif e == "n":
                if fight == "normal":
                    if fight == "normal":
                        ediceroll()
                    if fight == "Boss":
                        bossdiceroll()
        else:
            print("N/A")
            if fight == "normal":
                ediceroll()
            if fight == "Boss":
                bossdiceroll()
    if x.lower() == "strength elixir":
        if "Strength Elixir" in inventory:
            print("Strength Elixir gives 1d6 dice of damage for 2 moves"
                  "Would you like to activate Strength Elixir(y,n)")
            e = input()
            if e == "y":
                equip.append("Strength Elixir")
                strength = 2
                if strength <= 0:
                    equip.remove("Strength Elixir")
                if fight == "normal":
                    ediceroll()
                if fight == "Boss":
                    bossdiceroll()
            if e == "n":
                if fight == "normal":
                    ediceroll()
                if fight == "Boss":
                    bossdiceroll()
        else:
            print("N/A")
            if fight == "normal":
                ediceroll()
            if fight == "Boss":
                bossdiceroll()
    if x.lower() == "mana elixir":
        if "Mana Elixir" in inventory:
            print("Mana Elixir gives 50 mana"
                  "Would you like to activate Strength Elixir(y,n)")
            e = input()
            if e == "y":
                manaelixir()
                if fight == "normal":
                    ediceroll()
                if fight == "Boss":
                    bossdiceroll()
            if e == "n":
                if fight == "normal":
                    ediceroll()
                if fight == "Boss":
                    bossdiceroll()
        else:
            print("N/A")
            if fight == "normal":
                ediceroll()
            if fight == "Boss":
                bossdiceroll()
    if x.lower() == "fireball":
        fireball()
    if x.lower() == "heal":
        heal()
    if x.lower() == "vinegrow":
        vinegrow()
    if x.lower() == "freeze":
        freeze()
    if x.lower() == "exit":
        if fight == "normal":
            if classes == "Knight":
                knightdiceroll()
            if classes == "Rogue":
                roguediceroll()
            if classes == "Mage":
                magediceroll()
        if fight == "Boss":
            if classes == "Knight":
                knightdicerollb()
            if classes == "Rogue":
                roguedicerollb()
            if classes == "Mage":
                magedicerollb()


def healingelixir():
    global playerhealth
    playerhealth = playerhealth + 10


def manaelixir():
    global mana
    mana = mana + 50


def treasure():
    global gold
    global inventory
    t = randint(10, 50)
    gold = gold + t
    print("you gained", t, "gold")
    print("you now have", gold, "gold")
    x = randint(1, 5)
    if x == 2 or 4:
        x = randint(1, 3)
        e = ["Healing Elixir", "Strength Elixir", "Mana Elixir"]
        w = ["Long Sword", "Short Sword", "Staff", "Spell Book:Fire ball", "Spell Book: Heal", "Spell Book: Vine Grow",
             "Spell Book: Freeze"]
        a = ["Chest Piece", "Pants", "Gloves", "Helm", "Robe", "Boots"]
        if x == 1:
            t2 = random.choice(e)
            print("You also got", t2)
            inventory.append(t2)
        if x == 2:
            t2 = random.choice(w)
            print("You also got", t2)
            inventory.append(t2)
        if x == 3:
            t2 = random.choice(a)
            print("You also got", t2)
            inventory.append(t2)
    x = randint(1, 100)
    if x == 25 or 75:
        s = ["Long Sword of Demon Fire", "Black Widow's Short Sword", "Arch Mage's Staff"]
        ss = random.choice(s)
        print("You also got a legendary item", ss, "You think your lucky uh well... "
                                                   "\n I got no witty comment becuase "
                                                   "I don't even have one of these and I'm the narator "
                                                   "\nit's a 1/50 chance fyi")
        inventory.append(ss)


def enemylevel():
    global enemyhealth
    global enemykills
    if enemykills <= 10:
        level = randint(1, 10)
        print("a level", level, "enemy has appeared")
        enemyhealth = (25 + level)
        print("with", enemyhealth, "points of health")
    elif 10 < enemykills <= 20:
        level = randint(11, 20)
        print("a level", level, "enemy has appeared")
        enemyhealth = (50 + level)
        print("with", enemyhealth, "points of health")
    elif 20 < enemykills <= 30:
        level = randint(21, 30)
        print("a level", level, "enemy has appeared")
        enemyhealth = (75 + level)
        print("with", enemyhealth, "points of health")
    elif 30 < enemykills <= 40:
        level = randint(31, 40)
        print("a level", level, "enemy has appeared")
        enemyhealth = (100 + level)
        print("with", enemyhealth, "points of health")
    elif 40 < enemykills <= 50:
        level = randint(41, 50)
        print("a level", level, "enemy has appeared")
        enemyhealth = (150 + level)
        print("with", enemyhealth, "points of health")


def bosstats():
    global defence
    global enemykills
    global bosshealth
    bosshealth = (200 + enemykills)
    print("The boss has ", bosshealth, " points of health")


def fighting():
    global enemykills
    global classes
    global fight
    if enemykills < 50 or fight == "normal":
        enemylevel()
        print("would you like to 'fight' or 'turn back'")
        f = input()
        if f == "fight":
            print("You prepare for battle")
            if classes == "Knight":
                knightdiceroll()
            if classes == "Rogue":
                roguediceroll()
            if classes == "Mage":
                magediceroll()
        elif f == "turn back":
                print("You run in fear, (like a little baby)")
                crossroads()
        else:
            fighting()
    elif enemykills == 50:
        fight = "boss"
        print("You hear a large rumble as you search the hallway. (oooo you in trouble.)")
        print("As you reach the end a enormous beast comes charging at you three times your size.")
        print("(This is going to be fun.)")
        print("it belches 'So you are the one that has been killing my men, ")
        print("well now its time for you to feel their pain.'")
        print("(Quick someone get the popcorn, oh you guys cant see this, danget.)")
        bosstats()
        print("Buy the way no running, as you look around you see all your exits close around you")
        print("You prepare for battle")
        if classes == "Knight":
            knightdicerollb()
        if classes == "Rogue":
            roguedicerollb()
        if classes == "Mage":
            magedicerollb()
    elif fight == "END":
        enemylevel()
        print("would you like to 'fight' or 'turn back'")
        f = input()
        if f == "fight":
            print("You prepare for battle")
            if classes == "Knight":
                knightdiceroll()
            if classes == "Rogue":
                roguediceroll()
            if classes == "Mage":
                magediceroll()
        elif f == "turn back":
            print("You run in fear, (like a little baby)")
            village()
        else:
            fighting()


def knightdicerollb():
    global manacounter
    global equip
    global bosshealth
    global strength
    global bosskills
    if "Strength Elixir" in equip:
        a1 = randint(1, 6)
        a2 = randint(1, 6)
        a3 = randint(1, 6)
        a4 = randint(1, 6)
        strength = strength - 1
        a = a1+a2+a3+a4
        print("you did", a, "point of damage"
              "(wow that's all)")
        bosshealth = bosshealth - a
        print("enemy has", bosshealth, "health left")
        if bosshealth > 0:
            bossdiceroll()
        if bosshealth <= 0:
            treasure()
            bosskills = bosskills + 1
            manacounter()
            thechoice()

    elif "Strength Elixir" not in equip:
        a1 = randint(1, 6)
        a2 = randint(1, 6)
        a3 = randint(1, 6)
        a = a1+a2+a3
        print("you did", a, "point of damage"
                            "(wow that's all)")
        bosshealth = bosshealth - a
        print("enemy has", bosshealth, "health left")
        if bosshealth > 0:
            bossdiceroll()
        if bosshealth <= 0:
            treasure()
            bosskills = bosskills + 1
            manacounter()
            thechoice()


def knightdiceroll():
    global fight
    global equip
    global enemyhealth
    global strength
    global enemykills
    print("would you like to 'attack' or look through your 'inventory' to cast a spell or use a potion")
    x = input()
    if x == "attack":
        if "Strength Elixir" in equip:
            a1 = randint(1, 6)
            a2 = randint(1, 6)
            a3 = randint(1, 6)
            a4 = randint(1, 6)
            strength = strength - 1
            a = a1+a2+a3+a4
            if a1 and a2 and a3 == 6:
                print("you made a crit hit")
                print("you kill your enemy and move on to the next area"
                      "(OOO big shot here)")
                enemyhealth = 0
                treasure()
                if fight == "normal":
                    crossroads()
                if fight == "end":
                    village()
            else:
                print("you did", a, "point of damage"
                      "(wow that's all)")
                enemyhealth = enemyhealth - a
                print("enemy has", enemyhealth, "health left")
                if enemyhealth > 0:
                    ediceroll()
                if enemyhealth <= 0:
                    treasure()
                    enemykills = enemykills + 1
                    manacounter()
                    if fight == "normal":
                        crossroads()
                    if fight == "end":
                        village()
        elif "Strength Elixir" not in equip:
            a1 = randint(1, 6)
            a2 = randint(1, 6)
            a3 = randint(1, 6)
            a = a1+a2+a3
            if a1 and a2 and a3 == 6:
                print("you made a crit hit")
                print("you kill your enemy and move on to the next area"
                      "(OOO big shot here)")
                enemyhealth = 0
                treasure()
                if fight == "normal":
                    crossroads()
                if fight == "end":
                    village()
            else:
                print("you did", a, "point of damage"
                                    "(wow that's all)")
                enemyhealth = enemyhealth - a
                print("enemy has", enemyhealth, "health left")
                if enemyhealth > 0:
                    ediceroll()
                if enemyhealth <= 0:
                    treasure()
                    enemykills = enemykills + 1
                    manacounter()
                    if fight == "normal":
                        crossroads()
                    if fight == "end":
                        village()
    if x == "inventory":
        inventory2()


def roguedicerollb():
    global manacounter
    global bosshealth
    global equip
    global strength
    global bosskills
    if "Strength Elixir" in equip:
        a1 = randint(1, 4)
        a2 = randint(1, 4)
        a3 = randint(1, 4)
        a4 = randint(1, 4)
        a5 = randint(1, 6)
        strength = strength - 1
        a = a1+a2+a3+a4+a5
        print("you did", a, "point of damage"
                            "(wow that's all)")
        bosshealth = bosshealth - a
        print("enemy has", bosshealth, "health left")
        if bosshealth > 0:
            bossdiceroll()
        if bosshealth <= 0:
            treasure()
            bosskills = bosskills + 1
            manacounter()
            thechoice()
    elif "Strength Elixir" not in equip:
        a1 = randint(1, 4)
        a2 = randint(1, 4)
        a3 = randint(1, 4)
        a4 = randint(1, 4)
        a = a1+a2+a3+a4
        print("you did", a, "point of damage"
                            "(wow that's all)")
        bosshealth = bosshealth - a
        print("enemy has", bosshealth, "health left")
        if bosshealth > 0:
            bossdiceroll()
        if bosshealth <= 0:
            treasure()
            bosskills = bosskills + 1
            manacounter()
            thechoice()


def roguediceroll():
    global manacounter
    global enemyhealth
    global equip
    global strength
    global enemykills
    if "Strength Elixir" in equip:
        a1 = randint(1, 4)
        a2 = randint(1, 4)
        a3 = randint(1, 4)
        a4 = randint(1, 4)
        a5 = randint(1, 6)
        strength = strength - 1
        a = a1+a2+a3+a4+a5
        if a1+a2+a3+a4 == 16 or a1+a2 == 8 or a1+a3 == 8 or a1+a4 == 8 or a2+a3 == 8 or a2+a4 == 8 or a3+a4 == 8:
            print("you made a crit hit")
            print("you kill your enemy and move on to the next area"
                  "(OOO big shot here)")
            enemyhealth = 0
            treasure()
            if fight == "normal":
                crossroads()
            if fight == "end":
                village()
        else:
            print("you did", a, "point of damage"
                                "(wow that's all)")
            enemyhealth = enemyhealth - a
            print("enemy has", enemyhealth, "health left")
            if enemyhealth > 0:
                ediceroll()
        if enemyhealth <= 0:
            treasure()
            enemykills = enemykills + 1
            manacounter()
            if fight == "normal":
                crossroads()
            if fight == "end":
                village()
    elif "Strength Elixir" not in equip:
        a1 = randint(1, 4)
        a2 = randint(1, 4)
        a3 = randint(1, 4)
        a4 = randint(1, 4)
        a = a1+a2+a3+a4
        if a == 16 or a1+a2 == 8 or a1+a3 == 8 or a1+a4 == 8 or a2+a3 == 8 or a2+a4 == 8 or a3+a4 == 8:
            print("you made a crit hit")
            print("you kill your enemy and move on to the next area"
                  "(OOO big shot here)")
            enemyhealth = 0
            treasure()
            if fight == "normal":
                crossroads()
            if fight == "end":
                village()
        else:
            print("you did", a, "point of damage"
                                "(wow that's all)")
            enemyhealth = enemyhealth - a
            print("enemy has", enemyhealth, "health left")
            if enemyhealth > 0:
                ediceroll()
        if enemyhealth <= 0:
            treasure()
            enemykills = enemykills + 1
            manacounter()
            if fight == "normal":
                crossroads()
            if fight == "end":
                village()


def magedicerollb():
    global manacounter
    global bosshealth
    global equip
    global strength
    global bosskills
    if "Strength Elixir" in equip:
        a1 = randint(1, 6)
        a2 = randint(1, 6)
        a3 = randint(1, 6)
        strength = strength - 1
        a = a1 + a2 + a3
        print("you did", a, "point of damage"
                            "(wow that's all)")
        bosshealth = bosshealth - a
        print("enemy has", bosshealth, "health left")
        if bosshealth > 0:
            bossdiceroll()
        if bosshealth <= 0:
            treasure()
            bosskills = bosskills + 1
            manacounter()
            thechoice()
    elif "Strength Elixir" not in equip:
        a1 = randint(1, 6)
        a2 = randint(1, 6)
        a = a1 + a2
        print("you did", a, "point of damage"
                            "(wow that's all)")
        bosshealth = bosshealth - a
        print("enemy has", bosshealth, "health left")
        if bosshealth > 0:
            bossdiceroll()
        if bosshealth <= 0:
            treasure()
            bosskills = bosskills + 1
            manacounter()
            thechoice()


def magediceroll():
    global manacounter
    global enemyhealth
    global equip
    global strength
    global enemykills
    if "Strength Elixir" in equip:
        a1 = randint(1, 6)
        a2 = randint(1, 6)
        a3 = randint(1, 6)
        strength = strength - 1
        a = a1 + a2 + a3
        if a1 and a2 == 6:
            print("you made a crit hit")
            print("you kill your enemy and move on to the next area"
                  "(OOO big shot here)")
            enemyhealth = 0
            treasure()
            if fight == "normal":
                crossroads()
            if fight == "end":
                village()
        else:
            print("you did", a, "point of damage"
                                "(wow that's all)")
            enemyhealth = enemyhealth - a
            print("enemy has", enemyhealth, "health left")
            if enemyhealth > 0:
                ediceroll()
        if enemyhealth <= 0:
            treasure()
            enemykills = enemykills + 1
            manacounter()
            if fight == "normal":
                crossroads()
            if fight == "end":
                village()
    elif "Strength Elixir" not in equip:
        a1 = randint(1, 6)
        a2 = randint(1, 6)
        a = a1 + a2
        if a1 and a2 == 6:
            print("you made a crit hit")
            print("you kill your enemy and move on to the next area"
                  "")
            enemyhealth = 0
            treasure()
            if fight == "normal":
                crossroads()
            if fight == "end":
                village()
        else:
            print("you did", a, "point of damage"
                                "(wow that's all)")
            enemyhealth = enemyhealth - a
            print("enemy has", enemyhealth, "health left")
            if enemyhealth > 0:
                ediceroll()
        if enemyhealth <= 0:
            treasure()
            enemykills = enemykills + 1
            manacounter()
            if fight == "normal":
                crossroads()
            if fight == "end":
                village()


def bossdiceroll():
    global playerhealth
    global equip
    global defence
    global enemykills
    a1 = randint(1, 20)
    a2 = randint(1, 20)
    a3 = randint(1, 20)
    a = a1 + a2 + a3 - defence
    if a <= 0:
        a = 0
    print("The Boss did", a, "points of damage")
    playerhealth = playerhealth - a
    print("you have", playerhealth, "point of health left"
                                    "(weakling)")
    if playerhealth > 0:
        print("you prepare for your next fight")
        if classes == "Knight":
            knightdiceroll()
        if classes == "Rogue":
            roguediceroll()
        if classes == "Mage":
            magediceroll()
    if playerhealth <= 0:
        gameover()


def ediceroll():
    global playerhealth
    global equip
    global defence
    global enemykills
    while enemykills <= 10:
        a1 = randint(1, 5)
        a2 = randint(1, 5)
        a3 = randint(1, 5)
        a = a1 + a2 + a3 - defence
        if a <= 0:
            a = 0
        print("enemy did", a, "points of damage")
        playerhealth = playerhealth - a
        print("you have", playerhealth, "point of health left"
                                        "(weakling)")
        if playerhealth > 0:
            print("Do you want to continue the 'fight' or 'run'")
            x = input()
            if x == "fight":
                if classes == "Knight":
                    knightdiceroll()
                if classes == "Rogue":
                    roguediceroll()
                if classes == "Mage":
                    magediceroll()
            elif x == "run":
                print("you run from the fight escaping with you life"
                      "(like a little bi***, oh I can't say that, stupid rules, this is MY mind)")
                crossroads()
        if playerhealth <= 0:
            gameover()
    while 10 < enemykills <= 20:
        a1 = randint(1, 10)
        a2 = randint(1, 5)
        a3 = randint(1, 5)
        a = a1 + a2 + a3 - defence
        if a <= 0:
            a = 0
        print("enemy did", a, "points of damage")
        playerhealth = playerhealth - a
        print("you have", playerhealth, "point of health left"
                                        "(weakling)")
        if playerhealth > 0:
            print("Do you want to continue the 'fight' or 'run'")
            x = input()
            if x == "fight":
                if classes == "Knight":
                    knightdiceroll()
                if classes == "Rogue":
                    roguediceroll()
                if classes == "Mage":
                    magediceroll()
            elif x == "run":
                print("you run from the fight escaping with you life"
                      "(like a little bi***, oh I can't say that, stupid rules, this is MY mind)")
                crossroads()
        if playerhealth <= 0:
            gameover()
    while 20 < enemykills <= 30:
        a1 = randint(1, 10)
        a2 = randint(1, 10)
        a3 = randint(1, 5)
        a = a1 + a2 + a3 - defence
        if a <= 0:
            a = 0
        print("enemy did", a, "points of damage")
        playerhealth = playerhealth - a
        print("you have", playerhealth, "point of health left"
                                        "(weakling)")
        if playerhealth > 0:
            print("Do you want to continue the 'fight' or 'run'")
            x = input()
            if x == "fight":
                if classes == "Knight":
                    knightdiceroll()
                if classes == "Rogue":
                    roguediceroll()
                if classes == "Mage":
                    magediceroll()
            elif x == "run":
                print("you run from the fight escaping with you life"
                      "(like a little bi***, oh I can't say that, stupid rules, this is MY mind)")
                crossroads()
        if playerhealth <= 0:
            gameover()
    while 30 < enemykills <= 40:
        a1 = randint(1, 10)
        a2 = randint(1, 10)
        a3 = randint(1, 10)
        a = a1 + a2 + a3 - defence
        if a <= 0:
            a = 0
        print("enemy did", a, "points of damage")
        playerhealth = playerhealth - a
        print("you have", playerhealth, "point of health left"
                                        "(weakling)")
        if playerhealth > 0:
            print("Do you want to continue the 'fight' or 'run'")
            x = input()
            if x == "fight":
                if classes == "Knight":
                    knightdiceroll()
                if classes == "Rogue":
                    roguediceroll()
                if classes == "Mage":
                    magediceroll()
            elif x == "run":
                print("you run from the fight escaping with you life"
                      "(like a little bi***, oh I can't say that, stupid rules, this is MY mind)")
                crossroads()
        if playerhealth <= 0:
            gameover()
    while 40 < enemykills <= 50:
        a1 = randint(1, 10)
        a2 = randint(1, 10)
        a3 = randint(1, 15)
        a = a1 + a2 + a3 - defence
        if a <= 0:
            a = 0
        print("enemy did", a, "points of damage")
        playerhealth = playerhealth - a
        print("you have", playerhealth, "point of health left"
                                        "(weakling)")
        if playerhealth > 0:
            print("Do you want to continue the 'fight' or 'run'")
            x = input()
            if x == "fight":
                if classes == "Knight":
                    knightdiceroll()
                if classes == "Rogue":
                    roguediceroll()
                if classes == "Mage":
                    magediceroll()
            elif x == "run":
                print("you run from the fight escaping with you life"
                      "(like a little bi***, oh I can't say that, stupid rules, this is MY mind)")
                crossroads()
        if playerhealth <= 0:
            gameover()


# spells
def fireball():
    global mana
    global fight
    global equip
    global enemeyhealth
    global bosshealth
    global fbdamage
    global fbmana
    if fbmana < 0:
        fbmana = 0
    if fbmana > mana:
        print("you don't have enough mana to cast this")
    print("this fire ball does ", fbdamage, " damage and costs ", fbmana, " mana to cast")
    print("use it? 'y' or 'n'")
    x = input()
    if x == "y":
        if fight == "normal":
            print("You fling a ball of fire at the enemy")
            enemeyhealth = enemeyhealth - fbdamage
            mana = mana - fbmana
        if fight == "boss":
            print("You fling a ball of fire at the enemy")
            bosshealth = bosshealth - fbdamage
            mana = mana - fbmana
    if x == "n":
        if fight == "normal":
            print()


def heal():
    print()


def vinegrow():
    print()


def freeze():
    print()


def crossroads():
    paths = randint(2, 3)
    print("there are", paths, "paths")
    if paths == 2:
        paths = randint(1, 3)
        if paths == 1:
            print("right or left or you can check your 'inventory'")
            choice = input()
            if choice == "right":
                path()
            elif choice == "left":
                path()
            elif choice == "inventory":
                inventory1()
        if paths == 2:
            print("right or straight or you can check your 'inventory'")
            choice = input()
            if choice == "right":
                path()
            elif choice == "straight":
                path()
            elif choice == "inventory":
                inventory1()
        if paths == 3:
            print("left or straight or you can check your 'inventory'")
            choice = input()
            if choice == "left":
                path()
            elif choice == "straight":
                path()
            elif choice == "inventory":
                inventory1()
    if paths == 3:
        print("right, left, or straight or you can check your 'inventory'")
        choice = input()
        if choice == "right":
            path()
        elif choice == "left":
            path()
        elif choice == "straight":
            path()
        elif choice == "inventory":
            inventory1()


def path():
    x = randint(1, 7)
    x = 6
    if x == 1 or x == 2 or x == 3:
        fighting()
    elif x == 4 or x == 5:
        treasure()
    elif x == 6 or x == 7:
        tradingpost()


def village():
    print("okay, its your choice kid")
    print("You want to go to the 'shops'")
    print("You wanna 'sleep' and regain all your health")
    print("or do you want to 'explore', (after every fight you will come back here) ")
    x = input()
    if x == "shops":
        shops()


def shops():
    global gold
    global inventory
    sell = 0
    e = ["Healing Elixir", "Strength Elixir", "Mana Elixir"]
    w = ["Long Sword", "Short Sword", "Staff", "Spell Books"]
    a = ["Chest Piece", "Pants", "Gloves", "Helm", "Robe", "Boots"]
    shopping = 0
    while shopping == 0:
        print("This trader sells and buys all items as well as upgrades equipment "
              "\n'buy', 'sell', 'upgrade', or 'continue'")
        trading = input()
        if trading == "buy":
            print("This trader has", e,w,a, "for sale")
            w3 = random.choice("Spell Book: Fire Ball", "Spell Book: Heal", "Spell Book: Vine Grow",
                               "Spell Book: Freeze")
            p1 = 15
            p2 = 15
            p3 = 15
            p4 = randint(1, 10)
            p5 = randint(1, 10)
            p6 = randint(1, 10)
            p7 = 50
            p8 = randint(10, 30)
            p9 = randint(10, 30)
            p10 = randint(10, 30)
            p11 = randint(10, 30)
            p12 = randint(10, 30)
            p13 = randint(10, 30)
            print("the trader has", e[0], "for", p1, "gold")
            print("the trader has", e[1], "for", p2, "gold")
            print("the trader has", e[2], "for", p3, "gold")
            print("the trader has", w[0], "for", p4, "gold")
            print("the trader has", w[1], "for", p5, "gold")
            print("the trader has", w[2], "for", p6, "gold")
            print("the trader has", w3, "for", p7, "gold (for this input 'w3')")
            print("the trader has", a[0], "for", p8, "gold")
            print("the trader has", a[1], "for", p9, "gold")
            print("the trader has", a[2], "for", p10, "gold")
            print("the trader has", a[3], "for", p11, "gold")
            print("the trader has", a[4], "for", p12, "gold")
            print("the trader has", a[5], "for", p13, "gold")
            print("What can I get you? You have ", gold, " gold")
            x = input()
            if x.lower() == "healing elixir":
                if gold < p1:
                    print("You don't have enough gold for this purchase")
                if gold >= p1:
                    print("Thank you for you purchase")
                    gold = gold - p1
                    inventory.append("Healing Elixir")
            if x.lower() == "strength elixir":
                if gold < p2:
                    print("You don't have enough gold for this purchase")
                if gold >= p2:
                    print("Thank you for you purchase")
                    gold = gold - p2
                    inventory.append("Strength Elixir")
            if x.lower() == "mana elixir":
                if gold < p3:
                    print("You don't have enough gold for this purchase")
                if gold >= p3:
                    print("Thank you for you purchase")
                    gold = gold - p3
                    inventory.append("Mana Elixir")
            if x.lower() == "long sword":
                if gold < p4:
                    print("You don't have enough gold for this purchase")
                if gold >= p4:
                    print("Thank you for you purchase")
                    gold = gold - p4
                    inventory.append("Long Sword")
            if x.lower() == "short sword":
                if gold < p5:
                    print("You don't have enough gold for this purchase")
                if gold >= p5:
                    print("Thank you for you purchase")
                    gold = gold - p5
                    inventory.append("Short Sword")
            if x.lower() == "staff":
                if gold < p6:
                    print("You don't have enough gold for this purchase")
                if gold >= p6:
                    print("Thank you for you purchase")
                    gold = gold - p6
                    inventory.append("Staff")
            if x == w3:
                if sell == 0:
                    if gold < p7:
                        print("You don't have enough gold for this purchase")
                    if gold >= p7:
                        print("Thank you for you purchase")
                        gold = gold - p7
                        inventory.append(w3)
                        sell = 1
                if sell == 1:
                    print("Sorry all out, that's whats coming tomorrow")
            if x.lower() == "Chest Piece":
                if gold < p8:
                    print("You don't have enough gold for this purchase")
                if gold >= p8:
                    print("Thank you for you purchase")
                    gold = gold - p8
                    inventory.append("Chest Piece")
            if x.lower() == "Pants":
                if gold < p9:
                    print("You don't have enough gold for this purchase")
                if gold >= p9:
                    print("Thank you for you purchase")
                    gold = gold - p9
                    inventory.append("Pants")
            if x.lower() == "Gloves":
                if gold < p10:
                    print("You don't have enough gold for this purchase")
                if gold >= p10:
                    print("Thank you for you purchase")
                    gold = gold - p10
                    inventory.append("Gloves")
            if x.lower() == "Helm":
                if gold < p11:
                    print("You don't have enough gold for this purchase")
                if gold >= p11:
                    print("Thank you for you purchase")
                    gold = gold - p11
                    inventory.append("Helm")
            if x.lower() == "Robe":
                if gold < p12:
                    print("You don't have enough gold for this purchase")
                if gold >= p12:
                    print("Thank you for you purchase")
                    gold = gold - p12
                    inventory.append("Robe")
            if x.lower() == "Boots":
                if gold < p13:
                    print("You don't have enough gold for this purchase")
                if gold >= p13:
                    print("Thank you for you purchase")
                    gold = gold - p13
                    inventory.append("Boots")
        elif trading == "sell":
            print(inventory)
            p1 = 10
            p2 = 10
            p3 = 10
            p4 = randint(1, 10)
            p5 = randint(1, 10)
            p6 = randint(1, 10)
            p7 = 50
            p8 = randint(10, 20)
            p9 = randint(10, 20)
            p10 = randint(10, 20)
            p11 = randint(10, 20)
            p12 = randint(10, 20)
            p13 = randint(10, 20)
            print("the trader will buy", e[0], "for", p1, "gold")
            print("the trader will buy", e[1], "for", p2, "gold")
            print("the trader will buy", e[2], "for", p3, "gold")
            print("the trader will buy", w[0], "for", p4, "gold")
            print("the trader will buy", w[1], "for", p5, "gold")
            print("the trader will buy", w[2], "for", p6, "gold")
            print("the trader has", w[3], "for", p7, "gold")
            print("the trader has", a[0], "for", p8, "gold")
            print("the trader has", a[1], "for", p9, "gold")
            print("the trader has", a[2], "for", p10, "gold")
            print("the trader has", a[3], "for", p11, "gold")
            print("the trader has", a[4], "for", p12, "gold")
            print("the trader has", a[5], "for", p13, "gold")
            print("What can I take off your hands?")
            x = input()
            if x.lower() == "healing elixir":
                if "Healing Elixir" not in inventory:
                    print("You don't have any Healing Elixirs for this sale")
                if "Healing Elixir" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p1
                    inventory.remove("Healing Elixir")
            if x.lower() == "strength elixir":
                if "Strength Elixir" not in inventory:
                    print("You don't have any Strength Elixir for this sale")
                if "Strength Elixir" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p2
                    inventory.remove("Strength Elixir")
            if x.lower() == "mana elixir":
                if "Mana Elixir" not in inventory:
                    print("You don't have any Mana Elixir for this sale")
                if "Mana Elixir" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p3
                    inventory.remove("Mana Elixir")
            if x.lower() == "long sword":
                if "Long Sword" not in inventory:
                    print("You don't have any Long Swords for this sale")
                if "Long Sword" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p4
                    inventory.remove("Long Sword")
            if x.lower() == "short sword":
                if "Short Sword" not in inventory:
                    print("You don't have any Short Swords for this sale")
                if "Short Sword" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p5
                    inventory.remove("Short Sword")
            if x.lower() == "staff":
                if "Staff" not in inventory:
                    print("You don't have any Staff for this sale")
                if "Staff" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p6
                    inventory.remove("Staff")
            if x.lower() == "spell books":
                print("What book do you have? (Just type the spell)")
                s = input()
                if s.lower() == "fire ball":
                    if "Spell Book: Fire Ball" not in inventory:
                        print("You don't have the Spell Book: Fire Ball for this sale")
                    if "Spell Book: Fire Ball" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p7
                        inventory.remove("Spell Book: Fire Ball")
                if s.lower() == "heal":
                    if "Spell Book: Heal" not in inventory:
                        print("You don't have the Spell Book: Heal for this sale")
                    if "Spell Book: Heal" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p7
                        inventory.remove("Spell Book: Heal")
                if s.lower() == "vine grow":
                    if "Spell Book: Vine Grow" not in inventory:
                        print("You don't have the Spell Book: Vine Grow for this sale")
                    if "Spell Book: Vine Grow" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p7
                        inventory.remove("Spell Book: Vine Grow")
                if s.lower() == "freeze":
                    if "Spell Book: Freeze" not in inventory:
                        print("You don't have the Spell Book: Freeze for this sale")
                    if "Spell Book: Freeze" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p7
                        inventory.remove("Spell Book: Freeze")
            if x.lower() == "chest piece":
                if "Chest Piece" not in inventory:
                    print("You don't have any Chest Piece for this sale")
                if "Chest Piece" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p8
                    inventory.remove("Chest Piece")
            if x.lower() == "pants":
                if "Pants" not in inventory:
                    print("You don't have any Pants for this sale")
                if "Pants" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p9
                    inventory.remove("Pants")
            if x.lower() == "gloves":
                if "Gloves" not in inventory:
                    print("You don't have any Gloves for this sale")
                if "Gloves" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p10
                    inventory.remove("Gloves")
            if x.lower() == "helm":
                if "Helm" not in inventory:
                    print("You don't have any Helms for this sale")
                if "Helm" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p11
                    inventory.remove("Helm")
            if x.lower() == "robe":
                if "Robe" not in inventory:
                    print("You don't have any Robes for this sale")
                if "Robe" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p12
                    inventory.remove("Robe")
            if x.lower() == "boots":
                if "Boots" not in inventory:
                    print("You don't have any Boots for this sale")
                if "Boots" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p13
                    inventory.remove("Boots")
        elif trading == "upgrade":
            print()
        elif trading == 'continue':
            shopping = 1
            village()


def tradingpost():
    global gold
    global inventory
    global tpv
    trader = ["Elixir", "Weapon", "Armor"]
    e = ["Healing Elixir", "Strength Elixir", "Mana Elixir"]
    w = ["Long Sword", "Short Sword", "Staff", "Spell Books"]
    a = ["Chest Piece", "Pants", "Gloves", "Helm", "Robe", "Boots"]
    sell = 0
    t = random.choice(trader)
    t = trader[1]
    print("you come up to a", t, "traders post, would you like to")
    while t == trader[0]:
        print("'buy', 'sell', or 'continue'")
        if tpv == 0:
            print("(fyi elixirs is all that works for now)")
            tpv = 1
        trading = input()
        if trading == "buy":
            print("This trader has", e, "for sale")
            p1 = 15
            p2 = 15
            p3 = 15
            print("the trader has", e[0], "for", p1, "gold")
            print("the trader has", e[1], "for", p2, "gold")
            print("the trader has", e[2], "for", p3, "gold")
            print("What would you like? You have ", gold," gold")
            x = input()
            if x.lower() == "healing elixir":
                if gold < p1:
                    print("You don't have enough gold for this purchase")
                if gold >= p1:
                    print("Thank you for you purchase")
                    gold = gold - p1
                    inventory.append("Healing Elixir")
            if x.lower() == "strength elixir":
                if gold < p2:
                    print("You don't have enough gold for this purchase")
                if gold >= p2:
                    print("Thank you for you purchase")
                    gold = gold - p2
                    inventory.append("Strength Elixir")
            if x.lower() == "mana elixir":
                if gold < p3:
                    print("You don't have enough gold for this purchase")
                if gold >= p3:
                    print("Thank you for you purchase")
                    gold = gold - p3
                    inventory.append("Mana Elixir")
        elif trading == "sell":
            print(inventory)
            p1 = 10
            p2 = 10
            p3 = 10
            p4 = randint(1, 10)
            p5 = randint(1, 10)
            p6 = randint(1, 10)
            p7 = 50
            p8 = randint(10, 20)
            p9 = randint(10, 20)
            p10 = randint(10, 20)
            p11 = randint(10, 20)
            p12 = randint(10, 20)
            p13 = randint(10, 20)
            print("the trader will buy", e[0], "for", p1, "gold")
            print("the trader will buy", e[1], "for", p2, "gold")
            print("the trader will buy", e[2], "for", p3, "gold")
            print("the trader will buy", w[0], "for", p4, "gold")
            print("the trader will buy", w[1], "for", p5, "gold")
            print("the trader will buy", w[2], "for", p6, "gold")
            print("the trader has", w[3], "for", p7, "gold")
            print("the trader has", a[0], "for", p8, "gold")
            print("the trader has", a[1], "for", p9, "gold")
            print("the trader has", a[2], "for", p10, "gold")
            print("the trader has", a[3], "for", p11, "gold")
            print("the trader has", a[4], "for", p12, "gold")
            print("the trader has", a[5], "for", p13, "gold")
            print("What can I take off your hands?")
            x = input()
            if x.lower() == "healing elixir":
                if "Healing Elixir" not in inventory:
                    print("You don't have any Healing Elixirs for this sale")
                if "Healing Elixir" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p1
                    inventory.remove("Healing Elixir")
            if x.lower() == "strength elixir":
                if "Strength Elixir" not in inventory:
                    print("You don't have any Strength Elixir for this sale")
                if "Strength Elixir" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p2
                    inventory.remove("Strength Elixir")
            if x.lower() == "mana elixir":
                if "Mana Elixir" not in inventory:
                    print("You don't have any Mana Elixir for this sale")
                if "Mana Elixir" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p3
                    inventory.remove("Mana Elixir")
            if x.lower() == "long sword":
                if "Long Sword" not in inventory:
                    print("You don't have any Long Swords for this sale")
                if "Long Sword" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p4
                    inventory.remove("Long Sword")
            if x.lower() == "short sword":
                if "Short Sword" not in inventory:
                    print("You don't have any Short Swords for this sale")
                if "Short Sword" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p5
                    inventory.remove("Short Sword")
            if x.lower() == "staff":
                if "Staff" not in inventory:
                    print("You don't have any Staff for this sale")
                if "Staff" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p6
                    inventory.remove("Staff")
            if x.lower() == "spell books":
                print("What book do you have? (Just type the spell)")
                s = input()
                if s.lower() == "fire ball":
                    if "Spell Book: Fire Ball" not in inventory:
                        print("You don't have the Spell Book: Fire Ball for this sale")
                    if "Spell Book: Fire Ball" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p7
                        inventory.remove("Spell Book: Fire Ball")
                if s.lower() == "heal":
                    if "Spell Book: Heal" not in inventory:
                        print("You don't have the Spell Book: Heal for this sale")
                    if "Spell Book: Heal" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p7
                        inventory.remove("Spell Book: Heal")
                if s.lower() == "vine grow":
                    if "Spell Book: Vine Grow" not in inventory:
                        print("You don't have the Spell Book: Vine Grow for this sale")
                    if "Spell Book: Vine Grow" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p7
                        inventory.remove("Spell Book: Vine Grow")
                if s.lower() == "freeze":
                    if "Spell Book: Freeze" not in inventory:
                        print("You don't have the Spell Book: Freeze for this sale")
                    if "Spell Book: Freeze" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p7
                        inventory.remove("Spell Book: Freeze")
            if x.lower() == "chest piece":
                if "Chest Piece" not in inventory:
                    print("You don't have any Chest Piece for this sale")
                if "Chest Piece" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p8
                    inventory.remove("Chest Piece")
            if x.lower() == "pants":
                if "Pants" not in inventory:
                    print("You don't have any Pants for this sale")
                if "Pants" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p9
                    inventory.remove("Pants")
            if x.lower() == "gloves":
                if "Gloves" not in inventory:
                    print("You don't have any Gloves for this sale")
                if "Gloves" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p10
                    inventory.remove("Gloves")
            if x.lower() == "helm":
                if "Helm" not in inventory:
                    print("You don't have any Helms for this sale")
                if "Helm" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p11
                    inventory.remove("Helm")
            if x.lower() == "robe":
                if "Robe" not in inventory:
                    print("You don't have any Robes for this sale")
                if "Robe" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p12
                    inventory.remove("Robe")
            if x.lower() == "boots":
                if "Boots" not in inventory:
                    print("You don't have any Boots for this sale")
                if "Boots" in inventory:
                    print("Thank you for your sale")
                    gold = gold + p13
                    inventory.remove("Boots")
        elif trading == 'continue':
            t = "none"
            crossroads()
    while t == trader[1] or t == trader[2]:
        print("'buy', 'sell', 'upgrade', or 'continue'")
        trading = input()
        if t == trader[1]:
            if trading == "buy":
                print("This trader has", w, "for sale")
                p1 = randint(1, 10)
                p2 = randint(1, 10)
                p3 = randint(1, 10)
                p4 = 50
                w3 = random.choice("Spell Book: Fire Ball", "Spell Book: Heal", "Spell Book: Vine Grow", "Spell Book: Freeze")
                print("the trader has", w[0], "for", p1, "gold")
                print("the trader has", w[1], "for", p2, "gold")
                print("the trader has", w[2], "for", p3, "gold")
                print("the trader has", w3, "for", p4, "gold (for this input 'w3')")
                print("What would you like? You have ", gold, " gold")
                x = input()
                if x.lower() == "long sword":
                    if gold < p1:
                        print("You don't have enough gold for this purchase")
                    if gold >= p1:
                        print("Thank you for you purchase")
                        gold = gold - p1
                        inventory.append("Long Sword")
                if x.lower() == "short sword":
                    if gold < p2:
                        print("You don't have enough gold for this purchase")
                    if gold >= p2:
                        print("Thank you for you purchase")
                        gold = gold - p2
                        inventory.append("Short Sword")
                if x.lower() == "staff":
                    if gold < p3:
                        print("You don't have enough gold for this purchase")
                    if gold >= p3:
                        print("Thank you for you purchase")
                        gold = gold - p3
                        inventory.append("Staff")
                if x == w3:
                    if sell == 0:
                        if gold < p4:
                            print("You don't have enough gold for this purchase")
                        if gold >= p4:
                            print("Thank you for you purchase")
                            gold = gold - p4
                            inventory.append(w3)
                            sell = 1
                    if sell == 1:
                        print("Sorry all out, that's whats coming tomorrow")
            elif trading == "sell":
                print(inventory)
                p1 = 10
                p2 = 10
                p3 = 10
                p4 = randint(1, 10)
                p5 = randint(1, 10)
                p6 = randint(1, 10)
                p7 = 50
                p8 = randint(10, 30)
                p9 = randint(10, 30)
                p10 = randint(10, 30)
                p11 = randint(10, 30)
                p12 = randint(10, 30)
                p13 = randint(10, 30)
                print("the trader will buy", e[0], "for", p1, "gold")
                print("the trader will buy", e[1], "for", p2, "gold")
                print("the trader will buy", e[2], "for", p3, "gold")
                print("the trader will buy", w[0], "for", p4, "gold")
                print("the trader will buy", w[1], "for", p5, "gold")
                print("the trader will buy", w[2], "for", p6, "gold")
                print("the trader has", w[3], "for", p7, "gold")
                print("the trader has", a[0], "for", p8, "gold")
                print("the trader has", a[1], "for", p9, "gold")
                print("the trader has", a[2], "for", p10, "gold")
                print("the trader has", a[3], "for", p11, "gold")
                print("the trader has", a[4], "for", p12, "gold")
                print("the trader has", a[5], "for", p13, "gold")
                print("What can I take off your hands?")
                x = input()
                if x.lower() == "healing elixir":
                    if "Healing Elixir" not in inventory:
                        print("You don't have any Healing Elixirs for this sale")
                    if "Healing Elixir" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p1
                        inventory.remove("Healing Elixir")
                if x.lower() == "strength elixir":
                    if "Strength Elixir" not in inventory:
                        print("You don't have any Strength Elixir for this sale")
                    if "Strength Elixir" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p2
                        inventory.remove("Strength Elixir")
                if x.lower() == "mana elixir":
                    if "Mana Elixir" not in inventory:
                        print("You don't have any Mana Elixir for this sale")
                    if "Mana Elixir" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p3
                        inventory.remove("Mana Elixir")
                if x.lower() == "long sword":
                    if "Long Sword" not in inventory:
                        print("You don't have any Long Swords for this sale")
                    if "Long Sword" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p4
                        inventory.remove("Long Sword")
                if x.lower() == "short sword":
                    if "Short Sword" not in inventory:
                        print("You don't have any Short Swords for this sale")
                    if "Short Sword" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p5
                        inventory.remove("Short Sword")
                if x.lower() == "staff":
                    if "Staff" not in inventory:
                        print("You don't have any Staff for this sale")
                    if "Staff" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p6
                        inventory.remove("Staff")
                if x.lower() == "spell books":
                    print("What book do you have? (Just type the spell)")
                    s = input()
                    if s.lower() == "fire ball":
                        if "Spell Book: Fire Ball" not in inventory:
                            print("You don't have the Spell Book: Fire Ball for this sale")
                        if "Spell Book: Fire Ball" in inventory:
                            print("Thank you for your sale")
                            gold = gold + p7
                            inventory.remove("Spell Book: Fire Ball")
                    if s.lower() == "heal":
                        if "Spell Book: Heal" not in inventory:
                            print("You don't have the Spell Book: Heal for this sale")
                        if "Spell Book: Heal" in inventory:
                            print("Thank you for your sale")
                            gold = gold + p7
                            inventory.remove("Spell Book: Heal")
                    if s.lower() == "vine grow":
                        if "Spell Book: Vine Grow" not in inventory:
                            print("You don't have the Spell Book: Vine Grow for this sale")
                        if "Spell Book: Vine Grow" in inventory:
                            print("Thank you for your sale")
                            gold = gold + p7
                            inventory.remove("Spell Book: Vine Grow")
                    if s.lower() == "freeze":
                        if "Spell Book: Freeze" not in inventory:
                            print("You don't have the Spell Book: Freeze for this sale")
                        if "Spell Book: Freeze" in inventory:
                            print("Thank you for your sale")
                            gold = gold + p7
                            inventory.remove("Spell Book: Freeze")
                if x.lower() == "chest piece":
                    if "Chest Piece" not in inventory:
                        print("You don't have any Chest Piece for this sale")
                    if "Chest Piece" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p8
                        inventory.remove("Chest Piece")
                if x.lower() == "pants":
                    if "Pants" not in inventory:
                        print("You don't have any Pants for this sale")
                    if "Pants" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p9
                        inventory.remove("Pants")
                if x.lower() == "gloves":
                    if "Gloves" not in inventory:
                        print("You don't have any Gloves for this sale")
                    if "Gloves" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p10
                        inventory.remove("Gloves")
                if x.lower() == "helm":
                    if "Helm" not in inventory:
                        print("You don't have any Helms for this sale")
                    if "Helm" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p11
                        inventory.remove("Helm")
                if x.lower() == "robe":
                    if "Robe" not in inventory:
                        print("You don't have any Robes for this sale")
                    if "Robe" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p12
                        inventory.remove("Robe")
                if x.lower() == "boots":
                    if "Boots" not in inventory:
                        print("You don't have any Boots for this sale")
                    if "Boots" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p13
                        inventory.remove("Boots")
            elif trading == "upgrade":
                print("To upgrade you need both gold and a weapon the same type as the weapon you want to upgrade")
                print("what would you like to upgrade I know how to upgrade Long Swords, Short Swords, and Staffs")
                print("but know once you upgrade a weapon it will forever be in your inventory")
            elif trading == "continue":
                t = "none"
                crossroads()
        if t == trader[2]:
            if trading == "buy":
                print("This trader has", a, "for sale")
                p1 = randint(10, 30)
                p2 = randint(10, 30)
                p3 = randint(10, 30)
                p4 = randint(10, 30)
                p5 = randint(10, 30)
                p6 = randint(10, 30)
                print("the trader has", a[0], "for", p1, "gold")
                print("the trader has", a[1], "for", p2, "gold")
                print("the trader has", a[2], "for", p3, "gold")
                print("the trader has", a[3], "for", p4, "gold")
                print("the trader has", a[4], "for", p5, "gold")
                print("the trader has", a[5], "for", p6, "gold")
                if x.lower() == "chest piece":
                    if gold < p1:
                        print("You don't have enough gold for this purchase")
                    if gold >= p1:
                        print("Thank you for you purchase")
                        gold = gold - p1
                        inventory.append("Chest Piece")
                if x.lower() == "pants":
                    if gold < p2:
                        print("You don't have enough gold for this purchase")
                    if gold >= p2:
                        print("Thank you for you purchase")
                        gold = gold - p2
                        inventory.append("Pants")
                if x.lower() == "gloves":
                    if gold < p3:
                        print("You don't have enough gold for this purchase")
                    if gold >= p3:
                        print("Thank you for you purchase")
                        gold = gold - p3
                        inventory.append("Gloves")
                if x.lower() == "helm":
                    if gold < p4:
                        print("You don't have enough gold for this purchase")
                    if gold >= p4:
                        print("Thank you for you purchase")
                        gold = gold - p4
                        inventory.append("Helm")
                if x.lower() == "robe":
                    if gold < p5:
                        print("You don't have enough gold for this purchase")
                    if gold >= p5:
                        print("Thank you for you purchase")
                        gold = gold - p5
                        inventory.append("Robe")
                if x.lower() == "boots":
                    if gold < p6:
                        print("You don't have enough gold for this purchase")
                    if gold >= p6:
                        print("Thank you for you purchase")
                        gold = gold - p6
                        inventory.append("Boots")
            elif trading == "sell":
                print(inventory)
                p1 = 10
                p2 = 10
                p3 = 10
                p4 = randint(1, 10)
                p5 = randint(1, 10)
                p6 = randint(1, 10)
                p7 = 50
                p8 = randint(10, 30)
                p9 = randint(10, 30)
                p10 = randint(10, 30)
                p11 = randint(10, 30)
                p12 = randint(10, 30)
                p13 = randint(10, 30)
                print("the trader will buy", e[0], "for", p1, "gold")
                print("the trader will buy", e[1], "for", p2, "gold")
                print("the trader will buy", e[2], "for", p3, "gold")
                print("the trader will buy", w[0], "for", p4, "gold")
                print("the trader will buy", w[1], "for", p5, "gold")
                print("the trader will buy", w[2], "for", p6, "gold")
                print("the trader has", w[3], "for", p7, "gold")
                print("the trader has", a[0], "for", p8, "gold")
                print("the trader has", a[1], "for", p9, "gold")
                print("the trader has", a[2], "for", p10, "gold")
                print("the trader has", a[3], "for", p11, "gold")
                print("the trader has", a[4], "for", p12, "gold")
                print("the trader has", a[5], "for", p13, "gold")
                print("What can I take off your hands?")
                x = input()
                if x.lower() == "healing elixir":
                    if "Healing Elixir" not in inventory:
                        print("You don't have any Healing Elixirs for this sale")
                    if "Healing Elixir" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p1
                        inventory.remove("Healing Elixir")
                if x.lower() == "strength elixir":
                    if "Strength Elixir" not in inventory:
                        print("You don't have any Strength Elixir for this sale")
                    if "Strength Elixir" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p2
                        inventory.remove("Strength Elixir")
                if x.lower() == "mana elixir":
                    if "Mana Elixir" not in inventory:
                        print("You don't have any Mana Elixir for this sale")
                    if "Mana Elixir" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p3
                        inventory.remove("Mana Elixir")
                if x.lower() == "long sword":
                    if "Long Sword" not in inventory:
                        print("You don't have any Long Swords for this sale")
                    if "Long Sword" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p4
                        inventory.remove("Long Sword")
                if x.lower() == "short sword":
                    if "Short Sword" not in inventory:
                        print("You don't have any Short Swords for this sale")
                    if "Short Sword" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p5
                        inventory.remove("Short Sword")
                if x.lower() == "staff":
                    if "Staff" not in inventory:
                        print("You don't have any Staff for this sale")
                    if "Staff" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p6
                        inventory.remove("Staff")
                if x.lower() == "spell books":
                    print("What book do you have? (Just type the spell)")
                    s = input()
                    if s.lower() == "fire ball":
                        if "Spell Book: Fire Ball" not in inventory:
                            print("You don't have the Spell Book: Fire Ball for this sale")
                        if "Spell Book: Fire Ball" in inventory:
                            print("Thank you for your sale")
                            gold = gold + p7
                            inventory.remove("Spell Book: Fire Ball")
                    if s.lower() == "heal":
                        if "Spell Book: Heal" not in inventory:
                            print("You don't have the Spell Book: Heal for this sale")
                        if "Spell Book: Heal" in inventory:
                            print("Thank you for your sale")
                            gold = gold + p7
                            inventory.remove("Spell Book: Heal")
                    if s.lower() == "vine grow":
                        if "Spell Book: Vine Grow" not in inventory:
                            print("You don't have the Spell Book: Vine Grow for this sale")
                        if "Spell Book: Vine Grow" in inventory:
                            print("Thank you for your sale")
                            gold = gold + p7
                            inventory.remove("Spell Book: Vine Grow")
                    if s.lower() == "freeze":
                        if "Spell Book: Freeze" not in inventory:
                            print("You don't have the Spell Book: Freeze for this sale")
                        if "Spell Book: Freeze" in inventory:
                            print("Thank you for your sale")
                            gold = gold + p7
                            inventory.remove("Spell Book: Freeze")
                if x.lower() == "chest piece":
                    if "Chest Piece" not in inventory:
                        print("You don't have any Chest Piece for this sale")
                    if "Chest Piece" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p8
                        inventory.remove("Chest Piece")
                if x.lower() == "pants":
                    if "Pants" not in inventory:
                        print("You don't have any Pants for this sale")
                    if "Pants" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p9
                        inventory.remove("Pants")
                if x.lower() == "gloves":
                    if "Gloves" not in inventory:
                        print("You don't have any Gloves for this sale")
                    if "Gloves" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p10
                        inventory.remove("Gloves")
                if x.lower() == "helm":
                    if "Helm" not in inventory:
                        print("You don't have any Helms for this sale")
                    if "Helm" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p11
                        inventory.remove("Helm")
                if x.lower() == "robe":
                    if "Robe" not in inventory:
                        print("You don't have any Robes for this sale")
                    if "Robe" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p12
                        inventory.remove("Robe")
                if x.lower() == "boots":
                    if "Boots" not in inventory:
                        print("You don't have any Boots for this sale")
                    if "Boots" in inventory:
                        print("Thank you for your sale")
                        gold = gold + p13
                        inventory.remove("Boots")
            elif trading == "upgrade":
                print()
            elif trading == "continue":
                t = "none"
                crossroads()


def music():
    threading.Timer(190.2, music).start()
    winsound.PlaySound('C:/Users/ck02340/Desktop/audio/Glory.wav', winsound.SND_ASYNC)


class StartGame:
    music()
    print("Hello young adventure, Would you like to brave on a treacherous adventure")
    print("(that is most likely going to kill you because no one has gotten out of this dungeon)")
    print("(many people even live down there because they can't find the exit)")
    print("Oh did I say that out loud,(dam computers putting my thoughts into words,stop it,STOP IT I SAY!!)")
    print("Any how... would you like to be the next victi... I mean the next adventurer to brave this dungeon")
    choice = input()
    print("Great good luck, oh wait you gotta pick your class first")
    player()
    crossroads()

