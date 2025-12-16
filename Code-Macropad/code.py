import board
import keypad
import rotaryio
import digitalio
import time
import usb_hid
import maps

# Initialisation de la touche rotative et de son bouton
button = digitalio.DigitalInOut(board.D6)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
encoder = rotaryio.IncrementalEncoder(board.D7, board.D8)

# Initialisation du keypad matriciel + Bouton power
km = keypad.KeyMatrix(
    row_pins=(board.D3, board.D4, board.D5),
    column_pins=(board.D0, board.D1, board.D2),
)
bouton_power = keypad.Keys((board.D9,), value_when_pressed=False, pull=True)

# Variables de suivi
current_map = 1 # Map par défaut
maps.set_led(current_map) # Met la LED à jour au démarrage
button_state = None
last_position = encoder.position


def traiter_evenement(event, source="matrix"):
    global current_map
    if event.pressed:
        if source == "matrix":
            print(f"Touche {event.key_number} pressée")

            if event.key_number == 0:
                current_map = 2 if current_map == 1 else 1
                maps.set_led(current_map)
                print(f"Map {current_map} active")
            else:
                if current_map == 1:
                    maps.map1_actions(event.key_number)
                else:
                    maps.map2_actions(event.key_number)

        elif source == "power":
            print("Bouton Power pressé (GPIO9)")
            maps.Eteindre_PC()


print("Map 1 active")
while True:
    event = km.events.get()
    if event:
        traiter_evenement(event, source="matrix")

    event2 = bouton_power.events.get()
    if event2:
        traiter_evenement(event2, source="power")

    # Gestion de l'encodeur rotatif
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            maps.cc.send(maps.ConsumerControlCode.VOLUME_DECREMENT)
        print(f"Volume - ({current_position})")
    elif position_change < 0:
        for _ in range(-position_change):
            maps.cc.send(maps.ConsumerControlCode.VOLUME_INCREMENT)
        print(f"Volume + ({current_position})")
    last_position = current_position

    # Gestion du clic sur l'encodeur
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Bouton de l'encodeur pressé.")
        maps.cc.send(maps.ConsumerControlCode.PLAY_PAUSE)
        button_state = "released"
    if button.value and button_state == "released":
        print("Bouton de l'encodeur relâché.")
        button_state = None
