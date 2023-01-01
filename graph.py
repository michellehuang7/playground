import pydot

# windwos support
# import os
# os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

class Room:
    def __init__(self, name, desc, paths=[], objs=[]):
        self.name = name
        self.desc = desc
        self.paths = paths
        self.objs = objs

DIRECTIONS = ["downstairs", "upstairs", "west", "east"]

living_room = Room( "living room", "You are in the living room. A Wizard is snoring loudly on the couch.")
attic = Room("attic", "You are in the attic. There is a gigant welding roch in the corner.")
garden = Room("garden", "You are in a beautiful garden. There is a well in front of you.")

living_room.paths = [
    {"destination": attic, "direction": DIRECTIONS[1], "method": "door"},
    {"destination": garden, "direction": DIRECTIONS[2], "method": "ladder"},
]
garden.paths = [{"destination": living_room, "direction": DIRECTIONS[3], "method": "door"}]
attic.paths = [
    {
        "destination": living_room,
        "direction": DIRECTIONS[0],
        "method": "ladder",
    },
]

MAX_LABEL_LENGTH = 30

def format_name(name):
    return name.replace(" ", "_").upper()

def dot_name(exp):
    label = f"({exp.name.upper()}({exp.desc.upper()})"
    if len(label) > MAX_LABEL_LENGTH:
        label = label[0:MAX_LABEL_LENGTH-1] + '...'
    return label

def nodes_to_dot(rooms):
    res = ""
    for n in rooms:
        name = format_name(n.name)
        res = res + f'{name}[label="{dot_name(n)}"];\n'
    return res

def edges_to_dot(rooms):
    res = ""
    for n in rooms:
        name = format_name(n.name)
        for e in n.paths:
            name_e = format_name(e["destination"].name)
            res = res + f'{name}->{name_e}[label="({e["direction"].upper() + " " + e["method"].upper()})"];\n'
    return res

def graph_to_dot(rooms):
    return "digraph{\n" + f"{nodes_to_dot(rooms)}{edges_to_dot(rooms)}"[:-1] + "}"
    # this covers nodes_to_dot + edges_to_dot
    # for n in rooms:
    #     name = format_name(n.name).upper()
    #     res = res + f'{name}[label="{dot_name(n)}"];\n'
    #     for p in n.paths:
    #         name_p = format_name(p["destination"].name)
    #         res = res + f'{name}->{name_p}[label="({p["direction"].upper() + " " + p["method"].upper()})"];\n'
    # res = res + '}'

with open(r"graph.dot", "w") as f:
    f.write(graph_to_dot([living_room, garden, attic]))

(graph,) = pydot.graph_from_dot_file("graph.dot")
graph.write_png("graph.png")

# print(nodes_to_dot([living_room, attic, garden]))
# print(edges_to_dot([living_room, attic, garden]))
# print(graph_to_dot([living_room, garden, attic]))