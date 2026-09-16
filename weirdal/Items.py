# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2026 Benny Dreamly.
# Copyright (c) 2026 Ellie53

from BaseClasses import Item, ItemClassification

from typing import TypedDict

class WeirdAlItem(Item):
    game: str = "'Weird Al' Yankovic Discography"

class ItemDict(TypedDict):
    classification: ItemClassification
    name: str

ITEM_NAME_TO_ID = {
    "'Weird Al' Yankovic": 27,
    "'Weird Al' Yankovic in 3-D": 28,
    "Dare to Be Stupid": 29,
    "Polka Party!": 30,
    "Even Worse": 31,
    "UHF: Original Motion Picture Soundtrack and Other Stuff": 32,
    "Off the Deep End": 33,
    "Alapalooza": 34,
    "Bad Hair Day": 35,
    "Running With Scissors": 36,
    "Poodle Hat": 37,
    "Straight Outta Lynwood": 38,
    "Alpocalypse": 39,
    "Mandatory Fun": 40,
    "Medium Rarities": 41,
    "Singles": 42,
    "Easter Egg": 43,
    "Behind the Lyrics": 44,
    "Secret Message": 45,
    "Studio Session": 46,
    "Rocky Road Ice Cream": 47,
    "Jeopardy Home Game": 48,
    "Can of Spam": 49,
    "Glazed Donuts": 50,
    "Jelly Donuts": 51,
    "Bavarian Cream-Filled Donuts": 52,
    "Cinnamon Rolls": 53,
    "Apple Fritters": 54,
    "Bear Claws": 55,
    "Automatic Salt and Pepper Shakers": 56
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "'Weird Al' Yankovic": ItemClassification.progression,
    "'Weird Al' Yankovic in 3-D": ItemClassification.progression,
    "Dare to Be Stupid": ItemClassification.progression,
    "Polka Party!": ItemClassification.progression,
    "Even Worse": ItemClassification.progression,
    "UHF: Original Motion Picture Soundtrack and Other Stuff": ItemClassification.progression,
    "Off the Deep End": ItemClassification.progression,
    "Alapalooza": ItemClassification.progression,
    "Bad Hair Day": ItemClassification.progression,
    "Running With Scissors": ItemClassification.progression,
    "Poodle Hat": ItemClassification.progression,
    "Straight Outta Lynwood": ItemClassification.progression,
    "Alpocalypse": ItemClassification.progression,
    "Mandatory Fun": ItemClassification.progression,
    "Medium Rarities": ItemClassification.progression,
    "Singles": ItemClassification.progression,
    "Easter Egg": ItemClassification.filler,
    "Behind the Lyrics": ItemClassification.filler,
    "Secret Message": ItemClassification.filler,
    "Studio Session": ItemClassification.filler,
    "Rocky Road Ice Cream": ItemClassification.filler,
    "Jeopardy Home Game": ItemClassification.filler,
    "Can of Spam": ItemClassification.filler,
    "Glazed Donuts": ItemClassification.filler,
    "Jelly Donuts": ItemClassification.filler,
    "Bavarian Cream-Filled Donuts": ItemClassification.filler,
    "Cinnamon Rolls": ItemClassification.filler,
    "Apple Fritters": ItemClassification.filler,
    "Bear Claws": ItemClassification.filler,
    "Automatic Salt and Pepper Shakers": ItemClassification.filler,
}

ALBUM_OPTIONS = {
    "'Weird Al' Yankovic":           "include_debut",
    "'Weird Al' Yankovic in 3-D":               "include_in_3d",
    "Dare to Be Stupid": "include_dare_to_be_stupid",
    "Polka Party!":              "include_polka_party",
    "Even Worse": "include_even_worse",
    "UHF: Original Motion Picture Soundtrack and Other Stuff":                    "include_uhf",
    "Off the Deep End": "include_off_the_deep_end",
    "Alapalooza":                   "include_alapalooza",
    "Bad Hair Day": "include_bad_hair_day",
    "Running With Scissors":             "include_running_with_scissors",
    "Poodle Hat":                  "include_poodle_hat",
    "Straight Outta Lynwood":               "include_straight_outta_lynwood",
    "Alpocalypse":               "include_alpocalypse",
    "Mandatory Fun":              "include_mandatory_fun",
    "Medium Rarities": "include_medium_rarities",
    "Singles": "include_singles",
    "Alternate Recordings": "include_alt_recordings",
}

FILLER_NAMES = [
    "Easter Egg",
    "Behind the Lyrics",
    "Secret Message",
    "Studio Session",
    "Rocky Road Ice Cream",
    "Jeopardy Home Game",
    "Can of Spam",
    "Glazed Donuts",
    "Jelly Donuts",
    "Bavarian Cream-Filled Donuts",
    "Cinnamon Rolls",
    "Apple Fritters",
    "Bear Claws",
    "Automatic Salt and Pepper Shakers",
]


def create_item_with_correct_classification(world, name: str) -> WeirdAlItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return WeirdAlItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def get_random_filler_item_name(world) -> str:
    return world.random.choice(FILLER_NAMES)


def create_all_items(world) -> None:
    itempool: list[Item] = []

    for album_name, option_name in ALBUM_OPTIONS.items():
        if getattr(world.options, option_name).value:
            itempool.append(world.create_item(album_name))

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_filler = number_of_unfilled_locations - len(itempool)
    itempool += [world.create_filler() for _ in range(needed_filler)]

    world.multiworld.itempool += itempool