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

# if you tell goopitha you've already gotten a tour
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
