package room

type Room struct {
	Name  string
	Desc  string
	Objs  []string
	Paths []Path
}

type Path struct {
	Destination *Room
	Direction   string
	Method      string
}
