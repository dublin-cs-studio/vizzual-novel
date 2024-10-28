﻿# The script of the game goes in this file.

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
define t = Character("TV Head")
define f = Character("Fernsehkopf")
define c = Character("CEO")

#Colors
image white = "#ffff"

#Transitions
define fateslide = MultipleTransition([False, CropMove(0.5, "wipeleft"), "black", Pause(1.0), "black", CropMove(0.5, "wipeleft"), True])
define fatecollapse = ComposeTransition(dissolve, before=moveoutbottom, after=None)

#Character point variables
default goopithaPoints = 0
default sigmaPoints = 0
default jjPoints = 0
default lldPoints = 0
default pelotaPoints = 0
default tvheadPoints = 0

default smallpizza = True # used for choosing small or large pizzas when getting pizza with joejoe


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

transform centerleft:
    xpos 0.33 xanchor 0.33 ypos 1.0 yanchor 1.0

transform centerright:
    xpos 0.66 xanchor 0.66 ypos 1.0 yanchor 1.0

transform big:
    zoom 1.5

transform superbig:
    zoom 3.0

#### Image definitions
image splash = "splash.png"
image main_menu = "gui/main_menu_bright.png"
image main_menu_dark = "gui/main_menu.png"

# CGs
image CG_Cooler = "images/cg joe cooler.png"
image CG_Wack = "images/cg pelota wack.png"
image CG_Desk = "images/cg sigma desk.png"

# BGs
image BG_Alley_1 = "images/bg alley day.png"
image BG_Alley_2 = "images/bg alley dusk.png"
image BG_Alley_3 = "images/bg alley night.png"
image BG_Amusement_Main = "images/bg amusement area.png"
image BG_Amusement_Line = "images/bg amusement line.png"
image BG_Amusement_Outside = "images/bg amusement outside.png"
image BG_Apartment = "images/bg apartment outside.jpg"
image BG_Aquarium = "images/bg aquarium.jpg"
image BG_Beach_Main = "images/bg beach main.png"
image BG_Beach_Coast = "images/bg beach coast.png"
image BG_Bedroom = "images/bg bedroom.jpg"
image BG_Boardwalk = "images/bg boardwalk.png"
image BG_Burger = "images/bg burger.jpg"
image BG_Bus_1 = "images/bg bus inside.jpg"
image BG_Bus_2 = "images/bg bus other window.jpg"
image BG_Bus_3 = "images/bg bus window.jpg"
image BG_Beach_Changing = "images/bg changing room.png"
image BG_Cooler = "images/bg cooler.png"
image BG_Cubicle_1 = "images/bg cubicle day.png"
image BG_Cubicle_2 = "images/bg cubicle dusk.png"
image BG_Cubicle_3 = "images/bg cubicle early.png"
image BG_Cubicle_4 = "images/bg cubicle night.png"
image BG_Ferris = "images/bg ferris up.png"
image BG_Festival = "images/bg festival.png"
image BG_FrontDesk_1 = "images/bg frontdesk day.png"
image BG_FrontDesk_2 = "images/bg frontdesk dusk.png"
image BG_FrontDesk_3 = "images/bg frontdesk night.png"
image BG_Hospital = "images/bg hospital.jpg"
image BG_Konbini = "images/bg konbini.jpg"
image BG_LivingRoom = "images/bg livingroom.jpg"
image BG_Museum = "images/bg museum.jpg"
image BG_Office = "images/bg office.png"
image BG_OutsideOffice = "images/bg outside.jpg"
image BG_Park = "images/bg park day.jpg"
image BG_Pizza = "images/bg pizzeria.jpg"
image BG_Table = "images/bg table.jpg"

# Character sprites

label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return 

label before_main_menu:
    scene black
    scene main_menu with dissolve
    with Pause(2)
    scene main_menu_dark with dissolve
    return

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
            # renpy.call_in_new_context("easter1") 
            renpy.jump("easter1")
        else:
            renpy.jump("intro1")
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
    

