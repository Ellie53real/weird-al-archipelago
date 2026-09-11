# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2026 Benny Dreamly.

from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.rules import Has

if TYPE_CHECKING:
    from . import WeirdAlWorld


ALBUM_REGIONS: dict[str, str] = {
    "'Weird Al' Yankovic":                "include_debut",
    "'Weird Al' Yankovic in 3-D":                    "include_in_3d",
    "Dare to Be Stupid": "include_dare_to_be_stupid",
    "Polka Party!":                   "include_polka_party",
    "Even Worse": "include_even_worse",
    "UHF: Original Motion Picture Soundtrack and Other Stuff":                         "include_uhf",
    "Off the Deep End":      "include_off_the_deep_end",
    "Alapalooza":                        "include_alapalooza",
    "Bad Hair Day":     "include_bad_hair_day",
    "Running With Scissors":                  "include_running_with_scissors",
    "Poodle Hat":                       "include_poodle_hat",
    "Straight Outta Lynwood":                    "include_straight_outta_lynwood",
    "Alpocalypse":                    "include_alpocalypse",
    "Mandatory Fun":                   "include_mandatory_fun",
    "Medium Rarities": "include_medium_rarities",
    "Singles":      "include_singles",
}


def create_and_connect_regions(world: WeirdAlWorld) -> None:
    menu = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menu)

    for region_name, option_name in ALBUM_REGIONS.items():
        if getattr(world.options, option_name).value:
            album_region = Region(region_name, world.player, world.multiworld)
            world.multiworld.regions.append(album_region)
            menu.connect(album_region, rule=Has(region_name))
