def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    print("First project")
    for celsius in (0, 20, 37, 100):
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} C = {fahrenheit:g} F")
