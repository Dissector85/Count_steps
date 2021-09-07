input.onButtonPressed(Button.A, function () {
    basic.showString("" + (step))
})
input.onButtonPressed(Button.B, function () {
    step = 0
})
let step = 0
step = 0
radio.setGroup(1)
basic.forever(function () {
    if (input.acceleration(Dimension.Strength) > 1500) {
        step += 1
        music.playTone(262, music.beat(BeatFraction.Sixteenth))
        radio.sendString("" + (step))
    }
})
