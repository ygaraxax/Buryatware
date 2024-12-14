# Weapon category constants
WEAPON_KNIFE = 1
WEAPON_PISTOL = 2
WEAPON_SHOTGUN = 3
WEAPON_SUBMACHINE = 4
WEAPON_RIFLES = 5  # Fixed typo in RIFELS
WEAPON_SNIPER = 6
WEAPON_MACHINE = 7
WEAPON_GRENADE = 8
WEAPON_BOMB = 9
WEAPON_REVOLVER = 10
WEAPON_CZ75A = 11
WEAPON_TASER = 12
WEAPON_AUTOSNIPER = 13

# Weapon definitions with IDs and categories
WeaponList = {
    # Pistols
    "P2000": {"ID": 32, "Category": WEAPON_PISTOL},  # Fixed typo in Category
    "USP-S": {"ID": 61, "Category": WEAPON_PISTOL},
    "Glock": {"ID": 4, "Category": WEAPON_PISTOL},
    "Dual Berettas": {"ID": 2, "Category": WEAPON_PISTOL},
    "P250": {"ID": 36, "Category": WEAPON_PISTOL},
    "Tec-9": {"ID": 30, "Category": WEAPON_PISTOL},
    "CZ75-Auto": {"ID": 63, "Category": WEAPON_CZ75A},
    "Desert Eagle": {"ID": 1, "Category": WEAPON_PISTOL},
    "Five-SeveN": {"ID": 3, "Category": WEAPON_PISTOL},
    "R8": {"ID": 64, "Category": WEAPON_REVOLVER},

    # Shotguns
    "Nova": {"ID": 35, "Category": WEAPON_SHOTGUN},
    "XM1014": {"ID": 25, "Category": WEAPON_SHOTGUN},
    "MAG-7": {"ID": 27, "Category": WEAPON_SHOTGUN},
    "Sawed-Off": {"ID": 29, "Category": WEAPON_SHOTGUN},

    # Heavy
    "M249": {"ID": 14, "Category": WEAPON_MACHINE},
    "Negev": {"ID": 28, "Category": WEAPON_MACHINE},

    # SMGs
    "MAC-10": {"ID": 17, "Category": WEAPON_SUBMACHINE},
    "MP5-SD": {"ID": 23, "Category": WEAPON_SUBMACHINE},
    "UMP-45": {"ID": 24, "Category": WEAPON_SUBMACHINE},
    "P90": {"ID": 19, "Category": WEAPON_SUBMACHINE},
    "Bizon": {"ID": 26, "Category": WEAPON_SUBMACHINE},
    "MP9": {"ID": 34, "Category": WEAPON_SUBMACHINE},
    "MP7": {"ID": 33, "Category": WEAPON_SUBMACHINE},

    # Rifles
    "FAMAS": {"ID": 10, "Category": WEAPON_RIFLES},
    "M4A4": {"ID": 16, "Category": WEAPON_RIFLES},
    "M4A1-S": {"ID": 60, "Category": WEAPON_RIFLES},
    "AUG": {"ID": 8, "Category": WEAPON_RIFLES},
    "Galil": {"ID": 43, "Category": WEAPON_RIFLES},
    "AK-47": {"ID": 7, "Category": WEAPON_RIFLES},
    "SG 553": {"ID": 39, "Category": WEAPON_RIFLES},

    # Snipers
    "SSG 08": {"ID": 40, "Category": WEAPON_SNIPER},
    "AWP": {"ID": 9, "Category": WEAPON_SNIPER},

    # Auto-Snipers
    "SCAR-20": {"ID": 38, "Category": WEAPON_AUTOSNIPER},
    "G3SG1": {"ID": 11, "Category": WEAPON_AUTOSNIPER},

    # Grenades
    "Flashbang": {"ID": 43, "Category": WEAPON_GRENADE},
    "Hegrenade": {"ID": 44, "Category": WEAPON_GRENADE},
    "Smoke": {"ID": 45, "Category": WEAPON_GRENADE},
    "Molotov": {"ID": 46, "Category": WEAPON_GRENADE},
    "Decoy": {"ID": 47, "Category": WEAPON_GRENADE},
    "Incgrenage": {"ID": 48, "Category": WEAPON_GRENADE},

    # Equipment
    "C4": {"ID": 49, "Category": WEAPON_BOMB},
    "Taser": {"ID": 31, "Category": WEAPON_TASER},

    # Knives
    "Knife": {"ID": 42, "Category": WEAPON_KNIFE},  # Removed duplicate knife entry
    "Knife Gold": {"ID": 41, "Category": WEAPON_KNIFE},
    "Knife Ghost": {"ID": 80, "Category": WEAPON_KNIFE},
    "Knife Bayonet": {"ID": 500, "Category": WEAPON_KNIFE},
    "Knife Flip": {"ID": 505, "Category": WEAPON_KNIFE},
    "Knife Gut": {"ID": 506, "Category": WEAPON_KNIFE},
    "Knife Karambit": {"ID": 507, "Category": WEAPON_KNIFE},
    "Knife M9": {"ID": 508, "Category": WEAPON_KNIFE},
    "Knife Tactica": {"ID": 509, "Category": WEAPON_KNIFE},
    "Knife Falchion": {"ID": 512, "Category": WEAPON_KNIFE},
    "Knife Survival Bowie": {"ID": 514, "Category": WEAPON_KNIFE},
    "Knife Butterfly": {"ID": 515, "Category": WEAPON_KNIFE},
    "Knife Rush": {"ID": 516, "Category": WEAPON_KNIFE},
    "Knife Ursus": {"ID": 519, "Category": WEAPON_KNIFE},
    "Knife Gypsy Jackknife": {"ID": 520, "Category": WEAPON_KNIFE},
    "Knife Stiletto": {"ID": 522, "Category": WEAPON_KNIFE},
    "Knife Widowmaker": {"ID": 523, "Category": WEAPON_KNIFE}
}


class Weapon:
    @staticmethod
    def getWeaponName(WeaponID):
        """Get weapon name from weapon ID"""
        for weapon_name, weapon_data in WeaponList.items():
            if weapon_data["ID"] == WeaponID:
                return weapon_name
        return "Unknown"

    @staticmethod
    def getWeaponCategory(WeaponID):
        """Get weapon category from weapon ID"""
        for weapon_data in WeaponList.values():
            if weapon_data["ID"] == WeaponID:
                return weapon_data["Category"]
        return 0

    @staticmethod
    def getWeaponCategoryToCategory(WeaponCategory):
        """Get weapon category from category ID"""
        for weapon_data in WeaponList.values():
            if weapon_data["Category"] == WeaponCategory:
                return weapon_data["Category"]
        return "Unknown"
