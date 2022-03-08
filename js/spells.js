const spells = [
    "acid_splash",
    "blade_ward",
    "booming_blade",
    "chill_touch",
    "control_flames",
    "create_bonfire",
    "dancing_lights",
    "druidcraft",
    "eldritch_blast",
    "encode_thoughts",
    "fire_bolt",
    "friends",
    "frostbite",
    "green_flame_blade",
    "guidance",
    "gust",
    "infestation",
    "light",
    "lightning_lure",
    "mage_hand",
    "magic_stone",
    "mending",
    "message",
    "mind_sliver",
    "minor_illusion",
    "mold_earth",
    "poison_spray",
    "prestidigitation",
    "primal_savagery",
    "produce_flame",
    "ray_of_frost",
    "resistance",
    "sacred_flame",
    "sapping_sting",
    "shape_water",
    "shillelagh",
    "shocking_grasp",
    "spare_the_dying",
    "sword_burst",
    "thaumaturgy",
    "thorn_whip",
    "thunderclap",
    "toll_the_dead",
    "true_strike",
    "vicious_mockery",
    "word_of_radiance"
];

const createRow = (data, spell) => {
    let tr = document.createElement("tr");

    // Level
    let td = document.createElement("td");
    td.textContent = data.level;
    tr.appendChild(td);

    // Name (and Link)
    td = document.createElement("td");

    let b = document.createElement("b");

    let a = document.createElement("a");
    a.setAttribute("href", "spells/" + spell);
    a.textContent = data.name;

    b.appendChild(a);
    td.appendChild(b);
    tr.appendChild(td);

    // School
    td = document.createElement("td");
    td.textContent = " " + data.school;

    let icon = document.createElement("span");
    switch (data.school) {
        case "Abjuration":
            icon.textContent = "🛡️";
            break;
        case "Conjuration":
            icon.textContent = "🔀";
            break;
        case "Divination":
            icon.textContent = "🔮";
            break;
        case "Enchantment":
            icon.textContent = "🌀";
            break;
        case "Evocation":
            icon.textContent = "🪄";
            break;
        case "Illusion":
            icon.textContent = "❓";
            break;
        case "Necromancy":
            icon.textContent = "☠️";
            break;
        case "Transmutation":
            icon.textContent = "🔁";
            break;
        default:
            icon.textContent = "⚠️";
            break;
    }
    td.prepend(icon);

    tr.appendChild(td);

    // Components
    td = document.createElement("td");
    td.textContent = data.components;
    tr.appendChild(td);

    // Casting Time
    td = document.createElement("td");
    td.textContent = data.castingTime;
    tr.appendChild(td);

    // Duration
    td = document.createElement("td");
    td.textContent = data.duration;
    tr.appendChild(td);

    // Range / Area
    td = document.createElement("td");
    td.textContent = data.rangeArea;
    tr.appendChild(td);

    document.getElementById("tbody").appendChild(tr);
}

for (let s in spells) {
    fetch("json/" + spells[s] + ".json")
        .then(r => r.json())
        .then(d => createRow(d, spells[s]));
}
