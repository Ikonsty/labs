def calculate_borsch_ingredients(portions):
    def roundd(ingredient):
        if ingredient % 100 == 0:
            return ingredient
        else:
            return ingredient + 100 - ingredient % 100
    portions = int(portions)

    yal = int(roundd((700 / 8) * portions))
    bur = int(roundd((500 / 8) * portions))
    kar = int(roundd((500 / 8) * portions))
    mor = int(roundd((200 / 8) * portions))
    cyb = int(roundd((200 / 8) * portions))
    pom = int(roundd((300 / 8) * portions))
    kap = int(roundd((300 / 8) * portions))

    ingredients = [('яловичина', yal), ('буряк', bur), ('картопля', kar),
                   ('морква', mor), ('цибуля', cyb), ('помідори', pom), ('капуста', kap)]
    return ingredients
