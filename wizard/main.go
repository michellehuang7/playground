package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"wizard/player"
	"wizard/room"
)

var directions = [4]string{"downstairs", "upstairs", "west", "east"}

var livingRoom = room.Room{
	Name: "living_room",
	Desc: "You are in the living room. A Wizard is snoring loudly on the couch.",
	Objs: []string{"whisky", "bucket"},
}
var attic = room.Room{
	Name: "attic",
	Desc: "You are in the attic. There is a gigant welding roch in the corner.",
	Objs: []string{"frog", "chain"},
}
var garden = room.Room{
	Name: "garden",
	Desc: "You are in a beautiful garden. There is a well in front of you.",
	Objs: []string{},
}

func main() {

	livingRoom.Paths = []room.Path{
		{
			Destination: &attic,
			Direction:   directions[1],
			Method:      "door",
		},
		{
			Destination: &garden,
			Direction:   directions[2],
			Method:      "ladder",
		},
	}

	attic.Paths = []room.Path{
		{
			Destination: &livingRoom,
			Direction:   directions[0],
			Method:      "ladder",
		},
	}

	garden.Paths = []room.Path{
		{
			Destination: &livingRoom,
			Direction:   directions[3],
			Method:      "door",
		},
	}

	player := player.Player{
		Objects:         []string{},
		CurrentLocation: livingRoom,
	}

	scanner := bufio.NewScanner(os.Stdin)

	for {
		var input string
		if scanner.Scan() {
			input = scanner.Text()
		}
		inputs := strings.Split(input, " ")
		action := inputs[0]
		switch action {
		case "walk":
			if len(inputs) < 2 {
				fmt.Println("Please specify a direction")
				break
			}
			fmt.Println(player.Walk(inputs[1]))
		case "look":
			fmt.Println(player.Look())
		case "pickup":
			if len(inputs) < 2 {
				fmt.Println("Please specify an object")
				break
			}
			fmt.Println(player.PickUp(inputs[1]))
		case "inventory":
			fmt.Println(player.Inventory())
		default:
			fmt.Println("I do not know that command")
		}
	}

}
