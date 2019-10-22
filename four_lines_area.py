
def lines_intersection(k1, c1, k2, c2):
    if k1 == k2:
        return None
    else:
        x = (c2 - c1) / (k1 - k2)
        y = (c2*k1 - c1*k2)/(k1 - k2)
        return (round(x, 2), round(y, 2))


def distance(x1, y1, x2, y2):
    r = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return round(r, 2)


def quadrangle_area(a, b, c, d, f1, f2):
    if 4.0 * f1**2 * f2**2 < (b**2 + d**2 - a**2 - c**2)**2:
        return None
    else:
        s = ((4 * f1**2 * f2**2 - (b**2 + d**2 - a**2 - c**2)**2))**0.5 / 4
        return round(s, 2)


def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):

    coef = [k1, k2, k3, k4]

    if coef.count(k1) == 3 or coef.count(k2) == 3 or\
            coef.count(k3) == 3 or coef.count(k4) == 3:
        return 0
    else:
        point_12 = lines_intersection(k1, c1, k2, c2)
        point_23 = lines_intersection(k2, c2, k3, c3)
        point_34 = lines_intersection(k3, c3, k4, c4)
        point_41 = lines_intersection(k4, c4, k1, c1)

        line12 = distance(point_12[0], point_12[1], point_23[0], point_23[1])
        line23 = distance(point_23[0], point_23[1], point_34[0], point_34[1])
        line34 = distance(point_34[0], point_34[1], point_41[0], point_41[1])
        line41 = distance(point_41[0], point_41[1], point_12[0], point_12[1])

        diag1 = distance(point_12[0], point_12[1], point_34[0], point_34[1])
        diag2 = distance(point_23[0], point_23[1], point_41[0], point_41[1])

        s = quadrangle_area(line12, line23, line34, line41, diag1, diag2)
        return s


#print(four_lines_area(0, 20, 3, -0.3, 0.1, 10, -5, 3))  # 74.43
#print(four_lines_area(5, -3, -0.35, 5, 0.5, -1.5, 0, 2))  # 9.1
print(lines_intersection(3, -0.3, -5, 3))
print(quadrangle_area(3, 4, 3, 3, 1, 1))