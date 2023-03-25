# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Joe Joe")
define s = Character("Sigma", callback = name_callback, cb_name = "Sigma") # 
define s2 = Character("Sigma", image="sigma")
define temp = Character("Secretary")
define mc = Character("[name]") # , callback = name_callback, cb_name = "[name]"
define g = Character("Goopitha")
define l = Character("Lone Loan Dolphin")
define p = Character("Pelota")

default smallpizza = True # used for choosing small or large pizzas when getting pizza with joejoe

image side sigma = "sigmaside.png"

image sigma = At('sigma.png', sprite_highlight("sigma.png"))

transform jumper: #adjust the yoffset as necessary to your preference
    ease .06 yoffset 24 
    ease .06 yoffset -24 
    ease .05 yoffset 20 
    ease .05 yoffset -20 
    ease .04 yoffset 16 
    ease .04 yoffset -16 
    ease .03 yoffset 12 
    ease .03 yoffset -12 
    ease .02 yoffset 8 
    ease .02 yoffset -8 
    ease .01 yoffset 4 
    ease .01 yoffset -4 
    ease .01 yoffset 0
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music fadeout 1.0

    python:
        name = renpy.input("What is your name?", length=32)
        name = name.strip()
        if not name:
            name = "Toni"
        if name == "Andrew Zhou":
            renpy.call_in_new_context("easter1") 
        else:
            renpy.call_in_new_context("intro1")
label easter1:
    "omg!!! its andrew zhou (real)!"
    jump intro1 


label day1:  
    scene black
    with fade  

    "You stand outside of the office, preparing yourself for your new job."

    scene bg outside
    with dissolve

    mc "(So I’ll be working here from now on, huh. Aren’t I supposed to be fighting the diseases?)"
    mc "(No use backing out now; not like I really have a choice anyways.)"

    scene bg office 
    with fade 

    show sigma 

    mc "(A pretty alien woman as a secretary, huh. The secretary is the face of a company, after all.)" 
    # color graphic here, showing sigma being hot at the front desk (must be hot)

    mc 'Is this the Diseases Eradication Unit office? I got hired as a Charitable Urgency Manager recently.'

    "The secretary glances up from her computer and locks eyes with me."

    mc "(Her eye bags are incredibly dark, almost as if she hasn’t slept for the past week. She reminds me of… someone.)"

    mc "(Man, she’s even prettier up close. Definitely a 10-, no, maybe even an 11.)"

    temp "I haven’t gotten tired of your voice yet, so you must be a rookie."

    "She closes her eyes for a few seconds before opening them with fake excitement."

    s "My name is Sigma, but I don’t care what you call me if it isn’t important."

    s "Welcome to the office. The higher ups force me to give a tour to every newcomer, so hurry up and look around the place so I can get back to my work."

    with fade 

    "You approach the office desks with Sigma."

    s "Here’s the H(uman but alien as well I guess)R Department, where all the complaints about your pay go to."

    with fade 

    s "Here’s the Accounting and Finance Department. They commit tax fraud--I mean, they have the very important task of ensuring all our funds and expenses are properly accounted for."

    with fade 

    s "Over here’s the PR Department. They write propaganda so we can pretend we’re not a soul--crushing corporation that may or may not be responsible for multiple human rights abuses."

    with fade 

    "Sigma speeds past the departments, clearly bothered by the tour."

    "By the end of the tour, you've reached the water cooler, where you spot an insanely average looking man." 
    # insert color graphic here on Joe Joe, but focusing on the water cooler, with Joe Joe in the background and out of focus

    scene bg cooler
    
    with fade 

    hide sigma

    show joejoe emotionaldamage

    j "Oh, hey there, guys! Welcome to my spot!"

    s2 "Meet Joe Joe. That’s not his spot. He doesn’t work here."

    menu:
        "Hi, Joe Joe. I think your spot is great.":
            j "Thanks :]"

        "Pretty {i}cool{/i} water cooler you got there.":
            j "Thanks :]"
        "Uh. Okay.":
            j "*Waves*"
    
    hide joejoe emotionaldamage

    show sigma 

    s "Feel free to spend some time exploring our break... corner."

    s "I have customers to satisfy, KPIs to report, people to fire, souls to crush, tax fraud to commit..."

    s "...Y'know, normal secretary stuff. See ya."

    with move 
    
    show sigma at left 

    with move 
    
    hide sigma 

    s "{size=-10}Ugh, so much work. I don't get paid enough for all this.{/size}"

    show joejoe happy

    j "... :)"

    menu:
        "...":
            j "..."
        "... Is that coffee?":
            j "Yeah! This is my cup of Joe!"
    
    mc "So like... who are you, anyway?"

    j "You already forgot, huh..."

    j "But I'm Joe Joe! Like Secretary Sigma said, I don't even work here."

    mc "Uh huh. So, what do you do then?"

    j "I'm your water cooler buddy, [name]. Come around if you ever need a break."

    mc "Okay." # in the future, change this to a menu w/ option for the joe joe hate path

    jump fulfillment
    

