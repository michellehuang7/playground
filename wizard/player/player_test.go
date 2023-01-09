package player

import (
	"strings"
	"testing"
	"wizard/room"
)

var livingRoom = room.Room{
	Name: "living_room",
	Desc: "You are in the living room.",
	Objs: []string{"whisky", "bucket"},
	Paths: []room.Path{
		{
			Destination: &garden,
			Direction:   "downstairs",
			Method:      "ladder",
		},
	},
}

var garden = room.Room{
	Name: "garden",
	Desc: "You are in a beautiful garden.",
	Objs: []string{},
}

var p = Player{
	Objects:         []string{"apple"},
	CurrentLocation: livingRoom,
}

func testEq(a, b []string) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func TestPickUp(t *testing.T) {
	output := p.PickUp("key")
	expected := "You cannot get that"
	if output != expected {
		t.Errorf("Output %q not equal to expected %q", output, expected)
	}

	p.PickUp("whisky")
	expected_inventory := []string{"apple", "whisky"}
	if !testEq(p.Objects, expected_inventory) {
		t.Errorf("Objects %q not equal to expected %q", p.Objects, expected_inventory)
	}

	output = p.PickUp("whisky")
	if output != expected {
		t.Errorf("Whisky shouldn't be picked up twice")
	}
}

func TestWalk(t *testing.T) {
	output := p.Walk("east")
	expected := "You cannot go that way."
	if output != expected {
		t.Errorf("Output %q not equal to expected %q", output, expected)
	}

	p.Walk("downstairs")
	expected_location := "garden"
	if p.CurrentLocation.Name != expected_location {
		t.Errorf("Objects %q not equal to expected %q", p.CurrentLocation.Name, expected_location)
	}
}

func TestLook(t *testing.T) {
	p = Player{
		Objects:         []string{"apple"},
		CurrentLocation: livingRoom,
	}
	substrings := [3]string{
		"You are in the living room.",
		"There is a ladder going downstairs from here.",
		"You see a bucket on the floor.",
	}
	output := p.Look()
	for _, sub := range substrings {
		if !strings.Contains(output, sub) {
			t.Errorf("Output %q is missing expected substring %q", output, sub)
		}
	}
}

func TestInventory(t *testing.T) {
	p = Player{
		Objects:         []string{"apple"},
		CurrentLocation: livingRoom,
	}
	p.PickUp("bucket")
	output := p.Inventory()
	items := []string{"apple", "bucket"}
	for _, sub := range items {
		if !strings.Contains(output, sub) {
			t.Errorf("Output %q is missing expected substring %q", output, sub)
		}
	}

	p = Player{
		Objects:         []string{},
		CurrentLocation: livingRoom,
	}
	output = p.Inventory()
	expected := "You don't have any objects"
	if output != expected {
		t.Errorf("Output %q not equal to expected %q", output, expected)
	}
}
