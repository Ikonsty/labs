def rps_game(lst):
    # S scissors R rock P paper
    #  S>P P>R R>S
    results = []
    for ro_nd in lst:
        if ro_nd[0] == ro_nd[1]:
            results.append((False, False))
        elif (ro_nd[0] == 'S' and ro_nd[1] == 'P')\
                or (ro_nd[0] == 'P' and ro_nd[1] == 'R')\
                or (ro_nd[0] == 'R' and ro_nd[1] == 'S'):
            results.append((True, False))
        else:
            results.append((False, True))
    return results
