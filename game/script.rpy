# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aurora")
define m = Character("Macius")

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


    
transform slightleft:
    xalign 0.2
    
transform slightright:
    xalign 0.8

transform left2:
    xalign 0.35
    
transform right2:
    xalign 0.65

transform under:
    xalign 0.5
    yanchor 0.0
    ypos 1.0
    
transform down:
    yanchor 0.5
    ypos 1.0
    xalign 0.35
    

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

    scene am 1:
        zoom 1.2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show aurora at center
    
    # These display lines of dialogue.

    m "Czy chcesz grac w ta gre?"
    
    menu:
        "Tak."
            jump odp_tak
        "Nie"
            jump odp_nie
    
    return
    
label odp_tak:
    show aurora at nod
    a "TAK! Bardzo mi się podoba ta gra."
    m  "fajnie"
    jump kontynuacja
    return
    
label odp_nie:
    a "NIE. Nie chcę grać. Bez sensu jest ona!!!! Ta gra."
    m "A szkoda. Bo chcę ją tworzyć."
    jump kontynuacja
    return

label kontynuacja:
    
    m "tylko mi się jej nie chce projektować"
    m ";_____;"

    # This ends the game.

    return
