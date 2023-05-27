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
    mc "(The sun is just beginning to set. The sky is a )"
    mc "(Have I really been playing with this slime for that long?)"
    mc "(I should probably do something else.)"
    mc "(I look longingly at the slime before turning away.)"
    mc "(Sorry, but I need to touch some grass.)"
    mc "(I'll just leave it here. I won't be out for long.)"
    show bg alley dusk
    with fade
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
    mc "(I should kick myself off the ground...)"
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
    g "Do you remember?"
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
    hide goopitah surprised
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
    mc "(I think about Goopitha for a while before I head home to sleep.)"
    jump day7

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
    g "So, do you remember me?"
    mc "I don't."
    show goopitha sad
    g "..."
    mc "(She looks like she's about to cry.)"
    g "I..."
    hide goopitha sad
    with dissolve
    mc "(She leaves without another word.)"
    mc "(Mission successful, I guess?)"
    mc "(I don't really know how to feel about that.)"
    mc "(I spend a few more minutes at the park before heading home to sleep.)"
    jump day7
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
    mc "(I spend a few more minutes at the park, thinking about what Goopitha said, before heading back home to sleep.)"
    jump day7

label lldWalk: