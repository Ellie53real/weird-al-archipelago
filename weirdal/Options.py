# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2026 Benny Dreamly.

from dataclasses import dataclass

from Options import DefaultOnToggle, OptionGroup, PerGameCommonOptions, Toggle


class IncludeDebut(DefaultOnToggle):
    """Include his debut album ('Weird Al' Yankovic') in the shuffling."""
    display_name = "Include Debut"


class IncludeIn3D(Toggle):
    """Include the album 'Weird Al' Yankovic in 3-D in the shuffling."""
    display_name = "Include In 3-D"


class IncludeDareToBeStupid(Toggle):
    """Include the album Dare to Be Stupid in the shuffling."""
    display_name = "Include Dare to Be Stupid"


class IncludePolkaParty(Toggle):
    """Include the album Polka Party! in the shuffling."""
    display_name = "Include Polka Party!"


class IncludeEvenWorse(Toggle):
    """Include the album Even Worse in the shuffling."""
    display_name = "Include Even Worse"


class IncludeUHF(Toggle):
    """Include the UHF: Original Motion Picture Soundtrack and Other Stuff in the shuffling."""
    display_name = "Include UHF"


class IncludeOffTheDeepEnd(Toggle):
    """Include the album Off the Deep End in the shuffling."""
    display_name = "Include Off the Deep End"


class IncludeAlapalooza(Toggle):
    """Include the album Alapalooza in the shuffling."""
    display_name = "Include Alapalooza"


class IncludeBadHairDay(Toggle):
    """Include the album Bad Hair Day in the shuffling."""
    display_name = "Include Bad Hair Day"


class IncludeRunningWithScissors(Toggle):
    """Include the album Running With Scissors in the shuffling."""
    display_name = "Include Running With Scissors"


class IncludePoodleHat(Toggle):
    """Include the album Poodle Hat in the shuffling."""
    display_name = "Include Poodle Hat"


class IncludeStraightOuttaLynwood(Toggle):
    """Include the album Straight Outta Lynwood in the shuffling."""
    display_name = "Include Straight Outta Lynwood"


class IncludeAlpocalypse(Toggle):
    """Include the album Alpocalypse in the shuffling."""
    display_name = "Include Alpocalypse"


class IncludeMandatoryFun(Toggle):
    """Include the album Mandatory Fun in the shuffling."""
    display_name = "Include Mandatory Fun"


class IncludeMediumRarities(Toggle):
    """Include the album Medium Rarities in the shuffling."""
    display_name = "Include Medium Rarities"


class IncludeSingles(Toggle):
    """Include a few of Al's non-album singles in the shuffling."""
    display_name = "Include Singles"


class IncludeAltRecordings(Toggle):
    """Include alternate recordings from Medium Rarities (such as "Dare to Be Stupid"'s instrumental and the Japanese version of "Jurassic Park") in the shuffling."""
    display_name = "Include Alternate Recordings"


@dataclass
class WeirdAlOptions(PerGameCommonOptions):
    include_debut: IncludeDebut
    include_in_3d: IncludeIn3D
    include_dare_to_be_stupid: IncludeDareToBeStupid
    include_polka_party: IncludePolkaParty
    include_even_worse: IncludeEvenWorse
    include_uhf: IncludeUHF
    include_off_the_deep_end: IncludeOffTheDeepEnd
    include_alapalooza: IncludeAlapalooza
    include_bad_hair_day: IncludeBadHairDay
    include_running_with_scissors: IncludeRunningWithScissors
    include_poodle_hat: IncludePoodleHat
    include_straight_outta_lynwood: IncludeStraightOuttaLynwood
    include_alpocalypse: IncludeAlpocalypse
    include_mandatory_fun: IncludeMandatoryFun
    include_medium_rarities: IncludeMediumRarities
    include_singles: IncludeSingles
    include_alt_recordings: IncludeAltRecordings


option_groups = [
    OptionGroup("Album Options", [
        IncludeDebut,
        IncludeIn3D,
        IncludeDareToBeStupid,
        IncludePolkaParty,
        IncludeEvenWorse,
        IncludeUHF,
        IncludeOffTheDeepEnd,
        IncludeAlapalooza,
        IncludeBadHairDay,
        IncludeRunningWithScissors,
        IncludePoodleHat,
        IncludeStraightOuttaLynwood,
        IncludeAlpocalypse,
        IncludeMandatoryFun,
        IncludeMediumRarities,
        IncludeSingles,
    ]),
    OptionGroup("Song Options", [
        IncludeAltRecordings,
    ]),
]
