import random
adjectives = [
    "cool",
    "fast",
    "speedy",
    "efficient",
    "hot",
    "extreme",
    "snappy",
    "wild",
    "swift",
    "street",
    "turbo",
    "express",
    "tight",
    "rapid",
    "curvy",
    "groovy",
    "Great",
    "full",
    "pocket",
    "pocket size",
    "Flashy",
    "Flash",
    "street",
    "epic",
    "snap",
    "fun",
    "best",
]

verbs = [
    "race",
    "beat",
    "smack",
    "compete",
    "win",
    "loss",
    "finish",
    "accelerate",
    "drive",
    "tap",
    "steer",
    "drift",
    "swing",
    "gas up",
    "collect",
    "scan",
    "race aginst",
        ]


nouns = [
    "autos",
    "thumbs", 
    "acceleration",
    "cars",
    "engines",
    "tires",
    "curves",
    "roads",
    "trophies",
    "no competition",
    "mates",
    "friends",
    "buddies",
    "drivers",
    "race",
    "skidmarks",
    "Gears",
    "master",
    "masters",
    "Throttle",
    "exhaust",
    "wins",
    "racers",
    "victories",
    "pedals",
    "fingers",
    "Flash",
    "Wheels",
    ]

pronouns = [
    "me",
    "us",
    "you",
    "them",
    "competitors",
    "mates",
    "friends",
    "buddies",
    "pals",
    "buds",
    "it",
    "the race"
    ]

prepositions = [
        "up",
        "down",
        "over",
        "here",
        "under",
        "on",
        "onward",
        "between",
        "Past",
        "towards",
        "Beside",
        "aginst",
        "until",
        "with",
        "beyond",
        "out",
    ]

times = [
        "Go",
        "now",
        "again",
        "in ten",
        "first",
        "at once",
        "right away",
        "away"
        "instantly",
        "minute",
        "pronto",
        "on repeat",
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
        name = name + " " + random.choice(word_list)
    print (name.upper())
    someinput = input ("")
    getNewName()

def main():

    print ("To Generate New Name: Press Enter.")
    getNewName()

main()




