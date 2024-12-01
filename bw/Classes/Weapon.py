WEAPON_KNIFE = 1
WEAPON_PISTOL = 2
WEAPON_SHOTGUN = 3
WEAPON_SUBMACHINE = 4
WEAPON_RIFELS = 5
WEAPON_SNIPER = 6
WEAPON_MACHINE = 7
WEAPON_GRENADE = 8
WEAPON_BOMB = 9
WEAPON_REVOLVER = 10
WEAPON_CZ75A = 11
WEAPON_TASER = 12
WEAPON_AUTOSNIPER = 13


WeaponList = {
    "P2000" : { "ID" : 32, "Cattegory": WEAPON_PISTOL },
    "USP-S" : { "ID" : 61, "Cattegory": WEAPON_PISTOL },
    "Glock" : { "ID" : 4, "Cattegory": WEAPON_PISTOL }, 
    "Dual Berettas" : { "ID" : 2, "Cattegory": WEAPON_PISTOL },
    "P250" : { "ID" : 36, "Cattegory": WEAPON_PISTOL }, 
    "Tec-9" : { "ID" : 30, "Cattegory": WEAPON_PISTOL }, 
    "CZ75-Auto" : { "ID" : 63, "Cattegory": WEAPON_CZ75A },
    "Desert Eagle" : { "ID" : 1, "Cattegory": WEAPON_PISTOL },
    "Five-SeveN" : { "ID" : 3, "Cattegory": WEAPON_PISTOL }, 
    "R8" : { "ID" : 64, "Cattegory": WEAPON_REVOLVER },

    "Nova" : { "ID" : 35, "Cattegory": WEAPON_SHOTGUN },
    "XM1014" : { "ID" : 25, "Cattegory": WEAPON_SHOTGUN }, 
    "MAG-7" : { "ID" : 27, "Cattegory": WEAPON_SHOTGUN },
    "Sawed-Off" : { "ID" : 29, "Cattegory": WEAPON_SHOTGUN },

    "M249" : { "ID" : 14, "Cattegory": WEAPON_MACHINE },
    "Negev" : { "ID" : 28, "Cattegory": WEAPON_MACHINE },

    "MAC-10" : { "ID" : 17, "Cattegory": WEAPON_SUBMACHINE },
    "MP5-SD" : { "ID" : 23, "Cattegory": WEAPON_SUBMACHINE }, 
    "UMP-45" : { "ID" : 24, "Cattegory": WEAPON_SUBMACHINE },
    "P90" : { "ID" : 19, "Cattegory": WEAPON_SUBMACHINE },
    "Bizon" : { "ID" : 26, "Cattegory": WEAPON_SUBMACHINE }, 
    "MP9" : { "ID" : 34, "Cattegory": WEAPON_SUBMACHINE },
    "MP7" : { "ID" : 33, "Cattegory": WEAPON_SUBMACHINE }, 

    "FAMAS" : { "ID" : 10, "Cattegory": WEAPON_RIFELS }, 
    "M4A4" : { "ID" : 16, "Cattegory": WEAPON_RIFELS },
    "M4A1-S" : { "ID" : 60, "Cattegory": WEAPON_RIFELS },
    "AUG" : { "ID" : 8, "Cattegory": WEAPON_RIFELS },  
    "Galil" : { "ID" : 43, "Cattegory": WEAPON_RIFELS },
    "AK-47" : { "ID" : 7, "Cattegory": WEAPON_RIFELS },
    "SG 553" : { "ID" : 39, "Cattegory": WEAPON_RIFELS }, 

    "SSG 08" : { "ID" : 40, "Cattegory": WEAPON_SNIPER }, 
    "AWP" : { "ID" : 9, "Cattegory": WEAPON_SNIPER },

    "SCAR-20" : { "ID" : 38, "Cattegory": WEAPON_AUTOSNIPER }, 
    "G3SG1" : { "ID" : 11, "Cattegory": WEAPON_AUTOSNIPER },

    "Flashbang" : { "ID" : 43, "Cattegory": WEAPON_GRENADE },
    "Hegrenade" : { "ID" : 44, "Cattegory": WEAPON_GRENADE },
    "Smoke" : { "ID" : 45, "Cattegory": WEAPON_GRENADE },
    "Molotov" : { "ID" : 46, "Cattegory": WEAPON_GRENADE },
    "Decoy" : { "ID" : 47, "Cattegory": WEAPON_GRENADE },
    "Incgrenage" : { "ID" : 48, "Cattegory": WEAPON_GRENADE },

    "C4" : { "ID" : 49, "Cattegory": WEAPON_BOMB },
    "Taser" : { "ID" : 31, "Cattegory": WEAPON_TASER },

    "Knife" : { "ID" : 42, "Cattegory": WEAPON_KNIFE },
    "Knife Gold" : { "ID" : 41, "Cattegory": WEAPON_KNIFE },
    "Knife" : { "ID" : 59, "Cattegory": WEAPON_KNIFE },
    "Knife Ghost" : { "ID" : 80, "Cattegory": WEAPON_KNIFE },
    "Knife Bayonet" : { "ID" : 500, "Cattegory": WEAPON_KNIFE },
    "Knife Flip" : { "ID" : 505, "Cattegory": WEAPON_KNIFE },
    "Knife Gut" : { "ID" : 506, "Cattegory": WEAPON_KNIFE },
    "Knife Karambit" : { "ID" : 507, "Cattegory": WEAPON_KNIFE },
    "Knife M9" : { "ID" : 508, "Cattegory": WEAPON_KNIFE },
    "Knife Tactica" : { "ID" : 509, "Cattegory": WEAPON_KNIFE },
    "Knife Falchion" : { "ID" : 512, "Cattegory": WEAPON_KNIFE },
    "Knife Survival Bowie" : { "ID" : 514, "Cattegory": WEAPON_KNIFE },
    "Knife Butterfly" : { "ID" : 515, "Cattegory": WEAPON_KNIFE },
    "Knife Rush" : { "ID" : 516, "Cattegory": WEAPON_KNIFE },
    "Knife Ursus" : { "ID" : 519, "Cattegory": WEAPON_KNIFE },
    "Knife Gypsy Jackknife" : { "ID" : 520, "Cattegory": WEAPON_KNIFE },
    "Knife Stiletto" : { "ID" : 522, "Cattegory": WEAPON_KNIFE },
    "Knife Widowmaker" : { "ID" : 523, "Cattegory": WEAPON_KNIFE }
}


class Weapon():
    def getWeaponName(WeaponID):
        for Weapon in WeaponList.items():
            if (Weapon[1]["ID"] == WeaponID):
                return Weapon[0]
            
        return "Unknown"


    def getWeaponCategory(WeaponID):
        for Weapon in WeaponList.items():
            if (Weapon[1]["ID"] == WeaponID):
                return Weapon[1]["Cattegory"]
            
        return 0
    
    def getWeaponCategoryToCategory(WeaponCategory):
        for Weapon in WeaponList.items():
            if (Weapon[1]["Cattegory"] == WeaponCategory):
                return Weapon[1]["Cattegory"]
            
        return "Unknown"