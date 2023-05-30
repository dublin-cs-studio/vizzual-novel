label day5:
    with fade
    "*ding dong*"
    mc "(...)"
    "*ding dong*"
    mc "(What time is it?)"
    show bg livingroom
    with dissolve
    mc "(I drowsily look for my clock while the doorbell rings throughout my house.)"
    mc "(Who’s ringing my doorbell this early in the morning?)"
    mc "(I put on my clothes and open the door.)"
    show bg apartment inside
    show tvhead normal
    with fade
    mc "(It’s TV Head. He looks around quickly before covering the right half of his face.)"
    show tvhead chuuni
    f "The time for retribution has come, mortal. Your presence is needed. They’ve stepped up their security in the past week. Something’s not right."
    mc "(It is way too early for this bullshit.)"
    mc "Who?"
    show tvhead normal
    f "The Secret Organization: Dyna-Earth Enigma Zero. They might be planning an attack on the city."
    f "I’ve narrowed the site of attack to possible locations. I’ve seen evidence of their movement in both the aquarium and the tech museum."
    f "But I’m sure they don’t have the resources to attack both. You will come with me to investigate one of the two."
    show tvhead tired
    t "Only if you want to, of course."
    mc "(I don’t think I have anything better to do today. I’ll come along.)"
    mc "Sure. Where are we going?"
    show tvhead normal
    mc "(He smiles and motions me to step outside.)"
    show bg alley day
    with fade
    f "Like I said, there are two possible locations, but I doubt we have time to fully clear both. So we’ll just check one out, and if they aren’t there then we’ll rush over to the other one."
    f "So, which one do you want to go to?"
    menu:
        "Aquarium":
            $ lldPoints += 1
            jump aquarium
        "Tech Museum":
            $ tvheadPoints += 1
            jump museum
label aquarium:
    mc "Let’s go to the aquarium."
    f "Alright. Let’s get going."
    show bg alley day
    with fade
    f "Here we are. Technology and water typically don’t mix, but I should be fine."
    mc "(He buys two tickets and hands one to me.)"
    mc "Thanks."
    f "No problem. Alright, it’s time to investigate!"
    show bg aquarium
    show tvhead love
    with fade
    f "Woah, it looks awesome."
    mc "(The hall is in nearly complete darkness, save for a few mood lights. But the beauty is in the massive glass walls holding back countless tons of water and aquatic life.)"
    mc "(He continues to look at the fish, entranced by their movements until he realized that I was staring at him.)"
    show tvhead excited
    f "*ahem* Not bad."
    show tvhead normal
    f "Let’s start our investigation. I first saw evidence of Dyna-Earth at the back, near one of the emergency exits."
    f "We need to hurry."
    with fade
    f "It should be that one. Let’s see…"
    f "No signs of modifications. The door seems to be untouched. No footprints..."
    f "Should be all good. Nothing here."
    mc "(He stands back up and pulls out a postcard from his pocket.)"
    f "There should be some more possible entry points at the other exits. Let’s go."
    show tvhead normal at left
    with ease
    mc "(Are we gonna have to do this for every possible exit?)"
    show agent guy at right
    with dissolve
    "Random Man" "Hey there, girl. You look pretty fine."
    "Random Woman" "Sorry, I’m not looking to have a relationship."
    "Random Man" "Woah, I didn’t even ask you anything. But you can’t be too sure, right?"
    "Random Man" "I’ll treat you nice, I promise."
    "Woman" "Leave me alone, no means no."
    "Man" "I promise. You don’t even know how great I am, why are you refusing?"
    mc "(Huh...)"
    mc "(Should we do something about this? She’s clearly bothered by the guy, right?)"
    mc "(Someone should call security or something.)"
    show tvhead normal at center
    with ease
    t "Dude, stop it. She clearly doesn’t want to date you."
    mc "(TV Head grabs the man’s arm and tries to pull him away.)"
    "Man" "Leave me alone. You’re not in this."
    mc "(He tries to shove TV Head’s hand away, but his grip remains firm.)"
    t "No means no. Leave her alone, she doesn’t like you."
    "Man" "What do you know about her? She’s probably just not true to her feelings. You wanna fight?"
    mc "(The man raises his fists up, gearing up to punch.)"
    t "..."
    "Man" "That’s what I thought. Now leave us be."
    with hpunch
    "Man" "Ow, what the fuck!?"
    mc "(The man recoils in pain, but gets up quickly.)"
    "Man" "What was that fo-"
    "Man" "Huh? It doesn’t hurt."
    "Man" "Did you even punch me?"
    show tvhead normal at left
    with ease
    mc "(TV Head doesn’t seem to be the strongest. In fact, he’s shaking his hand in pain.)"
    t "Bro, is your body made of steel or something? What was that?"
    t "Hm? What’s this?"
    mc "(TV Head is holding a strap. It looks like it’s supposed to be attached to a coat or something.)"
    mc "(Suddenly, the man’s coat falls off.)"
    show agent chuuni
    with dissolve
    mc "(...)"
    mc "(What am I even looking at?)"
    mc "(TV Head’s metaphorical eyes shoot wide open.)"
    show tvhead excited
    f "I knew it! You were planning to attack this location, weren’t you. Hah!"
    f "Well, you’ve been read like a book! How foolish, to resort to underhanded tactics instead of trying to fight me head on."
    f "I shouldn’t have expected more from an agent of Dyna-Earth."
    mc "(The man looks split between being confused and embarrassed, but decides to play along.)"
    "Dyna-Earth Agent" "Hmph, to think that my disguise would be revealed so quickly. I’ll need to have a word with my suppliers."
    "DE Agent" "This aquarium will be your end, Fernsehkopf. You’ve played right into my hands."
    "DE Agent" "Water is the natural enemy of machines. In your arrogance, you decided to ignore your primordial understanding of your weakness."
    "DE Agent" "Your demise shall be a brutal one. I will not give mercy to those who oppose my order."
    mc "(He pulls out his comically sized sword and assumes a fighting position.)"
    f "Hah! I’d like to see you try."
    mc "(TV Head pulls out a prop dagger of some sort. The blade is bright orange.)"
    "DE Agent" "Take this!"
    show agent chuuni at left behind tvhead
    with ease
    show agent chuuni at right
    with ease
    f "Haaaaaa!"
    show tvhead excited at right behind agent
    with ease
    show tvhead excited at left
    with ease
    mc "(The two swing around their weapons with glee, carefully avoiding a hit every time. It looks somewhat impressive if not for the mildly cringy scenario.)"
    mc "(Finally, one of them makes a mistake. TV Head accidentally hits the agent in the face.)"
    "DE Agent" "Ouch."
    mc "(He looks slightly annoyed by the pain, but still tries to keep the show going.)"
    "DE Agent" "Foolish Fernsehkopf. Resistance is futile. I am only one of the thousands of agents, all ready to strike back."
    "DE Agent" "Ah, *pant* do not be too arrogant over this victory."
    mc "(Finally, he pretends to collapse on the ground.)"
    hide agent chuuni
    with dissolve
    "Crowd" "Woooooh!"
    mc "(I suddenly realize that the elaborate fight between the two has gathered quite a crowd. It’s mainly children and their parents.)"
    mc "(The children rush over to TV Head.)"
    "Kid" "Woah, that was so cool! How did you do that?"
    "Other Kid" "I wanna be like you when I grow up!"
    show tvhead chuuni
    f "Hmpf. It is not easy going down this path, young one. You must be prepared for a journey filled with pain and despair."
    show tvhead excited
    f "But I could use a few more assistants. I shall take you all under my wing."
    "Children" "Yeah! Wooooooh!"
    f "Hahahahahahahah!"
    "Security Guard" "Sorry sir, but you’re causing a disturbance to the other guests. You’re gonna have to quiet down or leave the premises."
    show tvhead chuuni
    f "Fool, you dare try to control the great Fe-"
    show tvhead normal
    t "Ah."
    show tvhead dead
    t "I mean, sorry about this. I’ll quiet them down."
    jump day5part2

label museum:
    mc "Let’s go to the tech museum."
    f "Alright. Let’s get going."
    with fade
    f "Man, this place takes me back. I used to go here all the time."
    f "But now, we’re here on official business. We’ll need to look for potential entry points and any signs of Dyna Earth."
    f "Let’s go."
    show bg museum
    with fade
    f "First, let’s check the emergency exits. The floor plans say that there’s one..."
    f "It should be that one. Let’s see..."
    f "No signs of modifications. The door seems to be untouched. No footprints…"
    f "Should be all good. Nothing here."
    mc "(He stands back up and pulls out a postcard from his pocket.)"
    f "There should be some more possible entry points at the other exits. Let’s go."
    show tvhead normal at left
    with ease
    mc "(Are we gonna have to do this for every possible exit?)"
    show agent guy at right
    with dissolve
    "Random Man" "Hey there, girl. You look pretty fine."
    "Random Woman" "Sorry, I’m not looking to have a relationship."
    "Random Man" "Woah, I didn’t even ask you anything. But you can’t be too sure, right?"
    "Random Man" "I’ll treat you nice, I promise."
    "Woman" "Leave me alone, no means no."
    "Man" "I promise. You don’t even know how great I am, why are you refusing?"
    mc "(Huh...)"
    mc "(Should we do something about this? She’s clearly bothered by the guy, right?)"
    mc "(Someone should call security or something.)"
    show tvhead normal at center
    with ease
    t "Dude, stop it. She clearly doesn’t want to date you."
    mc "(TV Head grabs the man’s arm and tries to pull him away.)"
    "Man" "Leave me alone. You’re not in this."
    mc "(He tries to shove TV Head’s hand away, but his grip remains firm.)"
    t "No means no. Leave her alone, she doesn’t like you."
    "Man" "What do you know about her? She’s probably just not true to her feelings. You wanna fight?"
    mc "(The man raises his fists up, gearing up to punch.)"
    t "..."
    "Man" "That’s what I thought. Now leave us be."
    with hpunch
    "Man" "Ow, what the fuck!?"
    mc "(The man recoils in pain, but gets up quickly.)"
    "Man" "What was that fo-"
    "Man" "Huh? It doesn’t hurt."
    "Man" "Did you even punch me?"
    show tvhead normal at left
    with ease
    mc "(TV Head doesn’t seem to be the strongest. In fact, he’s shaking his hand in pain.)"
    t "Bro, is your body made of steel or something? What was that?"
    t "Hm? What’s this?"
    mc "(TV Head is holding a strap. It looks like it’s supposed to be attached to a coat or something.)"
    mc "(Suddenly, the man’s coat falls off.)"
    show agent chuuni
    with dissolve
    mc "(...)"
    mc "(What am I even looking at?)"
    mc "(TV Head’s metaphorical eyes shoot wide open.)"
    show tvhead excited
    f "I knew it! You were planning to attack this location, weren’t you. Hah!"
    f "Well, you’ve been read like a book! How foolish, to resort to underhanded tactics instead of trying to fight me head on."
    f "I shouldn’t have expected more from an agent of Dyna-Earth."
    mc "(The man looks split between being confused and embarrassed, but decides to play along.)"
    "Dyna-Earth Agent" "Hmph, to think that my disguise would be revealed so quickly. I’ll need to have a word with my suppliers."
    "DE Agent" "This museum will be your end, Fernsehkopf. You’ve played right into my hands."
    "DE Agent" "Your demise shall be a brutal one. I will not give mercy to those who oppose my order."
    mc "(He pulls out his comically sized sword and assumes a fighting position.)"
    f "Hah! I’d like to see you try."
    mc "(TV Head pulls out a blue, cubical sword. The way it reflects light tells me that it's foam.)"
    show agent chuuni at left behind tvhead
    with ease
    show agent chuuni at right
    with ease
    f "Haaaaaa!"
    show tvhead excited at right behind agent
    with ease
    show tvhead excited at left
    with ease
    mc "(The two swing around their weapons with glee, carefully avoiding a hit every time. It looks somewhat impressive if not for the mildly cringy scenario.)"
    mc "(Finally, one of them makes a mistake. TV Head accidentally hits the agent in the face.)"
    "DE Agent" "Ouch."
    mc "(He looks slightly annoyed by the pain, but still tries to keep the show going.)"
    "DE Agent" "Foolish Fernsehkopf. Resistance is futile. I am only one of the thousands of agents, all ready to strike back."
    "DE Agent" "Ah, *pant* do not be too arrogant over this victory."
    mc "(Finally, he pretends to collapse on the ground.)"
    hide agent chuuni
    with dissolve
    "Crowd" "Woooooh!"
    mc "(I suddenly realize that the elaborate fight between the two has gathered quite a crowd. It’s mainly children and their parents.)"
    mc "(The children rush over to TV Head.)"
    "Kid" "Woah, that was so cool! How did you do that?"
    "Other Kid" "I wanna be like you when I grow up!"
    show tvhead chuuni
    f "Hmpf. It is not easy going down this path, young one. You must be prepared for a journey filled with pain and despair."
    show tvhead excited
    f "But I could use a few more assistants. I shall take you all under my wing."
    "Children" "Yeah! Wooooooh!"
    f "Hahahahahahahah!"
    "Security Guard" "Sorry sir, but you’re causing a disturbance to the other guests. You’re gonna have to quiet down or leave the premises."
    show tvhead chuuni
    f "Fool, you dare try to control the great Fe-"
    show tvhead normal
    t "Ah."
    show tvhead dead
    t "I mean, sorry about this. I’ll quiet them down."
    jump day5part2
label day5part2:
    scene bg apartment outside
    with fade
    mc "(That was certainly a day.)"
    mc "(Out of everything that could have happened today, seeing two chuunibyous fight in public was not something I expected.)"
    mc "(Oh well. Not like I could have done anything better with my time.)"
    mc "..."
    mc "(What's this?)"
    mc "(A strange letter is placed right outside of my apartment.)"
    mc "(I look at the other doors, but they don't have one. It seems like something only I'm dealing with.)"
    mc "(I'll take it inside I guess.)"
    show bg livingroom
    with dissolve
    "Notice from IRS"
    "Your taxes are overdue. You will be charged for late fees."
    mc "(Not this again...)"
    menu:
        "Rip up the letter":
            mc "(I tear the paper in half and ball up the remains.)"
            mc "(I don't have the money to spare on taxes.)"
            mc "(I toss the ball into the trash can.)"
        "Leave it be":
            mc "(I'm gonna keep this just in case, but I don't have the money to spare on taxes.)"
            mc "(As I look at the paper again, I notice a drawing on the back.)"
            mc "(It's a pencil sketch of a dolphin, surrounded by a heart.)"
            mc "(Did that dolphin dude draw this?)"
            mc "(Wait, does that mean he has my address?)"
            mc "(The thought of that scares me.)"
            mc "(Y'know what, I'm just not gonna think about it.)"
    mc "*yawn*"
    mc "(Is it dark already?)"
    mc "(Sleep time, I guess.)"
    jump day6