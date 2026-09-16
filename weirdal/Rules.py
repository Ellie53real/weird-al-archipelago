# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2026 Benny Dreamly.
# Copyright (c) 2026 Ellie53

from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll

from .Locations import LOCATION_TABLE
from .Regions import ALBUM_REGIONS

if TYPE_CHECKING:
    from . import WeirdAlWorld


def set_all_rules(world: WeirdAlWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: WeirdAlWorld) -> None:
    for loc in world.multiworld.get_locations(world.player):
        data = LOCATION_TABLE[loc.name]


def set_completion_condition(world: WeirdAlWorld) -> None:
    required_items = []
    for album_name, option_name in ALBUM_REGIONS.items():
        if getattr(world.options, option_name).value:
            required_items.append(album_name)

    world.set_completion_rule(HasAll(*required_items))
