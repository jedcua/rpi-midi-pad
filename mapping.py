import random

from gfx import Down, Right, Up, Left, Point, DownLine, RightLine, LeftLine, UpLine, Persist


gfx_dict = {
    # Down Points
    0 : lambda _ : Down(Point(0,0)),
    1 : lambda _ : Down(Point(1,0)),
    2 : lambda _ : Down(Point(2,0)),
    3 : lambda _ : Down(Point(3,0)),
    4 : lambda _ : Down(Point(4,0)),
    5 : lambda _ : Down(Point(5,0)),
    6 : lambda _ : Down(Point(6,0)),
    7 : lambda _ : Down(Point(7,0)),

    # Right Points
    8  : lambda _ : Right(Point(0,0)),
    9  : lambda _ : Right(Point(0,1)),
    10 : lambda _ : Right(Point(0,2)),
    11 : lambda _ : Right(Point(0,3)),
    12 : lambda _ : Right(Point(0,4)),
    13 : lambda _ : Right(Point(0,5)),
    14 : lambda _ : Right(Point(0,6)),
    15 : lambda _ : Right(Point(0,7)),

    # Up Points
    16 : lambda _ : Up(Point(0,7)),
    17 : lambda _ : Up(Point(1,7)),
    18 : lambda _ : Up(Point(2,7)),
    19 : lambda _ : Up(Point(3,7)),
    20 : lambda _ : Up(Point(4,7)),
    21 : lambda _ : Up(Point(5,7)),
    22 : lambda _ : Up(Point(6,7)),
    23 : lambda _ : Up(Point(7,7)),

    # Left Points
    24 : lambda _ : Left(Point(7,0)),
    25 : lambda _ : Left(Point(7,1)),
    26 : lambda _ : Left(Point(7,2)),
    27 : lambda _ : Left(Point(7,3)),
    28 : lambda _ : Left(Point(7,4)),
    29 : lambda _ : Left(Point(7,5)),
    30 : lambda _ : Left(Point(7,6)),
    31 : lambda _ : Left(Point(7,7)),

    # Persistent Points

    # Row 0
    32 : lambda _ : Persist(Point(0,0)),
    33 : lambda _ : Persist(Point(1,0)),
    34 : lambda _ : Persist(Point(2,0)),
    35 : lambda _ : Persist(Point(3,0)),
    36 : lambda _ : Persist(Point(4,0)),
    37 : lambda _ : Persist(Point(5,0)),
    38 : lambda _ : Persist(Point(6,0)),
    39 : lambda _ : Persist(Point(7,0)),

    ## Row 1
    40 : lambda _ : Persist(Point(0,1)),
    41 : lambda _ : Persist(Point(1,1)),
    42 : lambda _ : Persist(Point(2,1)),
    43 : lambda _ : Persist(Point(3,1)),
    44 : lambda _ : Persist(Point(4,1)),
    45 : lambda _ : Persist(Point(5,1)),
    46 : lambda _ : Persist(Point(6,1)),
    47 : lambda _ : Persist(Point(7,1)),

    ## Row 2
    48 : lambda _ : Persist(Point(0,2)),
    49 : lambda _ : Persist(Point(1,2)),
    50 : lambda _ : Persist(Point(2,2)),
    51 : lambda _ : Persist(Point(3,2)),
    52 : lambda _ : Persist(Point(4,2)),
    53 : lambda _ : Persist(Point(5,2)),
    54 : lambda _ : Persist(Point(6,2)),
    55 : lambda _ : Persist(Point(7,2)),

    ## Row 3
    56 : lambda _ : Persist(Point(0,3)),
    57 : lambda _ : Persist(Point(1,3)),
    58 : lambda _ : Persist(Point(2,3)),
    59 : lambda _ : Persist(Point(3,3)),
    60 : lambda _ : Persist(Point(4,3)),
    61 : lambda _ : Persist(Point(5,3)),
    62 : lambda _ : Persist(Point(6,3)),
    63 : lambda _ : Persist(Point(7,3)),

    ## Row 4
    64 : lambda _ : Persist(Point(0,4)),
    65 : lambda _ : Persist(Point(1,4)),
    66 : lambda _ : Persist(Point(2,4)),
    67 : lambda _ : Persist(Point(3,4)),
    68 : lambda _ : Persist(Point(4,4)),
    69 : lambda _ : Persist(Point(5,4)),
    70 : lambda _ : Persist(Point(6,4)),
    71 : lambda _ : Persist(Point(7,4)),

    ## Row 5
    72 : lambda _ : Persist(Point(0,5)),
    73 : lambda _ : Persist(Point(1,5)),
    74 : lambda _ : Persist(Point(2,5)),
    75 : lambda _ : Persist(Point(3,5)),
    76 : lambda _ : Persist(Point(4,5)),
    77 : lambda _ : Persist(Point(5,5)),
    78 : lambda _ : Persist(Point(6,5)),
    79 : lambda _ : Persist(Point(7,5)),

    ## Row 6
    80 : lambda _ : Persist(Point(0,6)),
    81 : lambda _ : Persist(Point(1,6)),
    82 : lambda _ : Persist(Point(2,6)),
    83 : lambda _ : Persist(Point(3,6)),
    84 : lambda _ : Persist(Point(4,6)),
    85 : lambda _ : Persist(Point(5,6)),
    86 : lambda _ : Persist(Point(6,6)),
    87 : lambda _ : Persist(Point(7,6)),

    ## Row 7
    88 : lambda _ : Persist(Point(0,7)),
    89 : lambda _ : Persist(Point(1,7)),
    90 : lambda _ : Persist(Point(2,7)),
    91 : lambda _ : Persist(Point(3,7)),
    92 : lambda _ : Persist(Point(4,7)),
    93 : lambda _ : Persist(Point(5,7)),
    94 : lambda _ : Persist(Point(6,7)),
    95 : lambda _ : Persist(Point(7,7)),
}


def standard_mapping(note):
    if note is not None:
        return gfx_dict.get(note - 12, lambda _: None)(None)
    return None


def randomize(_):
    dir = random.choice(['up', 'down', 'left', 'right', 'upline', 'downline', 'rightline', 'leftline'])
    rand_pos = random.randint(0,7)
    if dir == 'up':
        return Up(Point(rand_pos, 7))
    elif dir == 'down':
        return Down(Point(rand_pos, 0))
    elif dir == 'left':
        return Left(Point(7, rand_pos))
    elif dir == 'right':
        return Right(Point(0, rand_pos))
    elif dir == 'downline':
        return DownLine(0, 7, 0)
    elif dir == 'upline':
        return UpLine(0, 7, 7)
    elif dir == 'rightline':
        return RightLine(0, 0, 7)
    elif dir == 'leftline':
        return LeftLine(7, 0, 7)
