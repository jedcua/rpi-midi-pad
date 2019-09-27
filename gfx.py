from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def render(self, draw):
        pass


class Entity(ABC):
    @abstractmethod
    def update(self):
        pass


class Destroyable(ABC):
    @abstractmethod
    def can_destroy(self):
        return True


class BasicEntity(Drawable, Entity, Destroyable):
    def render(self, draw):
        pass


    def update(self):
        pass


    def can_destroy(self):
        return True


class Up(BasicEntity):
    def __init__(self, entity):
        self._origin = entity


    def render(self, draw):
        self._origin.render(draw)


    def update(self):
        x, y = self._origin._pos
        self._origin._pos = (x, y - 1)
        self._origin.update()


    def can_destroy(self):
        return self._origin.can_destroy()


class Down(BasicEntity):
    def __init__(self, entity):
        self._origin = entity


    def render(self, draw):
        self._origin.render(draw)


    def update(self):
        x, y = self._origin._pos
        self._origin._pos = (x, y + 1)
        self._origin.update()


    def can_destroy(self):
        return self._origin.can_destroy()


class Left(BasicEntity):
    def __init__(self, entity):
        self._origin = entity


    def render(self, draw):
        self._origin.render(draw)


    def update(self):
        x, y = self._origin._pos
        self._origin._pos = (x - 1, y)
        self._origin.update()


    def can_destroy(self):
        return self._origin.can_destroy()


class Right(BasicEntity):
    def __init__(self, entity):
        self._origin = entity


    def render(self, draw):
        self._origin.render(draw)


    def update(self):
        x, y = self._origin._pos
        self._origin._pos = (x + 1, y)
        self._origin.update()


    def can_destroy(self):
        return self._origin.can_destroy()


class Slow(BasicEntity):
    def __init__(self, entity, decrement=0.5):
        self._origin = entity
        self._decrement = decrement
        self._counter = 0


    def render(self, draw):
        self._origin.render(draw)


    def update(self):
        if self._counter == 0:
            self._origin.update()
            self._counter = 1
        else:
            self._counter -= self._decrement
            self._counter = max(0, self._counter)


    def can_destroy(self):
        return self._origin.can_destroy()


class Point(BasicEntity):
    def __init__(self, x, y):
        self._pos = (x, y)


    def render(self, draw):
        draw.point(self._pos, fill='white')


    def update(self):
        pass


    def can_destroy(self):
        x, y = self._pos
        return (x < 0 or x > 7) or (y < 0 or y > 7)


class DownLine(BasicEntity):
    def __init__(self, x1, x2, y):
        self._pos1 = (x1, y)
        self._pos2 = (x2, y)


    def render(self, draw):
        x, y = self._pos1
        draw.line([self._pos1, self._pos2], fill='white')


    def update(self):
        x1, y = self._pos1
        x2, y = self._pos2
        self._pos1 = (x1, y + 1)
        self._pos2 = (x2, y + 1)


    def can_destroy(self):
        return self._pos1[1] > 7


class LeftLine(BasicEntity):
    def __init__(self, x, y1, y2):
        self._pos1 = (x, y1)
        self._pos2 = (x, y2)


    def render(self, draw):
        draw.line([self._pos1, self._pos2], fill='white')


    def update(self):
        x, y1 = self._pos1
        x, y2 = self._pos2
        self._pos1 = (x - 1, y1)
        self._pos2 = (x - 1, y2)


    def can_destroy(self):
        return self._pos1[0] < 0


class RightLine(BasicEntity):
    def __init__(self, x, y1, y2):
        self._pos1 = (x, y1)
        self._pos2 = (x, y2)


    def render(self, draw):
        draw.line([self._pos1, self._pos2], fill='white')


    def update(self):
        x, y1 = self._pos1
        x, y2 = self._pos2
        self._pos1 = (x + 1, y1)
        self._pos2 = (x + 1, y2)


    def can_destroy(self):
        return self._pos1[0] > 7


class UpLine(BasicEntity):
    def __init__(self, x1, x2, y):
        self._pos1 = (x1, y)
        self._pos2 = (x2, y)


    def render(self, draw):
        x, y = self._pos1
        draw.line([self._pos1, self._pos2], fill='white')


    def update(self):
        x1, y = self._pos1
        x2, y = self._pos2
        self._pos1 = (x1, y - 1)
        self._pos2 = (x2, y - 1)


    def can_destroy(self):
        return self._pos1[1] < 0


class Group(BasicEntity):
    def __init__(self, entities):
        self._entities = entities


    def render(self, draw):
        for entity in self._entities:
            entity.render(draw)


    def update(self):
        for entity in self._entities:
            entity.update()


    def can_destroy(self):
        return all(map(lambda d: d.can_destroy()))
