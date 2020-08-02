import hid, keycodes, time

# Presses ctrl+alt+delete
keys = bytes([keycodes.F1])
modifier = bytes([keycodes.MOD_LEFT_CONTROL & keycodes.MOD_LEFT_ALT])
hid.keyboard_press_keys(keys, modifier)
time.sleep(0.1)
hid.keyboard_release()
