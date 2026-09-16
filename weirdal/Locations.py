# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2026 Benny Dreamly.
# Copyright (c) 2026 Ellie53

from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Location

if TYPE_CHECKING:
    from . import WeirdAlWorld


class WeirdAlLocation(Location):
    game = "'Weird Al' Yankovic Discography"


# (region, [alt recording?])
class LocationData(NamedTuple):
    region: str
    alt: bool = False


LOCATION_TABLE: dict[str, LocationData] = {
    # Freebie locations (accessible from start, no item required)
    "First Listen":                    LocationData("Menu"),
    "Encore":                          LocationData("Menu"),

    # 'Weird Al' Yankovic (Debut)
    "Ricky":                          LocationData("'Weird Al' Yankovic"),
    "Gotta Boogie":                     LocationData("'Weird Al' Yankovic"),
    "I Love Rocky Road":              LocationData("'Weird Al' Yankovic"),
    "Buckingham Blues":               LocationData("'Weird Al' Yankovic"),
    "Happy Birthday":                         LocationData("'Weird Al' Yankovic"),
    "Stop Draggin' My Car Around":                         LocationData("'Weird Al' Yankovic"),
    "My Bologna":          LocationData("'Weird Al' Yankovic"),
    "The Check's in the Mail":                      LocationData("'Weird Al' Yankovic"),
    "Another One Rides the Bus":                   LocationData("'Weird Al' Yankovic"),
    "I'll Be Mellow When I'm Dead":           LocationData("'Weird Al' Yankovic"),
    "Such a Groovy Guy":                            LocationData("'Weird Al' Yankovic"),
    "Mr. Frump in the Iron Lung":      LocationData("'Weird Al' Yankovic"),

    # 'Weird Al' Yankovic in 3-D
    "Eat It":                            LocationData("'Weird Al' Yankovic in 3-D"),
    "Midnight Star":                             LocationData("'Weird Al' Yankovic in 3-D"),
    "The Brady Bunch":                          LocationData("'Weird Al' Yankovic in 3-D"),
    "Buy Me a Condo":                         LocationData("'Weird Al' Yankovic in 3-D"),
    "I Lost on Jeopardy":                         LocationData("'Weird Al' Yankovic in 3-D"),
    "Polkas on 45":                  LocationData("'Weird Al' Yankovic in 3-D"),
    "Mr. Popeil":      LocationData("'Weird Al' Yankovic in 3-D"),
    "King of Suede":                         LocationData("'Weird Al' Yankovic in 3-D"),
    "That Boy Could Dance":                    LocationData("'Weird Al' Yankovic in 3-D"),
    "Theme from Rocky XIII (The Rye or the Kaiser)":                 LocationData("'Weird Al' Yankovic in 3-D"),
    "Nature Trail to Hell":                    LocationData("'Weird Al' Yankovic in 3-D"),

    # Dare to Be Stupid
    "Like a Surgeon":                          LocationData("Dare to Be Stupid"),
    "Dare to Be Stupid":                           LocationData("Dare to Be Stupid"),
    "I Want a New Duck":                        LocationData("Dare to Be Stupid"),
    "One More Minute":                       LocationData("Dare to Be Stupid"),
    "Yoda":                       LocationData("Dare to Be Stupid"),
    "George of the Jungle":                LocationData("Dare to Be Stupid"),
    "Slime Creatures from Outer Space":    LocationData("Dare to Be Stupid"),
    "Girls Just Want to Have Lunch":                       LocationData("Dare to Be Stupid"),
    "This Is the Life":                  LocationData("Dare to Be Stupid"),
    "Cable TV":               LocationData("Dare to Be Stupid"),
    "Hooked on Polkas":                  LocationData("Dare to Be Stupid"),

    # Polka Party!
    "Living with a Hernia":                               LocationData("Polka Party!"),
    "Dog Eat Dog":                         LocationData("Polka Party!"),
    "Addicted to Spuds":                   LocationData("Polka Party!"),
    "One of Those Days":                          LocationData("Polka Party!"),
    "Polka Party!":                          LocationData("Polka Party!"),
    "Here's Johnny":                               LocationData("Polka Party!"),
    "Don't Wear Those Shoes":                    LocationData("Polka Party!"),
    "Toothless People":                      LocationData("Polka Party!"),
    "Good Enough for Now":                          LocationData("Polka Party!"),
    "Christmas at Ground Zero":                LocationData("Polka Party!"),

    # Even Worse
    "Fat":                                              LocationData("Even Worse"),
    "Stuck in a Closet with Vanna White":                                        LocationData("Even Worse"),
    "This Song's Just (Six Words Long)":                                  LocationData("Even Worse"),
    "You Make Me":                                         LocationData("Even Worse"),
    "I Think I'm a Clone Now":                                         LocationData("Even Worse"),
    "Lasagna":                                              LocationData("Even Worse"),
    "Melanie":                                   LocationData("Even Worse"),
    "Alimony":                                     LocationData("Even Worse"),
    "Velvet Elvis":                                         LocationData("Even Worse"),
    "Twister":                               LocationData("Even Worse"),
    "Good Old Days":                                          LocationData("Even Worse"),

    # UHF: Original Motion Picture Soundtrack and Other Stuff
    "Money for Nothing/Beverly Hillbillies":                     LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "Gandhi II":                                LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "Attack of the Radioactive Hamsters from a Planet Near Mars":                        LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "Isle Thing":           LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "The Hot Rocks Polka":                       LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "UHF":                                 LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "Let Me Be Your Hog":                        LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "She Drives Like Crazy": LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "Generic Blues":                     LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "Spatula City": LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "Fun Zone":                        LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "Spam":               LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),
    "The Biggest Ball of Twine in Minnesota":                      LocationData("UHF: Original Motion Picture Soundtrack and Other Stuff"),

    # Off the Deep End
    "Smells Like Nirvana":                                         LocationData("Off the Deep End"),
    "Trigger Happy":                                                    LocationData("Off the Deep End"),
    "I Can't Watch This":                                            LocationData("Off the Deep End"),
    "Polka Your Eyes Out":                                LocationData("Off the Deep End"),
    "I Was Only Kidding":                                           LocationData("Off the Deep End"),
    "The White Stuff":                                                     LocationData("Off the Deep End"),
    "When I Was Your Age":                                            LocationData("Off the Deep End"),
    "Taco Grande":                LocationData("Off the Deep End"),
    "Airline Amy":                                         LocationData("Off the Deep End"),
    "The Plumbing Song":                   LocationData("Off the Deep End"),
    "You Don't Love Me Anymore":                                            LocationData("Off the Deep End"),

    # Alapalooza
    "Jurassic Park":              LocationData("Alapalooza"),
    "Young, Dumb & Ugly":                      LocationData("Alapalooza"),
    "Bedrock Anthem":                            LocationData("Alapalooza"),
    "Frank's 2000″ TV":                 LocationData("Alapalooza"),
    "Achy Breaky Song":       LocationData("Alapalooza"),
    "Traffic Jam":                     LocationData("Alapalooza"),
    "Talk Soup":                 LocationData("Alapalooza"),
    "She Never Told Me She Was a Mime":                        LocationData("Alapalooza"),
    "Harvey the Wonder Hamster":                   LocationData("Alapalooza"),
    "Waffle King":             LocationData("Alapalooza"),
    "Bohemian Rhapsody":                        LocationData("Alapalooza"),

    # Bad Hair Day
    "Amish Paradise":                                   LocationData("Bad Hair Day"),
    "Everything You Know is Wrong":                                           LocationData("Bad Hair Day"),
    "Cavity Search":                                                 LocationData("Bad Hair Day"),
    "Callin' In Sick":                                      LocationData("Bad Hair Day"),
    "The Alternative Polka":                            LocationData("Bad Hair Day"),
    "Since You've Been Gone":                                          LocationData("Bad Hair Day"),
    "Gump":                                      LocationData("Bad Hair Day"),
    "I'm So Sick of You":                                             LocationData("Bad Hair Day"),
    "Syndicated Inc.":                                        LocationData("Bad Hair Day"),
    "I Remember Larry":                                  LocationData("Bad Hair Day"),
    "Phony Calls":                                             LocationData("Bad Hair Day"),
    "The Night Santa Went Crazy":                                         LocationData("Bad Hair Day"),

    # Running With Scissors
    "The Saga Begins":                LocationData("Running With Scissors"),
    "My Baby's in Love with Eddie Vedder": LocationData("Running With Scissors"),
    "Pretty Fly for a Rabbi":             LocationData("Running With Scissors"),
    "The Weird Al Show Theme":                  LocationData("Running With Scissors"),
    "Jerry Springer":                        LocationData("Running With Scissors"),
    "Germs":        LocationData("Running With Scissors"),
    "Polka Power!":                   LocationData("Running With Scissors"),
    "Your Horoscope for Today":                        LocationData("Running With Scissors"),
    "It's All About the Pentiums":                     LocationData("Running With Scissors"),
    "Truck Drivin' Song":                LocationData("Running With Scissors"),
    "Grapefruit Diet":     LocationData("Running With Scissors"),
    "Albuquerque":                           LocationData("Running With Scissors"),

    # Poodle Hat
    "Couch Potato":       LocationData("Poodle Hat"),
    "Hardware Store":                    LocationData("Poodle Hat"),
    "Trash Day":                           LocationData("Poodle Hat"),
    "Party at the Leper Colony":                         LocationData("Poodle Hat"),
    "Angry White Boy Polka":                      LocationData("Poodle Hat"),
    "Wanna B Ur Lovr":                LocationData("Poodle Hat"),
    "A Complicated Song": LocationData("Poodle Hat"),
    "Why Does This Always Happen to Me?":                     LocationData("Poodle Hat"),
    "Ode to a Superhero":                 LocationData("Poodle Hat"),
    "Bob":        LocationData("Poodle Hat"),
    "eBay":                      LocationData("Poodle Hat"),
    "Genius in France": LocationData("Poodle Hat"),

    # Straight Outta Lynwood
    "White & Nerdy":                           LocationData("Straight Outta Lynwood"),
    "Pancreas":                        LocationData("Straight Outta Lynwood"),
    "Canadian Idiot": LocationData("Straight Outta Lynwood"),
    "I'll Sue Ya":          LocationData("Straight Outta Lynwood"),
    "Polkarama!":               LocationData("Straight Outta Lynwood"),
    "Virus Alert":                      LocationData("Straight Outta Lynwood"),
    "Confessions Part III":                           LocationData("Straight Outta Lynwood"),
    "Weasel Stomping Day":                          LocationData("Straight Outta Lynwood"),
    "Close but No Cigar":               LocationData("Straight Outta Lynwood"),
    "Do I Creep You Out":                 LocationData("Straight Outta Lynwood"),
    "Trapped in the Drive-Thru":                LocationData("Straight Outta Lynwood"),
    "Don't Download This Song":                       LocationData("Straight Outta Lynwood"),

    # Alpocalypse
    "Perform This Way":                          LocationData("Alpocalypse"),
    "CNR":              LocationData("Alpocalypse"),
    "TMZ":                       LocationData("Alpocalypse"),
    "Skipper Dan":            LocationData("Alpocalypse"),
    "Polka Face":                     LocationData("Alpocalypse"),
    "Craigslist":  LocationData("Alpocalypse"),
    "Party in the CIA":                       LocationData("Alpocalypse"),
    "Ringtone":                        LocationData("Alpocalypse"),
    "Another Tattoo": LocationData("Alpocalypse"),
    "If That Isn't Love":                             LocationData("Alpocalypse"),
    "Whatever You Like":                  LocationData("Alpocalypse"),
    "Stop Forwarding That Crap to Me":                LocationData("Alpocalypse"),

    # Mandatory Fun
    "Handy":                   LocationData("Mandatory Fun"),
    "Lame Claim to Fame":                          LocationData("Mandatory Fun"),
    "Foil":                       LocationData("Mandatory Fun"),
    "Sports Song": LocationData("Mandatory Fun"),
    "Word Crimes":         LocationData("Mandatory Fun"),
    "My Own Eyes":                   LocationData("Mandatory Fun"),
    "NOW That's What I Call Polka!":                    LocationData("Mandatory Fun"),
    "Mission Statement":                  LocationData("Mandatory Fun"),
    "Inactive":                       LocationData("Mandatory Fun"),
    "First World Problems":                       LocationData("Mandatory Fun"),
    "Tacky":                           LocationData("Mandatory Fun"),
    "Jackson Park Express":                   LocationData("Mandatory Fun"),

    # Medium Rarities
    "Take Me Down":   LocationData("Medium Rarities"),
    "My Bologna (Demo)":   LocationData("Medium Rarities", True),
    "Yoda (Demo)": LocationData("Medium Rarities", True),
    "Dr. Demento Jingle":                        LocationData("Medium Rarities"),
    "Pac-Man":                 LocationData("Medium Rarities"),
    "Dare to Be Stupid (Instrumental)":            LocationData("Medium Rarities", True),
    "Jurashiku Park":           LocationData("Medium Rarities", True),
    "Headline News": LocationData("Medium Rarities"),
    "Since You've Been Gone (Karaoke)":                  LocationData("Medium Rarities", True),
    "The Night Santa Went Crazy (Extra Gory Version)":  LocationData("Medium Rarities", True),
    "Spy Hard": LocationData("Medium Rarities"),
    "Lousy Haircut":                            LocationData("Medium Rarities"),
    "Homer and Marge": LocationData("Medium Rarities"),
    "The Brain Song": LocationData("Medium Rarities"),
    "30 Rock Theme Parody":                     LocationData("Medium Rarities"),
    "Super Duper Party Pony":                       LocationData("Medium Rarities"),
    "Sir Isaac Newton vs. Bill Nye":                   LocationData("Medium Rarities"),
    "Let the Pun Fit the Crime":               LocationData("Medium Rarities"),
    "Hey, Hey, We're the Monks":                   LocationData("Medium Rarities"),
    "Comedy Bang! Bang! Theme": LocationData("Medium Rarities"),
    "It's My World (And We're All Living In It)":                 LocationData("Medium Rarities"),
    "Beat on the Brat":                  LocationData("Medium Rarities"),
    "Happy Birthday (New Version)":                  LocationData("Medium Rarities", True),

    # Singles
    "You're Pitiful":             LocationData("Singles"),
    "The Hamilton Polka":             LocationData("Singles"),
    "Now You Know":             LocationData("Singles"),
    "Polkamania!":             LocationData("Singles"),
}

LOCATION_NAME_TO_ID = {
    name: 27 + i for i, name in enumerate(LOCATION_TABLE)
}

REGIONS: dict[str, list[str]] = {}
for name, data in LOCATION_TABLE.items():
    REGIONS.setdefault(data.region, []).append(name)


def create_all_locations(world: WeirdAlWorld) -> None:
    for region_name, location_names in REGIONS.items():
        try:
            region = world.get_region(region_name)
        except KeyError:
            continue
        for loc_name in location_names:
            if LOCATION_TABLE[loc_name].alt and not world.options.include_alt_recordings.value:
                continue
            loc = WeirdAlLocation(
                world.player,
                loc_name,
                LOCATION_NAME_TO_ID[loc_name],
                region,
            )
            region.locations.append(loc)
