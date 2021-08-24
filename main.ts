input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    hand = randint(0, 2)
    if (hand == 0) {
        basic.showLeds(`
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        `)
    } else if (hand == 1) {
        basic.showLeds(`
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        `)
    } else {
        basic.showLeds(`
            # # . . #
                        # # . # .
                        . . # . .
                        # # . # .
                        # # . . #
        `)
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showNumber(0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    lives += -1
    basic.showNumber(0)
})
let hand = 0
let lives = 3
basic.forever(function on_forever() {
    if (lives <= 0) {
        while (true) {
            basic.showIcon(IconNames.Sad)
        }
    }
    
})
