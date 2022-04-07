#!/bin/env python3

import chevron, html, os, shutil

class Level:
    CANTRIP = "Cantrip"
    FIRST = "1st level"
    SECOND = "2nd level"
    THIRD = "3rd level"
    FOURTH = "4th level"
    FIFTH = "5th level"
    SIXTH = "6th level"
    SEVENTH = "7th level"
    EIGHTH = "8th level"
    NINTH = "9th level"

class School:
    ABJURATION = "🛡️ Abjuration"
    CONJURATION = "🔀 Conjuration"
    DIVINATION = "🔮 Divination"
    ENCHANTMENT = "😵‍💫 Enchantment"
    EVOCATION = "🪄 Evocation"
    ILLUSION = "❓ Illusion"
    NECROMANCY = "☠️ Necromancy"
    TRANSMUTATION = "🔁 Transmutation"

class Class:
    ARTIFICER = "Artificer"
    BARD = "Bard"
    CLERIC = "Cleric"
    DRUID = "Druid"
    PALADIN = "Paladin"
    RANGER = "Ranger"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    WIZARD = "Wizard"

# HTML
def bold(s: str) -> str:
    return "<b>" + s + "</b>"
def paragraph(s: str) -> str:
    return "<p>" + s + "</p>"
def unorderedList(*s: str) -> str:
    items = ""
    for item in s:
        items += "<li>" + item + "</li>"
    return "<ul>" + items + "</ul>"

# Formatting
def toCamelCase(s: str) -> str:
    first = True
    newString = ""
    for c in s:
        if first:
            newString += c.lower()
            first = False
        elif c == ' ':
            pass
        else:
            newString += c
    return newString
def toKebabCase(s: str) -> str:
    newString = ""
    for c in s:
        if c.isupper():
            newString += c.lower()
        elif c == ' ':
            newString += '-'
        else:
            newString += c
    return newString

seperator = ", "

spells = {
    "spells": [
        {
            "name": "Acid Splash",
            "level": Level.CANTRIP,
            "school": School.CONJURATION,

            "castingTime": "1 Action",
            "rangeArea": "60 feet",
            "components": "V, S",
            "duration": "Instant",

            "description": paragraph("You hurl a bubble of acid. Choose one creature within range, or choose two creatures within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage.") + paragraph(bold("At higher levels:") + " This spell's damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."),

            "classes": seperator.join([ Class.ARTIFICER, Class.SORCERER, Class.WIZARD ])
        },
        {
            "name": "Blade Ward",
            "level": Level.CANTRIP,
            "school": School.ABJURATION,

            "castingTime": "1 Action",
            "rangeArea": "Self",
            "components": "V, S",
            "duration": "1 Round",

            "description": paragraph("You extend your hand and trace a sigil of warding in the air. Until the end of your next turn, you have resistance against bludgeoning, piercing, and slashing damage dealt by weapon attacks."),

            "classes": seperator.join([ Class.BARD, Class.SORCERER, Class.WARLOCK, Class.WIZARD ])
        },
        {
            "name": "Booming Blade",
            "level": Level.CANTRIP,
            "school": School.EVOCATION,

            "castingTime": "1 Action",
            "rangeArea": "Self (5 foot radius)",
            "components": "S, M (a melee weapon worth at least 1 silver piece)",
            "duration": "1 Round",

            "description": paragraph("You brandish the weapon used in the spell's casting and make a melee attack with it against one creature within 5 feet of you. On a hit, the target suffers the weapon attack's normal effects and then becomes sheathed in booming energy until the start of your next turn. If the target willingly moves 5 feet or more before then, the target takes 1d8 thunder damage, and the spell ends.") + paragraph(bold("At higher levels:") + " At 5th level, the melee attack deals an extra 1d8 thunder damage to the target on a hit, and the damage the target takes for moving increases to 2d8. Both damage rolls increase by 1d8 at 11th level (2d8 and 3d8) and again at 17th level (3d8 and 4d8)."),

            "classes": seperator.join([ Class.ARTIFICER, Class.SORCERER, Class.WARLOCK, Class.WIZARD ])
        },
        {
            "name": "Chill Touch",
            "level": Level.CANTRIP,
            "school": School.NECROMANCY,

            "castingTime": "1 Action",
            "rangeArea": "120 feet",
            "components": "V, S",
            "duration": "1 Round",

            "description": paragraph("You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can't regain hit points until the start of your next turn. Until then, the hand clings to the target. If you hit an undead target, it also has disadvantage on attack rolls against you until the end of your next turn.") + paragraph(bold("At higher levels:") + " This spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."),

            "classes": seperator.join([ Class.SORCERER, Class.WARLOCK, Class.WIZARD ])
        },
        {
            "name": "Control Flames",
            "level": Level.CANTRIP,
            "school": School.TRANSMUTATION,

            "castingTime": "1 Action",
            "rangeArea": "60 feet",
            "components": "S",
            "duration": "Instant or 1 hour",

            "description": paragraph("You choose a nonmagical flame that you can see within range and that fits within a 5-foot cube. You affect it in one of the following ways:") + unorderedList("You instantaneously expand the flame 5 feet in one direction, provided that wood or other fuel is present in the new location.", "You instantaneously extinguish the flames within the cube.", "You double or halve the area of bright light and dim light cast by the flame, change its color, or both. The change lasts for 1 hour.", "You cause simple shapes—such as the vague form of a creature, an inanimate object, or a location—to appear within the flames and animate as you like. The shapes last for 1 hour.") + paragraph("If you cast this spell multiple times, you can have up to three of its non-instantaneous effects active at a time, and you can dismiss such an effect as an action."),

            "classes": seperator.join([ Class.DRUID, Class.SORCERER, Class.WIZARD ])
        },
        {
            "name": "Create Bonfire",
            "level": Level.CANTRIP,
            "school": School.CONJURATION,

            "castingTime": "1 Action",
            "rangeArea": "60 feet",
            "components": "V, S",
            "duration": "Concentration, up to 1 minute",

            "description": paragraph("You create a bonfire on ground that you can see within range. Until the spell ends, the bonfire fills a 5-foot cube. Any creature in the bonfire's space when you cast the spell must succeed on a Dexterity saving throw or take 1d8 fire damage. A creature must also make the saving throw when it enters the bonfire's space for the first time on a turn or ends its turn there.") + paragraph(bold("At higher levels:") + " The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."),

            "classes": seperator.join([ Class.DRUID, Class.SORCERER, Class.WARLOCK, Class.WIZARD ])
        },
        {
            "name": "Dancing Lights",
            "level": Level.CANTRIP,
            "school": School.EVOCATION,

            "castingTime": "1 Action",
            "rangeArea": "120 feet",
            "components": "V, S, M (a bit of phosphorus or wychwood, or a glowworm)",
            "duration": "Concentration, up to 1 minute",

            "description": paragraph("You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration. You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light sheds dim light in a 10-foot radius.") + paragraph("As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell's range."),

            "classes": seperator.join([ Class.ARTIFICER, Class.BARD, Class.SORCERER, Class.WIZARD ])
        },
        {
            "name": "Druidcraft",
            "level": Level.CANTRIP,
            "school": School.TRANSMUTATION,

            "castingTime": "1 Action",
            "rangeArea": "30 feet",
            "components": "V, S",
            "duration": "Instant",

            "description": paragraph("Whispering to the spirits of nature, you create one of the following effects within range:") + unorderedList("You create a tiny, harmless sensory effect that predicts what the weather will be at your location for the next 24 hours. The effect might manifest as a golden orb for clear skies, a cloud for rain, falling snowflakes for snow, and so on. This effect persists for 1 round.", "You instantly make a flower blossom, a seed pod open, or a leaf bud bloom.", "You create an instantaneous, harmless sensory effect, such as falling leaves, a puff of wind, the sound of a small animal, or the faint odor of skunk. The effect must fit in a 5-foot cube.", "You instantly light or snuff out a candle, a torch, or a small campfire."),

            "classes": Class.DRUID
        },
        {
            "name": "Eldritch Blast",
            "level": Level.CANTRIP,
            "school": School.EVOCATION,

            "castingTime": "1 Action",
            "rangeArea": "120 feet",
            "components": "V, S",
            "duration": "Instant",

            "description": paragraph("A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 force damage.") + paragraph(bold("At higher levels:") + " The spell creates more than one beam when you reach higher levels: two beams at 5th level, three beams at 11th level, and four beams at 17th level. You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam."),

            "classes": Class.WARLOCK
        }
    ]
}

if os.path.isdir("build"):
    shutil.rmtree("build")
os.mkdir("build")
os.mkdir(os.path.join("build", "backgrounds"))
os.mkdir(os.path.join("build", "classes"))
os.mkdir(os.path.join("build", "css"))
os.mkdir(os.path.join("build", "js"))
os.mkdir(os.path.join("build", "spells"))

# spells.html
with open("spells.mustache", "r") as f:
    for spell in spells.get("spells"):
        spell["id"] = toCamelCase(spell.get("name"))
        spell["link"] = toKebabCase(spell.get("name"))

    render = chevron.render(f, spells)
with open(os.path.join("build", "spells.html"), "w", encoding="utf-8") as f:
    f.write(render)

# spells/*.html
for spell in spells.get("spells"):
    link = spell.get("link")

    school = spell.get("school")
    level = spell.get("level")
    spell["schoolAndLevel"] = f"{school} cantrip" if spell.get("level") == "Cantrip" else f"{level} {school} spell"

    with open("spell.mustache", "r") as f:
        render = chevron.render(f, spell)
    with open(os.path.join("build", "spells", f"{link}.html"), "w", encoding="utf-8") as f:
        f.write(html.unescape(render))

# All the other files
for file in os.listdir("backgrounds"):
    shutil.copy(os.path.join("backgrounds", file), os.path.join("build", "backgrounds"))
for file in os.listdir("classes"):
    shutil.copy(os.path.join("classes", file), os.path.join("build", "classes"))
for file in os.listdir("css"):
    shutil.copy(os.path.join("css", file), os.path.join("build", "css"))
for file in os.listdir("js"):
    shutil.copy(os.path.join("js", file), os.path.join("build", "js"))
files = [
    "backgrounds.html",
    "classes.html",
    "equipment.html",
    "feats.html",
    "index.html",
    "logo.svg",
    "magic-items.html",
    "monsters.html",
    "races.html",
    "vehicles.html"
]
for file in files:
    shutil.copy(file, "build")
