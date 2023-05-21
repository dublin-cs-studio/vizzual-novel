label day3:
    scene bg nightalley
    with fade
    mc "(Wow, it got dark fast. The streetlights are turning on, lighting up the sidewalk.)"
    mc "(It's not a long walk home, but I have to carry my food with me. The plastic bags are slowly pressing into my hands.)"
    scene bg livingroom
    with dissolve
    mc "(At last, I am home again. My hands are tired of carrying the bags, so I drop them off on the counter. I sit down in the chair and relax for a bit before I start to make dinner.)"
    mc "(I'll just heat up some of the frozen food. It should be simple enough, right? I just need to follow the instructions on the box and it should be alright.)"
    mc "..."
    mc "(Smells good. I'll just eat this and go to sleep.)"
    scene bg bedroom
    with fade
    mc "(Yet another day of life. I can't say I'm excited to go to work, but at least it gives me something to do.)"
    mc "(I get out of bed and get ready for the day. I probably shouldn't eat ramen for breakfast, but I'm an adult and I can make decisions for myself.)"
    scene bg dayfrontdesk
    with fade
    mc "(I arrive at the office building, ready to fill out more paperwork.)"
    show sigma glasses
    with dissolve
    mc "Morning, Sigma."
    s "Good morning."
    scene bg cubicle1
    with dissolve
    mc "(It's not even lunch break yet but I'm already bored of working. My focus begins to waver from the identical looking papers and soon enough I'm fully distracted.)" 
    mc "(I can't make any mistakes in the documentation, but I also can't be bothered to do something this boring for hours upon hours. It's probably time for me to take a break.)"
    scene bg cooler
    with dissolve
    mc "(Joe Joe still isn't here, huh. Well, I guess I came at a different time than usual.)"
    menu:
        "I'll get a cup of..."
        "Water":
            mc "(I grab one of the paper cups attached to the water cooler and fill it up slowly. The conical shape makes it easier to stack and fold the cups, but it holds significantly less water.)" 
            mc "(I admire the bubbles rising from the water cooler into the water jug and take a sip of water.)"
            mc "(The water is quite refreshing, but I don’t feel like it’s helping very much. Maybe the coffee would’ve been a better choice.)"
            mc "(I slowly sip the cup while looking around the office. I feel more focused now.)"
        "Coffee":
            mc "(I grab a cup and place it underneath the nozzle. With a press of a button the coffee begins pouring out, filling up the cup with a light whirring noise.)"
            mc "(The coffee smells amazing and I can feel the heat of it through the paper cup. It warms up my fingers, making me feel more energized before I even take a sip.)"
            mc "(The coffee is quite energizing. It doesn’t taste particularly good, but it does the job.)"
            mc "(I finish the cup, trying to get the last remaining drops of coffee before tossing it away. I feel more energetic now.)"
    mc "(I try to head back to my cubicle when someone bumps into me, knocking me over.)" 
    with vpunch
    "Random Woman" "Sorry!"
    mc "It’s fine."
    mc "(I look up at the woman who knocked me down.)"
    scene cg goopitha meet
    with dissolve
    #This could also be a normal sprite
    with dissolve
    mc "(She’s... a slime.)"
    mc "(Her body seems to be made of a gelatinous material. Some of it is on my clothes where she bumped into me. She looks quite pretty though.)"
    mc "(She seems to have noticed that her slime got on me.)"
    scene bg cooler
    show goopitha happy 1
    with dissolve
    "Slime Woman" "Oh, I’m so sorry about your clothes."
    mc "(She touches her main body to the parts on my clothing and pulls some of it off. My clothes are stained in the process.)"
    mc "Thanks."
    mc "(I get up from the ground and dust myself off.)"
    show goopitha neutral
    "Slime Woman" "Wait, are you..."
    mc "Have I met you before?"
    mc "(She might be an old friend of mine from before I lost my memories. Not good.)"
    show goopitha happy 2
    "Slime Woman" "Wow, it is you! I haven’t seen you in forever!"
    mc "Haha, yeah. It’s been so long."
    mc "(I have no idea what she’s talking about.)"
    "Slime Woman" "What were you doing all this time? I thought you moved."
    mc "(Should I tell her? I should probably be honest with my friends but I don't even know her name. How would she feel if I completely forgot about her?)"
    mc "About that..."
    mc "(She looks at me earnestly, waiting for my answer. What should I do?)"
    "Random Guy" "Hey Goopitha, can you take these papers to the front desk for me?"
    mc "(So she’s Goopitha, huh. Makes sense considering she’s a slime.)"
    g "Yeah, just give me a sec."
    g "Sorry, I’ll listen to your story later. I need to run some errands real quick."
    show goopitha neutral
    g "Wait, why are you even here? Do you even work here?"
    mc "(I was hoping she’d leave me alone...)"
    mc "No, I just got hired a few days ago. This is my third day here."
    show goopitha happy 2
    g "I can show you around then! Or did Sigma already do that?"
    menu:
        "Sigma already gave me a tour":
            jump touralready


        "Show me around":
            $ goopithaPoints += 1
            jump goopithatour

label touralready:
    mc "Sigma already did that."
    show goopitha neutral
    mc "(Her smile flattens ever so slightly. I feel kinda bad for her now. But she quickly regains her energy.)"
    show goopitha happy 1
    g "Oh, that’s fine. Hold on."
    mc "(She looks around to see if her coworker is still around. To her delight, he has already headed off to somewhere else.)"
    show goopitha grin
    g "I’ll just take those papers later. No one has to know…"
    mc "(Her bright smile turns into a cheeky grin as she winks at me. There goes my plans of not talking about my amnesia.)"
    show goopitha happy 2
    g "So, how have you been lately? I haven’t seen you in ages!"
    mc "I’ve been good. Not really much happening in my life. What about you?"
    mc "(I hope that I can divert the attention onto her. She seems like the type of person who can’t stop talking once she starts.)"
    g "Oh, you won’t believe what’s happened lately. So, y'know how the company made some policy changes a while ago?"
    mc "Mhm."
    g "There was this lady..."
    show bg cubicle2
    with fade
    mc "(It looks like I was right on the money. She's not even close to done talking.)"
    mc "(She doesn’t really notice that I’m not really responding to her. A few \"mhm\"s and nods are enough to satisfy her.)"
    mc "(As I approach my cubicle, I realize someone is sitting down at my spot. Er, maybe not. All these cubicles look the same after all.)"
    mc "(I rub my eyes and take another look.)"
    g "Did you not sleep well? That’s not good for you, y’know. A normal adult should sleep 7 hours a day."
    mc "No, it’s just..."
    mc "I think someone’s in my cubicle."
    hide goopitha happy 2
    show pelota neutral at right
    with dissolve
    mc "(I point it over to the woman at my desk. Her legs are kicked up on the table and she leans back so far that I’m scared she’ll fall over.)"
    mc "(A black baseball bat is placed on her lap. It almost falls out of her lap as she yawns, but she miraculously grabs it with her free hand.)"
    show goopitha happy 1 at left
    with dissolve
    g "Oh, that’s Pelota! You totally need to meet her!"
    show goopitha happy 1 behind pelota at right 
    with move
    mc "(She grabs Pelota and hugs her from the back.)"
    show goopitha happy 2
    g "Pelotaaaa!"
    show pelota death
    p "Gah!"
    mc "(Pelota twitches in surprise and falls backwards into Goopitha’s slime body. The chair falls straight through Goopitha, but Pelota is suspended in the slime and brought back up to her feet.)"
    show pelota mad
    p "What do you want?"
    mc "(She hasn’t noticed me at all. Her casual tone makes me think that this is a regular occurrence.)"
    g "Well..."
    hide goopitha happy 2
    with easeoutleft
    mc "(Goopitha reaches over to me and pushes me towards Pelota.)"
    show pelota neutral at center
    with dissolve
    g "This is [name], my old friend! I haven’t seen them in ages!"
    g "[name], this is Pelota. I met her while working here, and I think she’s also quite new to the job!"
    mc "Nice to meet you, Pelota."
    mc "(I reach out my hand. Isn’t Pelota Spanish for-)"
    p "Yo. Nice to meet you too, I guess."
    mc "(She looks into my eyes with a terrifying stare that pierces into my brain, reading my thoughts. She somehow notices my opinion of her name.)"
    show pelota mad:
        ease 1 zoom 1.5 xoffset 0 yoffset 500
    p "{size=-10}Not a fucking word.{/size}"
    mc "(She grasps my hand like a vice, crushing my fingers together.)"
    show pelota neutral:
        ease 1 zoom 1.0 xoffset 0 yoffset 0
    g "So, what do you do here, [name]?"
    mc "I’m a Charitable Urgency Manager. I think I'm supposed to fight the diseases and stuff, but I've only been doing paperwork for the past three days."
    show pelota smile
    p "Oh, you too? I’ve been waiting for another one to show up."
    p "Work is nothing but a pain in the ass, so I just stopped coming here."
    show pelota neutral
    p "So, what’d you do to get stuck with this job?"
    mc "Huh?"
    show pelota mad
    p "Everyone who gets this job usually gets assigned it by some rich dumbass. I haven’t seen anyone do this voluntarily."
    mc "Why not?"
    p "Cause it sucks ass. If you aren’t wasting your life away doing paperwork, you’re dealing with some disease that you aren't trained to deal with."
    p "I’m only here cause I beat the last C.U.M. out of commision and had to cover for him as a payment."
    show pelota neutral
    p "But you don’t seem like the type to beat some dude up. What’s your story?"
    mc "Well..."
    mc "(If only Goopitha wasn’t here, then I could just tell the truth to her. Pelota’s thousand mile stare looks like she wouldn’t believe me if I lied, but what other choice do I have?)"
    mc "I..."
    p "Nevermind. I’m sure you don’t wanna talk."
    mc "(Huh?)"
    mc "(She picks up her bat from the floor and tosses it into the air.)"
    p "Whatever. Actions speak louder than words, right? Tell me your story through your fists."
    g "Guys, don’t fight. We can settle this peacefully."
    mc "(She assumes a fighting pose while motioning me to do the same.)"
    mc "Wai-"
    mc "(Her bat hits the floor. She swings her left leg into my shins. She’s not gonna wait.)"

    # minigame here, for now filler with manual win/lose selection 

    menu:
        "Win":
            $ pelotaPoints += 1
            mc "*cough* (My body hurts. She really didn't pull her punches.)"
            show pelota laugh
            p "Not bad. I didn't expect that much out of you, but you don't suck as much as I thought you would."
            mc "(She steps on the handle of her bat, launching it into her hand.)"
            show pelota smile
            p "Here. Drink up. You deserve it."
            mc "(She hands me a bottle of water. My hands can barely move though, so she opens the cap for me.)"
        "Lose":
            mc "*pant* (That really hurt. I think she broke my shoulders or something. I can’t move my right arm.)"
            mc "(I collapse on the ground as my body aches and pulses. It's not a good feeling.)"
            mc "Thanks."
            show pelota smile
            p "You did well. Not to my expectations, but no one's met those before."
            mc "(She tosses a bottle of water onto my body.)"
            mc "(I grab the bottle, but my hands can't muster the strength to uncap it.)"
            mc "(Pelota grabs the bottle from me and removes the cap)."
            mc "Thanks."
    p "No problem."
    mc "(I take a sip from the bottle. It's every so slightly sweeter than normal water.)"
    mc "(After a few more minutes of resting I get up from the floor.)"
    mc "(Pelota is still sitting at my cubicle, but I can probably get her to move. She’s downing an entire bottle of water. I don't think she's taken a breath since she started.)"
    p "Hah."
    mc "(Pelota caps the bottle and tosses it into the waste bin. It almost lands perfectly until...)"
    show pelota smile at right
    show goopitha angry at left
    with dissolve
    mc "(Goopitha grabs it out of the air and bonks Pelota over the head.)"
    show pelota happymad
    g "Don’t do that, Pelota. No one likes getting beat up on their first meeting. You’re gonna scare [name] off."
    p "Gah, I forgot you were here."
    mc "(To be honest, I did too.)"
    g "Apologize to [name]."
    mc "(Goopitha continues to bonk Pelota over the head with the water bottle.)"
    show pelota neutral
    p "Alright, alright. I get it."
    show pelota mad
    p "My bad. Sorry about that. I like to test everyone that I meet."
    mc "It’s fine."
    mc "(Goopitha doesn't look satisfied but drops the bottle into the waste bin anyways.)"
    show goopitha happy 1
    g "Right, as I was saying, this is-"
    "Coworker" "Yo Goopitha, have you delivered those papers yet?"
    show goopitha happy 2
    g "I’m on it!"
    show goopitha happy 1
    g "Sorry guys, I’ll have to talk to you later. Be nice to each other!"
    hide goopitha happy 1
    with easeoutleft
    mc "(Goopitha heads back to her department, leaving Pelota and I with an awkward silence to fill.)"
    mc "So… how was your day?"
    p "It’s not even lunch break yet and you’re asking me how my day was?"
    mc "...Yeah."
    show pelota neutral
    p "..."
    show pelota mad
    p "It was fine."
    mc "Mhm."
    mc "(I decide to get back to work. Pelota’s still at my desk, but the cubicles near us are empty. I move my papers over and start to fill out the forms.)"
    scene bg cubicle
    with fade
    mc "(Finally, the clock hits 5PM. I get up and stretch my arms out.)"
    mc "(Looks like Pelota never came back from lunch break. Well, she didn't seem like she wanted to stay.)"
    mc "(I gather up my things, head to the lobby, and wave goodbye to Sigma.)"
    scene bg duskalley
    with slideawayleft
    mc "(What should I eat tonight?)"
    mc "(As I step outside, a voice comes from behind me.)"
    g "Hey [name]!"
    show goopitha happy 1
    with dissolve
    mc "(I turn around to greet the cheery slime girl following me.)"
    mc "Hey Goopitha."
    g "How was your day today?"
    mc "Pretty good. Not much happened, but Pelota is pretty cool."
    g "Yeah, she is."
    jump day3part2
    
label goopithatour:
    mc "You can show me around."
    show goopitha happy 2
    g "Perfect! Just follow me."
    mc "(She grabs my hand and pulls me towards the main lobby.)"
    scene bg dayfrontdesk
    with fade
    show goopitha happy 1 at left
    show sigma glasses at right
    with dissolve
    g "Okay, so here is the main lobby! I’m sure you’ve already seen this before."
    show goopitha happy 2
    g "Hey Sigma!"
    mc "(She waves over at Sigma, who glances up from her computer. She looks at us questioningly, no doubt because we’re supposed to be working.)"
    mc "(I wave at Sigma too and smile as she silently stares at me.)"
    g "This way!"
    mc "(Goopitha pulls me with her. We reach the junction where I would normally turn left, but Goopitha drags me to the right. After a few more twists and turns, she finally stops at a department I don’t recognize.)"
    scene bg cubicle1
    with fade
    show goopitha happy 1
    with dissolve
    g "This is where I work! Pretty neat, huh?"
    mc "(Her cubicle looks identical to mine, save for the lack of a chair. I guess she doesn’t need to sit down since she’s a slime.)"
    mc "What do you do here?"
    g "I just fill out paperwork. It’s not very interesting, but I get to meet a bunch of cool people. Plus, the pay is pretty decent."
    g "Here, lemme show you what I have to do."
    mc "No it’s fine, I know wha-"
    g "Here!"
    hide goopitha happy 1
    with dissolve
    mc "(Goopitha steals a chair from the cubicle next to hers and sits me down in it. She scrambles around her desk, looking for any paperwork that she can show me.)"
    g "Where is it, where is it?"
    mc "(I don’t think she’s noticed, but she’s slowly covering my body with her slime. It’s not the most comfortable feeling. My clothes are sticking to each other and my back is cold.)"
    g "Aha! Here, look at this."
    mc "(Her voice comes from above as she pulls out an empty form. I instinctively look upwards.)"
    show cg goopitha slime
    with dissolve
    #Make this first person with like a slime filter or something it doesn't need to look good
    mc "(Woah, she’s close! Her entire body is looming over me as she explains how she does her job. I quickly look back down before she notices that I’m not paying attention.)"
    g "Right, so normally you would have a file on someone and..."
    mc "(She continues to explain. Goopitha speaks with much more enthusiasm than one should have when talking about paperwork.)"
    mc "(She flips the sheet when I feel a heavy weight on my shoulders. It presses against my back, squeezing me downwards. Are those her-)"
    "Coworker" "Goopitha, did you deliver those papers yet?"
    mc "(I can feel my face flush with red. I hope that guy can’t see the predicament I’m in. That would be beyond embarrassing. I’m afraid to look up, since Goopitha’s body is so close to mine.)" 
    mc "(She might notice that her breasts- or what I hope are her breasts- Actually, why am I hoping that it’s her breasts? Does she even know that they are pressing against me? Her unspecified body part, but preferably-)"
    g "I’m working on it, hold on."
    show bg cubicle1
    with dissolve
    mc "(Goopitha suddenly moves, scaring me out of my trance. I quickly look up.)"
    mc "(Unfortunately, or maybe fortunately, it’s just her slime on me. I guess it technically counts as breasts, since they’re in that general area, but that means that any part of her body would also count.)"
    mc "(I feel my face going even more red when I realize that I hoped that they were her breasts. I hope no one here is a mindreader, however unlikely that would be.)"
    "Random Guy" "Hurry up."
    g "*sigh* Sorry about that. I still need to do a bunch of stuff. But anyways, where were we?"
    show cg goopitha chair
    with dissolve
    #This should be the third person one
    mc "(Goopitha’s body slowly creeps forward as she tries to find her place on the paper again. I try my hardest not to move even a millimeter.)"
    g "Oh right. Yeah, from here you would..."
    mc "(Goopitha slowly tightens her slime around me. Maybe it’s instinctual, maybe it’s habitual. Either way, I doubt that she’s doing it on purpose. I mean, is this normal? Maybe she just does this to everyone she meets, and I’m just getting worked up over nothing.)"
    mc "(The slime is quite cold, but over time my body heat warms it up. It’s gotten surprisingly warm now.)"
    mc "(I start to relax my movements when I suddenly start to feel weightless.)"
    mc "Aah!"
    mc "(I accidentally spoke from my surprise. Goopitha’s body twitches and I land back in my seat.)"
    g "What’s wrong, [name]? Did you-"
    mc "(Goopitha looks down at me. I freeze in fear, hoping she wouldn’t find what happened weird. I mean, she did this herself, right? Surely I’m not at fault, right?)"
    g "Ah."
    scene bg cubicle1
    show goopitha embarrassed
    with dissolve
    mc "(Her face instantly turns a bright red. She covers her face with her hands.)"
    mc "No, this is- or, I mean-"
    mc "(I stammer out an attempt at a response before going quiet.)"
    mc "I’m sorry."
    mc "(Goopitha pauses for a moment before unveiling her face, still bright with embarrassment.)"
    g "No, it’s my bad. I did- I didn’t realize I was that close."
    g "I, uh. I’m just gonna, I’m gonna go now."
    mc "Yeah."
    g "Uh, bye. I guess."
    hide goopitha embarrassed
    with easeoutleft
    mc "(Goopitha exits the awkward situation, leaving me alone, blushing like crazy.)"
    mc "(I continue to stay seated for a few minutes, contemplating what just happened.)"
    mc "(I sigh for a fifth time in a minute before I finally decide to get up and get back to work. I’m still covered in slime.)"
    scene bg cubicle1
    with fade
    mc "(I try my best to speed walk through the office, hoping that no one questions my slime-stained outfit. It’s dried somewhat, but my shirt is ever so slightly green in some spots)"
    mc "(I finally reach the department, ready to spend the rest of my work day filling out paperwork.)"
    mc "(There’s something different about my cubicle though. More specifically, there’s someone sitting at it.)"
    show pelota neutral at right
    with dissolve
    mc "(There’s a young woman at my desk, kicking her feet up and leaning back on the chair. Her hat is pulled over her eyes so I can’t tell if she’s asleep or not. I doubt it's possible to sleep the way she's oriented.)"
    mc "(Do I move her out of the way? The cubicles next to her are open and I could just work there. But her legs are on top of all my papers, and I don’t want to redo so many of them.)"
    mc "(I reach towards the few papers that are free. It’s not a lot of work, but hopefully she wakes up before I finish these so I can do the rest.)"
    mc "(Suddenly, the woman twitches. She tries to get up, but nearly falls over. Miraculously, she manages to catch herself before she hits the ground, but she seems dazed.)"
    show pelota anger at center
    with ease
    "Woman" "What the fuck?"
    mc "(She rubs her eyes and looks up at me before getting back up on her feet.)"
    show pelota mad
    "Woman" "What do you want?"
    mc "(She seems slightly flustered by what just happened, but she does her best to hide it.)"
    "Woman" "Who do you think you are, waking me up from my sleep?"
    mc "(She picks up a baseball bat from underneath the desk and menacingly slings it over her shoulder.)"
    mc "Sorry, I was just trying to get my papers."
    mc "(I try to de-escalate the situation carefully so I don’t get whacked in the head.)"
    show pelota neutral
    "Woman" "Hm?"
    mc "(I point at the stack of papers on the desk that she was using as a footrest.)"
    mc "(She picks one up and skims through it.)"
    "Woman" "Hm."
    show pelota smile
    "Woman" "Oh, are you another Charitable Urgency Manager? I haven’t seen someone else here in ages."
    show pelota neutral
    "Woman" "Looks like all you’re doing is paperwork though. That’s lame."
    mc "(She sits back down at my chair but doesn’t kick her feet back up, leaving me free to take the papers and move to the next cubicle.)"
    mc "(I try to gather up all the papers on my desk, but there’s way too many for me to carry in one go. I grab the blank forms and a few pens.)"
    "Woman" "Hm? What’s on your clothes?"
    mc "(Oh shoot, my clothes! They’re still covered in slime!)"
    mc "(I step away from the desk, trying to prevent her from getting a good look at my clothes.)"
    show pelota mad
    "Woman" "Hey, why do you have Goopitha’s slime stuck to your suit?"
    mc "What? Goopitha? Who’s that?"
    mc "(I try to lie my way out of the situation.)"
    "Woman" "Don’t lie to me, I’d recognize that slime anywhere. How’d it get on your shirt?"
    mc "(She stares into my eyes, demanding an answer. I want to look away, but something about her look freezes me in place.)"
    mc "(I don’t want to tell her. It’s way too embarrassing. She probably knows Goopitha too, so I doubt she’d be very happy if I told her.)"
    mc "(...)"
    mc "(Finally, she sighs.)"
    show pelota neutral
    "Woman" "Whatever. I’ll beat an answer out of you. The name’s Pelota. You better remember that."
    with fade
    #Sudoku transition
    $ pelotaPoints += 1
    #May or may not keep this, check later
    p "That’s a wrap. You win."
    mc "(Huh?)"
    mc "(I’m lying on the ground right now, trying to catch my breath after getting beat so hard. But I guess this is what victory looks like?)"
    show pelota smile
    p "I’m sure whatever happened to you this morning isn’t my problem. My bad."
    mc "(She picks me up off the ground and sits me down at the cubicle. I can’t stand up, but I feel like I can remain balanced while sitting at least.)"
    mc "(She uncaps a bottle of water and brings it to my lips.)"
    p "Drink up."
    mc "(I slowly sip the bottle as I recover my strength.)"
    show pelota neutral
    mc "(Now she’s just awkwardly staring at me. Her eyes aren’t as penetrating as they were a few minutes ago, but they’re still quite intimidating. Eventually, I’m back in shape and ready to move about.)"
    mc "(I guess I’ll just do my work now. The papers I grabbed earlier are scattered across the desk, so I’ll have to sort them first.)"
    mc "(What a day. And it’s not even lunch break yet.)"
    scene bg cubicle
    with fade
    mc "(Finally, the clock hits 5PM. I get up and stretch my arms out.)"
    mc "(Looks like Pelota never came back from lunch break. Well, she didn't seem like she wanted to stay.)"
    mc "(I gather up my things, head to the lobby, and wave goodbye to Sigma.)"
    scene bg duskalley
    with dissolve
    mc "(What should I eat tonight?)"
    mc "(As I step outside, a voice comes from behind me.)"
    g "Oh, hey [name]!"
    show goopitha happy 1
    with dissolve
    mc "(I turn around to greet the cheery slime girl following me. She seems to have wiped today's event from her mind with how carefree acts.)"
    mc "Hey Goopitha."
    g "How was your day today?"
    mc "(I'll play along.)"
    mc "Pretty good. I met this girl called Pelota, and she was pretty cool."
    g "Oh, you met Pelota? Yeah, she's pretty cool."
    jump day3part2

label day3part2:
    g "Anyways, do you have any plans for dinner today?"
    mc "Not particularly. I was just gonna finish some of the instant ramen I have."
    show goopitha pout
    mc "(She looks quite unhappy.)"
    g "That’s not good for you! You need to eat proper meals, not just ramen. It’s fine to have these sorts of things every once in a while, but you shouldn’t eat them for a meal!"
    mc "I don’t really have anything else to eat though."
    g "Why not? Don’t you at least buy groceries?"
    mc "Yeah, about that…"
    mc "(I don’t want to tell her that I’m broke. I feel like I’d be forcing her to give me money.)"
    show goopitha happy 2
    g "Oh! I have an idea! What if I cooked your meals for you? You wouldn’t need to worry about the ingredients, I have plenty!"
    mc "(Hm, that does sound very appealing.)"
    menu:
        "Sure":
            jump goopithaCook
            $ goopithaPoints += 1
        "No":
            jump noCook
label goopithaCook:
    mc "That sounds great."
    mc "(Her smile grows even larger as she hears my words.)"
    g "Great! I’ll cook you dinner today!"
    show goopitha neutral
    g "I need to stop by the grocery store first though. You live in the company apartments, right? There should be a store on the way back from here."
    hide goopitha neutral
    with easeoutleft
    mc "(Goopitha zooms ahead of me, clearly excited because she gets to cook. I wonder what she’ll make for me.)"
    show bg konbini
    show goopitha happy 1
    with dissolve
    mc "(Once we get to the grocery store, she grabs some vegetables, rice, and a box of curry roux. It’s not very expensive, but Goopitha insists on paying for it.)"
    g "Cooking is my hobby. You shouldn’t have to pay for it if I’m the one who’s doing the cooking."
    mc "(Once we have the ingredients, we head back to my house.)"
    show bg outside
    with fade
    mc "(308, 308, 308.)"
    show bg kitchen
    with dissolve
    mc "(I reach the door and unlock it. The door opens, revealing my lightly furnished apartment. Goopitha immediately heads over to the kitchen area.)"
    g "Wow, so this is where you live. It’s quite cozy."
    mc "(That’s a nice way of describing it. It looks like she’s making a quick curry rice, which is fine by me. It’s better than anything I could do, and it’s probably better than the frozen food and ramen.)"
    show goopitha happy 1
    g "Okay, I’ll be done in about half an hour. You can watch if you want."
    mc "(I want to watch. It’d probably be a good learning experience.)"
    mc "I’ll watch."
    show goopitha happy 2
    g "Great! Here, I’ll teach you how it’s done."
    show goopitha cooking
    g "ALright, first you want to cut all of your vegetables." 
    mc "(She grabs the knife and blazes through the carrots, potatoes, and onions. The previously round shapes become a pile of evenly sized vegetable chunks.)"
    g "Saute the onions until golden."
    mc "(She slides the onions into a pot with a squirt of oil. It takes a while, but the onions eventually turn a nice yellow color.)"
    g "Mmmmm. Beautiful."
    show goopitha happy 1
    g "Oh yeah, we need the rice."
    mc "(She gestures at the small packet of rice, vacuum-sealed into a hard brick.)"
    show goopitha cooking
    g "Wash that in a pot to get rid of the excess starch."
    mc "All of it?"
    g "All of it."
    mc "(I pour the dry rice into a spare pot and run water over it. I swirl it around with my fingers, which turns the water opaque.)"
    mc "(I wash it a few more times until the water runs clear.)"
    mc "It’s washed."
    show goopitha happy 2
    g "Perfect!"
    show goopitha cooking
    g "Fill the pot with some water and just put it on the stove."
    mc "(I follow her instructions and after I set it down on the burner she turns the fire up.)"
    mc "(I peer into the pot with the onions. It looks like she’s added water and the rest of the vegetables.)"
    show goopitha happy 1
    g "It needs to simmer for a while. Let’s do something else in the meantime."
    show bg livingroom
    with dissolve
    mc "We should..."
    menu:
        "Watch TV":
            mc "Let’s watch TV."
            g "Ooh, what shows are on right now?"
            mc "Let’s see."
            mc "(I turn on the TV and surf through the channels with Goopitha. I don’t think there’s anything terribly interesting, but every once in a while Goopitha stops me when she sees something she likes.)"
        "Talk":
            mc "Let’s talk."
            mc "So, how was your day today?"
            g "Pretty good actually. You met Pelota today, right? I heard her talk about you. Nothing bad, don’t worry. But the story of how I met her was actually really cool. Back when I first started work…"
            mc "(She talks about her life for quite a bit. I don’t want to interrupt her.)"
    with fade

    g "Alright, the vegetables should be done now."
    mc "(I turn off the TV and head over to the kitchen area with her.)"
    show bg kitchen
    with dissolve
    mc "(She adds the box of curry roux to the pot and stirs it.)"
    show goopitha cooking
    g "We need to simmer it again, but it should take less time now."
    mc "(I can see the TV from here, so I turn it back on. The two of us continue to watch as Goopitha stirs the pot every so often.)"
    mc "(Finally, the curry is done.)"
    mc "(Goopitha uses a spoon to taste for seasoning.)"
    g "Mmm. Delicious." 
    show goopitha neutral
    mc "Goopitha turns off the heat and pulls out two plates. She places a hearty scoop of rice onto them before covering half of the plate with the curry.)"
    mc "(It looks and smells incredible. I had no idea that food could be this good.)"
    mc "(Goopitha takes our plates over to the dining table and finally we can eat.)"
    mc "(I scoop up a small bit of the curry, making sure that some rice is underneath. I can feel the heat radiating from the curry before I even touch it. I sniff it again, taking in the wonderful scents of the spices before thrusting the spoon into my mouth.)"
    mc "(It tastes beyond incredible. The spices warm me up, like an invisible blanket.)"
    mc "(I dig into the curry, making sure to get every last grain of rice.)"
    show goopitha happy 1
    g "Wow, you certainly seem to be enjoying it."
    mc "(I look up at Goopitha. She’s smiling as she watches me eat.)"
    mc "It tastes amazing. Thank you so much, Goopitha."
    show goopitha smug
    g "Hehe. No problem. It’s been so long since I’ve seen that smile. I’d cook as many curries as you want if it means you would keep on smiling."
    mc "(I can feel my body warming up even more. Her voice calms my body, yet her words get me fired up. It’s a hypnotizing combination, and I can feel my heart beating faster.)"
    mc "Uh, thanks."
    show goopitha happy 1
    mc "(She continues to watch me as I finish the meal. It fills me up completely.)"
    mc "Damn, that was delicious."
    g "You can freeze the rest if you want. It’s quite a bit and it lasts long when frozen."
    mc "Thank you so much Goopitha. I don’t know what I’d do without you."
    g "No problem. I’m always here for you. Just give me a call."
    mc "(She cleans up the kitchen and places the dishes and pots into the dishwasher.)"
    show bg livingroom
    show goopitha happy 2
    with dissolve
    g "Alright then. See you tomorrow."
    mc "See you."
    hide goopitha happy 2
    with dissolve
    mc "(I close the door behind her and lock it.)"
    mc "(It’s already quite late in the evening, so I’ll just go to sleep now. I toss my clothes into the washer to get rid of the slime stains. Oh yeah, about the slime. I wonder if Goopitha noticed, or if it’s just something that happens normally.)"
    show bg bedroom
    with dissolve
    mc "(I put on my pajamas and get into bed. I fall asleep quickly since my stomach is filled with good food.)"
    jump day4
label noCook:
    mc "No, I’ll just eat whatever I have in my house."
    show goopitha angry
    mc "(Goopitha looks bothered by my words.)"
    g "That’s not healthy for you. You can’t just eat whatever. You need nutrition to keep your body running, y’know?"
    mc "I’ll be fine. Don’t worry about me."
    show goopitha sad
    g "Are you sure? I don’t feel comfortable with you eating like this, but if you insist..."
    mc "(She looks saddened by my choices, but in the end she leaves me be.)"
    show goopitha happy 1
    g "Alright then. See you!"
    mc "Bye."
    mc "(We wave goodbye to each other and part ways. I head back to my home.)"
    show bg kitchen
    with fade
    mc "(What should I eat for dinner?)"
    mc "(I think I still have a frozen pizza in the freezer. I’ll just toss that in the oven.)"
    mc "(The pizza cooks up quickly and I transfer it to a large plate.)"
    mc "(I’ll watch some TV while I’m eating.)"
    show bg livingroom
    with dissolve
    mc "(I turn on the TV and get comfortable in the armchair. There’s not much on the channels, but it passes the time.)"
    with fade
    mc "(I finish the last slice of pizza and yawn. It’s almost time for me to go to sleep. I should check the weather first though.)"
    mc "(I try to swap the channels, but the TV doesn’t respond. I doubt the remote is out of batteries since I’ve only used it for a few days. I press the buttons again. Nothing happens.)"
    mc "(Suddenly, the TV flashes red for a few seconds before it turns off.)"
    menu:
        "Turn it back on":
            mc "(I press the red power button and turn the TV back on. There doesn’t seem to be anything wrong with the device. I guess the power must’ve cut or something. I check the weather channel for anything interesting.)"
            mc "(Looks like it’s just a normal day tomorrow. I shut off the TV and prepare for bed.)"
        "Leave it":
            $ tvheadPoints += 1
            mc "(I decide to leave the TV. Surely the weather can’t be that different from today’s weather, right.)"
            mc "(I put my slime covered clothes into the washer and put on my pajamas.)"
            mc "(I get into bed and fall asleep.)"
    jump day4