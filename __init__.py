import appconfig, time, hid, keycodes, keypad, display
#touchpads for future idea: 'pages' with e.g. ctrl, alt, shift 

#NOTE: THIS PROGARM DOES NOT WORK.
# it appears the writer does not understand Python
# the writer should learn the basics
# before stealing other people's code

print ("Configure what each button does")
# for inspiration, check:
# https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2
settings = appconfig.get("hotkeys", {
 "0" : {"vkey" : "F13", "modifier": "", "colour" : "#000011"},
 "1" : {"vkey" : "F14", "modifier": "", "colour" : "#000011"},
 "2" : {"vkey" : "F15", "modifier": "", "colour" : "#000011"},
 "3" : {"vkey" : "F16", "modifier": "", "colour" : "#000011"},
 "4" : {"vkey" : "F17", "modifier": "", "colour" : "#000011"},
 "5" : {"vkey" : "F18", "modifier": "", "colour" : "#000011"},
 "6" : {"vkey" : "F19", "modifier": "", "colour" : "#000011"},
 "7" : {"vkey" : "F20", "modifier": "", "colour" : "#000011"},
 "8" : {"vkey" : "F21", "modifier": "", "colour" : "#000011"},
 "9" : {"vkey" : "F22", "modifier": "", "colour" : "#000011"},
 "10" : {"vkey" : "F23", "modifier": "", "colour" : "#000011"},
 "11" : {"vkey" : "F24", "modifier": "", "colour" : "#000011"},
 "12" : {"vkey" : "V", "modifier": "MOD_LEFT_CONTROL", "colour" : "#000011"},
 "13" : {"vkey" : "Q", "modifier": "", "colour" : "#9A0011"},
 "14" : {"vkey" : "Y", "modifier": "", "colour" : "#009A11"},
 "15" : {"vkey" : "F1", "modifier": "", "colour" : "#0000BB"},
})

print ("initialise screen")
for z in range(0,16):
if settings[str(z)]["vkey"] != "":
	x, y = z % 4, int(z / 4)
	colour = int(settings[str(z)]["colour"].replace("#","0x"),16)
	display.drawPixel(x, y, colour)    
display.flush();
         
# Execute key press
def on_key(key_index, is_pressed):
    if is_pressed and settings[str(key_index)]["vkey"] != "":
		selectedkey = bytes([keycodes.vkey])
		modifier = bytes([keycodes.modifier])
		print ("pressed: " key_index, "returning: ", selectedkey)
		hid.keyboard_press_keys(selectedkey, modifier)
		time.sleep(0.1)
		hid.keyboard_release()

keypad.add_handler(on_key)
