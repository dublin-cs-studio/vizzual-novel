label day6dream:
    python:
        highestPoints = 0
        dreamChara = -1
        sameValue = True
        charaList = [goopithaPoints, pelotaPoints, lldPoints, jjPoints, sigmaPoints, tvheadPoints]
        for i in range(len(charaList)):
            if charaList[i] == highestPoints and highestPoints != 0:
                sameValue = False
            if charaList[i] > highestPoints:
                sameValue = True
                highestPoints = charaList[i]
                dreamChara = i

    if sameValue == False:
        jump day7
    elif dreamChara == 0:
        jump goopDream
    elif dreamChara == 1:
        jump pelotaDream
    elif dreamChara == 2:
        jump lldDream
    elif dreamChara == 3:
        jump jjDream
    elif dreamChara == 4:
        jump sigmaDream
    elif dreamChara == 5:
        jump tvheadDream
    else:
        jump day7
    mc "Something went wrong whoops"

label goopDream:
    show goopita
    g "hello"
    jump day7

label pelotaDream:
    show pelota death
    p "hello"
    jump day7

label lldDream:
    show lld
    l "hello"
    jump day7

label jjDream:
    show joejoe disgusted
    j "hello"
    jump day7

label sigmaDream:
    show sigma noglasses
    s "hello"
    jump day7

label tvheadDream:
    show tvhead dead
    t "hello"
    jump day7