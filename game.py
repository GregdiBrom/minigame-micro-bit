def on_button_pressed_a():
    player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def OddPlayer_str():
    music._play_default_background(music.built_in_playable_melody(Melodies.WAWAWAWAA),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_string("" + str((LIFE)))

def on_button_pressed_ab():
    player.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

player: game.LedSprite = None
LIFE = 0
game.set_life(10)
LIFE = 10
player = game.create_sprite(2, 2)

def on_forever():
    if True:
        pass
    else:
        pass
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)

def on_forever3():
    pass
basic.forever(on_forever3)
