from boards import (
    TEST_BOARD01,
    TEST_BOARD02,
    TEST_BOARD1,
    TEST_BOARD2,
    TEST_BOARD3,
    TEST_BOARD4,
)

HORIZONTAL = 'h'
VERTICAL = 'v'

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

SOLVING_BLOCK = 'z'
EMPTY_BLOCK = '*'


def find_neighbours(data, point, kind=None):
    x_length, y_length = get_board_dimensions(data)

    pos_x = point[0]
    pos_y = point[1]

    current_kind = data[pos_y][pos_x]

    posible_neighbours = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1),
    ]

    found_neighbours = []

    for nb_y, nb_x in posible_neighbours:

        x = pos_x + nb_x
        y = pos_y + nb_y

        # skip if any of the cordinates is out of the board
        if min((x, y)) < 0 or x >= x_length or y >= y_length:
            continue

        if kind and kind != EMPTY_BLOCK:
            if data[y][x] != kind:
                continue

        found_neighbours.append({
            'value': data[y][x],
            'x': x,
            'y': y,
        })

    return found_neighbours


class Board(object):

    width = 6
    height = 6

    exit = (5, 2)

    blocks = None

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.parsed_data = self._parse_raw_data()
        self.block_names = self._get_block_names()
        self.width, self.height = self._get_board_dimensions()
        self.blocks = {
            name: self.get_block_by_name(name) for name in self.block_names
        }

    def _parse_raw_data(self):
        data = self.raw_data.replace(' ', '').split('\n')
        return [list(row) for row in data if row]

    def _get_block_names(self):
        data = self.raw_data.replace('\n', '').replace(' ', '')
        return set(data.replace(EMPTY_BLOCK, ''))

    def _get_board_dimensions(self):
        x_length = len(self.parsed_data[0])
        y_length = len(self.parsed_data)

        assert all([len(row) == x_length for row in self.parsed_data])

        return (x_length, y_length)

    def get_block_by_name(self, name):
        points = []
        for y in range(self.height):
            for x in range(self.width):
                if self.parsed_data[y][x] == name:
                    points.append((x, y))

        return Block(
            name=name,
            points=points,
            main=name == SOLVING_BLOCK,
        )

    def get_available_moves(self):
        # return all, currently available moves on the board
        return []

    def is_game_finished(self):
        return self.exit in self.blocks[SOLVING_BLOCK].points


class Block(object):

    name = None
    points = None  # list of points, i.e. [(0, 1), (0, 2)]
    lenght = None  # 2 or 3
    orientation = None  # HORIZONTAL or VERTICAL
    main = False  # Bolean

    def __init__(self, name, points, main=False):
        self.name = name
        self.points = points
        self.main = main

    def move(self, direction):
        # moves a block to a new point
        # can go up/down or left/right
        return

    def get_available_moves(self):
        # get a list of all available moves for the block
        return []
