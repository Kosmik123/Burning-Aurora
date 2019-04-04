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
    
    scene black
    
    "Oto jest historia Aurory Burning. Genialnej studentki, której losy jednak nie były tak genialne."
    pause 0.3
    "Po tym jak zdała maturę w wieku 16 lat rozpoczęła studia medyczne."
    pause 0.3
    "W wieku 18 lat pracowała już nad swoją pracą dyplomową."
    pause 0.3
    "Wszystko potoczyłoby się dobrze gdyby nie jej jeden problem."
    pause 0.3
    "Jednak ta tragiczna historia może potoczyć się inaczej dzięki twojej pomocy."
    pause 0.3
    "Od ciebie zależy to czy życie Aurory okaże się pasmem sukcesów czy może jednym wielkim piekłem."
    pause 0.3
    "Zanim jednak zadecydujesz o jej losie powiedz coś o sobie."
    pause 0.3
    menu:
        "Jak masz na imię?"
        
        "Maciupinder":
            jump maciupinder_story
    
        "Michał":
            jump michal_story
    return
