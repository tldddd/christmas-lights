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
        Light("Candy Canes", 1, 1, "cc"),
        Light("Christmas Trees", 2, 2, "ct"),
        Light("Waving Santa", 3, 3, "ws"),
        Light("Snowman", 4, 4, "sm"),
        Light("Motorbike Santa", 5, 5, "ms"),
        Light("Ho ho ho santa", 6, 6, "hh"),
        # Light("", 7),
        # Light("", 8),
    }

    return lights


def setup_pins(lights: list[Light]):
    for light in lights:
        GPIO.setup(light.pin, GPIO.OUT)


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
