input.onPinPressed(TouchPin.P0, function () {
    Radio_Group += 1
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("Hi")
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString("I'm Hungry")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("Bye!")
})
input.onPinPressed(TouchPin.P1, function () {
    radio.sendString("Got it!")
})
let Radio_Group = 0
let item = 0
radio.setGroup(1)
basic.forever(function () {
    radio.setGroup(Radio_Group)
})
