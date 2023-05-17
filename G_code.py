def modify_temperature_gcode(gcode):
    modified_gcode = ""
    for line in gcode.split("\n"):
        if line.startswith("G1"):
            layer = extract_layer(line)
            temperature = calculate_temperature(layer)
            modified_line = line.replace(";", " T" + str(temperature) + " ;")
            modified_gcode += modified_line + "\n"
        else:
            modified_gcode += line + "\n"
    return modified_gcode

def extract_layer(line):
    # Extract the layer number from the G-code line
    # Modify this function based on your G-code format
    pass

def calculate_temperature(layer):
    if layer <= 20:
        return 180 + (layer - 1) * 0.5
    elif layer <= 80:
        return 190 + (layer - 21) * 1.25
    else:
        return 220

def modify_speed_gcode(gcode):
    modified_gcode = ""
    for line in gcode.split("\n"):
        if line.startswith("G1") and "F" in line:
            layer = extract_layer(line)
            speed = calculate_speed(layer)
            modified_line = line.replace("F", "F" + str(speed) + " ")
            modified_gcode += modified_line + "\n"
        else:
            modified_gcode += line + "\n"
    return modified_gcode

def calculate_speed(layer):
    if layer <= 20:
        return 100
    elif layer <= 80:
        return 100 + (layer - 20) * 2.5
    else:
        return 200

def modify_extrusion_gcode(gcode):
    modified_gcode = ""
    for line in gcode.split("\n"):
        if line.startswith("G1"):
            layer = extract_layer(line)
            extrusion_multiplier = calculate_extrusion(layer)
            modified_line = line.replace("E", "E" + str(extrusion_multiplier) + " ")
            modified_gcode += modified_line + "\n"
        else:
            modified_gcode += line + "\n"
    return modified_gcode

def calculate_extrusion(layer):
    if layer <= 20:
        return 1.0 + (layer - 1) * 0.02
    elif layer <= 80:
        return 1.0 + (layer - 20) * 0.05
    else:
        return 1.0

def modify_position_gcode(gcode, offset_x, offset_y):
    modified_gcode = ""
    for line in gcode.split("\n"):
        if line.startswith("G1"):
            modified_line = line.replace("X", "X" + str(offset_x) + " ").replace("Y", "Y" + str(offset_y) + " ")
            modified_gcode += modified_line + "\n"
        else:
            modified_gcode += line + "\n"
    return modified_gcode

# Example usage
gcode = """
G1 X10 Y20 ; Move to starting position
G1 Z0.2 ; Move to layer 1
G1 E1.0 ; Extrude filament
G1 F100 ; Set initial speed
; More G-code lines...
"""

modified_gcode = modify_temperature_gcode(gcode)
modified_gcode = modify_speed_gcode(modified_gcode)
modified_gcode = modify_extrusion_gcode(modified_gcode)
modified_gcode = modify_position_gcode(modified_gcode, offset
