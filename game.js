input.onButtonPressed(Button.A, function on_button_pressed_a() {
    player.move(-1)
})
function OddPlayer_str() {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Wawawawaa), music.PlaybackMode.InBackground)
    basic.showString("" + ("" + LIFE))
}

input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    player.change(LedSpriteProperty.Y, -1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    player.move(1)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
})
let player : game.LedSprite = null
let LIFE = 0
game.setLife(10)
LIFE = 10
player = game.createSprite(2, 2)
basic.forever(function on_forever() {
    if (true) {
        
    } else {
        
    }
    
})
basic.forever(function on_forever2() {
    
})
basic.forever(function on_forever3() {
    
})
