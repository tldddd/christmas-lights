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
        Light("Christmas Trees", 2, 11, "ct"),
        Light("Waving Santa", 3, 12, "ws"),
        Light("Snowman", 4, 13, "sm"),
        Light("Motorbike Santa", 5, 15, "ms"),
        Light("Ho ho ho santa", 6, 16, "hh"),
        Light("Emtpy_7", 7, 18, "em7"),
        Light("Empty_8", 8, 22, "em8"),
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
    gpio_value = GPIO.HIGH
    if state == True:
        gpio_value = GPIO.LOW

    GPIO.output(light.pin, gpio_value)
    light.state = state


def clean_gpio():
    GPIO.cleanup()
