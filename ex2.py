class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return (self._length * self._width * 25 * 5) / 1000

r = Road(5000, 20)
print(f'Масса асфальта: {r.mass()} т')