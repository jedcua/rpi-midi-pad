from gfx import Down, Point


notes_to_entity = {
    60 : lambda _ : Down(Point(0,0)),
    62 : lambda _ : Down(Point(1,0)),
    64 : lambda _ : Down(Point(2,0)),
    65 : lambda _ : Down(Point(3,0)),
    66 : lambda _ : Down(Point(4,0)),
    67 : lambda _ : Down(Point(5,0)),
    69 : lambda _ : Down(Point(6,0)),
    70 : lambda _ : Down(Point(7,0)),
}


def standard_mapping(note):
    return notes_to_entity.get(note, lambda _: None)(None)
