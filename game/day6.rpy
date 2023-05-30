label day6:
    show bg livingroom
    with fade
    mc "(Is it already noon?)"
    mc "(I look out my curtains and sure enough, the sun is high up in the sky.)"
    mc "(At least it's Sunday. I didn't have any plans for today.)"
    mc "*sigh*"
    mc "(What should I do today...)"
    show bg kitchen
    with dissolve
    mc "(Is that slime on the table?)"
    show goopitha slime
    with dissolve
    mc "(It looks almost identical to Goopitha's slime.)"
    mc "(It might be an offshoot or something. It's moving slightly.)"
    mc "(It's pretty cute. Is it even safe for me to have it, though?)"
    mc "(I don't know what it could do. It might even try to attack me or something for taking it away from Goopitha.)"
    mc "(But at the same time... it looks really squishy.)"
    menu:
        "Keep it":
            $ goopithaPoints += 1
            jump goopithaSlime
        "Give it to Goopitha":
            $ lldPoints += 1
            jump lldWalk

label goopithaSlime:
    mc "(I'll keep it with me.)"
    mc "(It's way too cute to leave be.)"
    mc "(I press my finger into it.)"
    mc "(It's quite cold, but my finger passes through it with little resistance.)"
    mc "(I cup it with my hands and lift it into the air.)"
    mc "(This is pretty fun.)"
    with fade
    mc "(Wow, is it evening already?)"
    mc "(The sun is just beginning to set. The sky is slowly becoming a beautiful mosaic of light and clouds.)"
    mc "(Have I really been playing with this slime for that long?)"
    mc "(I should probably do something else.)"
    mc "(I look longingly at the slime before turning away.)"
    mc "(Sorry, but I need to touch some grass.)"
    mc "(I'll just leave it here. I won't be out for long.)"
    scene bg alley dusk
    with fade
    mc "(It's pretty quiet at this time of the evening. It gives me time to think about life.)"
    mc "(It's been almost a week since my life has changed, hasn't it.)"
    mc "(So much has happened that I can't really believe that. Was my life this chaotic before I lost my memories?)"
    mc "(So many new people and things have been thrown into my life. It's hard to keep track of it all.)"
    mc "(Without all of them around, it feels really quiet. But to be honest, that's what I need right now.)"
    show bg park dusk
    with dissolve
    mc "(Didn't know there was a park here.)"
    mc "(It's a Sunday evening, so not many people are here. I look around the park until I eventually sit down at a childrens' playground.)"
    mc "(The air here is so nice. It feels like I'm breathing in the night itself.)"
    mc "(I don't remember my childhood, but it shouldn't be too hard to use the playground structures. I mean, they're meant for a kid to use.)"
    mc "(Let's start with the swings.)"
    mc "(I need to kick myself off the ground...)"
    mc "(...)"
    mc "(Wow, this is pretty fun. I think I can go higher.)"
    mc "(...)"
    mc "Hah!"
    mc "(I jump off the swing at the peak of its height, catapulting myself towards the seesaw.)"
    "Voice" "Woah there."
    show goopitha neutral
    with dissolve
    #This section is kinda wack
    g "That's dangerous."
    mc "Hello, Goopitha. Funny seeing you here."
    g "I could say the same. I've never seen you here before."
    mc "Oh yeah, I just found this place. It's pretty cool."
    g "Isn't this the most popular park in the city though?"
    mc "(Oh crap.)"
    mc "Oh, is it? Hahah, I've never been here. I really need to know the city more."
    g "Haven't you been living here most of your life though?"
    mc "(Fuck.)"
    mc "I, uh, I. I don't really go outside that much."
    mc "(My reputation can tank this, I just can't let her find out.)"
    g "Hmmmm. If you say so."
    show goopitha happy 2
    g "Oh well. It's quite nice here, isn't it."
    g "It's calm and quiet. No one's around to bother us."
    g "Don't you think it's great?"
    mc "Yep, uh-huh."
    mc "(I think she bought it.)"
    show goopitha happy 1
    g "At times like this, I'm glad I met you."
    g "Do you still remember? The first time we met?"
    g "It was a long, long time ago."
    g "Come walk with me."
    mc "(I don't think I'm out of the woods yet.)"
    show goopitha yandere 1
    with fade
    g "Do you remember the swings?"
    g "You were on the blue one, the one with the rope."
    g "You had been there for an hour at least. I was there too."
    g "I was much more shy back then. I didn't approach you. I only watched."
    g "But I was looking at you. You got so excited when you found out you could jump off. You were doing it over and over and over."
    g "You went so high into the air, it was like you could fly."
    g "It didn't look safe. Not one bit. But none of the adults were watching."
    g "They were too busy talking to each other to watch their kids."
    g "What bad parents. But I supposed I can't fault them too much."
    g "After all, they let me meet you for the first time."
    g "It was the fifth time you jumped off the swings. You landed perfectly, and climbed back on for another jump."
    g "But this time, it wasn't the same. Maybe you had gotten tired from jumping so much, maybe your hands got blistered from the ropes."
    g "This time, when you tried to jump off, it didn't go so well."
    g "You didn't land on the ground, but instead onto a young girl."
    g "She was so surprised, with you landing onto her out of nowhere."
    pause(1.5)
    g "Do you remember? That girl?"
    mc "I-"
    g "Sorry, I got nostalgic for a second, seeing this place again."
    g "But that girl, she caught you back then."
    g "And now, she caught you again."
    if goopithaPoints > lldPoints and goopithaPoints > pelotaPoints and goopithaPoints > jjPoints and goopithaPoints > sigmaPoints and goopithaPoints > tvheadPoints:
        jump goopNormal
    else:
        jump goopYandere

label goopNormal:
    $ goopKnows = False
    mc "(She grabs onto me and squeezes around my chest.)"
    show goopitha sad at center:
        ease 0.25 zoom 1.0 xoffset 0 yoffset 300
    g "I've missed you so much!!!"
    g "It's been so long since I've seen you!!"
    g "And- *sniff* and when you left for college, I-"
    g "I cried so much!!!!"
    mc "(She rubs her face against me and cries into my shirt.)"
    mc "(I gently pat her head as she cries her sorrows out.)"
    g "*sniff*"
    g "Hah,"
    g "..."
    show goopitha neutral
    g "Thank you."
    show goopitha neutral:
        ease 1.5 zoom 1.0 xoffset 0 yoffset -300
    g "*sniff*"
    show goopitha surprised
    g "Ah!"
    g "Sorry, sorry, sorry, sorry, sorry!"
    hide goopitha surprised
    with dissolve
    g "Uuuuuuuuuuuuuuuuuuuuuuuuuu."
    #It's fauning time
    g "{size=-10}I shouldn't have done that...{/size}"
    show goopitha embarrassed at right
    with dissolve
    g "Please don't mention this to anyone."
    g "I'll... get going."
    hide goopitha
    with dissolve
    mc "(...huh.)"
    jump day6dream

label goopYandere:
    g "You seem different now, [name]."
    g "You got taller. You look different now. Your voice changed."
    show goopitha yandere 1
    g "But I didn't think your scent would have changed too."
    g "I marked you back then, [name], so you wouldn't get away."
    g "You should smell the same now, [name]."
    g "It was a mark made with love. It shouldn't go away."
    show goopitha yandere 3
    g "So why do you smell different now, [name]?"
    g "Do you love someone else, [name]?"
    mc "..."
    menu:
        "Tell her":
            $ goopKnows = True
            jump goopKnows
        "Don't tell her":
            $ goopKnows = False
            jump goopNoKnow

label goopKnows:
    show goopitha neutral
    g "I figured that was the case."
    mc "No, that- that's not what I meant."
    mc "I've..."
    mc "(No going back.)"
    mc "I've lost my memories."
    mc "I got into an accident and got permanent amnesia."
    mc "I've only recovered a week ago."
    g "... I see."
    mc "I'm sor-"
    g "So, do you remember me?"
    mc "...I don't."
    show goopitha sad
    g "..."
    mc "(She looks like she's about to cry.)"
    g "I..."
    hide goopitha sad
    with dissolve
    mc "(She leaves without another word.)"
    mc "(Mission successful, I guess?)"
    mc "(I don't really know how to feel about that.)"
    mc "(...)"
    jump day6dream
label goopNoKnow:
    show goopitha neutral
    g "I figured that was the case."
    show goopitha yandere 3
    g "Why, why do you love someone else?!!?"
    g "I love you, I've always loved you, from the bottom of my heart!"
    g "Ever since that day our fates crossed, my eyes have always been set on you!"
    g "*hah*"
    show goopitha yandere 4
    g "Every single day, I would go back to that park, hoping that I would see you again."
    g "Day, night, rain, hail. No matter what, I would go there, every day."
    g "I've worked so hard, just for you. I've done some much for you."
    show goopitha yandere 3
    g "Why have you betrayed me?!?!"
    g "I-I'll."
    g "I..."
    show goopitha sad
    mc "(She looks like she's about to cry.)"
    hide goopitha sad
    with dissolve
    mc "(Goopitha leaves without another word.)"
    mc "(...)"
    jump day6dream

label lldWalk:
    mc "(I'll give it to Goopitha tomorrow. It's not my responsibility.)"
    mc "(In the meantime, I'll just go for a walk.)"
    mc "(I don't think it'll go anywhere, so I'll just leave it in my room for now.)"
    scene bg alley day
    with fade
    mc "(Where should I go today...)"
    mc "(I'll just walk around for a bit.)"
    mc "(I should probably familiarize myself with the city.)"
    with fade
    mc "(There's a park here. That's cool.)"
    scene bg park day
    with dissolve
    mc "(Not that many people here though. I guess it is a Sunday morning.)"
    mc "(Oh, there's a playground here.)"
    mc "(I guess I'll play on the swings.)"
    mc "(While my anxiety tells me that being an adult and playing on swings is bound to attract attention, I'm too bored to be embarrassed.)"
    mc "(I just need to sit here, and kick off the ground, right.)"
    pause(1.5)
    mc "(This isn't that difficult. In fact, it's pretty fun, swinging around like I don't have weight.)"
    mc "(I play on the swings for a few more minutes before stopping.)"
    mc "(Let's see what else there is to play with...)"
    "Voice" "Hold on, you dropped something."
    mc "(Hm?)"
    show lld normal
    with dissolve
    mc "What the-"
    "Dolphin Man" "Your taxes."
    "Dolphin Man" "They are due."
    pause(1.5)
    mc "(I quickly look around, hoping that Sigma or Pelota is somehow at the park to save me.)"
    "Dolphin Man" "It's a Sunday morning, no one is around."
    "Dolphin Man" "No one will be able to hear you scream."
    scene bg alley day
    with CropMove(0.1, mode="slideleft")
    mc "(I am not sticking around.)"
    mc "(What's the fastest way I can lose him...)"
    mc "(To the left!)"
    "Hold on, I'm not done talking."
    mc "(???)"
    show lld normal
    with CropMove(0.5, mode="wiperight")
    "Dolphin Man" "This is just a reminder."
    "Dolphin Man" "What are you worried about?"
    mc "(... It's hopeless.)"
    mc "(My knell has been knolled.)"
    mc "(All I can do is wait for my death.)"
    scene black
    with fade
    "Dolphin Man" "Get up, young one."
    "Dolphin Man" "Your time is not over yet."
    scene bg alley day
    show lld normal
    with fade
    "Dolphin Man" "Rejoice."
    "Dolphin Man" "Salvation looks upon you and smiles. There is nothing to fear."
    pause(1.5)
    show lld happy
    "Dolphin Man" "Pfffffff."
    "Dolphin Man" "What is your face?"
    "Dolphin Man" "What kind of reaction is that?"
    mc "(Huh?)"
    "Dolphin Man" "Hm?"
    pause(1.5)
    show lld normal
    "Dolphin Man" "Okay, I may have convoluted things by saying that, whoops."
    "Dolphin Man" "Alright, let's start from the beginning."
    "Dolphin Man" "I work for a tax collection company. You have not paid your taxes yet, and as a result we send an agent to collect it."
    l "That agent is me, the Lone Loan Dolphin."
    l "Nice to meet you."
    mc "Nice... to meet you."
    mc "(I cautiously shake the dolphin man's hand, wary of any signs of danger.)"
    mc "(His grip is incredibly firm. )"
    show lld happy
    l "Anywho, about your taxes."
    mc "(Not this again...)"
    show lld normal
    l "According to my records, your taxes are overdue by about..."
    l "2 years."
    l "Now, normally, this is what we tax collectors call an \"uh-oh no good irresponsible moment\"."
    l "But, your case is kinda special."
    l "A few checks with other government agencies tells us that you haven't been doing anything for the past 2 years."
    l "You didn't spend money, didn't earn money, didn't pay back your student loans."
    l "That's pretty weird. I don't believe you're an immortal who doesn't need to eat, so something must've happened in those 2 years."
    l "I'm not sure what, though, so you're gonna have to come down to the IRS headquarters for some questioning."
    l "Don't worry, it's not gonna be anything bad. Probably."
    l "At the very least, you can get some pretzels for your time."
    mc "(Free pretzels, great.)"
    mc "Do I have to go to th-"
    l "Aight, let's get moving."
    hide lld
    with CropMove(0.5, mode="wiperight")
    mc "(...)"
    mc "(Would he notice if I just left?)"
    scene bg apartment outside
    with dissolve
    mc "(That was easier than I thought. Did he not even bother to check behind him?)"
    mc "(Anyways, I don't think I'm safe here. He has my address, after all.)"
    l "Hey, don't leave me behind like that."
    mc "!!!"
    show lld normal
    with dissolve
    l "You know how annoying it is to walk around in a suit all day?"
    l "Hmph."
    show lld comb
    l "My hair was blown out of place. I spend most of my morning on this, y'know?"
    mc "(Ignoring that he has no hair, the fact that he managed to follow me without make a single sound is terrifying.)"
    mc "(I even looked behind my shoulder a dozen times to make sure he wasn't behind me. Either he's just that fast or just that elusive.)"
    show lld sparkle
    with dissolve
    mc "(Did he get even brighter?)"
    show lld normal
    l "Alright, it should be fine now, I think."
    l "Anyways, why did you not follow me?"
    show lld happy
    l "I promise, the IRS is not going to do anything bad to you."
    l "We're just trying to find out what happened, okay?"
    mc "(I don't trust that one bit.)"
    show lld
    l "Please?"
    mc "(...)"
    mc "Fine."
    show lld happy
    pause(1.5)
    scene bg alley day
    show lld normal
    with fade
    mc "(How far away is the IRS headquarters? We've been walking for like 20 minutes.)"
    l "*growl*"
    show lld flushed
    pause(1.0)
    show lld bruh
    l "Shall we get something to eat?"
    mc "Why not."
    show lld normal
    l "*ahem*"
    l "There should be a good seafood restaurant near here."
    mc "(Is he not a fish?)"
    mc "You eat seafood?"
    l "Well, yeah. I'm a dolphin. What else would I eat?"
    mc "(Y'know what, that makes sense. In fact, it would be weird for him not to eat fish.)"
    #Maybe replace this but it sort of fits well
    scene bg burger
    with fade
    mc "(Isn't this just the burger place Sigma likes.)"
    mc "(Well, they serve salmon burgers so technically it's a seafood restaurant.)"
    mc "(I had \"sushi restaurant\" more in mind though when he talked about seafood.)"
    show lld happy
    with dissolve
    l "Ready to order yet?"
    mc "Yeah."
    l "Aight."
    show lld normal
    with fade
    l "Mmm. This is pretty good."
    mc "(He bites into the salmon burger, taking out triangle-shaped chunks as he goes.)"
    l "So... what have you been up to these past 2 years?"
    mc "(Well I've been in a coma, so I don't really know.)"
    l "Like I said, no one's heard of you even a single bit for 2 years. The IRS has been sending out agents to try to find you, but no dice."
    l "Not until we got notice that you got employed to work at..."
    l "\"DEEZ Corp\"?"
    show lld happy
    l "What, is this a prank?"
    l "Haha, you've been gone for 2 years just for a de-"
    show lld bruh
    l "{size=-10}No, okay, it's the actual name of the company. Are you serious?{/size}"
    l "Oh, it's an abbreviation."
    show lld normal
    l "Well, I learned something new today. What even is this company?"
    mc "It's like a disease extermination group, I think?"
    mc "I don't really know myself."
    l "Well, what do you do at work?"
    mc "I work as a Charitable Urgency Manager and fill out paperwork and stuff."
    show lld happy
    l "You work as a what?"
    mc "As a CU-"
    show lld normal
    #This entire section is just an info dump, change later i guess
    l "Y'know what, let's move on."
    l "It's pretty weird that you've just started to work now."
    l "I mean, you haven't spent a single cent during those 2 years, so why would you need to start working now?"
    l "As a matter of fact, how did you even survive without spending any money? No way you just started living off the land or something. We live in an urban city."
    mc "Well..."
    mc "(Honestly, I don't think I could hide this from him. Plus, if I'm caught lying I might make it worse.)"
    mc "(But then again, I've already evaded taxes for 2 years. It might not get worse than this.)"
    mc "(...)"
    mc "(Probably won't hurt to tell him this. It's not like he's a close friend of mine.)"
    mc "So, those past 2 years."
    mc "I was in a coma."
    l "Uh-huh."
    mc "Cause I got hit by a car."
    l "Mhm."
    mc "And I lost my memories and stuff."
    l "I see."
    mc "(He's doesn't seem to be a good listener.)"
    l "How did you pay the medical bill though?"
    mc "This random dude just paid it off for me."
    l "Some random dude?"
    mc "Yeah, he was wearing a suit and whatnot."
    mc "Looked pretty important."
    l "Do you know who he was? Like, at all?"
    mc "No clue."
    l "What'd he tell you?"
    mc "Something about how I should work for DEEZ Corp or something."
    l "Just like that?"
    mc "He kinda like forced it onto me."
    mc "He even gave me an apartment and stuff. It was pretty generous."
    l "That sounds..."
    pause(1.0)
    l "Hm. Something seems off."
    l "Whatever. Anyways, I'm leaving. You don't need to go to the IRS headquarters anymore."
    l "I'll deal with this."
    hide lld
    with dissolve
    mc "(That doesn't sound good.)"
    mc "(I don't think the IRS is gonna come after me anymore.)"
    mc "(Though I might have awakened a whole new beast.)"
    jump day6dream