import RPi.GPIO as GPIO


class Light:
    def __init__(self, name: str, id: int, pin: int, seq_code: str) -> None:
        self.name: str = name
        self.id: int = id
        self.pin: int = pin
        self.state: bool = False
        self.seq_code: str = seq_code


# Pin map
def load_lights() -> list[Light]:
    lights: list[Light] = {
        Light("Candy Canes", 1, 7, "cc"),
        Light("Motorbike Santa", 2, 11, "ms"),
        Light("Waving Santa saying (ho ho ho!!!!!!!)", 3, 12, "ws"),
        Light("Ho Ho Ho train", 4, 13, "hh"),
        Light("Dangling Lights", 5, 15, "li"),
        Light("FAT ( MADE BY IZZY) santa", 6, 16, "fs"),
        Light("Snowman", 7, 18, "sm"),
        Light(" Big fat OLLY gingerbread man", 8, 22, "gm"),
    }

    return lights


def setup_pins(lights: list[Light]):
    for light in lights:
        GPIO.setup(light.pin, GPIO.OUT)
        on(light)


def on(light: Light):
    print(f"Turning {light.name} ON.")
    set_light(light, True)


def off(light: Light):
    print(f"Turning {light.name} OFF.")
    set_light(light, False)


def set_light(light: Light, state: bool):
    gpio_value = GPIO.LOW
    if state == True:
        gpio_value = GPIO.HIGH

    GPIO.output(light.pin, gpio_value)
    light.state = state


def setup_gpio():
    GPIO.setmode(GPIO.BOARD)


def clean_gpio():
    GPIO.cleanup()
