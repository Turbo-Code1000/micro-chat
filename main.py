def on_pin_pressed_p0():
    global Radio_Group
    Radio_Group += 1
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    radio.send_string("Hi")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_string("I'm Hungry")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("Bye!")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    radio.send_string("Got it!")
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

Radio_Group = 0
radio.set_group(1)
item = 0

def on_forever():
    radio.set_group(Radio_Group)
basic.forever(on_forever)
