import random

from gfx import Down, Right, Up, Left, Point, DownLine, RightLine, LeftLine, UpLine, Slow


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

    # Slow Down Points
    32 : lambda _ : Slow(Down(Point(0,0))),
    33 : lambda _ : Slow(Down(Point(1,0))),
    34 : lambda _ : Slow(Down(Point(2,0))),
    35 : lambda _ : Slow(Down(Point(3,0))),
    36 : lambda _ : Slow(Down(Point(4,0))),
    37 : lambda _ : Slow(Down(Point(5,0))),
    38 : lambda _ : Slow(Down(Point(6,0))),
    39 : lambda _ : Slow(Down(Point(7,0))),
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
