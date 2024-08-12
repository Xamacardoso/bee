def main():
    leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6];
    casos = int(input());
    for caso in range(casos):
        num = input();
        nleds = 0;
        for car in num:
            nleds += leds[int(car)];

        print(nleds, "leds");


main();