# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Joe Joe")
define s = Character("Sigma")
define temp = Character("Secretary")
define mc = Character("[name]")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    python:
        name = renpy.input("What is your name?", length=32)
        name = name.strip()
        if not name:
            name = "Toni"
    
    scene black
    with fade  

    "You stand outside of the office, preparing yourself for your new job."

    scene bg outside
    with dissolve

    mc "(So I’ll be working here from now on, huh. Aren’t I supposed to be fighting the diseases?)"
    mc "(No use backing out now; not like I really have a choice anyways.)"

    scene bg room 
    with fade 

    show sigma

    mc "(A pretty alien woman as a secretary, huh. The secretary is the face of a company, after all.)"

    mc 'Is this the Diseases Eradication Unit office? I got hired as a Charitable Urgency Manager recently.'

    "The secretary glances up from her computer and locks eyes with me."

    mc "(Her eye bags are incredibly dark, almost as if she hasn’t slept for the past week. She reminds me of… someone.)"

    mc "(Man, she’s even prettier up close. Definitely a 10-, no, maybe even an 11.)"

    temp "I haven’t gotten tired of your voice yet, so you must be a rookie."

    "She closes her eyes for a few seconds before opening them with fake excitement."

    s "My name is Sigma, but I don’t care what you call me if it isn’t important."

    s "Welcome to the office. The higher ups force me to give a tour to every newcomer, so hurry up and look around the place so I can get back to my work."

    with fade 

    "You approach the office desks with Sigma"

    s "Here’s the H(uman but alien as well I guess)R Department, where all the complaints about your pay go to."

    with fade 

    s "Here’s the Accounting and Finance Department. They commit tax fraud--I mean, they have the very important task of ensuring all our funds and expenses are properly accounted for."

    with fade 

    s "Over here’s the PR Department. They write propaganda so we can pretend we’re not a soul--crushing corporation that may or may not be responsible for multiple human rights abuses."

    with fade 

    "Sigma speeds past the departments, clearly bothered by the tour."

    "By the end of the tour, you've reached the water cooler, where you spot an insanely average looking man."

    hide sigma

    show joejoe

    j "Oh, hey there, guys! Welcome to my spot!"

    hide joejoe 
    
    show sigma

    s "Meet Joe Joe. That’s not his spot. He doesn’t work here."









    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.



    # This ends the game.

    return
