def egg_carton_box(eggs):
    '''
    this function find the least amount the cartons for
    the ammount of eggs given
    >>> egg_carton_box(12) # дві коробки по 6 яєць
    [6, 6]
    >>> egg_carton_box(28) # три коробки по 10 яєць.
    [10, 10, 10]
    >>> egg_carton_box(24) # дві коробки по 10 яєць та одна коробка на 4
    [4, 10, 10]
    '''
    boxes = []
    if eggs == 0:
        return []
    if eggs % 10 == 1 or eggs % 10 == 2 or\
        eggs % 10 == 3 or eggs % 10 == 4:
        boxes.append(4)
    elif eggs % 10 == 5 or eggs % 10 == 6:
        boxes.append(6)
    else:
        boxes.append(10)
    tens = eggs // 10
    for i in range(tens):
        boxes.append(10)
    boxes = sorted(boxes)
    return boxes
