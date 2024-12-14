import json

# Constants for file paths
OFFSETS_FILE = "C:\MyOffsets\offsets.json"
CLIENT_DLL_FILE = "C:\MyOffsets\client_dll.json"

# Load main game offsets
with open(OFFSETS_FILE) as file:
    offsets_json = json.loads(file.read())
    client_dll = offsets_json["client.dll"]

    # Core game offsets
    dwLocalPlayerPawn = client_dll["dwLocalPlayerPawn"]
    dwEntityList = client_dll["dwEntityList"] 
    dwViewAngles = client_dll["dwViewAngles"]
    dwViewMatrix = client_dll["dwViewMatrix"]
    dwPlantedC4 = client_dll["dwPlantedC4"]
    dwGameRules = client_dll["dwGameRules"]

# Load detailed client.dll offsets
with open(CLIENT_DLL_FILE) as file:
    client_json = json.loads(file.read())
    client_classes = client_json["client.dll"]["classes"]

    # Base entity fields
    m_iTeamNum = client_classes["C_BaseEntity"]["fields"]["m_iTeamNum"]
    m_iHealth = client_classes["C_BaseEntity"]["fields"]["m_iHealth"]
    m_lifeState = client_classes["C_BaseEntity"]["fields"]["m_lifeState"]
    m_pGameSceneNode = client_classes["C_BaseEntity"]["fields"]["m_pGameSceneNode"]
    m_fFlags = client_classes["C_BaseEntity"]["fields"]["m_fFlags"]

    # Player pawn base fields
    player_pawn_base = client_classes["C_CSPlayerPawnBase"]["fields"]
    m_iIDEntIndex = player_pawn_base["m_iIDEntIndex"]
    m_vecLastClipCameraPos = player_pawn_base["m_vecLastClipCameraPos"]
    m_angEyeAngles = player_pawn_base["m_angEyeAngles"]
    m_pClippingWeapon = player_pawn_base["m_pClippingWeapon"]
    m_flFlashOverlayAlpha = player_pawn_base["m_flFlashOverlayAlpha"]

    # CS player pawn specific fields
    player_pawn = client_classes["C_CSPlayerPawn"]["fields"]
    m_bIsScoped = player_pawn["m_bIsScoped"]
    m_ArmorValue = player_pawn["m_ArmorValue"]
    m_iShotsFired = player_pawn["m_iShotsFired"]
    m_flEmitSoundTime = player_pawn["m_flEmitSoundTime"]
    m_aimPunchAngle = player_pawn["m_aimPunchAngle"]
    m_entitySpottedState = player_pawn["m_entitySpottedState"]

    # Economy and item related fields
    m_iItemDefinitionIndex = client_classes["C_EconItemView"]["fields"]["m_iItemDefinitionIndex"]
    m_AttributeManager = client_classes["C_EconEntity"]["fields"]["m_AttributeManager"]

    # Base player pawn fields
    m_vOldOrigin = client_classes["C_BasePlayerPawn"]["fields"]["m_vOldOrigin"]
    m_pWeaponServices = client_classes["C_BasePlayerPawn"]["fields"]["m_pWeaponServices"]

    # Entity spotting fields
    m_bSpotted = client_classes["EntitySpottedState_t"]["fields"]["m_bSpotted"]
    m_bSpottedByMask = client_classes["EntitySpottedState_t"]["fields"]["m_bSpottedByMask"]

    # Scene node fields
    m_bDormant = client_classes["CGameSceneNode"]["fields"]["m_bDormant"]
    m_vecAbsOrigin = client_classes["CGameSceneNode"]["fields"]["m_vecAbsOrigin"]

    # C4 bomb fields
    planted_c4 = client_classes["C_PlantedC4"]["fields"]
    m_nBombSite = planted_c4["m_nBombSite"]
    m_bBeingDefused = planted_c4["m_bBeingDefused"]
    m_flDefuseLength = planted_c4["m_flDefuseLength"]
    m_flTimerLength = planted_c4["m_flTimerLength"]

    # Miscellaneous fields
    m_hPawn = client_classes["CBasePlayerController"]["fields"]["m_hPawn"]
    m_modelState = client_classes["CSkeletonInstance"]["fields"]["m_modelState"]
    m_vecViewOffset = client_classes["C_BaseModelEntity"]["fields"]["m_vecViewOffset"]
    m_iClip1 = client_classes["C_BasePlayerWeapon"]["fields"]["m_iClip1"]
    m_Item = client_classes["C_AttributeContainer"]["fields"]["m_Item"]
    m_sSanitizedPlayerName = client_classes["CCSPlayerController"]["fields"]["m_sSanitizedPlayerName"]
