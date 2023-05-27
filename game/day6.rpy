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
    