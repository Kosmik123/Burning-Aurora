# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aurora", color = "#ee1177")
define m = Character("Macius")
define p = Character("Profesor", color = "#1155ff", what_suffix = " Hej!")
define u = Character("???")
define s = Character("Starzec")


# To się razem stosuje do animacji wędrówki (2 tła łączące się ze sobą z lewej i prawej)
transform walk1:
    xanchor 0.0
    xpos 0.0
    linear 100/abs(walk_speed) xpos -1.0*walk_speed/abs(walk_speed)
    xpos 1.0*walk_speed/abs(walk_speed)
    linear 100/abs(walk_speed) xpos 0.0
    repeat
transform walk2:
    xzoom -1
    xanchor 0.0
    xpos 1.0*walk_speed/abs(walk_speed)
    linear 100/abs(walk_speed) xpos 0.0
    linear 100/abs(walk_speed) xpos -1.0*walk_speed/abs(walk_speed)
    repeat

transform default:
    xalign 0.5
    yanchor 0.8
    ypos 1.0 #:

transform center:
    xalign 0.5
    yanchor 0.8
    ypos 1.0

transform left:
    xalign 0.0
    yanchor 0.
    ypos 1.0

transform right:
    xalign 1.0
    yanchor 0.8
    ypos 1.0
    
transform slightleft:
    xalign 0.2
    yanchor 0.8
    ypos 1.0
    
transform slightright:
    xalign 0.8
    yanchor 0.8
    ypos 1.0

transform left2:
    xalign 0.35
    yanchor 0.8
    ypos 1.0
    
transform right2:
    xalign 0.65
    yanchor 0.8
    ypos 1.0

transform under:
    xalign 0.5
    yanchor 0.0
    ypos 1.0
    
transform down:
    yanchor 0.5
    ypos 1.0

transform nod:
    linear 0.2 yoffset 20
    linear 0.2 yoffset 0  

transform walking:
    pause renpy.random.randint(0,1)
    block:
        linear 0.8 yoffset 6
        linear 0.8 yoffset -6  
        repeat
# 


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show aurora at center
    
    # These display lines of dialogue.

    pause 0.5
    
    "Zapytasz mnie pewnie jak znalazłam się w takiej sytuacji w jakiej jestem."
    pause 0.5
    "No cóż... Moja historia jest krótka. "
    
    

    pause 1.0
    "Wszystko zaczęło się gdy mój profesor na uczelni dowiedział się o mojej przeszłości."
    show aurora at slightleft with move
    
    pause 0.3
    scene bg auditorium 
    show aurora at slightleft 
    with dissolve
    
    pause 0.5
    show professor smile:
        xalign 1.5
        yanchor 0.8
        ypos 1.0
    show professor at right2 with move
    #pause 0.4
    
    p "Oooo!! Panna Aurora. Dobrze widzieć studentkę taką jak pani."
    a "Dzieńdobry, panie psorze..."
    p "Dzieńdobry dzień dobry. U nas w górach to nie ma takich uprzejmych kobiet."
    a "Ooohh... Panie psorze..."

    menu:
        "Jestem zaszczycona":
            $podryw = False
            jump odp1
        "Czy pan mnie podrywa?":
            $podryw = True
            jump odp2
    
    return
    
label odp1:
    a "Jestem zaszczycona."
    a "Pańskie komplementy bardzo mi łechtają moje ego..."
    jump kontynuacja
    return
    
label odp2:
    a "Czy pan mnie podrywa?"
    p "Ależ gdzieżbym śmiał panno Auroro."
    jump kontynuacja
    return

label kontynuacja:
    
    p "Panno Auroro. Proszę spojrzeć co też się tam wyczynia!"
    a "Przecież tu biegnie jakiś człowiek!!!"
    p "Lepiej się odsuńmy."
   

    show aurora at right2
    show professor at right 
    with move
    
    show old walking:
        xalign -0.5
        yanchor 0.8
        ypos 1.0
    #
    
    u "Ojojoj! Moja stopa!!"
    
    pause 0.5
    show old at slightleft with move
    
    s "Moja stopa! Boli mnie moja stopa!!!"
    
    show aurora at center with move
    
    a "Proszę się zatrzymać! Pomogę panu."
    s "Już stanąłem. Co mam robić jak mi pani pomoże?!"
    a "Proszę się położyć. Zaraz obejrzę pana stopę"
    s "Okej"
    
    show old at down with move
    pause 0.1
    show aurora at down with move
    
    a "Hmmm... Co my tu mamy..."
    pause 0.5
    a "Hmmm...."
    
    pause 0.6
    a "Hmmmm.."
    
    pause 0.8
    a "Już wiem"
    
    pause 0.5
    s "Tak? I co to jest?"
    a "Ma pan chorą stopę."
    s "!!!"
    s "!!!!!!"
    s "!!!!!!!!!!!!"
    s "!!!!!!!!!!!!!!!!!!!!!!!!"
    s "!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!"
    s "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!"
    s "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    s "!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!"
    
    pause 0.3
    s "Wiedziałem. Tego się obawiałem."
    show old at slightleft
    show aurora at center
    with move
    s "Dziękuję pani auroro. To ja się zbieram."
    a "Spoko. Żegnam."
    
    show old:
        xzoom -1.0
    #
    s "Baju."
    pause 0.1
    
    show old:
        linear 1.0 xalign -0.5
    
    pause 1.0
    hide old
    
    show professor at slightright with move
    p "Łał..."
    p "Skąd pani się tak nauczyła medycyny?"
    a "No cóż."
    a "przyznam nieskromnie że na coś przydało się przedwczesne zaliczenie matury"
    a "Mam lat 18 i kończę już studia medyczne na Collegium Medicum Uniwersytetu Jagiellońskiego w Krakowie."
    a "Swoją drogą, bardzo polecam Collegium Medicum Uniwersytetu Jagiellońskiego w Krakowie."
    a "Studiuj na Collegium Medicum Uniwersytetu Jagiellońskiego w Krakowie i ty."
   
    p "{size=-8}Hyhyhyh taka młoda... idealnie się nadaje... Hyhyyh{/size}"
    a "Co?! Do czego się nadaje?"
    p "co? Nie!!!!!!!"
    p "Tak tylko do siebie."
    p "{size=-8}Muszę się pilnować z tym co mówię bo jeszcze się wyda jakie okropne rzeczy chcę jej uczynić... {/size}"
    p "A tymczasem dziękuję za wspólnie spędzony czas. Muszę już iść przygotować nóż do operacji..."
    
    if podryw:
        a "Okej. Następnym razem podrywaj inne dziewczyny stary kapciu!"
    else:
        a "Okej. Dziękuję za komplementy jakby co/"
    a "... i dowidzenia."
    
    
    show aurora:
        linear 1.0 xalign -0.5 
    
    show professor:
        linear 1.0 xalign 1.5

    pause 2.0
    
    "Dziękujemy za zagranie w demo  gry Burning Aurora. Dalsze losy sympatycznej bohaterki ukaże się w drugim demie gry"
    

    # This ends the game.

    return
