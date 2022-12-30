class Room:
    def __init__(self, name, desc, paths=[], objs=[]):
        self.name = name
        self.desc = desc
        self.paths = paths
        self.objs = objs


class Player:
    def __init__(self, room):
        self.objects = []
        self.current_location = room

    def pick_up(self, obj):
        try:
            self.current_location.objs.remove(obj)
        except (IndexError, ValueError):
            raise ValueError("You cannot get that.")
        self.objects.append(obj)

    def inventory(self):
        print("Items - ")
        for obj in self.objects:
            print(obj)

    def look(self):
        print(self.current_location.desc)
        for p in self.current_location.paths:
            print(
                f"There is a {p['method']} going {p['direction']} from here."
            )
        for obj in self.current_location.objs:
            print(f"You see a {obj} on the floor.")

    def walk(self, direction):
        for p in self.current_location.paths:
            if p["direction"] == direction:
                self.current_location = p["destination"]
                return
        raise ValueError("You cannot go that way.")

DIRECTIONS = ["downstairs", "upstairs", "west", "east"]

living_room = Room(
    "living room",
    "You are in the living room. A Wizard is snoring loudly on the couch.",
    objs=["whisky", "bucket"],
)
attic = Room(
    "attic",
    "You are in the attic. There is a gigant welding roch in the corner.",
    objs=["frog", "chain"],
)
garden = Room(
    "garden", "You are in a beautiful garden. There is a well in front of you."
)

living_room.paths = [
    {"destination": attic, "direction": DIRECTIONS[1], "method": "door"},
    {"destination": garden, "direction": DIRECTIONS[2], "method": "ladder"},
]
garden.paths = [
    {"destination": living_room, "direction": DIRECTIONS[3], "method": "door"},
]
attic.paths = [
    {
        "destination": living_room,
        "direction": DIRECTIONS[0],
        "method": "ladder",
    },
]


if __name__ == "__main__":
    player = Player(living_room)
    while True:
        userInput = input().split(" ")
        action = userInput[0]
        try:
            if action == "walk":
                player.walk(userInput[1])
            elif action == "look":
                player.look()
            elif action == "pickup":
                player.pick_up(userInput[1])
            elif action == "inventory":
                player.inventory()
            else:
                raise ValueError("I do not know that command")
        except (IndexError, ValueError) as e:
            print(e)
