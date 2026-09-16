# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2026 Benny Dreamly.
# Copyright (c) 2026 Ellie53

from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World
from Utils import visualize_regions
from .Items import WeirdAlItem, ITEM_NAME_TO_ID, create_all_items, create_item_with_correct_classification, get_random_filler_item_name
from .Locations import LOCATION_NAME_TO_ID, create_all_locations
from .Regions import create_and_connect_regions
from .Rules import set_all_rules, set_completion_condition
from .Options import WeirdAlOptions
from .Web import WeirdAlWeb
from .UT import UTMixin

class WeirdAlWorld(World, UTMixin):
    """'Weird Al' Yankovic's discography as an archipelago integration where you get checks by listening to music"""

    game = "'Weird Al' Yankovic Discography"
    web = WeirdAlWeb()

    base_id = 27

    options_dataclass = WeirdAlOptions
    options: WeirdAlOptions

    item_name_to_id = ITEM_NAME_TO_ID
    location_name_to_id = LOCATION_NAME_TO_ID

    def create_regions(self) -> None:
        create_and_connect_regions(self)
        create_all_locations(self)
        # visualize_regions(
        #     self.get_region("Menu"),
        #     "weirdal.puml",
        #     show_entrance_names=True,
        #     show_entrance_rules=True,
        # )

    def set_rules(self) -> None:
        set_all_rules(self)
        set_completion_condition(self)

    def create_item(self, name: str) -> WeirdAlItem:
        return create_item_with_correct_classification(self, name)

    def create_items(self) -> None:
        create_all_items(self)

    def get_filler_item_name(self) -> str:
        return get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "include_debut": self.options.include_debut.value,
            "include_in_3d": self.options.include_in_3d.value,
            "include_dare_to_be_stupid": self.options.include_dare_to_be_stupid.value,
            "include_polka_party": self.options.include_polka_party.value,
            "include_even_worse": self.options.include_even_worse.value,
            "include_uhf": self.options.include_uhf.value,
            "include_off_the_deep_end": self.options.include_off_the_deep_end.value,
            "include_alapalooza": self.options.include_alapalooza.value,
            "include_bad_hair_day": self.options.include_bad_hair_day.value,
            "include_running_with_scissors": self.options.include_running_with_scissors.value,
            "include_poodle_hat": self.options.include_poodle_hat.value,
            "include_straight_outta_lynwood": self.options.include_straight_outta_lynwood.value,
            "include_alpocalypse": self.options.include_alpocalypse.value,
            "include_mandatory_fun": self.options.include_mandatory_fun.value,
            "include_medium_rarities": self.options.include_medium_rarities.value,
            "include_singles": self.options.include_singles.value,
            "include_alt_recordings": self.options.include_alt_recordings.value,
        }
