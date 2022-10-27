# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Joe Joe")
define s = Character("Sigma")
define s2 = Character("Sigma", image="sigma")
define temp = Character("Secretary")
define mc = Character("[name]")
define g = Character("Goopitha")

image side sigma = "sigmaside.png"


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

    scene bg office 
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

    "You approach the office desks with Sigma."

    s "Here’s the H(uman but alien as well I guess)R Department, where all the complaints about your pay go to."

    with fade 

    s "Here’s the Accounting and Finance Department. They commit tax fraud--I mean, they have the very important task of ensuring all our funds and expenses are properly accounted for."

    with fade 

    s "Over here’s the PR Department. They write propaganda so we can pretend we’re not a soul--crushing corporation that may or may not be responsible for multiple human rights abuses."

    with fade 

    "Sigma speeds past the departments, clearly bothered by the tour."

    "By the end of the tour, you've reached the water cooler, where you spot an insanely average looking man."

    with fade 
    
    scene bg cooler

    hide sigma

    show joejoe

    j "Oh, hey there, guys! Welcome to my spot!"

    s2 "Meet Joe Joe. That’s not his spot. He doesn’t work here."

    menu:
        "Hi, Joe Joe. I think your spot is great.":
            j "Thanks :]"

        "Pretty {i}cool{/i} water cooler you got there.":
            j "Thanks :]"
        "Uh. Okay.":
            j "*Waves*"
    
    hide joejoe 

    show sigma 

    s "Feel free to spend some time exploring our break... corner."

    s "I have customers to satisfy, KPIs to report, people to fire, souls to crush, tax fraud to commit..."

    s "...Y'know, normal secretary stuff. See ya."

    with move 
    
    show sigma at left 

    with move 
    
    hide sigma 

    s2 "{size=-10}Ugh, so much work. I don't get paid enough for all this.{/size}"

    show joejoe 

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
    
label fulfillment:
    scene bg office
    with fade 

    

    "You walk away from the break corner to start working, but run into a strange green woman."
    
    with dissolve 
    show goopita

    mc "(I feel like I’ve seen someone who looks like that woman. Maybe an old friend, or perhaps a classmate?)"

    "Familiar-Looking Woman" "Hey, [name]! *Waves*"

    "Familiar-Looking Woman" "I haven't seen you in a while. Are you new here?"

    mc "Yeah, I just got hired a few days ago."

    mc "(I guess she's an old friend of mine with how sociable she seems to be around me. I don't know her name though, but I can't say that to her face.)"

    hide goopita

    "Random Coworker" "Goopitha, can you take these papers down to Finance real quick?"

    mc "(Goopitha, huh. I guess she is a slime after all.)"

    show goopita

    g "Yeah, I'll be there in a minute!"

    mc "(She seems to be very excited about her job, for some reason. Comparing her to Sigma, it's hard to believe they work at the same office.)"

    g "So, do you need a tour around the place? Or did Ms. Sigma already cover that for you?"

    menu: 
        "Yeah, Sigma gave me the tour already.": 
            jump already  
        "No, I just got here half an hour ago.":
            
            jump tour 

label already:
    g "Really? Aw man, I wanted to show you all the cool things around the office. But I suppose it is Ms. Sigma’s job to do that, not mine."

    g "No use dwelling on the past, though. I hope our time together here will be more than enough to make up for how long we’ve been apart. *She hugs me*"

    with vpunch

    mc "(Woah, she’s too close. I guess that’s normal for childhood friends, but she’s still a girl. I normally wouldn’t mind being this close to a girl, but I am not enjoying having cold, wet slime cover my shirt.)"

    "Goopitha heads off to do her tasks, leaving your shirt slightly damp."

    scene black 
    with fade 
    

    "{b}To be Continued...{/b}"


    return 

label tour:
    "(I’ve already seen the entire office, but I probably should get to know Goopitha better if I don’t want to make conversations with her awkward.)"
    
    "(Her eyes brightened so much when I said that. I must have been really close to her beforehand, unless she’s this enthusiastic about everything.)"

    g "I’d gladly show you around the place! We should start at my cubicle!"

    "She grabs your hand and pulls you along. "

    with move 
    
    show goopita at right 

    with move 
    
    hide goopita 

    with fade 

    show goopita at center

    mc "(Her hands are really cold. She is a slime after all, but I thought she’d produce at least some body heat to move around.)"

    mc "(She certainly moves quickly for a slime. Then again, I can’t say I’ve seen a slime move before.)"

    g "This is where I work as a Charitable Fulfillment Expert!"

    mc "That seems pretty cool."

    mc "(I should probably add on to that, but I honestly have no idea what to add on. Maybe I could ask about what she does?)"

    mc "What do you do as a Charitable Fulfillment Expert?"

    g "I’m glad you asked! I’ve wanted to show you this for a long time!"

    mc "(Woah, she seems really happy that I asked her that. Does she just really like her job, or is she just happy to reunite with me again? Speaking of which, how long have we been apart?)"

    g "Please, sit down! I have so much to tell you, so make yourself at home!"

    mc "(This chair is really uncomfortable. That would matter less for a slime, but I’m pretty sure office furniture is all identical.)"


    scene black 
    with fade 
    

    "Goopita launches into a long story about how she started working at the company..."

    
    scene bg office 
    with fade 

    show goopita

    g "...and then I said to Sigma, you really need to take your morning coffee! 'Cause she was being even more of a downer than she normally is..."

    mc "(Her slime is pressing against my back… Oddly enough, it actually feels quite comfortable. But seriously, does she not realize how close she is? Childhood friend magic really is something, huh.)"

    g "...and that's how I met Pelota! She's so cool! Rumor is that she's killed over a hundred different nefarious entities with just her baseball bat. and..."

    mc "(Is she subconsciously shaping herself into a back rest? I feel like this chair is becoming softer slowly. It might just be my body heat warming her up, though.)"

    g "...and after that I... sorry, I usually head for the break corner afterwards..."

    mc "(What was that pause? Does she not like Joe Joe and his break corner?)"

    "You look upwards for the first time in a while and see that Goopitha has maneuvered her body around the chair and around you."

    mc "(Jeez, she’s close! I can’t even begin to try to hide my blushing. Does she do this to everyone who sits down in her chair?)" 
    
    mc "(I wish I realized that earlier, I can feel my cheeks turning red like a furnace.)"

    mc "(I hope she just ignores it, I’m way too close to pretend like it’s something else.)"

    mc "(Wait, did she just realize it as well? Her face is covered with a light red color, even though slimes shouldn’t have the blood to blush properly.)"

    mc "(Does she not normally get this close to people? If so, why did she do so to me? Why?)"

    mc "(I can’t take this pressure anymore!)"

    "You quick stand up from the chair, avoiding eye contact with Goopitha."

    g "I-I-I'm sorry. I didn't realize I was that close."

    scene black 
    with fade 
    

    "{b}To be Continued...{/b}"


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.



    # This ends the game.

    return
