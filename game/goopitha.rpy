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
    

    "Goopitha launches into a long story about how she started working at the company..."

    
    scene bg office 
    with fade 

    show goopita

    g "...and then I said to Sigma, you really need to take your morning coffee! 'Cause she was being even more of a downer than she normally is..."

    mc "(Her slime is pressing against my back… Oddly enough, it actually feels quite comfortable. But seriously, does she not realize how close she is? Childhood friend magic really is something, huh.)"

    with fade 

    g "...and that's how I met Pelota! She's so cool! Rumor is that she's killed over a hundred different nefarious entities with just her baseball bat. and..."

    mc "(Is she subconsciously shaping herself into a back rest? I feel like this chair is becoming softer slowly. It might just be my body heat warming her up, though.)"

    with fade 

    g "...and after that I... sorry, I usually head for the break corner afterwards..."

    mc "(What was that pause? Does she not like Joe Joe and his break corner?)"

    "You look upwards for the first time in a while and see that Goopitha has maneuvered her body around the chair and around you."

    # insert color graphic here, showing goopitha wrapped around the chair and MC 

    mc "(Jeez, she’s close! I can’t even begin to try to hide my blushing. Does she do this to everyone who sits down in her chair?)" 
    
    mc "(I wish I realized that earlier, I can feel my cheeks turning red like a furnace.)"

    mc "(I hope she just ignores it, I’m way too close to pretend like it’s something else.)"

    mc "(Wait, did she just realize it as well? Her face is covered with a light red color, even though slimes shouldn’t have the blood to blush properly.)"

    mc "(Does she not normally get this close to people? If so, why did she do so to me? Why?)"

    mc "(I can’t take this pressure anymore!)"

    "You quick stand up from the chair, avoiding eye contact with Goopitha."

    g "I-I-I'm sorry. I didn't realize I was that close."

    menu:
        "It's alright. (Hiding the fact that your face has become one with the tomatoes)":
            "Goopitha smiles, her blush clearing up."
            g "We should hang out and grab some coffee together-"
        "(Continue to blush like a maniac)":
            g "I-I'll be going-"
    
    hide goopita

    with vpunch 

    "Strange Voice" "*dophin noises* YOUR DEBTS…THEY ARE DUE!"

    mc "(Huh?)"

    with hpunch

    "Strange Voice" "*more dolphin noises* YOU ARE $30,000 IN DEBT AND IT WAS DUE YESTERDAY!"

    mc "(Is there a dolphin in the office? More importantly, why can the dolphin talk?)"

    "Suddenly, the door crashes down, and someone barges into the office." 
    
    with vpunch

    with vpunch

    with hpunch

    "Strange Voice" "*dolphin noises* I HAVE COME TO COLLECT YOUR DEBT!"

    "Goopitha turns towards the commotion, looking crossed."

    show goopita

    g "Again?"

    hide goopita

    "You try to look at the newcomer, but your view is blocked by the cubicle walls."
    
    show sigma at center

    with moveinleft

    s "I'll grab Pelota real quick." # add emotion here -sigma frowning

    hide sigma

    with moveoutleft

    "Strange Voice" "Are you ignoring me? I know you haven’t bothered to reply to my emails, but you could at least pretend to care about me."

    "The voice comes from your left. As you try to recover from your embarrassment someone grabs your shoulder and forces you to face them."

    mc "(Woah there, calm down. I nearly fell over. What’s all this about a debt collection?)"

    mc "(What kind of person thinks it’s a good idea to push someone without their consent?)"

    "As you look up at your strange assailant, you are blinded by sparkling bright lights."
    
    show lld

    "Strange Dolphin Man" "*Clapping his hands on every syllable* Listen here, kiddo." 
    
    "Strange Dolphin Man" "I have better things to be doing than lecturing a college dropout on paying their debts. Either you hand over $30,000, or your paycheck will be cut accordingly."

    mc "What."

    mc "The."

    mc "Hell?!"

    "Strange Dolphin Man" "*Scoffs* What’s wrong? Did you forget about me as well?"

    mc "(Who the hell is this dolphin man? He's absolutely terrifying!)"

    "Strange Dolphin Man" "*Sighs and lets out a dramatic clucking noise* “I should’ve known better from someone who hasn’t bothered to pay his loans in over ." 
    # insert however long the MC was unconscious for 


    # insert color graphic of loan loan dolphin straightening his shirt and combing his bald head here
    l "The name’s Lone Loan Dolphin, a college student’s worst nightmare. I come to collect debt whenever someone forgets to pay off their student loans or any other types of loans."

    hide lld 

    show goopita

    "Goopitha leans over to you and whispers in your ear."

    g "By the way, debt collectors aren’t legally allowed to use physical force to collect money. According to the FDCPA, they can only email or call you to remind you of your debt."

    hide goopita 

    show lld

    l "While I can’t {i}legally{/i} use physical force, it’d be easier to find a dolphin’s ears than to actually contact law enforcement here. *cracks knuckles while maniacally chittering*"

    hide lld
    
    #with move
    
    #show sigma at left 

    #with move 
    
    show sigma at center
    
    with moveinleft

    # with move 

    # show pelota at left 

    "Cool woman with a baseball bat" "That one? *She points the bat at you.*"

    s "No, the dolphin head. That’s the fourth time he came here this month."

    hide sigma 

    with fade 

    

    # cutscene or CG of pelota beating up LLD

    # show pelota here

    "Cool Woman" " *Dusting herself off* Fourth time? Didn’t know dolphins liked their debt collection so much."

    "She glances up at you while picking up her bat."

    "Cool Woman" "You new? Never seen your face before."

    p "Name's Pelota. I'll see you around, I guess."

    # with move

    # hide pelota 

    mc "(Isn't Pelota Spanish for-)"

    show sigma 

    s "Wait, come back. Can you show them the basics of being a Charitable Urgency Manager?"

    p "Seriously? I thought they were just the local paper carrier. I haven’t seen someone more unfit for such a job than them."

    "Sigma whispers something into Pelota’s ear, causing her to freeze up."

    s "Just deal with it. I trust that you will handle this properly."

    with move 
    
    show sigma at left 

    with move 
    
    hide sigma 

    "She walks away, leaving you alone with Pelota."

    p "{size=-10}I'll kill her.{/size}"

    p "*sighs* Follow me."

    with fade 

    "You follow her to a room lined with cushioning, with one floor-to-ceiling mirror on the opposite side of the door."

    p "Aight, I'll show you how to properly box. *She tosses her bat to the side*"

    # insert combat minigame or other minigame here

    with fade  

    # in the future, add diverging labels based on if you did good or bad in the game 

    p "Not bad. You'd make for a good boxer. I think. I don't really fight with my fists that often. *She hands you a bottle of water*"

    mc "(That was the worst experience of my life. I can’t believe I’m still alive after all that. My body is soaked in sweat, I should probably take a shower after this.)"

    mc "(Damn, that water is good though. Not even Joe Joe’s water cooler can beat this.)"

    "You stumble up from the floor and leave the training room."

    mc "(Even the best water in the world can’t fix the fact that I’m covered in sweat, huh. I should probably take off my jacket.)"

    mc "(Work is still happening, isn’t it. I should probably do something before someone starts looking at me like I’ve been rammed by a bus and have a caffeine problem.)"

    menu:
        "(I should go spend time with…)"

        "Sigma":
            jump sigmaday1 

        "Goopitha":
            jump goopithaday1

        "Joe Joe":
            jump joejoeday1

        "Pelota":
            jump pelotaday1
        
        "Do some paperwork":
            jump paperwork




    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.



    # This ends the game.

    
