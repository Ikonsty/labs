def grade_count(grades):
    '''
    this function calculates average grade and converts it
    in ECTS
    >>> grade_count([85, 90, 67, 70, 87])
    (79.8, 'C')
    >>> grade_count([97, 93, 84, 78, 80])
    (86.4, 'B')
    '''
    for gr in grades:
        if gr > 100 or gr < 0:
            return (None, None)
    percent_grade = round(((grades[0]+grades[1]+grades[2]\
        +grades[3]+grades[4])/5),2)
    if 0 <= percent_grade <= 59:
        letter_grade = 'F'
    elif percent_grade <= 66:
        letter_grade = 'E'
    elif percent_grade <= 74:
        letter_grade = 'D'
    elif percent_grade <= 82:
        letter_grade = 'C'
    elif percent_grade <= 89:
        letter_grade = 'B'
    else:
        letter_grade = 'A'
    
    return (percent_grade, letter_grade)

