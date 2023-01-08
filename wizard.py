class Player:
    def __init__(self, room):
        self.objects = []
        self.current_location = room

    def pick_up(self, obj):
        try:
            self.current_location['objs'].remove(obj)
        except ValueError:
            raise ValueError("You cannot get that.")
        self.objects.append(obj)

    def inventory(self) -> str:
        return f"Items - {'.'.join([obj for obj in self.objects])}"

    def look(self):
        res = f"{self.current_location['desc']} \n"
        for p in self.current_location['paths']:
            res = res + f"There is a {p['method']} going {p['direction']} from here. \n"
        for obj in self.current_location['objs']:
            res = res + f"You see a {obj} on the floor. \n"
        return res

    def walk(self, direction):
        for p in self.current_location['paths']:
            if p["direction"] == direction:
                self.current_location = p["destination"]
                return
        raise ValueError("You cannot go that way.")

DIRECTIONS = ["downstairs", "upstairs", "west", "east"]

living_room = dict(
    name="living_room", 
    desc="You are in the living room. A Wizard is snoring loudly on the couch.",
    objs=["whisky", "bucket"],
)

attic = dict(
    name="attic",
    desc="You are in the attic. There is a gigant welding roch in the corner.",
    objs=["frog", "chain"],
)

garden = dict(
    name="garden", 
    desc="You are in a beautiful garden. There is a well in front of you.",
    objs=[],
)

living_room["paths"] = [
    {"destination": attic, "direction": DIRECTIONS[1], "method": "door"},
    {"destination": garden, "direction": DIRECTIONS[2], "method": "ladder"},
]
garden["paths"] = [
    {"destination": living_room, "direction": DIRECTIONS[3], "method": "door"},
]
attic["paths"] = [
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
                print(player.look())
            elif action == "pickup":
                player.pick_up(userInput[1])
            elif action == "inventory":
                print(player.inventory())
            else:
                raise ValueError("I do not know that command")
        except (IndexError, ValueError) as e:
            print(e)
