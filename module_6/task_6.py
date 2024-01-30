from math import pi


def count_pizza_cost_per_m2(pizza: tuple) -> float:
    cm_area = (pi * pizza[0]**2) / 4
    return pizza[1] / (cm_area / 100**2)   # Return pizza cost per m^2


def main():

    pizza1 = (
        float(input("Anna ensimmäisen pizzan halkaisija (cm): ")),
        float(input("Anna ensimmäisen pizzan hinta (x.xx€): "))
    )

    pizza2 = (
        float(input("Anna toisen pizzan halkaisija (cm): ")),
        float(input("Anna toisen pizzan hinta (x.xx€): "))
    )

    pizza1_m2_cost = count_pizza_cost_per_m2(pizza1)
    pizza2_m2_cost = count_pizza_cost_per_m2(pizza2)

    if pizza1_m2_cost == pizza2_m2_cost:
        print(f"Pizzojen yksikköhinta hinta neliömetreinä on sama: {pizza1_m2_cost:.2f} €/m^2")
    else:
        if pizza1_m2_cost < pizza2_m2_cost:
            print(f"Ensimmäisen pizzan yksikköhinta neliömetreinä on alhaisempi: {pizza1_m2_cost:.2f} €/m^2")
        else:
            print(f"Toisen pizzan yksikköhinta neliömetreinä on alhaisempi: {pizza2_m2_cost:.2f} €/m^2")


if __name__ == "__main__":
    main()
