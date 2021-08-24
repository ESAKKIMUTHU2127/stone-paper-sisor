def on_button_pressed_a():
    global hand
    hand = randint(0, 2)
    if hand == 0:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    elif hand == 1:
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
    else:
        basic.show_leds("""
            # # . . #
                        # # . # .
                        . . # . .
                        # # . # .
                        # # . . #
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global lives
    lives += -1
    basic.show_number(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

hand = 0
lives = 3

def on_forever():
    if lives <= 0:
        while True:
            basic.show_icon(IconNames.SAD)
basic.forever(on_forever)
