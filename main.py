def on_button_pressed_a():
    basic.show_string("" + str((step)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global step
    step = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

step = 0
step = 0

def on_forever():
    global step
    if input.acceleration(Dimension.STRENGTH) > 1500:
        step += 1
        music.play_tone(262, music.beat(BeatFraction.SIXTEENTH))
basic.forever(on_forever)
