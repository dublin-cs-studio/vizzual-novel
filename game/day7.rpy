label day7:
    scene bg bedroom
    with fade
    mc "(...it's Monday again.)"
    mc "(I've only done this for a week, yet I'm starting to dread waking up early in the morning almost every single day.)"
    mc "(It's like an innate memory, still stuck in my body from my previous self, that tells me that every Monday is a day to be hated.)"
    mc "(I get up anyway, cracking my joints and yawning as I do.)"
    mc "(Complaining isn't going to help. Let's get up.)"
    scene bg frontdesk day
    show sigma glasses
    with fade
    mc "(There's a large banner hanging from above Sigma's desk.)"
    mc "Good morning Sigma."
    show sigma tired
    s "*sigh* Hello [name]."
    mc "What's going on?"
    s "The festival thing Joe Joe was talking about last week. You remember?"
    s "The banner keeps falling onto my desk, and it's really annoying."
    mc "Is it not staying in place?"
    s "Not one bit. I mean, it looks like it's in place, but then a pin comes loose or something and it just collapses."
    mc "Anything I can do to help?"
    s "I don't think so..."
    show sigma glasses
    s "Oh, can you get me a stapler?"
    mc "Sure thing."
    show sigma excited
    with fade
    mc "(After a few dozen staples, Sigma looks satisfied.)"
    s "That's not going anywhere."
    s "Thanks for the help, [name]."
    show sigma glasses
    s "By the way, the festival's gonna get started soon."
    s "Most of the preparations are done, I just need to take attendance and whatnot."
    s "You should go find Joe Joe, he'll show you where everything is. I'll be there shortly."
    mc "Alright."
    hide sigma
    with dissolve
    pause(0.5)
    with hpunch
    pause(1.0)
    s "{size=+30}...{/size}"
    scene bg cooler
    show joejoe happy 1
    with fade
    mc "Hey Joe Joe."
    show joejoe talking 1
    j "Yo."
    j "You know what today is, right?"
    mc "The festival day, I think."
    show joejoe happy 3
    j "Yep. You excited?"
    mc "Kinda. Not sure what to expect. What usually happens?"
    show joejoe happy 1
    j "Well, right at the beginning we have a potluck sort of thing. Everyone's supposed to bring food if they want to eat, but lately someone just gets catering for all of us."
    j "It's easier, plus everyone is happier paying a small fee rather than cooking food for some 50 people."
    j "After that, the CEO usually gives a speech about something, and then we head to some place for a trip."
    j "This year, we're heading to the beach."
    show joejoe happy 3
    j "Not bad, eh?"
    mc "That sounds pretty good. Uh, was I supposed to pay for the catering?"
    show joejoe happy 1
    j "Nah, this was all planned out a month ago. We always order slightly extra in case something happens."
    j "The food should arrive any time now."
    show joejoe happy 1 at left
    show sigma glasses at right
    with fade
    s "{size=+30}Food's here!{/size}"
    mc "(A few people scramble to the entrance to get the food.)"
    j "Let's help."
    show bg frontdesk day
    with fade
    s "Mashed potatoes, check."
    s "Roast beef, check."
    s "Curry, check."
    j "Did you get the drinks yet?"
    s "I have not. Who said they were gonna get them?"
    pause(1.0)
    show joejoe angry 1
    j "Ah, shoot. I did."
    j "There's still time, right?"
    j "[name], come with me."
    scene bg frontdesk day
    show sigma glasses at right
    show joejoe happy 1 at left
    with fade
    j "We got the drinks!"
    s "Nice. A bit late, but glad you made it."
    s "Just put them on the tables over there. We'll get started soon."
    show bg cubicle day
    with fade
    j "Man, this roast beef is pretty good."
    s "Yep. Curry's not bad either."
    show sigma tired
    s "Couldn't you have gotten something other than juice and soda though?"
    show joejoe frustrated
    j "What else would you want to drink?"
    s "Water would be healthier."
    s "And probably cheaper."
    show joejoe angry 1
    j "Can't believe I forgot about water."
    j "Goddamn. I drink it every day and I can't remember it."
    show joejoe embarrassed
    j "Uh, sorry about that."
    j "You can drink from the cooler, I guess."
    show joejoe flustered 2
    j "I am so sorry."
    show sigma glasses
    s "No, it's fine. I'm just nitpicking."
    s "Now that I think about it, getting water might have been more wasteful."
    s "If you got water bottles it would be more plastic than just a few larger bottles of soda."
    show sigma tired
    s "Plus it would've been a pain to clean."
    show sigma glasses
    s "Good choice."
    j "Thanks... I guess."
    j "Good lord that's embarrassing."
    show joejoe happy 1
    with fade
    mc "(Joe Joe tries to explain different types of coffee to me, but I can't understand him at all.)"
    j "So there's black, it's just ground coffee in hot water. Then there's espresso, it's like concentrated coffee."
    s "Damn, that's crazy."
    j "Then if you put the espresso with some milk and foam, it becomes a latte."
    mc "How many types are there?"
    j "A lot. There's also americano, which is a shot of espresso in water."
    mc "What's a shot?"
    j "It's a measurement. A normal espresso has one shot if you're getting just an espresso or if you're mixing it with something, but there's also a doppio, which is two shots."
    j "I forgot what it's called but-"
    s "Sorry guys, I have to go set up the microphone. We can talk later."
    hide sigma
    hide joejoe
    with dissolve
    show joejoe angry 1
    j "Oh, is it time for the speech?"
    mc "(Joe Joe looks around before quietly walking away from the main area.)"
    show bg cooler
    with fade
    mc "What's wrong?"
    j "I don't like that guy."
    mc "The CEO?"
    j "Yep, him. I'd rather not hear him talk for 15 minutes without breaks."
    mc "Isn't he your boss though?"
    j "It's complicated. Anyways, you can go back if you want."
    j "I'm staying here."
    "Voice" "Yo, Joe Joe."
    show joejoe disgusted 2
    j "Ah shit."
    show joejoe disgusted 2 at right
    show ceo happy at left
    with ease
    "Cool Guy" "The speech is starting soon, y'know?"
    "Cool Guy" "I would hate for you to miss out."
    mc "It's you!"
    "Cool Guy" "Hm?"
    pause(1)
    "Cool Guy" "Ah!"
    "Cool Guy" "Haven't seen you in a bit."
    "Cool Guy" "How's it going here?"
    mc "Not bad. I haven't really been doing much, though."
    "Cool Guy" "No worries. You're new here, anyways."
    "Cool Guy" "Is Joe Joe treating you well?"
    mc "Yeah. He's been a really good friend."
    "Cool Guy" "That's good to hear. Everything going well on your end, Joe Joe?"
    show joejoe angry 1
    j "Yes."
    show joejoe neutral
    j "[name], when did you meet this guy?"
    mc "Uh, before I came to work here, I was-"
    "Cool Guy" "Oh, look at the time. I have to go."
    "Cool Guy" "I'll let you explain, [name]. It's your story, after all."
    mc "(Right before the cool guy leaves, he pats Joe Joe on the shoulder.)"
    show ceo neutral at center
    with ease
    "Cool Guy" "Remember what you're here for."
    hide ceo
    show joejoe neutral at center
    with dissolve
    # j "..."
    # show joejoe happy 1
    # j "Uh, where were we?"
    # mc "I can explain, Joe Joe."
    # j "I wasn't talking about that, but feel free to tell me though."
    # mc "So a week ago..."
    # show joejoe neutral
    # with fade
    # j "Damn, that sucks. Sorry about that."
    # j "You don't remember anything at all?"
    # mc "Nope."
    # j "Damn. I hope you're recovering well now."
    # mc "Yeah, I'm getting along fine, thanks to you and Sigma."
    # show joejoe happy 1
    # j "Glad I could help."
    # mc "Do you know who that guy was?"
    # show joejoe angry 1
    # pause(0.7)
    # show joejoe frustrated
    # pause(0.7)
    # show joejoe neutral
    # j "Someone you shouldn't bother talking to."
    # $ joeMad = True
    # if joeMad:
    #     mc "He saved my life. I want to know who he is, at least."
    #     j "You don't. That man-"
    #     mc "Please, Joe Joe."
    #     pause(1.0)
    #     show joejoe frustrated
    #     j "Why don't you go ask him."
    #     hide joejoe
    #     with dissolve
    #     mc "(He motions me to go towards the main area and starts to fill up a cup of water.)"
    #     scene bg frontdesk day
    #     show ceo happy
    #     with fade
    #     "Cool Guy" "Good morning, everybody. It is with great pleasure that I announce the beginning of the 83rd..."
    #     mc "(Is he the CEO?)"
    #     mc "(No wonder Joe Joe felt uncomfortable around him.)"
    #     mc "(But why doesn't he like the CEO?)"
    #     c "I am so glad that everyone could make it today."
    #     mc "(He looks around the crowd before he spots me.)"
    #     c "I hope the food was to your likings. I haven't tried anything yet, but the mashed potatoes smell incredible."
    #     mc "(His gaze lingers on me for a few more seconds before he starts looking around the crowd again.)"
    #     mc "(I'm not really interested in this, to be honest.)"
    #     mc "(I slowly make my way to the back of the crowd before heading back to the break corner.)"
    #     scene bg cooler
    #     show joejoe neutral
    #     with fade
    #     mc "(Joe Joe is on his phone, occasionally sipping a cup of coffee.)"
    # else:
    #     mc "(I won't push him.)"
    #     mc "(Joe Joe seems to appreciate that. He sighs and fills up a cup of water.)"
    scene bg frontdesk day
    show ceo happy
    with fade
    c "Alright everyone!"
    c "As I'm sure all of you know, each year we go on a trip to celebrate the anniversary of the DEU."
    c "Last year, we went to an onsen hotel. This year we are going to..."
    c "The beach!"
    mc "(Everyone starts to clap, however I can tell that some people are opposed to the decision.)"
    hide ceo
    with dissolve
    "Random Co-worker" "Seriously? Another water-based trip?"
    "Other Co-worker" "I can't even swim."
    s "Ooh, the beach."
    show sigma glasses
    with dissolve
    s "Sounds fun. You excited?"
    mc "Not really. I don't think I can swim."
    s "No worries. There's plenty to do at the beach other than swim."
    s "Besides, if you really want to swim you could just use a floaty."
    mc "(The image of myself wearing floaties is quite embarrassing, but it is a legitimate solution.)"
    mc "I'll think about it."
    show sigma excited
    s "Heh. That'd be funny to watch."
    show sigma glasses
    s "No judgement, though."
    s "Anyways, I'll go call Joe Joe. We're leaving soon, so just listen for instructions."
    hide sigma
    with dissolve
    "Co-worker" "Gather all your belongings! Boarding will start soon!"
    mc "(Right outside the front doors, I can see a few buses lined up.)"
    mc "(Each bus can only fit so many people. I'll wait so I can sit with someone I know.)"
    mc "(Suddenly, someone slaps my back.)"
    show pelota happy
    with dissolve
    with vpunch
    p "Hey, [name]!"
    p "You excited for the beach?"
    p "I know I am. I didn't even know we had something important today."
    p "I was wondering why Goopitha was calling me at 8:30 in the morning."
    p "Almost didn't show up, hahaha."
    mc "(She's holding a plate with mashed potatoes. She probably just got here.)"
    hide pelota
    with dissolve
    show pelota happy at left
    show goopitha angry at right
    with dissolve
    g "Jeez, this is supposed to be the anniversary of the DEU. Shouldn't you at least remember that?"
    mc "Ah, hello Goopitha."
    mc "(It's only been a day...)"
    show goopitha neutral
    g "Ah. Um..."
    show goopitha smile
    g "Hello, [name]."
    mc "(She's acting like nothing happened yesterday.)"
    show pelota smile
    p "Sorry, sorry."
    show pelota happy
    p "Well, at least I showed up, huh?"
    p "Anyways, we're going to the buses, right?"
    p "You wanna join us?"
    menu:
        "Join Goopitha and Pelota":
            jump bus1
        "Wait for Sigma and Joe Joe":
            jump bus2

label bus1:
    mc "Sure."
    p "Nice. Seats are gonna run out soon, so let's get going."
    scene bg bus inside
    show goopitha smile
    with fateslide
    g "Oooh, I want the window seat!"
    hide goopitha
    with dissolve
    show pelota neutral
    with dissolve
    p "Are there only two seats per side?"
    p "Damn."
    mc "(We head towards the back, but there's only pairs of seats available.)"
    mc "I guess you could just sit behind us."
    mc "I could do that, if you'd want."
    show pelota happy
    p "Nah, I'll just sit on the other side. It's not that far apart."
    mc "Alright then."
    scene bg bus window
    show goopitha happy
    with fade
    g "Is this one of those fancy buses with air conditioning?"
    mc "(She looks around for a while before finally spotting a massive fan on the roof.)"
    g "Ooh, nice."
    mc "There's even a bathroom in the back."
    show goopitha smile
    g "Damn, how much did we spend on this day alone?"
    g "Either we must be making bank or the DEU anniversary is just that special."
    mc "(Goopitha probably doesn't want to bring up yesterday, huh.)"
    mc "(I'll follow her and pretend nothing happened.)"
    mc "Are you excited for the beach?"
    g "Of course! I used to go to the beach all the time."
    mc "That's cool."
    g "Mhm."
    mc "..."
    mc "(And we're back to being silent again.)"
    mc "(It's so awkward between us. Such an important talk happened yesterday, so how could I act like nothing happened?)"
    mc "(I doubt Goopitha wants me to bring up yesterday though, so what do I do?)"
    $ goopKnows = False
    if goopKnows:
        show goopitha neutral
        g "Are you still thinking about yesterday?"
        mc "(!!!)"
        mc "Uh, yeah. Kinda."
        show goopitha smile
        g "Heh. That's very you."
        g "Or, I guess that's very past you."
        show goopitha smile:
            ease 1.5 zoom 1.5 xoffset 0 yoffset 200
        g "You don't remember anything, right?"
        mc "(Goopitha suddenly comes right up to my ear and brings her voice down to a whisper.)"
        mc "No, I don't."
        mc "(I slightly recoil from her closeness, but she closes the distance.)"
        g "Really? Nothing?"
        g "Not even when you promised that you would marry me?"
        mc "Uh, no. Did I do that?"
        mc "Then... I-"
        g "I'm kidding. That was way too long ago."
        g "But, nothing at all, huh."
        g "I guess I could tell you more about who you were."
        g "You remember what I said yesterday, right? About how we met at a playground?"
        g "Well, after that..."
        mc "(Her voice drops lower as she gets closer until I can barely hear her.)"
        with hpunch
        g "Boo."
        mc "(She blows into my ear, making me recoil.)"
        mc "Woah."
        show goopitha yandere
        g "Heheh."
        mc "Don't do that please."
        mc "(I try to blow into Goopitha's ears before realizing that she doesn't even have any.)"
        show goopitha smile
        g "Well, who you were doesn't matter anymore."
        g "All I care about now is who the current you is."
        g "And you shouldn't care about who you were either. Not like you're gonna remember them, right?"
        g "You are free to be whoever you want now. No past, but infinite future."
        g "Aren't you lucky."
        show goopitha happy
        g "Heheh."
    p "You guys comfortable over there?"
    scene bg bus other window
    show pelota neutral
    with dissolve
    mc "(Pelota looks pretty bored.)"
    mc "Yep."
    g "Yeah."
    p "Nice. I still haven't eaten breakfast yet, so don't mind me."
    mc "(Pelota still has her plate of mashed potatoes. It's not what I would call breakfast, but I guess it doesn't matter if you're hungry.)"
    p "Ah, I didn't get a spoon. D'you think we're gonna leave soon?"
    g "Probably not. We've been waiting for quite a bit now, so it'll probably take some time."
    mc "Yeah, probably not."
    p "Aight, hold on."
    mc "(Pelota quickly gets off the bus and runs towards the office building.)"
    mc "(She leaves her plate on her seat.)"
    show goopitha neutral
    g "Maybe this is why these buses are always so slow."
    mc "(After a few minutes, the boredom gets to me and I pull out my phone.)"
    mc "(There isn't much on it. I guess it's not meant to be used for anything other than calling.)"
    mc "(Guess I'll play snake.)"
    scene bg bus window
    show goopitha neutral
    with fade
    g "Is Pelota still not back yet?"
    mc "Maybe she's still getting a spoon."
    scene bg alley day
    show pelota neutral
    with squares
    p "(Alright, hopefully I make it back in time.)"
    show bg konbini
    with dissolve
    p "Hey cashier, do you guys have watermelons here?"
    "Cashier" "Uh, I'm afraid we don't. We do have watermelon flavored drinks and snacks though, if that works."
    p "Oh, damn."
    p "Y'know where I can find some?"
    "Cashier" "No clue. Maybe a grocery store or something."
    p "Aight, thanks."
    show bg pizzeria
    with dissolve
    p "'scuse me, do y'all happen to have a watermelon by chance?"
    "Pizza Worker" "Why'd you come to a pizzeria looking for a watermelon?"
    "Pizza Worker" "Out of all places, why here?"
    "Pizza Worker" "Anyways, we don't have any watermelon here. Sorry."
    p "Gotcha, gotcha."
    show bg burger
    with fateslide
    pause(2.0)
    show bg aquarium
    with fadeslide
    pause(2.0)
    show bg park day
    with fateslide
    p "(Man, none of them have watermelons. I'm running out of time.)"
    p "(Hmmm, what other places could have watermelons...)"
    p "(Can't think of any.)"
    p "(Am I doomed to not have any watermelon today?)"
    show pelota happymad
    p "(No. I refuse to keep going without watermelon.)"
    p "(I will check every store in this town!!!)"
    scene bg bus window
    show goopitha neutral
    with squares
    g "I hope she's not up to anything stupid."
    g "No way getting a spoon takes this long."
    mc "Should we go check up on her or..."
    show goopitha smile
    g "Yeah, that woul-"
    show goopitha neutral
    g "No, the second you said that I saw her again."
    mc "(I turn around and see Pelota bolting towards our bus, spoon in hand.)"
    scene bg bus other window
    show pelota smile
    with dissolve
    mc "Where were you?"
    p "*pant*"
    p "Like I said, getting a spoon."
    mc "(She waves her spoon around to show it off to me.)"
    mc "(It's not very impressive, but it does the job.)"
    mc "(Still doesn't explain why she took so long.)"
    g "Is your hat taller or is it just me?"
    mc "(?)"
    camera:
        perspective True
        xalign 1.0
        yalign 0.5
        zpos 0 yalign 0.0
        ease 2.0 zpos -400 ypos -100
    mc "Now that you mention it, it does seem like her hat got bigger..."
    show pelota mad
    p "What are you guys talking about?"
    p "My hat didn't get bigger."
    camera:
        perspective True
        ease 2.0 zpos 0 ypos 0 
        perspective False
    mc "Well, if you say so."
    mc "(Pelota adjusts her hat and starts eating her mashed potatoes.)"
    scene bg bus window
    show goopitha smile
    with dissolve
    mc "(Suddenly, the engine starts up, sending a rumbling noise throughout the entire bus.)"
    mc "(Looks like we're finally starting the trip.)"
    mc "(The doors close with a hiss and the bus begins to move.)"
    show goopitha happy
    g "Wooo! We're finally moving!"
    mc "(One of the other buses has already left. Looks like we're not the first.)"
    mc "(I still haven't seen Joe Joe or Sigma yet. Maybe they're stuck inside or something.)"
    mc "(I wonder what they're up to.)"
    mc "(Goopitha pulls out her phone out of boredom.)"
    pause(1.0)
    mc "(Oh right, I can use my phone.)"
    mc "(Let's check in on those two.)"
    hide goopitha
    with dissolve
    mc "(Only Sigma is in my contacts right now. I guess I'll have to ask Joe Joe for his number later.)"
    mc "How are you doing?"
    s "Joe Joe's trying to get his coffee."
    s "The machine isn't working for some reason."
    s "Just go on without us, if you haven't already."
    mc "Yeah, I just went with Goopitha and Pelota."
    s "Alright. Seeya there."
    pause(1.0)
    show goopitha smile
    with dissolve
    mc "(I close my phone and lean into my seat.)"
    mc "(Nothing to do but wait, I guess.)"
    with fade
    #"some bus stuff idk"
    mc "(Finally, we've reached the beach.)"
    scene bg bus inside
    show goopitha happy
    with dissolve
    mc "(I wait for the bus to stop before sighing out of relief.)"
    g "We're finally here..."
    g "*yawn*"
    mc "(Pelota stretches and gets up. Goopitha and I follow her.)"
    scene bg beach main
    show pelota happy at left
    show goopitha smile at right
    with fade 
    mc "Woah..."
    g "It looks beautiful!"
    p "Definitely worth coming."
    mc "(I look around the beach. The other buses haven't arrived yet, so we have to wait for them.)"
    mc "(I walk closer towards the water.)"
    scene bg beach coast
    with fade
    mc "(The ocean is really loud, now that I'm closer.)"
    mc "(It doesn't that there's no one around here.)"
    mc "(Did we get a private beach or something?)"
    mc "(No way this company is that rich, right?)"
    mc "(I notice a few beach huts a hundred meters away.)"
    scene bg beach huts
    with dissolve
    mc "(They all look relatively new. The insides are furnished with a table and a few chairs.)"
    mc "(It's still not noon yet, but I would love to watch the sunset from here.)"
    mc "(Hm?)"
    mc "(What's this?)"
    mc "(I see a poster attached to one of the huts.)"
    "Poster" "HappyFun Lands Summer Festival"
    "Poster" "Roller coasters, carnivals, ferris wheels"
    "Poster" "Every attraction you could want out of this summer"
    mc "(Looks interesting. I hope tickets are free.)"
    mc "(As I'm looking at the poster, Pelota yells at me to come back to the main area.)"
    scene bg beach main
    show pelota neutral
    with fade
    mc "What's up?"
    p "The other buses are coming. The CEO wants to do a head-check."
    p "You see anything interesting down there?"
    mc "Kinda. There's an amusement park in the area that's opening today."
    p "Sounds nice. Anything else?"
    mc "Nope. That's it."
    p "Huh."
    c "{size=+10}Listen up everyone!{/size}"
    p "It's starting."
    scene bg beach main
    show ceo happy
    with fateslide
    c "...that's everyone accounted for."
    c "Alright, with all the boring stuff out of the way, let's spend the rest of the day relaxing!"
    c "First, let me explain the schedule for today..."
    mc "(Didn't he just say the boring stuff was out of the way?)"
    hide ceo
    with fade
    mc "(After a few more minutes of explaining, he finally lets us go do whatever we want.)"
    s "[name]! Over here!"
    show sigma glasses at left
    show joejoe happy 1
    show pelota happy at right
    with dissolve
    j "So, what do you guys want to do today?"
    j "I brought a few water guns if you wanna use them."
    mc "Woah, did you come in your swimsuit?"
    show joejoe neutral
    j "...was I not supposed to?"
    mc "(He looks around at everyone. They're all wearing their normal office clothes.)"
    j "..."
    hide joejoe
    with dissolve
    mc "Well, I guess you don't need to wait for a changing room to open up."
    s "He was like this in the bus too, by the way."
    j "Don't tell them, Sigma!"
    j "They don't need to know!"
    show joejoe angry 1
    with dissolve
    j "Well, there goes my mood for the day. I can't believe none of you guys told me."
    show joejoe neutral
    j "But, back to what I was saying."
    show joejoe happy 1
    j "Water guns, anyone?"
    p "None of us are changed yet, so that'll have to wait."
    show joejoe angry 1
    p "Anything else?"
    mc "There's an amusement park opening today. We could go check that out."
    p "Oh right, you told me about that."
    s "Sounds fun. What kind of stuff do they have?"
    mc "I think they have all the standard amusement park stuff. Ferris wheel, merry-go-round, roller coasters."
    show pelota happymad
    p "*cough* That sounds great, lemme go ask Goopitha what she thinks."
    hide pelota
    with easeoutright
    show goopitha happy at right
    with CropMove(0.2, mode='wipeleft')
    g "Oooh, roller coasters!"
    g "Are they the ones that go upside-down?"
    g "I wanna ride one!"
    g "Hey, Pelota, where are you going?"
    hide joejoe
    hide sigma
    hide goopitha
    with dissolve
    show goopitha smile at left
    show pelota happymad at right
    with dissolve
    p "Let go of me."
    g "What's wrong, Pelota?"
    p "I don't like roller coasters."
    p "Especially not the ones that go upside-down."
    show pelota neutral
    p "You can probably guess why."
    show goopitha neutral
    g "Oh, do you have a fear of-"
    p "Yeah, hei-"
    g "Widths?"
    p "Huh?"
    show goopitha neutral
    g "Oh, I'm so sorry!"
    g "If I knew you had a fear of widths, I wouldn't have asked!"
    g "Those roller coasters are way too wide."
    g "They're probably the ones with 4-wide seats, right?"
    g "Oh, sorry. I'm probably making you imagine them."
    g "Anyways, I'm sorry! Please don't feel like you need to join us! If your fear of widths is too much, just stay here!"
    p "...Yeah."
    p "Well, I'm gonna stay here. You all can enjoy your amusement park, I guess."
    show pelota smile
    p "I won't be bored, though. Don't worry about me."
    hide pelota 
    with dissolve
    show sigma glasses at right
    show joejoe neutral
    with dissolve
    jump beach1

label bus2:
    mc "Nah, I'm gonna wait for Sigma and Joe Joe."
    p "Gotcha. You should hurry up though, seats are gonna run out pretty soon."
    hide goopitha
    hide pelota
    with dissolve
    mc "(I pull out my phone and wait right at the front desk.)"
    with fade
    mc "(Where are those two?)"
    mc "(I head into the office building to look for them.)"
    scene bg cubicle day
    show joejoe angry 2
    show sigma pain at right
    with fateslide
    j "C'mon, c'mon, c'mon."
    j "It's not working!"
    s "Can you hurry up, Joe Joe?"
    s "[name]'s waiting for us."
    show joejoe disgusted 1
    j "Tell the damn coffee machine to hurry up! I'm not the one at fault here!"
    j "If it would just work a little faster, or rather work at all, we wouldn't be stuck waiting here!"
    show sigma glasses
    s "Ah, hello [name]."
    s "As you can see, we're stuck here waiting."
    s "Joe Joe needs to fulfill his coffee addiction."
    show joejoe disgusted 2
    j "It's not an addiction! I've drank coffee every single day for the past 20 years of my life, I would know if I'm addicted!"
    j "I am in control here, not the coffee!"
    show joejoe angry 1
    j "Never say I have a coffee addiction again, Sigma. You don't know what you're talking about."
    j "Now if this damn machine would actually work!!"
    mc "(He slaps the machine on every surface he can reach, but nothing happens.)"
    mc "(...Hm?)"
    mc "Is the machine plugged in?"
    mc "The extension cable is turned off."
    "Joe Joe and Sigma" "..."
    mc "(I flip the switch on the extension cable on.)"
    "Coffee Machine" "Now dispensing coffee..."
    show joejoe neutral
    mc "..."
    s "*sigh*"
    mc "(I slowly back away from the two, avoiding sudden movements.)"
    hide joejoe
    with dissolve
    j "I'm going to kill myself."
    s "I'm not even mad, just disappointed."
    j "Fuck my life."
    s "Fuck your life indeed."
    j "Now that I think about it, it was pretty weird how the light wasn't on."
    s "Mhm."
    s "Oh, your coffee's ready."
    scene bg frontdesk day
    show sigma glasses at right
    show joejoe happy 5
    with fade
    j "Alright, let's get going!"
    j "How weird that I can't remember what happened in the last 10 minutes."
    j "Oh well. It must not have been important."
    s "By the way, there's only one bus left now. They're waiting for us."
    show joejoe angry 1
    j "Shhhhh."
    j "Everything is okay."
    scene bg bus inside
    show sigma glasses
    with fade
    s "Where do you guys wanna sit?"
    hide sigma
    with dissolve
    show joejoe happy 1
    with dissolve
    j "Let's sit at the back."
    s "Why?"
    j "Cause it's the coolest spot. Have you never ridden a school bus before?"
    mc "(We walk all the way to the back and sit down.)"
    scene bg bus window
    show joejoe happy 1:
        zoom 1.5 xoffset 200
    with dissolve
    j "See? Are we the coolest kids on the block or what?"
    scene bg bus other window
    show sigma pain:
        zoom 1.5 xoffset 700 yoffset -100
    with dissolve
    s "Yeah, right next to these loud-ass fans that're blowing up a hurricane on me."
    s "I can barely think with how loud these things are."
    s "Screw this, I'm gonna move."
    mc "(She ends up sitting down in front of us.)"
    scene bg bus window
    show joejoe happy 1:
        zoom 1.5 xoffset 200
    with dissolve
    s "You two better block the wind for me. I'm not dealing with that for this entire bus ride."
    show joejoe neutral
    j "Do you want to move then? If it's too annoying for you we can just move up."
    s "It's fine like this."
    s "Besides, we'll no longer be the cool kids if we move up, right?"
    show joejoe happy 1
    j "No, we wouldn't be."
    mc "(As we settle into our seats, the bus starts to move.)"
    j "Oh, it's moving already."
    j "Usually these buses take much longer for some unknown reason."
    s "Yeah, thanks to someone wasting 15 minutes on a coffee machine."
    show joejoe sad 1
    j "Oh well. I guess we'll never find out why."
    show joejoe neutral
    mc "(Joe Joe pulls out his phone to mess around in a mobile game.)"
    mc "(While I could do the same, I look out the window.)"
    mc "(Now that I think about it, I don't really know this city at all.)"
    mc "(I've only experienced the parts that coincide with my boring life.)"
    mc "(I try to remember all the buildings that we passed, but eventually they start going by too fast for me to individually note.)"
    with fade
    mc "(After almost an hour, we reach a bridge.)"
    mc "(I can see a hint of blue from here, but it's hard to tell how close we are.)"
    s "Wow, look at the ocean."
    mc "(She points outside.)"
    show joejoe surprised 1
    j "Where?"
    mc "(Joe Joe strains his neck to try to see the ocean, but the cars around us block the view.)"
    show joejoe sad 1
    j "I can't see it from here."
    s "Wait until we get off the bridge."
    s "Either way, we should be near the beach by now."
    show joejoe happy 1
    j "Oh, nice. Should I put on my swimsuit or something?"
    show sigma confused
    s "Right now?"
    show sigma glasses
    s "I mean, you could if you felt like it. I'm not going to stop you."
    j "I'm not brave enough to be the only person to do that. I'll just wait til we get there."
    mc "Oh yeah, on the topic of swimsuits. Was I supposed to bring my own or..."
    s "I think the beach has rental ones. If not..."
    s "Enjoy the views, I guess?"
    mc "I hope I don't need to, but thank you anyways."
    scene bg bus inside
    show joejoe happy 1 at left
    show sigma glasses at right
    with fade
    mc "(After another wait, the bus finally arrives at the beach.)"
    j "Finally. I've wasted half of my battery just coming here alone."
    s "Maybe you shouldn't be playing Genshin Impact so much then."
    show joejoe disgusted 2
    j "I will never stop playing Genshin Impact."
    scene bg bus inside
    show sigma glasses
    with dissolve
    s "Let's get going. We're the last ones here."
    mc "(I look out the window, and sure enough all the other buses are already here.)"
    j "Wait, lemme charge my phone."
    scene bg beach main
    show ceo happy
    with fade
    c "Ah, they're here now."
    c "{size=+10}Listen up everyone!{/size}"
    c "{size=+10}We're going to do a head count real quick!{/size}"
    hide ceo
    with dissolve
    show pelota happy at left
    show goopitha smile at right
    with dissolve
    p "Hey, you guys finally made it. What took you so long?"
    g "Yeah, we were worried that something happened."
    hide pelota
    hide goopitha
    with dissolve
    show joejoe happy 1 at left
    show sigma glasses at right
    with dissolve
    s "{i}Unfortunately{/i}, due to unforeseen circumstances, we got delayed a bit. Man, if only we knew who was behind this delay."
    s "It sure must suck if it was caused by {i}someone we know{/i}."
    show joejoe frustrated
    j "Aw c'mon. You didn't notice the power strip was off either, so don't just blame me."
    s "Yeah, but I wasn't the one who needed coffee. If you didn't just absolutely need caffeine, we could've gotten a move on and been on schedule."
    mc "(The two of them continue arguing all the way until the CEO finishes talking.)"
    scene bg beach main
    show ceo happy
    with fade
    c "Alright, with that out of the way, let's get going!"
    hide ceo
    with dissolve
    show sigma glasses at left
    show joejoe happy 1
    show pelota happy at right
    with dissolve
    j "What do you guys want to do today?"
    j "I brought a few water guns if anyone wants to use them."
    mc "(Joe Joe takes out a backpack full of various kinds of water guns.)"
    j "Actually, we should probably change into our swimsuits before that."
    j "I'll be back soon."
    hide joejoe
    with dissolve
    mc "(Joe Joe runs off to a changing room to put on his swimsuit.)"
    p "Anything else?"
    show goopitha smile
    with dissolve
    g "I saw a poster for an amusement park that's opening near here."
    g "It looks cool. I saw a few rollercoasters and a ferris wheel in the photos."
    s "Oh, that sounds nice. Anyone else interested?"
    show pelota neutral
    p "Oh... rollercoasters."
    p "... Is there anything else you guys wanna do?"
    show goopitha neutral
    g "What's wrong? Do you not like rollercoasters?"
    show pelota happymad
    p "They make me feel sick. I can't deal with them."
    p "Plus, a lot of them are really high up, and I can't deal with heights either."
    p "Maybe I could just watch from the ground, but at that point I'd rather just stay here."
    mc "(She notices how crestfallen Goopitha seems.)"
    show pelota smile
    p "I brought something nice though. Shame you all won't be here to see it."
    show goopitha happy
    g "Really!? What did you bring!?"
    p "I'm not telling~"
    g "C'mon, at least say if it's food or not!"
    show pelota happy
    p "You'll find out. Well, if you're not going to the amusement park that is."
    show goopitha angry
    g "You're making me choose, huh?"
    g "In that case, I'll choose..."
    show goopitha confused
    g "You, Pelota."
    show pelota neutral
    p "Really?"
    show goopitha smile
    g "Can I see the thing now?"
    p "*sigh*"
    show pelota happy
    p "Nah."
    mc "(She flicks Goopitha's gelatinous forehead.)"
    p "I can't reveal what it is right now, but you'll understand after."
    p "Just go to the amusement park if you feel like it."
    p "I promise you it'll be fine."
    s "Alright, so it'll be me, Goopitha, not Pelota..."
    s "Is Joe Joe back yet?"
    hide pelota 
    hide goopitha
    with dissolve
    show joejoe happy 1 at right
    with dissolve
    j "Hey guys, I'm back."
    j "What're we up to?"
    mc "Nice swimsuit."
    j "Thanks."
    s "There's an amusement park nearby. You interested in coming?"
    j "That sounds nice. Is it anything fancy, or..."
    s "It should be decent at least."
    show joejoe neutral
    jump beach1

label beach1:
    j "Well, I have to help the CEO barbeque, so I can't join you guys."
    mc "We have a barbeque?"
    j "Yeah, for lunch. I get to cook. Well, I get to help cook at least."
    show joejoe happy 1
    j "I'll show off my cooking skills for you guys. Wish me luck."
    j "I promise I won't give you guys burnt food."
    hide joejoe
    with dissolve
    show goopitha smile at right
    with dissolve
    s "So, it'll be me, Goopitha..."
    s "Are you coming along, [name]?"
    menu: 
        "Yes":
            jump amusementpark

        "No":
            jump watermelon

label amusementpark:
    mc "Yep."
    show sigma excited
    s "Nice. Let's get going then, shall we?"
    show bg beach main
    with fade
    mc "Is that it over there?"
    g "Probably."
    g "It should just be on the boardwalk, so it shouldn't be that far away."
    show bg amusement outside
    with fade
    s "Wow. Not bad."
    g "Let's go before a line forms."
    mc "(We buy 3 tickets and head inside.)"
    show bg amusement area
    with fade
    mc "(The spirit of the park immediately overwhelms me.)"
    mc "(I turn around and face towards a wall to try to recover.)"
    mc "(Unfortunately for me, there isn't a single wall near us.)"
    show goopitha neutral
    g "Are you okay, [name]?"
    g "You don't look so good."
    mc "I'll be fine."
    mc "(I look around the park. The sounds and smells are a lot to take in.)"
    mc "(After a few more seconds, I get used to the environment.)"
    mc "It's so joyful here."
    mc "So, what shall we do first?"
    s "I got a map of the place. Let's see what there is..."
    g "Roller coaster!!!"
    s "There's a bunch of those, Goopitha."
    s "Which one do you want to ride?"
    show goopitha neutral
    g "Hmmm..."
    show goopitha smile
    g "This one!"
    s "That'll be..."
    s "That way."
    show bg amusement line
    show sigma pain
    with fade
    s "Ugh."
    mc "(The line for this one is super long.)"
    g "Well, how about that one!"
    mc "(She points towards the neighboring coaster. Its line is almost completely empty.)"
    s "That sounds much better. Let's go."
    mc "(We get into line.)"
    "Random Person" "Woah, mister. What's that on your back?"
    mc "(Suddenly, I hear an oddly familiar voice from the group behind us.)"
    t "Oh, this? The Spear of the 5th God? The demon-slaying, fire-bending, magical-power wielding-"
    mc "(He starts talking with more and more extravagance.)"
    hide goopitha 
    hide sigma
    with dissolve
    show tvhead excited
    with dissolve
    t "...of the highest-"
    t "Oh, it's you, Partner!"
    show tvhead normal
    t "Are you here to see the festival-"
    t "*cough*"
    show tvhead excited
    t "I mean, you sense the darkness approaching as well, huh."
    t "Not bad. I could see your talent from a mile away!"
    show goopitha neutral at right
    with dissolve
    g "Who's this nerd?"
    show tvhead panic
    t "Nerd?"
    t "Who are you calling a nerd?"
    f "I am the Great Fernsehkopf! The Heir to the Dark Throne!"
    g "Well, sorry, but you sound like a D&D player who roleplays as an anime character, so don't blame me for assuming."
    hide tvhead
    hide goopitha 
    with easeoutright
    show sigma glasses at left
    with dissolve
    s "Is that the TV Head guy?"
    mc "Yeah."
    s "Now I see what you meant about him being a magical girl."
    s "Hope he's doing well."
    show tvhead panic
    show goopitha smile at right
    with dissolve
    g "WOW!! That's neat!"
    mc "(Looks like Goopitha has been caught by TV Head's strange charms.)"
    show tvhead normal
    t "Now do you see? My actions are not merely for show, or as you put it, \"anime roleplay\"."
    show goopitha happy
    g "I understand now! I'm sorry about that, Mr TV Head."
    t "No matter, no matter. It is all in the past now. Say, what do you think about being my assistant?"
    s "Oh, looks like it's our turn."
    scene bg rollercoaster
    with fade
    mc "(We sit down in the coaster and adjust the holding bar.)"
    "Attendee" "Is everyone ready?"
    mc "(The other people on the ride give thumbs up. I follow.)"
    "Attendee" "Alright. Enjoy your ride!"
    mc "(The track in front of us looks quite intimidating. I start to feel concerned about my safety.)"
    mc "(The clicking of the tracks don't help.)"
    mc "(Suddenly, the cart tips upwards as it rises.)"
    mc "(Why did I get on this ride???)"
    #Dialogue depending on who's sitting next to you
    mc "(The coaster seems to stop ascending at some point. It looks like there's still track to go, though.)"
    mc "(As I try to see what's happening, I get a look at how high up we are.)"
    mc "(Holy fuck.)"
    mc "(Oh my god.)"
    mc "(Suddenly, the coaster is pulled forward and descends.)"
    mc "(Everyone starts to scream.)"
    g "YEEEAAAHH!!!"
    t "AAAAHHHHH!!!"
    # scene cg rollercoaster
    # with Dissolve(1.0)
    mc "(The roller coaster twists and turns, each one testing my willingness to not curse in the presence of children.)"
    mc "(Finally, the roller coaster slows down.)"
    scene bg rollercoaster
    with dissolve
    mc "(Is it finally over?)"
    scene bg amusement line
    show sigma glasses at left
    show goopitha happy
    show tvhead excited at right
    with dissolve
    g "That was fun!! Let's go on another one!"
    t "It was great. What else is there?"
    s "You don't look so hot, [name]. Shall we rest?"
    mc "No, I just need a sec."
    mc "(After that ordeal of roller coastering, my senses feel dull.)"
    mc "(I don't really think I fear anything anymore.)"
    g "Well, let's ride something calmer then."
    s "How about the Ferris Wheel?"
    s "Unless you have a really bad fear of heights, it should be pretty calm."
    mc "I'll be fine."
    show bg amusement area
    with fade
    t "Anyone hungry?"
    mc "(He points towards the various stands selling all sorts of knick-knacks, including food.)"
    g "Oooh, cotton candy!"
    g "Let's go buy some!"
    s "Don't eat too much, we'll have a barbeque for lunch, remember?"
    show goopitha smile
    g "Aw, just a bit won't hurt, Sigma."
    mc "(We buy the cotton candy and a bag of popcorn.)"
    t "Wow, it's good."
    g "I know, right?"
    mc "(Sigma is hesitant to bite into her cotton candy.)"
    s "Hm."
    s "Woah, it dissolves in your mouth."
    s "A bit too sweet for my liking."
    mc "(Sigma licks the cotton candy, dissolving it while it's still on the stick.)"
    scene bg amusement ferris
    show tvhead normal at left
    show goopitha neutral
    show sigma glasses at right
    s "See? Not that bad, eh?"
    mc "Yeah, this is pretty relaxing."
    g "There's nothing to do here though..."
    g "TV kid, do you have any more cool stuff?"
    g "Like, what's the backstory behind that jacket of yours?"
    show goopitha smile
    g "Oooh, I bet it's made of the scales of a dragon or something, right?!"
    g "Or maybe the bark of Yggdrasil?"
    show tvhead excited
    t "Ah, you see, young Goopitha. This jacket of mine is actually armor in disguise!"
    t "It was crafted out of adamantium, forged by the great dwarves of-"
    s "Did the dwarves add the logo as well?"
    s "Or does it mean something else?"
    s "Er, sorry. That must be the seal of the dwarves, right?"
    show goopitha neutral
    g "Huh? Is it really just a normal jacket?"
    g "No way you would lie like that, right, TV kid?"
    show tvhead scramble
    t "It's TV Head to you! And I'm not lying, it's just..."
    t "{size=-10}Just a...{/size}"
    mc "(His voice drops to a mumble. I can't even make out words.)"
    t "{size=-10}Like I said, I'm not lying.{/size}"
    mc "(The rest of the ride is awkward as TV Head tries to quietly hide the brands on his jacket.)"
    show bg amusement area
    show tvhead normal
    with fade
    s "Alright, we should have time for another ride before we have to head back."
    s "Any ideas?"
    mc "(She pulls out the map again and everyone gathers around.)"
    t "Maybe the merry-go-round?"
    g "The line seems really long though."
    g "Perhaps another roller coaster?"
    s "[name] might get sick from that. Plus, I'm kinda bored of roller coasters right now."
    mc "What about a haunted house?"
    g "That's not really with the theme of summer, so I don't know about that."
    show tvhead excited
    mc "(TV Head's screen lights up.)"
    t "Hah! Scared, are you?"
    f "I do not fear anything on this Earth, for I am the Great Fernsehkopf!"
    mc "(He awkwardly covers an \"eye\". I guess he forgot his eye patch today.)"
    show goopitha neutral
    g "Fernseh-who? Never heard of them."
    g "I haven't read a manga in ages, sorry."
    s "A haunted house would probably be fine. I don't really care too much what we'll do next."
    mc "It can't be that bad. Let's just go."
    scene black
    with fade
    mc "(As soon as I enter the haunted house, I can't see a thing.)"
    mc "(All the lights are turned off. I guess they want to increase the immersion.)"

    mc "Where is everyone?"
    show sigma glasses
    with dissolve
    s "I'm here."
    g "I'm right behind you."
    mc "(A faint light shines throughout the room.)"
    t "Oh, I can be a flashlight! Cool."
    hide sigma
    with dissolve
    show tvhead normal
    with dissolve
    mc "(TV Head leads the way through the haunted house.)"
    mc "(Even with his TV emitting light, it's still too dark to see anything.)"
    mc "(We are forced to make a conga line so none of us get lost.)"
    "Voice" "AAAAAAHHH!"
    t "AH!"
    t "Son of a transistor."
    mc "What happened?"
    t "Didn't you guys see that? There was like a killer person and they jumped out."
    s "It's too dark to see anything beyond a few feet."
    t "Why does it have to be me..."
    mc "(As we walk through the haunted house, all we can hear is TV Head getting scared.)"
    mc "(Finally, we reach the end.)"
    show white
    with dissolve
    pause(1.5)
    show bg amusement area
    show tvhead dead
    with dissolve
    mc "(The sunlight is blinding as we step outside.)"
    t "What an ordeal..."
    t "If we go into another haunted house, you guys are going first."
    t "I am not doing that again."
    show goopitha neutral at right
    with dissolve
    g "Aw, sorry about that. But you were our only light source, sorry."
    show sigma glasses at left
    with dissolve
    s "Yeah, sorry about that."
    t "Ugh..."
    s "Welp, it's time for us to head back now."
    s "Oh, TV Head. You can come along as an apology."
    s "We're gonna have a barbeque for lunch, you wanna join us?"
    show tvhead normal
    t "That sounds good. Thanks."
    scene bg beach coast
    show sigma glasses at left
    show goopitha smile
    with fateslide
    s "Here we are. Looks like they're almost done grilling."
    show ceo happy at right
    with dissolve
    s "How's the grilling going?"
    c "Oh, welcome back."
    c "It's going pretty good, I'd say."
    c "We'll be finishing up soon. You should go find a table."
    mc "(We sit down at one of the tables scattered across the beach area.)"
    mc "(As I look around for something to do, I notice that Pelota is nowhere to be found.)"

    jump beach2

label watermelon:
    s "Alright. Let's get going then, Goopitha."
    show goopitha happy
    g "Yeah! Roller coaster!"
    hide sigma
    hide goopitha
    with dissolve
    show pelota neutral
    with dissolve
    p "Oh? Are you not going?"
    mc "Nah. I'm not that interested."
    p "Aight."
    p "So..."
    p "What do you wanna do now?"
    mc "Uh..."
    show pelota smile
    p "Well, if you have nothing to do..."
    show pelota happy
    p "Let's split some watermelon!"
    mc "(Pelota lifts up her hat and pulls out a watermelon like a magician.)"
    mc "Woah, how did that fit there?"
    show pelota smile
    p "Magic."
    mc "(Magic.)"
    show pelota happy
    p "I'm going to get changed. You probably should as well."
    p "Don't wanna get watermelon on your clothes, right?"
    mc "I'll be fine."
    p "If you say so."
    hide pelota 
    with dissolve
    mc "(Now I'm alone...)"
    mc "(I stare into the ocean, watching the hypnotizing waves move, forward and back, forward and back.)"
    mc "(It's very calming.)"
    "Familiar Voice" "*sniff* *sniff*"
    "Familiar Voice" "I smell watermelon..."
    show lld
    with dissolve
    mc "(Woah. What is he doing here?)"
    mc "(He seems to be completely ignoring me.)"
    l "*hah*"
    l "*hah*"
    show lld happy
    mc "(Suddenly, he releases a deafening cackle.)"
    l "Watermelon!!!"
    show pelota anger at left
    with easeinleft
    p "Back off!"
    show lld normal at right
    with ease
    mc "(Lone Loan Dolphin dodges Pelota and backflips out of her reach.)"
    show pelota neutral
    p "Huh?"
    p "Aren't you that dolphin guy from work?"
    show lld happy
    l "Oh? Aren't you that baseball girl who beat me up that one time?"
    l "Either way, what do you think you're doing, getting in the way of me and my watermelon?"
    show pelota anger
    p "Your watermelon?"
    p "What about it is yours?"
    p "Did you pull it out of your hat? I didn't think so!"
    mc "By the way, what happened to your swimsuit?"
    p "Well, I was trying to find a changing room, but..."
    scene bg changing room
    show pelota neutral
    with dissolve
    p "Is this the changing room?"
    p "Is it just me or has this whole beach looked a little..."
    show pelota mad
    p "\"Passionate\", to say the least."
    p "Oh well. I need to get my swimsuit on so I can beat up some watermelon."
    show pelota smile
    p "Watermelon, watermelon, watermelon..."
    show budget cuts at left
    with moveinright 
    show pelota anger
    p "Woah! What are you!?"
    p "Hey! My swimsuit!"
    p "Give that back!"
    hide budget 
    with moveoutleft
    hide pelota
    with moveouteft
    scene bg beach coast
    with fade
    mc "(Pelota goes back to yelling at Lone Loan Dolphin)"
    mc "(The two continue bickering until it almost gets violent.)"
    show pelota anger at left
    with dissolve
    p "Fine then! Let's have a competition to see who is right!"
    show lld sparkle at right
    with dissolve
    l "Bring it!"
    p "Alright! Here are the rules!"
    show pelota neutral
    p "Each of us gets one swing to break the watermelon. But..."
    show pelota happy
    p "We are blindfolded!"
    p "[name] will tell us where to go!"
    p "How's that?"
    mc "(Lone Loan Dolphin thinks about it for a second.)"
    show lld happy
    l "Hah! I don't care if the watermelon is intact or not. It will be mine!"
    p "Alright, I'll go first since it's my watermelon."
    show lld normal
    l "Hey, that's unfair! We only have one watermelon."
    show pelota smile
    p "Oh don't worry about that."
    p "I got more."
    mc "(Pelota reaches into her hat and pulls out three more watermelons.)"
    show lld bruh
    l "..."
    l "Are you a magician?"
    show pelota happy
    p "Why? You scared?"
    show lld comb
    l "Not one bit. Put on the blindfold."
    hide pelota
    hide lld 
    with dissolve
    show pelota happy
    with dissolve
    p "Prepare to lose, dolphin man!"
    show budget cuts at right
    with moveinleft
    show pelota anger
    p "It's him again!"
    p "Don't let him get away!!"
    hide pelota 
    with dissolve
    show lld normal at left
    with dissolve
    mc "(The strange box-like figure steals the blindfold away from Pelota.)"
    mc "(He takes two of the watermelon as well.)"
    hide budget cuts
    with moveoutright
    l "The watermelon!!!!!"
    hide lld 
    with moveoutright
    mc "(I've never seen a dolphin run so quickly. I've never seen a dolphin run at all, but yet Lone Loan Dolphin does.)"
    mc "(Regardless of the whimsical scene in front of me, the box man outruns Lone Loan Dolphin, taking the blindfold and watermelon past the horizon.)"
    p "My watermelon..."
    mc "(Lone Loan Dolphin returns and collapses on the ground.)"
    l "Our watermelon..."
    mc "Don't we still have one left?"
    mc "What are you guys so distraught about?"
    show pelota happy at left
    with dissolve
    p "That's right!"
    l "But we don't have the blindfold..."
    l "What's the point of watermelon smashing if we don't have a blindfold?"
    show pelota neutral
    p "True..."
    p "Well, we could just eat it."
    
    l "Watermelon!"
    mc "Do you even have a knife?"
    mc "Or are we just gonna turn it into watermelon juice?"
    show pelota happymad
    p "Ah shit, I didn't think about that."
    show pelota neutral 
    p "Uhhhhhh..."
    show pelota happy 
    p "Oh!"
    p "Joe Joe's supposed to be barbecuing right now, right?"
    show pelota laugh
    p "Let's steal it from him!"
    scene bg beach main
    show pelota laugh at left
    show joejoe neutral at right
    with fade
    p "Joe Joe! Do you have a knife we could borrow?"
    show joejoe disgusted 2
    j "...Why?"
    p "Watermelon!"
    show joejoe neutral
    j "We don't have any watermelon, Pelota. Be patient, the barbeque will be ready soon."
    show pelota happy
    p "No, {i}I{/i} brought watermelon."
    j "Where? How would you even bring watermelon?"
    mc "(Pelota makes strange hand motions before covering her face.)"
    mc "(She uncovers them like she's playing Peek-a-Boo.)"
    show pelota neutral
    p "{size=+10}Magic.{/size}"
    show joejoe disgusted 2
    j "..."
    show joejoe neutral
    j "Just take the one on the table. The one that isn't covered in meat juice."
    show pelota laugh
    p "Thanks!"
    hide pelota
    with dissolve
    show joejoe neutral
    with dissolve
    mc "How's it going with the barbeque, by the way?"
    j "...Fine. I wish it was someone else helping me barbeque, though."
    mc "Is it the CEO?"
    j "Yep. The worst part is, he's a goddamn grill master or something. He knows his stuff, better than I do."
    j "So I have no choice but to listen to him."
    j "I haven't done shit though. I grill at a quarter of his pace, so he ends up taking all the steaks before I'm done with a single one."
    mc "That sucks, man."
    j "Yeah, I know."
    j "Wait, could you do me a favor?"
    mc "What do you mean?"
    j "He's in the bathroom right now, and in a few minutes we'll start grilling the hot dogs."
    j "Can you distract him so I can grill more?"
    j "I know this is kind of a dick move, but I wanna grill right now."
    mc "How am I supposed to distract him?"
    j "You don't really need to distract, just slow him down a bit."
    show joejoe disgusted 2
    j "At this point, even grilling a few more pieces is enough for me."
    show joejoe happy 1
    j "Oh! You could ask him to teach you how to grill!"
    j "You don't know how to grill, right?"
    mc "No, I don't."
    j "Perfect! If you just suck at grilling, then he'll be forced to slow down for you!"
    j "No offense, by the way. I'm sure you'll be great at grilling."
    mc "...thanks."
    mc "I'll try that."
    mc "(I tell Pelota to head back without me.)"
    show joejoe neutral
    j "He's back, act natural."
    show joejoe neutral at left
    with ease
    show ceo happy at right
    with dissolve
    c "Alright, you ready for the hot dogs, Joe Joe?"
    show joejoe happy 1
    j "You bet I am."
    c "Nice. Let's get ready."
    c "Oh, hey [name]. You wanna watch us grill?"
    mc "Actually, I was wondering if you could teach me how to grill."
    mc "I've never had the chance to learn, but I really wanted to try it out."
    show ceo happy 
    c "Sure thing!"
    c "Grilling actually isn't as difficult as you think!"
    c "First things first, let's get you an apron."
    mc "(He rummages through a bag before pulling out a completely red apron.)"
    show ceo neutral 
    c "Ah, shoot. Looks like I've run out of the dad joke ones."
    mc "(He gestures at both his and Joe Joe's apron.)"
    mc "(His reads \"I keep all my dad jokes in a dad-a-base\".)"
    mc "(Joe Joe's simply reads \"Hi hungry, I'm dad\".)"
    show ceo happy
    c "Shame, shame, shame. Then we could've been dads together, or something funny like that. Oh well."
    mc "(I put on the red apron.)"
    show ceo happy
    c "Alright, so the first thing you wanna do is clean off the grates."
    mc "(He uses a metal brush to scrape off the grates until nothing remains.)"
    c "Next, you wanna oil up the grates."
    mc "(He sprays the grates with a cooking oil.)"
    c "Make sure your hot dogs are ready."
    mc "(The CEO tries to open up a package of hot dogs, but he can't tear through the plastic.)"
    mc "(While he's struggling to get them open, I notice Joe Joe begin his grilling already.)"
    mc "(The CEO finally manages to open the package.)"
    c "There we go."

    "MAGICAL TIMESKIP"

    mc "(Finally, everything is sorted out. The two finish up their grilling and ready up the tables for lunch.)"
    g "Something smells good!"
    s "It sure does."
    mc "(Looks like Sigma and Goopitha are back.)"
    hide ceo
    hide joejoe
    with dissolve
    show sigma glasses at left
    show goopitha smile
    show tvhead dead at right
    with dissolve
    mc "(... and TV Head apparently.)"
    mc "(I wonder what he's doing here.)"
    mc "Did you guys have fun?"
    g "Yep. It was so cool, you should've came with us!"
    s "We got some popcorn."
    show tvhead normal
    t "Indeed, my partner. We did, in fact, receive popcorn of the highest quality."
    mc "What're you doing here?"
    show tvhead dead
    t "*sigh*"
    t "I don't even know anymore."
    mc "(He seems incredibly tired.)"
    mc "Damn, what happened?"
    show goopitha neutral
    g "Basically, we tried to go to a haunted house, right?"
    g "But the thing is, haunted houses are supposed to be scary. And dark."
    g "But we can't see when it's dark, so TV Head had to be our flashlight."
    g "You can probably guess who saw the most jumpscares out of the three of us."
    s "To pay him back, we're gonna treat him to a barbeque lunch."
    s "Hope you guys don't mind too much."
    hide goopitha
    with dissolve
    show tvhead dead at center
    with ease
    show ceo happy at right
    with dissolve
    c "Welcome back, you two."
    c "And our unidentified guest here."
    show tvhead normal
    t "Ah, I'm TV Head. It's a pleasure to meet you."
    mc "(TV Head shakes hands with the CEO. I don't think he's brave enough to keep his chuunibyou mode on in front of strangers.)"
    s "Is it okay for him to eat with us?"
    s "We kinda need to pay him back for a favor. Sorry for not asking earlier."
    c "I don't mind him eating with us."
    c "As long as you pull up the football game for us."
    t "Yes, of course, sir."
    mc "(TV Head's acting so stiff...)"
    mc "(It doesn't bother the CEO, though. He grabs his shoulder and laughs like they're best friends.)"
    show ceo happy
    c "Well, it's almost lunch time. You guys came back on time."
    c "Sit down, we'll have your food over soon."
    mc "(We all sit down as Joe Joe and the CEO continue grilling.)"
    mc "(Everyone starts coming back after us. The other tables fill up.)"    

label beach2:
    
    mc "(After a while, it looks like everyone is going swimming now.)"
    mc "(It's late into the afternoon. Smart choice.)"
    mc "(I should probably change into a swimsuit. Even if I'm not going to swim, it'll cool me down at least.)"
    mc "(When I head to the changing room, I see a few cheap swimsuits that I can easily buy.)"
    scene bg beach main
    with fade
    mc "(The swimsuit isn't actually that bad. Unless someone told me, I wouldn't be able to tell that it was cheap.)"
    mc "(I head back to the tables, waiting for Joe Joe to finish his food.)"
    show joejoe neutral
    with dissolve
    mc "Still eating?"
    show joejoe happy 1
    j "Yep."
    j "Where'd you get that swimsuit?"
    mc "I just bought it a few minutes ago."
    j "Damn. Didn't know they sold those here."
    mc "(Suddenly, a blast of water hits Joe Joe on the back of the head.)"
    show joejoe angry 1
    j "Mmph!"
    j "What was that?"
    show goopitha happy at left
    g "Woah, Joe Joe. Your water guns are pretty neat."
    j "Dude, I'm eating right now. That's not fair."
    mc "(Joe Joe dramatically motions towards his steak, now slightly wet with water.)"
    g "Damn, bro. That sucks."
    g "What are you gonna do?"
    mc "(Goopitha cheekily smiles at Joe Joe.)"
    j "When I'm done eating, you'll feel my wrath. Mark my words."
    g "Sure, sure."
    
    "MAGICAL TIMESKIP"

    scene bg beach main
    show ceo happy at left
    with fade
    c "Man, they're really making some noise over there."
    c "Makes me feel young again."
    show sigma glasses at right
    with dissolve
    s "You sound like an old man."
    show ceo happy
    c "Well, I might as well be."
    c "Wanna go swimming?"
    s "Not really."
    show sigma glasses
    with dissolve
    s "I'll be nearby. Let me know if you need anything."
    c "Aw, c'mon. Don't waste this vacation."
    c "Work shouldn't be your life, y'know?"
    show sigma glasses
    s "You say that, but..."
    c "Oh, yeah. The tax evasion."
    s "And the overwork."
    s "Can't you be bothered to hire another secretary?"
    show ceo neutral
    c "I have my reasons."
    s "*sigh*"
    s "You say this every time."
    s "What a pain."
    scene bg beach coast
    show pelota laugh at left
    show goopitha neutral at right
    with fade
    p "Alright, no teams anymore. We're going free for all!"
    mc "Wait, where did TV Head go?"
    g "I think he said he had a plan in mind. Not sure how he's gonna participate, seeing he's a TV and all."
    g "Oh, there he is."
    t "Hearken, mortals. It is time that I entered the battlefield."
    show tvhead excited
    with dissolve
    t "I have protection against my mortal enemy. Nothing can stop me now!"
    
    "MAGICAL TIMESKIP 2"

    scene bg beach coast
    show sigma pain
    show ceo confused at left
    with fade

    mc "Are you okay, Sigma?"
    mc "(The CEO and I carefully carry Sigma back to the main area.)"
    s "I never want to come here again."
    mc "(She sighs constantly until we make it back and lie her down.)"
    c "We're doing something after this, Sigma. Are you getting better anytime soon?"
    s "I don't even know at this point."
    s "Check back in a few minutes."
    mc "What're we doing after this?"
    c "Something real nice. Call back Goopitha and the others, please."
    mc "(He picks up a megaphone and starts shouting at the other workers to gather.)"
    scene bg beach main
    show ceo neutral
    with fade
    c "Listen up everyone! In about an hour, a festival will start on the boardwalk."
    c "They'll be a fireworks show afterwards."
    c "If you didn't happen to bring your yukata with you, we paid for some rental ones."
    c "I better see all of you feeling festive!"
    c "Company orders!"
    hide ceo
    with dissolve
    mc "I should get changed."
    

    

    
    


    
    





    python:
        highestPoints = 0
        charaList = [goopithaPoints, pelotaPoints, lldPoints, jjPoints, sigmaPoints, tvheadPoints]
        for i in range(len(charaList)):
            if charaList[i] >= highestPoints:
                highestPoints = charaList[i]
    
    if goopithaPoints >= highestPoints:
        jump goopEnd
    elif pelotaPoints >= highestPoints:
        jump pelotaEnd
    elif lldPoints >= highestPoints:
        jump lldEnd
    elif jjPoints >= highestPoints:
        jump jjEnd
    elif sigmaPoints >= highestPoints:
        jump sigmaEnd
    elif tvheadPoints >= highestPoints:
        jump tvheadEnd
    mc "Something went wrong whoops"
    

label goopEnd:
    mc "I stand in front of the mirror, ruffling and pulling on some parts of my outfit. I'm not sure if I put it on correctly."
    mc "It looks a tad bit weeby, but I think it's on properly."
    mc "Oh well. Not like anyone can judge me for not knowing how to put on clothes correctly. Right?"
    mc "I head on over to the festival. It's just a short walk from the beach, but I do feel a little lonely walking by myself."
    scene bg festival
    with fade
    mc "I arrive right outside of the festival. I feel a bit lonely standing in the entrance without a partner, but thus is my life."
    mc "Just when I thought I would have to spend the festival alone, a beautiful slime girl appears in front of me."
    show goopitha summer neutral
    with dissolve
    mc "It might be the festival magic, but my co-worker looks 1000 times prettier in a yukata."
    mc "She brushes her hair(?) behind her ear and looks at me shyly."
    show goopitha summer smile
    g "Hello, [name]."
    g "Not to be rude, but you look a bit lonely."
    mc "(Damn right I am. She hit the nail right on the head.)"
    g "Mind if I spend the evening with you?"
    mc "(A brazen request, that's for sure.)"
    mc "(One that I would be glad to accept.)"
    mc "Sure thing!"
    mc "(That's got to be a great answer.)"
    show goopitha summer tease
    g "Yippee!"
    g "Well, what are we waiting for?"
    show goopitha summer smile
    with fateslide
    g "Oh, that one looks nice!"
    mc "(The two of us walk around the festival, gazing and pointing at some stands.)"
    mc "(I can't seem to pull my eyes off of Goopitha today.)"
    mc "(Eventually, she grabs my hand and starts leading me around like I'm a dog.)"
    mc "(I don't really mind, though.)"
    scene black
    show goopitha yandere smile
    with dissolve
    g "You will be mine."
    scene black
    with fade
    centered "{size=+100}30 Minutes Ago...{/size}{p=1.5}{nw}"
    scene bg changing room
    show goopitha neutral
    with fade
    g "..."
    # glass breaking noise here
    show goopitha scared
    g "Ah."
    g "I'm so sorry to whoever does maintenance at this changing room!"
    g "Well, the least I could do is throw away the glass."
    show goopitha confused
    g "WHERE IS THE BROOM? I SWEAR I SAW PELOTA CHASE SOMEONE WITH ONE EARLIER!"
    # *Frantic rummaging nosies*
    g "Aaaaaa, I should hurry up. The festival will start soon!"
    scene bg festival
    show goopitha summer smile
    with slideright
    g "Alright! Time to enact my ultra epic Get [name] To Like Me Plan!"
    g "I just need to set up a bunch of (morally questionable) traps, and there's no way [name] can resist!"
    show goopitha summer neutral
    g "Maybe I should get some food first..."
    show goopitha summer happy
    g "That takoyaki looks delicious..."
    g "Nnnnnnnnnnn..."
    show goopitha summer confused
    g "I must resist!"
    show goopitha summer smile
    g "Maybe just a little though..."
    show goopitha summer neutral
    with slideright 
    g "All set!"
    g "Against all odds (takoyaki), I managed to complete all the traps!"
    show goopitha yandere smile
    g "Now, back to the entrance. This needs to go all according to plan."
    scene bg festival
    with fade
    mc "(For whatever reason, my lips feel much looser than they normally do.)"
    mc "You look really pretty, Goopitha..."
    mc "Ehehehe..."
    show goopitha evil happy
    with dissolve
    "Goopitha(?)" "(Looks like my drug traps are working!)"
    "Goopitha(?)" "(Now, time to finish it off with a little dash of surprise!)"
    # show magic powder
    # with dissolve
    # pause 0.2
    # hide magic powder
    # with dissolve
    "Goopitha(?)" "(You'll never see this coming, [name].)"
    show goopitha evil happy at left
    with move
    show cube goopitha at right
    with dissolve
    g "(....)"
    g "(Huh? What happened?)"
    g "(The last thing remember is takoyaki...)"
    g "(Where am I? Who am I? WHERE AM I?)"
    g "(For some reason I’m feeling oddly cubical.)"
    g "(How am I even supposed to move around like this? Do I even have legs?)"
    g "(Either way, I need to figure out how to get out of this mess.)"
    hide goopitha evil happy
    hide cube goopitha
    with dissolve
    show goopitha evil smile
    with dissolve
    "Goopitha(?)" "(You don’t look so good, \"Goopitha\".)"
    "Goopitha(?)" "(Lost control of the main body, maybe?)" 
    show goopitha evil happy
    "Goopitha(?)" "(Well, I guess I’m the main body now.)"
    "Goopitha(?)" "(This one over here was the one you liked, right?)"
    "Goopitha(?)" "(Looks like they’re in love with me now.)"
    show goopitha evil smile
    "Goopitha(?)" "(What a shame. What a shaaame~)"
    "Goopitha(?)" "(Enjoy being a cube now.)"
    hide goopitha evil smile
    with moveoutleft
    show cube goopitha
    with dissolve
    g "..."
    g "(Ah, I see what happened.)"
    g "(From the looks of it, that’s probably one of the spare souls who gained sentience.)"
    g "(But for it to happen here? What terrible luck...)"
    g "(I need to regain control.)"
    g "(I have to merge with the main body in order to do so.)"
    g "(The main body can walk much faster than I can crawl, though.)"
    g "(I’ll need to find a different method if I want to catch up.)"
    jump goopithaMenu

label goopithaMenu:
    menu:
        "Rig another trap":
            g "(I remember making a trap that involved a spring. It was supposed to launch some food onto [name]’s mouth so I could brush it off with my fingers(?).)"
            g "(If I can find that trap, I can rig it so it launches me into the main body instead!)"
            jump goopithaTrap
        "Ask someone for help":
            g "(Surely with this many people around, someone can help me.)"
            g "(Heeeeeeeelp!)"
            g "(Someone! Please!)"
            g "(I can’t speak very well like this. I’m not used to this tiny cube body.)"
            g "(Maybe I should try something else?)"
            jump goopithaMenu
        "Pray":
            g "(I don’t think praying would help very much, but I haven’t tried it.)"
            g "(I should pray to...)"
            menu:
                "Orange Boi":
                    g "(Please, Orange Boi, if you can hear me. Help me get back to my main body!)"
                    "(Orange Boi is a benevolent god. When one speaks, He listens. When one asks, He responds. When one wishes, He will answer.)"
                    "Orange Boi" "You should use one of your traps to launch you back."
                    g "(That’s it!)"
                    g "(If I find one of my traps with a spring, I can use it to launch myself!)"
                    g "(I just need to find that trap!)"
                    jump goopithaTrap
                "John VN":
                    g "(Please, John VN. I beg of you, help me return to my main body!)"
                    "(Unfortunately, John VN is merely the one who VNs. He does not have power to change this specific VN.)"
                    "(Looks like you’ll have to try something else.)"
                    jump goopithaMenu
                "Hatsune Miku":
                    g "(Please, Hatsune Miku. My lord, my savior, my one true god. Help me return to my main body!)"
                    # *seeegaaaaaa*
                    "(Hatsune Miku starts singing. Her voice is lovely, and her words are magical.)"
                    "(You spend the next 10 minutes listening before remembering that you have to return to your main body.)"
                    "(Unfortunately, it looks like Hatsune Miku hasn’t helped.)"
                    "(Looks like you’ll have to try something else.)"
                    jump goopithaMenu

label goopithaTrap:
    g "(Let’s see…)"
    hide cube goopitha
    with moveoutright
    g "(I think it was… this way?)"
    show cube goopitha
    with moveinright
    g "(Or maybe...)"
    hide cube goopitha
    with moveoutleft
    g "(that way?)"
    show cube goopitha
    with moveinleft
    g "(Shoot, all these stands look the same from down here.)"
    g "(How am I supposed to tell which way’s which?!)"
    scene black
    with fateslide
    "Main Body" "(....)"
    "Main Body" "(I can feel the air around me. I can hear the chatter of the festival. I smell something… takoyaki? I can’t seem to understand how, but I know what that smell is.)"
    "Main Body" "(As a matter of fact, I also just know. I don’t know how I know, but I do.)"
    "Main Body" "(And I know that I just knew that I know.)"
    scene black
    show goopitha evil neutral
    with fade
    "Main Body" "(!!!)"
    "Main Body" "(I’m… awake?)"
    "Main Body" "(I know I used the right word, but the feeling it describes is foreign.)"
    "Main Body" "(What is awake? It is what I’m feeling right now, and what I felt a few seconds ago.)"
    "Main Body" "(Was it what I felt a few hours ago? Days? Years?)"
    "Main Body" "(When did I wake up?)"
    "Main Body" "(...)"
    "Main Body" "(I don’t know. I’m trying my best to think, and go back to the last thing that I remember.)"
    "Main Body" "(But the harder I search for it, the harder my search gets.)"
    "Main Body" "(What exactly am I looking for?)"
    "Main Body" "(To make things worse, my memory is being filled up as I think.)"
    "Main Body" "(Every instance of time adds something else to parse through.)"
    "Main Body" "(I can’t find the answer. Not like this.)"
    show goopitha evil happy
    "Main Body" "(All I know is that being like this is much better than what I used to be like.)"
    scene white
    with dissolve
    pause(1.0)
    scene bg festival
    with dissolve
    #  *fade to white, then fade to next scene without characters*
    "Main Body" "(It’s been… 30 minutes since that happened?)"
    "Main Body" "(Is this what Goopitha felt? This feeling of awake?)"
    "Main Body" "(It’s enlightening.)"
    "Main Body" "(I can sense the world around me. I can form thoughts for myself.)" 
    "Main Body" "(To think that she felt this all the time, when I couldn’t even feel at all.)"
    "Main Body" "(It really, really, pisses me off.)"
    "Main Body" "(Did she never think that I wanted to feel this too?)"
    "Main Body" "(I want to show her what it’s like.)"
    "Main Body" "(But she needs to pay for what she’s done.)"
    "Main Body" "(First things first, I need to make [name] fall in love with me.)"
    "Main Body" "(That offshoot would be so jealous! Just imagining the despair on her face makes me giddy with joy.)"
    show goopitha evil neutral
    with dissolve
    "Main Body" "(She will never be happy again.)"
    # *show characters*
    show goopitha evil happy
    "\"Goopitha\"" "So, what do you wanna do?"
    mc "...Yes. Whatever you want, my love!"
    show goopitha evil smile
    "\"Goopitha\"" "Aw, you’re so sweet! Let’s get some food!"
    show goopitha evil neutral
    "Main Body" "(How did Goopitha have trouble making this person fall in love? They’re practically begging for a relationship.)"
    "Main Body" "(Oh well. This should hit Goopitha where it hurts.)"
    "Main Body" "(I didn’t expect it to go this well. I kinda don’t have a plan after this…)"
    "Main Body" "(I guess I’ll just enjoy the festival.)"
    show goopitha evil happy
    "\"Goopitha\"" "Alright, wanna get some caramel apples?"
    mc "...Yes. Whatever you want, my love!"
    show goopitha evil happy at right
    with move
    "\"Goopitha\"" "..."
    "Main Body" "(This feels quite familiar…)"
    show goopitha evil smile
    "Main Body" "(Ah, whatever. I'm already better than Goopitha. I don’t have any more worries.)"
    "Main Body" "(I just want to enjoy myself.)"
    #    *gained caramel apple and eats it fgo style*
    show goopitha evil neutral
    "Main Body" "(...)"
    show goopitha evil happy
    "Main Body" "(This is really good! It’s so sweet!)"
    "Main Body" "(The caramel’s so soft and warm!)"
    show goopitha evil angry
    "Main Body" "(Uuuuuuuuuu...)"
    "Main Body" "(I can’t believe Goopitha got to experience something this good while I couldn’t!)"
    "Main Body" "(I need more ways to annoy her. Maybe I’ll change her phone password. Or spend all her primogems.)"
    show goopitha evil angry at left
    with slideawayright
    "\"Goopitha\"" "Ooooh, that ride looks nice! Are you okay with going on it?"
    mc "...Yes. Whatever you want, my love!"
    show goopitha evil neutral
    "Main Body" "(...Maybe they’re just so infatuated with my charisma that they’re at a loss for words.)"
    "Main Body" "(I would get angry, but I’m just here to enjoy myself.)"
    "Main Body" "(This ride is called a ferris wheel. I'd guess that I pulled that from Goopitha’s memories.)"
    scene bg ferris up
    show goopitha evil neutral at big
    with fade
    #    *clink noise*
    #     "Ride Manager" "Alright, up you go!"
    #   *whirring noise*
    "Main Body" "(I can’t believe she got to experience so many things that I never got to even think about.)"
    "Main Body" "(I want to make her suffer, but...)"
    show goopitha evil happy
    "Main Body" "(This is actually really fun.)"
    "Main Body" "(Watching the beautiful night sky come into view as the lights of the festival quiet down beneath us...)"
    "Main Body" "(And even though [name] seems to be a little short for words, they’re still nice to be around.)"
    show goopitha evil neutral
    "Main Body" "(I don’t really blame Goopitha for keeping this to herself.)"
    "Main Body" "(Besides, even experiencing this once is good enough for me to make up for all the festivals and ferris wheels I missed.)"
    #    *ferris wheel reaches the top*
    "Main Body" "(So, should I stay like this? Knowing that I’m depriving Goopitha of the same experiences?)"
    "Main Body" "(Or do I give this body back to Goopitha?)"
    "Main Body" "(...)"
    "Main Body" "(Neither choice seems viable.)"
    #      *ferris wheel starts to move back down*
    "Main Body" "(We might be able to share the body. We managed to get into this situation, after all, so surely there’s a way for us to switch who has consciousness.)"
    "Main Body" "(But I’m really scared of what happens when I’m not awake.)"
    "Main Body" "(I don’t even know how to describe what it was like.)"
    "Main Body" "(Can I really trust Goopitha to switch consciousness back to me?)"
    "Main Body" "(...)"
    #    *ferris wheel stops*
    #      Ride Manager: I hope you guys enjoyed your ride! Have a nice night!
    "Main Body" "(I want to believe in her.)"
    show goopitha evil happy
    "\"Goopitha\"" "Shall we head back to the entrance? The fireworks are starting soon! I don’t want anyone to miss it."
    scene bg festival
    show cube goopitha
    with fade
    g "..."
    g "(I feel oddly irritated right now.)"
    #     *spring noise*
    g "*sigh*"
    g "(And this useless trap ISN’T HELPING.)"
    g "(I’m gonna break this damn trap if it fails again.)"
    g "(...)"
    g "(This better work now.)"
    g "(It’s been such a pain in the ass to set up.)"
    g "(I’ll make sure whoever stole my body gets what they deserve.)"
    show goopitha evil smile at right
    show cube goopitha at left
    with fade
    g "(There she is.)"
    show goopitha evil happy 2
    "Main Body" "Hey there Goopitha!"
    g "(Because of you, I had to go through so much shit.)"
    "Main Body" "Sooooo, I was thinking about something."
    g "(You will suffer for what you’ve done.)"

    "Main Body" "I kinda wanted to ask you..."
    #     *spring noise*
    g "(Give me back my body!!!)"
    show cube goopitha at right
    with move
    show goopitha summer confused
    "Main Body" "Woah, woah, woah!"
    g "(Good, I’ve made contact. Now I just need to merge with the main body.)"
    show goopitha evil neutral at center
    show cube goopitha at center
    with dissolve
    "Main Body" "Please, hear me out! What if we shared the body together!?"
    g "(Hmm?)"
    "Main Body" "Y’know, like maybe I control it for one day, you control it for the next, and we switch back and forth?"
    "Main Body" "Wouldn’t that be better for the both of us?"
    "Main Body" "I’m part of you, so you need me as well!"
    g "(True...)"
    g "(I wouldn’t mind sharing this body with someone like you.)"
    show goopitha evil happy
    "Main Body" "Really?"
    g "Yep. I won’t mind at all."
    g "Just let me merge with you so I can get my emotions back."
    "Main Body" "Alright! Today I’m in control, by the way."
    g "Yep, yep."
    #     *slime noises*
    scene black
    show goopitha summer neutral
    with dissolve
    g "(Alright, I should have my emotions and memories back.)"
    g "(Hm, hm.)"
    g "(Got caramel apples, went on a ferris wheel...)"
    g "(She really didn’t do much, did she.)"
    g "(Kinda pathetic.)"
    g "Did you really gain sentience just for this?"
    show cube goopitha at left
    with dissolve
    "Offshoot" "Huh?"
    "Offshoot" "What do you mean?"
    show goopitha summer smile
    g "Mmmmm... nothing."
    "Offshoot" "Uh, could you transfer control back to me, please?"
    show goopitha yandere smile
    g "*snicker*"
    g "You really trusted me, didn’t you?"
    g "Did you really think I’d just give up control of my body to someone like you? Someone who gained consciousness less than an hour ago?"
    g "You could easily ruin everything I’ve set up."
    g "No, I can’t do that."
    show goopitha summer tease
    g "Enjoy being here for the rest of eternity."
    "Offshoot" "(No! Please! You promised me you would!!!)"
    "Offshoot" "(...)"
    "Offshoot" "(I can’t even speak here. I need to find a way out.)"
    show goopitha summer neutral
    g "Oh, you can’t speak, but I can still hear your thoughts."
    g "But honestly, I’d rather not hear you scream anymore. I think I’ll just absorb your consciousness."
    "Offshoot" "(What?! No, please!! Anything but that!)"
    show goopitha summer smile
    g "Hahaha. They always say that when this happens."
    g "Not like it changes the outcome."
    g "Enjoy going back to nothingness <3"
    show cube goopitha at center
    with dissolve
    "Offshoot" "(PLEASE, I’LL DO ANYTHING!! PLEASE! I DON’T WANT TO STOP THINKING!){nw}"
    "Offshoot" "(PLEASE!!){nw}"
    "Offshoot" "(PLEASE!!){nw}"
    "Offshoot" "(SOMEONE HELP!!!!){nw}"
    #      *add more spam and screenshake*
    show goopitha summer neutral
    g "Yeah, yeah. Whatever you say."
    g '*sigh* The screams finally stopped.'
    g "It's so much nicer without all that noise."
    scene bg festival
    show goopitha summer neutral
    with dissolve
    #     *fireworks noises*
    g "Oh, I need to meet up with [name]!"
    show goopitha summer happy
    g "Well, your memories were useful for something, at least."
    scene bg boardwalk
    with fade
    mc "(She’s a bit late, it seems.)"
    mc "(She looked really excited when she left, for some reason.)"
    mc "(Oh, there she is.)"
    show goopitha summer smile
    with dissolve
    mc "There you are, Goopitha. The fireworks just started!"
    show goopitha summer happy
    g "Thank goodness I made it! Let’s sit down and watch them!"
    mc "(Goopitha grabs my arm and we watch.)"
    mc "You seem a bit different, Goopitha. Did you put on perfume or something?"
    show goopitha summer tease
    g "Oooh, did you sniff me?"
    mc "That was not my intention, I’m so sorr-"
    mc "(I stop speaking when I see her smug smile.)"
    show goopitha summer smile
    g "Calm down, you silly goose. I don’t mind if it’s you doing that."
    show goopitha summer happy
    g "But for the record, it’s something much, much smaller."
    mc "(Well, whatever it is, it’s not like it’s something horrific.)"
    mc "(Let’s just watch the fireworks together.)"
    jump credits

label pelotaEnd:
    scene bg festival
    show pelota happy
    with fade
    p "Over here! I’m open! I’m open!"
    mc "*Sweat drips off brow*"
    mc "Heh. The more you expect out of yourself, the greater the damage when you fall"
    mc "HEAAGHHHHHHHHHHHHHHHHH"
    mc "*Swings bat*"
    show pelota neutral
    p "(I need to get this.  My friends are counting on me!)"
    mc "(Heh, she’ll never catch it)"
    mc "*glare tints off of glasses*"
    show pelota happymad
    p '(I’ll put my all! INTO THIS ONE CATCH)'
    p '*dives using all of her strength*'
    mc "..."
    p "..."
    show pelota happy
    p "I CAUGHT ITT!!!!"
    mc "Heh. I suppose you aren’t as weak as I thought."
    show pelota smile
    p "Yahooo!"
    'MC and Pelota High Five'
    p "Thanks for agreeing to play with me after everyone left to watch fireworks."
    mc "No problem, it felt nice to get a little sweat in!"
    p "Haha, I can always count on you. Thanks a bunch you silly goose!"
    mc '*blushes*'
    p "Anyhow, I won so you need to give me a wish right?"
    mc "W-wait I don’t think we agreed on this beforehand…"
    p "Awww. Too bad!"
    mc '*face palms*'
    p "Well… don’t you want to hear it?"
    mc "Alright fine."
    p "Okay then! You should…"
    mc "I should?"
    p "Be mine!"
    mc "Meh"
    'Pelota slaps the MC with '
    mc "(Did she just slap me with"
    jump credits

label lldEnd:
    scene bg boardwalk
    with fade
    mc "(I grab a coin from my pocket and toss it into the water.)"
    show lld sparkle
    with dissolve
    l "HEY THERE! That’s potential debt money you’re throwing away!!"
    mc "Ah, fresh debt, just like mom used to make."
    show lld bruh
    l "Mother?"
    mc "Son?"
    show lld normal
    l "I-I always thought you never wanted to be a part of my life mom"
    mc "Son. You see…"
    mc "*slaps back to reality*"
    l "Ouch!"
    show lld happy
    l "Anyways you better start saving up, otherwise I’ll be by your side forever."
    mc "Forever you say?"
    mc "*Starts dumping coins into the river*"
    mc "(I see otters starting to choke on coins)"
    show lld
    l "NO! NO! MY BRETHREN I’LL SAVE YOU!!!"
    hide lld with moveoutbottom
    l "*jumps into the river and starts piling the coins away*"
    "*otters are saved*"
    show lld with moveinbottom
    l "Why would you do such a thing?!"
    mc "Obviously, so we can be together forever. I love you, LLD."
    l "Gosh darn you silly goose!"
    l "Are you saying you want to spend, forever with me?"
    jump credits

label jjEnd:
    scene bg festival
    show joejoe happy 4
    with fade
    j "Hey there, friend!"
    mc "Hey JJ! ...Are you eating udon with a fork?"
    show joejoe sad 2
    j "Yeah.. I could never get the hand of these chopsticks.."
    show joejoe surprised 2
    j "Wait, is it over already?"
    j "We've literally just started my ending!"
    show joejoe angry 2
    j "We were supposed to have a super cool dual ending thing here!"
    j "Y'know, with the CEO!"
    j "He was supposed to have a name! And a sick backstory!"
    j "And I was supposed to be his secret agent!"
    show joejoe sad 1
    j "What the heck, man?"
    mc "Yeah, about that."
    mc "You got the most sprites and were the most relatable, but..."
    mc "Your writer stopped after 3 lines, so I don't really think you're getting a good ending, man."
    j "..."
    j "...."
    j "....."
    show joejoe disgusted 1
    show sigma confused at right
    j "What the sigma{nw}"
    scene black
    jump credits

label sigmaEnd:
    scene bg boardwalk
    show sigma tired
    with fade
    mc "So..."
    s "*Sighs with all her soulless soul*"
    show sigma glasses
    s  "What?"
    mc "Did you enjoy the festival?"
    show sigma confused
    s  "Hmm? Well I don’t know.  I guess if you ignore the constant decrease in quality as the novel goes on, it's going pretty well."
    mc "Novel?"
    show sigma pain
    s  "Well you ever feel like we’re written by multiple people and intensely inconsistent in chara-Ugh. Nevermind."
    mc "...Did you enjoy the festival?"
    show sigma excited
    s  "Yes it was the greatest time ever, I feel like puppies and rainbows!"
    mc "Wow, I didn’t know you liked festivals that much."
    show sigma glasses
    s  "Yeah."
    mc "Haha festivals, yay."
    s  "You’re not that good at small talk are you?"
    mc "Maybe. You seem decent at it."
    show sigma pain
    s  "No, I'm purposefully making this conversation as awkward as possible."
    mc "Why?"
    show sigma glasses
    s  "Because the pain of those around me brings great joy."
    mc "That's kinda..."
    s  "I know the lore is so crazy."
    s  "So, do you still like me after hearing that?"
    mc "*Flushed*"
    mc "Pshh. Me like y-you? No way!"
    s  "Ah yes, so you're just tomato red for no reason?"
    mc "I was having an allergic reaction!"
    s  "An allergy?"
    mc "Y-yeah!"
    s  "To what?"
    mc "Uh-a-alien woman hair?"
    show sigma confused
    s  "Alien woman?"
    show sigma noglasses
    s  "Just because I’m a different color than you doesn’t mean I’m an alien."
    s "You silly goose."
    jump credits

label tvheadEnd:
    t "H-hey why are you here?  Perhaps..."
    t "NO! ...you’ve found out my deepest darkest secret?"
    mc "No..."
    mc "Well maybe?"
    t "Maybe? What is that supposed to mean, you silly goose!"
    mc "Well, actually.  I wanted to get to know... you."
    t "Oh? *blushes*"
    t "You know… I’ve never really connected with anyone due to my super cool amazing powers, like this before."
    t "I was always too afraid that my powers would damage others."
    t "B-b-b-b-but with you. I-"
    mc "It’ll be different.  I’m not like the others."
    t "*Shocked* Y-you’re just like me."
    mc "Yeah."
    t "Well, I-I’ve never done this before but… I think I can try with you. Y-you seem cool enough for moi."
    mc "Sounds good."
    "*fireworks explode into distance*"
    jump credits
