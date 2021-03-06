import sys
import random
import pyperclip

try:

    settings = {}
    settings['QUIT'] = 'q'
    settings['MANUAL'] = 'm'
    settings['SAVE'] = 's'


    saved_names = []

    adjectives = [
        "cool", "fast", "speedy", "efficient",
        "hot", "extreme", "snappy", "wild",
        "Focus", "Sharp", "swift", "street",
        "turbo", "express", "tight", "rapid",
        "curvy", "Real", "Casual", "groovy",
        "Great", "full", "pocket", "pocket size",
        "Flashy", "Flash", "Social", "small",
        "tiny", "Micro", "Machines", "Burning",
        "Global", "street", "epic", "snap",
        "fun", "best", "easy", "too easy",
        "no effort", "big", "small", "Swift",
        "cute", "racing", "fueled", "custom",
        ]

    verbs = [
        "race", "beat", "smack", "compete",
        "win", "loss", "finish", "Challenge",
        "drive", "tap", "steer", "drift",
        "swing", "gas up", "collect", "scan",
        "race", "Customize", "Can't beat", 
        ]


    nouns = [
        "autos", "thumbs", "acceleration", "cars",
        "engines", "tires", "pistons", "springs",
        "curves", "valves", "roads", "trophies",
        "no competition", "mates", "friends", "buddies",
        "drivers", "race", "skidmarks", "Gears",
        "master", "masters", "Throttle", "exhaust",
        "wins", "racers", "victories", "pedals",
        "fingers", "Flash", "Wheels", "rewards",
        "tools", "greens", "world", "suspension",
        ]

    pronouns = [
        "me", "us", "you", "them",
        "competitors", "mates", "friends", "buddies",
        "pals", "buds", "it", "the race"
        "drivers", "them all", "all", "everybody",
        "fam", "players", "time",
        ]

    prepositions = [
        "up", "down", "over", "here",
        "under", "against", "on", "onward",
        "between", "Past", "towards", "Beside",
        "aginst", "until", "with", "beyond",
        "out", "to go", "GO", "Travel",
        ]

    times = [
        "Go", "now", "again", "in ten",
        "first", "at once", "right away", "away",
        "instantly", "minute", "pronto", "on repeat", "30s"
        ]

    pairs = []
    pairs.append([verbs, times])
    pairs.append([verbs, pronouns])
    pairs.append([verbs, prepositions])
    pairs.append([verbs, adjectives])
    pairs.append([verbs, pronouns, times])
    pairs.append([verbs, prepositions, pronouns])
    pairs.append([adjectives, nouns])
    pairs.append([adjectives, verbs])
    pairs.append([adjectives, nouns, times])
    pairs.append([nouns, pronouns])



    def getNewName():
        new_combination = random.choice(pairs)
        name = ""
        for word_list in new_combination:
            name = (name + " " + random.choice(word_list)).upper().lstrip(" ")
        print (name)

        handle_user_interaction(name)

        getNewName()

    def handle_user_interaction(name):
        user_input = input ("").lower()

        if (user_input == settings['QUIT']):
            exit()

        elif (user_input == settings['MANUAL']):
            manual_entry()

        elif ( user_input == settings['SAVE']):
            save_name(name)


    def save_name(name):
        saved_names.append(name)
        pyperclip.copy(name)

    def manual_entry():
        manual_name = input("\nEnter Name Manually and then press Enter:\n")
        save_name(manual_name.upper())
        print("")

    def exit():
        name_file = open("saved_names.txt", 'a')
        for saved_name in saved_names:
            name_file.write(saved_name)
            name_file.write("\n")
        name_file.close()
        print_saved_names()
        sys.exit()

    def print_saved_names():
        if len(saved_names) > 0:
            plural = ""
            these = "this"
            if len(saved_names) > 1:
                plural = "s" 
                these = "these"
            print("You saved %s " % these + str(len(saved_names)) + " name%s:" % plural)
            copy_all = ""
            for saved_name in saved_names:
                print("   - " + saved_name)
                copy_all = copy_all + saved_name + "\n"
            pyperclip.copy(copy_all)
            print ("Now copied to clipboard.")
        

    def main():
        print ("")
        print ("Welcome, this tool assebles names that could be used for a game. Good Luck.")
        print ("- To Generate New Name: Press Enter.")
        print ("- To Save (and copy) Name: Type '%s', Then Press Enter." % settings['SAVE'])
        print ("- To Manually Enter Name: Type '%s', Then Press Enter." % settings['MANUAL'])
        print ("- To Quit: Type '%s', Then Press Enter." % settings['QUIT'])
        print ("")
        getNewName()


    main()

except KeyboardInterrupt:
    exit()




