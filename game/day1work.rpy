label day1work:
    scene bg outside
    with squares
    mc "(The building is in sight now. That only took around 20 minutes, I think.)"
    "The MC is outside of the DEEZ Corp building."
    mc "(What a tall building. It's the tallest one on the block.)"
    mc "(No one's walking into the building. I'm getting a bit nervous.)"
    mc "(Am I in the right place? I check the map again, certain that I read it wrong, yet every street marker and building tells me that I'm at the correct location.)"
    mc "(I should be more confident. No one would walk into an office building if they don't work there, right? I'm one of the few people who has the right to go in.)"
    mc "(I adjust my already correctly adjusted tie and step through the automatic doors.)"
    mc "(My face is hit by a light sweep of air conditioning. It's a comfortable feeling for an office building, but it's already cold outside.)"
    scene bg dayfrontdesk 
    with dissolve 
    mc "(Right in front of the entrance is a medium-sized desk. There's a woman sitting at the desk, typing on her computer.)"
    show sigma glasses at center 
    with dissolve
    mc "(Even though she's looking down, I can tell that she's beautiful. Both her clothes and her hair are very finely kept.)"
    mc "(I adjust my tie again and walk up to the front desk.)"
    mc "H-Hello."
    "The woman at the desk" "..."
    mc "(Did she hear me?)"
    mc "(I sit in silence while the woman types on her computer for a few more seconds.)"
    mc "(She finally looks up at me, but she looks back to her screen.)"
    show cg sigma desk
    with Dissolve(1.0)
    mc "(Wow, she's even prettier close up. Her eyes are nice. At least a 10, maybe even an 11.)"
    mc "(After a few more seconds, she stops typing and leans back to look at me.)"
    "Woman" "How may I help you?"
    mc "I recently got hired to work here. "
    "Woman" "Mhm."
    mc "(She carefully studies my clothes, as if she's scanning for every single imperfection in my outfit.)"
    mc "(I think I see the slightest bit of a frown appear on her face, but it's so slight that I can't tell if I was just seeing things.)"
    mc "(Her antennae twitch before she finally breaks the silence.)"
    "Woman" "Welcome to the company. I'm Sigma."
    s "I'll give you a tour."
    hide cg sigma desk
    with Dissolve(1.0)
    show sigma glasses at right 
    with move
    mc "(She gets up from her chair and walks around the desk area.)"
    s "Follow me."
    hide sigma glasses 
    with moveoutright
    mc "(She turns around on her heels and walks away at a rapid pace.)"
    mc "(I have to run to catch up with her.)"
    scene bg office 
    show sigma glasses at center 
    with dissolve 
    s "If you're the same [name] as the files tell me, you're working as a Charitable Urgency Manager. If there's a disease that someone needs handling, it's your job to suit their needs and help them."
    s "Work starts at 9 am sharp every weekday, but sometimes you might get called in on the weekends."
    s "You don't need to follow the dress code every day, by the way. I would like it if you wore a suit every day, but the quality managers only check once a month."
    scene bg cubicle1
    show sigma glasses at center 
    with dissolve 
    mc "(Finally, Sigma pauses in front of a department layered with cubicles.)"
    s "Charitable Urgency Managers are grouped in with the Disease Management section. Most of these guys deal with the paperwork though. You should probably make as many friends with them as possible."
    mc "(She walks around the lines of cubicles until she finds one without a name labeled on the chair.)"
    s "This one will be yours. You can put your personal belongings underneath your desk, but be careful not to let them move outside of your designated area."
    show sigma glasses at left
    with ease
    mc "(Sigma starts to walk away before she suddenly stops.)" # do some transition stuff here? either fade her out for a sec or have her move out and move back
    show sigma glasses at center 
    with move 
    s "Oh, I forgot to mention. You'll get an hour break at 12 for lunch and other stuff, but you can also take a 5-minute break whenever you want. You only get two per workday, though. Don't waste them."
    mc "(Sigma gestures for me to follow her before she walks toward the back of the department.)"
    scene bg cooler
    with dissolve 
    s "Here is the break corner."
    hide sigma glasses 
    mc "(There's a small coffee machine on the desk and a water cooler right next to it.)"
    mc "(I reach for a paper cup, but I suddenly bump into another person doing the same thing.)"
    show joejoe surprised at center
    with zoomin
    mc "Oh, sorry."
    "Other guy" "Sorry."
    show joejoe neutral at center 
    mc "(I let him take the cup first since he was there first.)"
    mc "(But he does the same thing, for some reason. I'll accept his act of kindness.)"
    mc "(I reach for the cup again, but he does the same. Our hands bump into each other.)"
    mc "(I look up at this strange man who mirrors my every action.)"
    mc "(Have I seen this guy before?)"
    mc "(Wasn't he one of the people I passed on the way here? Or was he the guy back at the cubicle?)"
    "Incredibly average man" "I'll go ahead."
    mc "(He grabs a paper cup while I'm trying to remember who he is, and fills it up silently.)"
    show sigma glasses at left
    with moveinleft
    s "That's Joe Joe, one of your co-workers. I honestly can't remember when he got here, or what he does, but he frequents the water cooler every break."
    mc "(Joe Joe downs his water cup in a single gulp. He looks satisfied with his amount of water, even though I could probably hold more in my bare hands.)"
    j "Nice to meet you."
    j "Sorry about those water cooler shenanigans. I'm not the best at interacting with other people."
    hide sigma glasses 
    with easeoutleft
    mc "(Sigma walks away without a sound, leaving me to deal with someone I've just met.)"
    mc "(He sips the cup again, only taking in the few remaining droplets.)"
    j "I see you've already met Sigma. She's a hard worker, that woman."
    mc "(He laughs quietly before filling up his cup again.)"
    j "I assume you're new to this place. What's your name?"
    mc "I'm [name]. Nice to meet you."
    j "Nice to meet you too. If you're confused about something, you can just ask me about it."
    menu: 
        "What do you do here?":
            show joejoe surprised at center 
            mc "(His face shows a hint of surprise before he smiles again.)"
            j "Oh, this will sound kinda bad, but..." 
            show joejoe embarrassed at center
            j "I'm not sure."
            mc "Huh?"
            show joejoe talking 1 at center
            j "No, I mean, like, I come here every day, right?"
            j "And every day Sigma allows me in without a hitch."
            j "But I don’t do anything for the company. I just wander around for the entire day. Sometimes I help someone with paperwork or run errands for them, but I’m not paid to do that."
            j "I work for the company, but I don't {i}work{/i} for the company. Y'know what I'm saying?"
            j "Oh, I do go get lunch with the crew every once in a while."
            mc "...I see."
            mc "(Why is he even getting paid?"
        "What do I do here?":
            j "I don't know. Did Sigma tell you your position or anything?"
            mc "Yeah, she said I was a Cherishable Undergraduate Major or something like that."
            show joejoe talking 2 at center 
            mc "(His face lights up like a candle once I say that.)"
            j "Ah, yes, the Charitable Urgency Managers. I always loved that title."
            j "I believe you're the ones who handle the diseases. Like, fighting them and whatnot."
            j "But that doesn't happen that often, so I think you just spend most of your time doing paperwork."
            mc "That sounds like a pain."
            j "Yeah, it does."
        "I'm good.":
            show joejoe sad 2 at center
            j "Glad I could... help?"
            mc "(He looks a bit crestfallen that I didn't ask anything. I feel bad for him now."
    show joejoe neutral         
    j "Anyways, welcome to the company. I look forward to working with you. I’ll be your water cooler buddy too, I guess."
    menu:
        "Sure.":
            show joejoe happy 1
            mc "(He nods and waves at me as he walks away.)"
            hide joejoe 
            with easeoutright
        "No thanks.":
            show joejoe happy 2
            mc "(He gives me a thumbs up and walks away.)"
            hide joejoe 
            with easeoutright
    mc "(Now I'm alone at the water cooler.)"
    mc "(I should probably do work now.)"
    scene bg cubicle2
    with fade 
    mc "(I depart from the break corner and head towards the cubicle that Sigma assigned to me.)"
    mc "(Everybody in this cubicle group is working on something. I sit down as quietly as I can to not bother them.)"
    mc "(No one's around this area except for a single man in the cubicle in front of mine. I guess the other Charitable Urgency Managers are on break or something.)"
    mc "(There's a stack of papers on my desk. It's quite a bit of paper, but it doesn't seem like it would be that difficult.)"
    mc "(I look through the papers to see what I have to do, but they're all completely blank.)"
    mc "(Name, Date of Birth, Disease. They're all important information, but I don't have any information to put in the form.)"
    mc "(I shift around the papers to try to find anything that can help me, but they're forms.)"
    mc "(I keep looking around the papers to see if I had just missed one. Nothing. I check underneath my desk to see if I dropped one. Nothing.)"
    mc "(What do I do...)"
    menu:
        "Ask a coworker":
            mc "(I stand up from my chair so I can see the cubicle in front of me.)"
            mc "(He looks like he's hard at work. Maybe I shouldn't bother him…)"
            mc "(But I have no choice. I don't want to sit here for another 3 hours without anything to do.)"
            mc "Hey."
            mc "(I don't think he heard me.)"
            mc "Hey, you."
            mc "(He looks up from his papers.)"
            show joejoe neutral 
            mc "(His face reminds me of Joe Joe.)"
            mc "(He has the same brown hair and light blue shirt. The same dark blue pants. He even has a cup of water next to him.)"
            mc "(Wait…)"
            show joejoe talking 1
            j "Oh, hey [name]! What's up?"
            mc "Oh, it's you."
            mc "Uh, I was wondering, what am I supposed to do for this?"
            mc "(I show him a paper from my stack. He glances over it, then turns it around.)"
            show joejoe neutral
            j "Oh for these, you need to get files from the archive. Do you see how each sheet has an ID on it? That corresponds with their file number."
            mc "Thanks."
            j "No problem. The file archive should be right outside the department. You should be able to see the files through the windows."
            hide joejoe 
            mc "(I try to scoop up the stack of papers before realizing I can just write down the ID numbers.)"
            mc "(After that, I head towards the archive room to grab some files.)"
            mc "(All of the people I need to document have ID numbers in the 10000s. I don't think I'll get through all of them though, so I only take the first 10 I need.)"
            mc "(I head back to my cubicle and begin filling out the forms for each and every person.)"
            scene bg cubicle
            with fade
            mc "(It takes a lot longer than I expected. I didn't know just how much information we had to record on these people.)"
            mc "(And to think that there are at least 10,000 different files…)"
            mc "(By the time I finish the 9th file, it's almost dark outside, and my shift is over.)"
            mc "(I yawn as I get up from my desk. This job isn't difficult, but it sure is a lot of work.)"
            mc "(I need to return these files to the archive room, and then I can leave.)"
            mc "(After I do that, I head for the main lobby.)"
            scene bg duskfrontdesk
            with dissolve 
            mc "(When I pass the front desk, I can see that Sigma is still working hard. I guess she ends her shift later, or maybe she just likes working.)"
            show sigma pain
            s "{size=-10}Fuck this shit. This fucking sucks so bad.{/size}"
            mc "(Yeah, her shift probably ends later.)"
            mc "(I'd rather not bother her while she's working.)"
            hide sigma 
            mc "(I leave the building and head home.)"
            jump day2
        "Ask Sigma":
            $ sigmaPoints += 1
            mc "(I get up from my desk and start heading for the front desk. The office building is quite large, but there are markings on the ground leading toward the main lobby.)"
            mc "(As I walk to the front desk, I take a glance at the other departments on the way. They all look identical, except for a few extra storage rooms in some of them.)"
            scene bg dayfrontdesk
            with dissolve 
            mc "(I finally reach the front desk.)"
            mc "(Am I even allowed to go behind the front desk? I know I'm technically an employee but it still feels wrong to be there. Sigma might think I'm weird if I do that. But she also might think I'm weird if I talk to her across the desk like a guest.)"
            mc "(I end up deciding to head behind the desk to talk to her.)"
            show sigma tired 
            mc "(She's working hard. Her hands move at light speed, filling out form after form and stacking each paper on top of the other in a neat stack. Based on the number of papers next to her, she has been doing this non-stop for a while.)"
            mc "(I gently knock on the entryway to notify her of my presence.)"
            mc "Sigma."
            s "Yeah."
            mc "I have a question."
            s "Yeah."
            mc "(She doesn't even bother looking up.)"
            mc "I was wondering, how do I fill out the paperwork?"
            show sigma confused  
            mc "(She pauses for a moment.)"
            s "You just... fill it out."
            mc "No, I meant like, what do I fill in?"
            show sigma glasses  
            s "Oh. There should be files in the department's archive room. It should have the proper information, and you can just write whatever it says onto the form."
            s "Each paper should have an ID number on it, and that matches with a specific file. Can I see one of the forms?"
            mc "(Sigma finally looks up from her papers, but at that moment I realized I hadn't brought any of the forms with me. Regret fills my mind as I quickly look away from Sigma.)"
            mc "I, uh. I didn't bring them with me."
            show sigma tired 
            mc "(She looks surprised. She begins to frown, but quickly stops and returns to a neutral expression.)"
            s "No, it's fine. You're new here. And everyone makes mistakes sometimes."
            mc "(Her voice is covered in mild annoyance. I start to feel bad about myself, and it seems that it showed on my face.)"
            show sigma glasses
            s "Don't worry about it. There are other ways you can help, like..."
            mc "(She begins shuffling around her papers to try to find something I can do.)"
            mc "No, it's fine, I can just-"
            mc "(Sigma cuts me off with a few sheets that had been paper-clipped together.)"
            s "Here, you can do these. They're the company tax forms. And these..."
            mc "(She places a folder and a ballpoint pen on top of the stack.)"
            s "...are the records. Just look through the file for the appropriate paper, and put the information in the form."
            mc "(I grab the stack of papers from her and sit down at the small desk facing opposite the main one.)"
            mc "(Before I even open the files I hear Sigma laugh quietly behind me.)"
            mc "(I turn around inconspicuously to see if she was laughing at me, but she was already back to work.)"
            mc "(Before I sit back down and pretend as if nothing happened, Sigma turns around slightly to look at me. We make eye contact.)"
            show sigma excited 
            mc "(She laughs. This time I'm sure it's at me.)"
            mc "What?"
            show sigma glasses
            mc "(Sigma averts her eyes and turns back to her work.)"
            mc "(I stand in silence, confused by her actions. The silence remains for a few more seconds before she speaks.)"
            s "Sorry about that. That desk is usually reserved for the CEO, on the rare occasion that he shows up."
            mc "Oh."
            mc "(I back away from the desk and look around for another surface to work on.)"
            s "No, it's fine. I doubt the CEO would care much if someone sat at his special desk. Especially if that someone was doing his tax work for him."
            mc "(I don't feel very reassured about this, but I trust Sigma. She doesn't have a reason to lie to me, right?)"
            hide sigma 
            mc "(I sit back in the seat and get to work.)"
            with fade
            mc "(It's not a lot of work, these tax reports. It's less than a fourth of the stack in my cubicle.)" 
            mc "(I wonder if Sigma gave me less work cause she didn't think I could handle anything else. It hurts that I'm not seen as terribly competent, but it is a proper assessment of my skill level.)"
            mc "(Every once in a while, I come across something that I don't understand.)" 
            mc "(Sigma is always ready to help, but the sarcastic way she explains it makes me feel uncomfortable whenever I need to ask her something often.)"
            mc "(I can tell that she means no harm when she acts like that, but it still makes me nervous about taking too much.)"
            scene bg duskfrontdesk 
            with fade
            mc "(I finally finish the papers. The massive floor-to-ceiling windows of the main lobby shine a golden-red light onto the ground, forming a carpet-like shape onto the floor of the lobby.)"
            mc "(The hues make me feel nostalgic for a memory I don't have, but it's a good indicator of when my shift ends.)"
            mc "(I get up from my chair with a yawn to hand the papers to Sigma.)"
            mc "I finished the tax papers, Sigma."
            show sigma glasses 
            mc "(I stack the papers on top of the file folder and place the pen on top of the stack.)"
            s "Thanks."
            mc "(She gives me a thumbs-up with her free hand before going back to work.)"
            s "You can leave now if you want. You don't get paid for any work after 5 pm."
            mc "(I leave the desk area and walk to the main lobby, ready to go home.)"
            mc "(Sigma's still working, though. I wonder if secretaries get paid differently.)"
            mc "Are you gonna stay?"
            show sigma pain 
            s "Yeah. I need to finish up all of {i}this.{/i}"
            mc "(She motions at the various stacks of paper covering her desk. It seems like a lot of work. It'd probably take me a week to do even half of it.)"
            mc "Good luck, I guess."
            s "Thanks."
            hide sigma 
            mc "(I wave her goodbye and head out the door. The sky is slowly but surely beginning to darken. I need to hurry home to escape the night.)"
            jump day2
