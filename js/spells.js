fetch("../spells.json")
    .then((response) => response.json())
    .then((spells) => {
        const hideSpell = (spellAspect) => {
            spellAspect = spellAspect.toLowerCase();

            for (const spell of spells) {
                if (spell.level == spellAspect || spell.school == spellAspect) {
                    document.getElementById(spell.name).hidden = true;
                } else {
                    // This is not how this should work
                    for (const c of spell.classes) {
                        if (c == spellAspect) {
                            document.getElementById(spell.name).hidden = true;
                        }
                    }
                }
            }
        }

        const searchParams = new URLSearchParams(window.location.search);
        for (const [ key, _ ] of searchParams) {
            hideSpell(key);
        }
    });
