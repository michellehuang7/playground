package player

import (
	"fmt"
	"strings"
	"wizard/room"
)

type Player struct {
	Objects         []string
	CurrentLocation room.Room
}

func (p *Player) Look() string {
	res := fmt.Sprintf("%s \n", p.CurrentLocation.Desc)
	for _, p := range p.CurrentLocation.Paths {
		res += fmt.Sprintf("There is a %s going %s from here. \n", p.Method, p.Direction)
	}
	for _, o := range p.CurrentLocation.Objs {
		res += fmt.Sprintf("You see a %s on the floor. \n", o)
	}
	return res
}

func (p *Player) Walk(dir string) string {
	for _, path := range p.CurrentLocation.Paths {
		if path.Direction == dir {
			p.CurrentLocation = *path.Destination
			return ""
		}
	}
	return "You cannot go that way."
}

func (p *Player) PickUp(obj string) string {
	contains := false
	s := p.CurrentLocation.Objs
	for i, v := range s {
		if v == obj {
			contains = true
			s = append(s[:i], s[i+1:]...)
			break
		}
	}
	if contains {
		p.CurrentLocation.Objs = s
		p.Objects = append(p.Objects, obj)
		return ""
	} else {
		return "You cannot get that"
	}
}

func (p *Player) Inventory() string {
	if len(p.Objects) == 0 {
		return "You don't have any objects"
	} else {
		return fmt.Sprintf("Items - %s", strings.Join(p.Objects, ", "))
	}
}
