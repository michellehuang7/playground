import random

DIRECTIONS = {
    "q": -65,
    "w": -64,
    "e": -63,
    "a": -1,
    "d": 1,
    "z": 63,
    "x": 64,
    "c": 65,
}

NUM_OF_ROBOTS = 10


class Robot:
    def __init__(self):
        self.pos = random.randint(0,1023)
    
    def move(self, target_pos: int) -> None:
        min_distance = float('inf')
        min_pos = self.pos
        for (_, displacement) in DIRECTIONS.items():
            new_pos = self.pos + displacement
            distance = self._distance(new_pos, target_pos)
            if distance < min_distance:
                min_distance = distance
                min_pos = new_pos
        self.pos = min_pos

    def _distance(self, pos1: int, pos2: int) -> float:
        x1 = pos1 % 64
        y1 = round(pos1 / 64)
        x2 = pos2 % 64
        y2 = round(pos2 / 64)
        return (x1 - x2) ** 2 + (y1 - y2) ** 2


class Player:
    def __init__(self):
        self.pos = 544

    def move(self, displacement):
        self.pos = self.pos + displacement

    def teleport(self):
        self.pos = random.randint(0,1023)


def render(player, robots):
    print("*" * 64)
    for y in range(16):
        for x in range(64):
            pos = y * 64 + x
            if pos == player.pos:
                print('@', end='')
            elif pos in [r.pos for r in robots]:
                print('A', end='')
            elif pos in dead_bodies:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print("*" * 64)


if __name__ == "__main__":
    player = Player()
    robots = [Robot() for _ in range(NUM_OF_ROBOTS)]
    dead_bodies = []
    while True:
        render(player, robots)
        userInput = input()
        try:
            if userInput in DIRECTIONS:
                displacement = DIRECTIONS.get(userInput)
                player.move(displacement)
                seen = set()
                for r in robots:
                    r.move(player.pos)
                    if r.pos in seen:
                        dead_bodies.append(r.pos)
                    else:
                        seen.add(r.pos)
                robots = [r for r in robots if r.pos not in dead_bodies]
            elif userInput == 't':
                player.teleport()
            else:
                raise ValueError("I do not know that command")
            if len(robots) == 0:
                print("Player wins!")
                exit()
            if player.pos in [r.pos for r in robots]:
                print("Play loses!")
                exit()
        except (IndexError, ValueError) as e:
            print(e)
