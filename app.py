from random import choice
import time

jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call cheese that isn’t yours? Nacho cheese.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "How do you organize a space party? You planet.",
    "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    "What do you get if you cross a snowman and a vampire? Frostbite.",
    "Why did the bicycle fall over? It was two-tired.",
    "What do you call a fake noodle? An impasta.",
    "How does a penguin build its house? Igloos it together.",
    "Why was the math book sad? It had too many problems.",
    "What’s orange and sounds like a parrot? A carrot.",
    "Why don’t scientists trust atoms? Because they make up everything.",
    "What do you get when you cross a dog with a phone? A golden receiver.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "What do you call a bear with no teeth? A gummy bear.",
    "How do cows stay up to date with current events? They read the moos-paper.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "What did one wall say to the other wall? I’ll meet you at the corner.",
    "How does a scientist freshen her breath? With experi-mints.",
    "Why don’t oysters donate to charity? Because they are shellfish.",
    "What kind of shoes do ninjas wear? Sneakers.",
    "Why did the coffee file a police report? It got mugged.",
    "What do you call a fish with no eyes? Fsh.",
    "What’s brown and sticky? A stick.",
    "Why did the cookie go to the hospital? Because it felt crummy.",
    "How do you catch a squirrel? Climb a tree and act like a nut.",
    "Why did the math teacher break up with the calculator? She felt like he was too calculating.",
    "What’s a vampire’s favorite fruit? A necktarine.",
    "Why did the banana go to the doctor? Because it wasn’t peeling well.",
    "How do you make holy water? You boil the hell out of it.",
    "What did the grape do when it got stepped on? Nothing but let out a little wine.",
    "Why did the chicken go to the séance? To talk to the other side.",
    "What did the janitor say when he jumped out of the closet? Supplies.",
    "How does a rabbi make his coffee? Hebrews it.",
    "Why did the physics professor break up with the biology professor? There was no chemistry.",
    "What’s green and has wheels? Grass, I lied about the wheels.",
    "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.",
    "Why was the computer cold? It left its Windows open.",
    "Why did the computer go to the doctor? It had a virus.",
    "What do you call an alligator in a vest? An investigator.",
    "What did the baby corn say to the mama corn? Where’s popcorn.",
    "Why did the belt go to jail? For holding up a pair of pants.",
    "How does a farmer count his cows? With a cow-culator.",
    "Why did the golfer bring an extra pair of socks? In case he got a hole in one.",
    "What’s brown and sounds like a bell? Dung.",
    "How does a cat end a fight? By purring it out.",
    "What do you call a bear who’s stuck in the rain? A drizzly bear.",
    "Why can’t you trust stairs? They’re always up to something.",
    "Why did the picture go to jail? Because it was framed.",
    "What do you call a lazy kangaroo? A pouch potato."
]


while True:
    start = input('Do you want to hear a joke? y/n: ').strip().lower()
    if start == "y" or start == "yes":
        print(choice(jokes))
    elif start == "n" or start == "no":
        print('Ok, see you next time.')
        time.sleep(1.5)
        break
    else:
        print('Invalid option. Please enter "y" or "n".')
        

# ENJOY!
