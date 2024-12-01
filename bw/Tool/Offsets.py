import json


with open("C:\MyOffsets\offsets.json") as File:
    Json = json.loads(File.read())

    dwLocalPlayerPawn = Json["client.dll"]["dwLocalPlayerPawn"]
    dwEntityList = Json["client.dll"]["dwEntityList"]
    dwViewAngles = Json["client.dll"]["dwViewAngles"]
    dwViewMatrix = Json["client.dll"]["dwViewMatrix"]
    dwPlantedC4  = Json["client.dll"]["dwPlantedC4"]
    dwGameRules  = Json["client.dll"]["dwGameRules"]


with open("C:\MyOffsets\client_dll.json") as File:
    Json = json.loads(File.read())

    m_iTeamNum = Json["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_iTeamNum"]
    m_iHealth = Json["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_iHealth"]
    m_lifeState = Json["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_lifeState"]
    m_pGameSceneNode = Json["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_pGameSceneNode"]
    m_fFlags = Json["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_fFlags"]

    m_iIDEntIndex = Json["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_iIDEntIndex"]
    m_vecLastClipCameraPos = Json["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_vecLastClipCameraPos"]
    m_angEyeAngles = Json["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_angEyeAngles"]
    m_pClippingWeapon = Json["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_pClippingWeapon"]
    m_flFlashOverlayAlpha = Json["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_flFlashOverlayAlpha"]

    m_bIsScoped = Json["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_bIsScoped"]
    m_ArmorValue = Json["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_ArmorValue"]
    m_iShotsFired = Json["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_iShotsFired"]
    m_flEmitSoundTime = Json["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_flEmitSoundTime"]
    m_aimPunchAngle = Json["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_aimPunchAngle"]
    m_entitySpottedState = Json["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_entitySpottedState"]

    m_iItemDefinitionIndex = Json["client.dll"]["classes"]["C_EconItemView"]["fields"]["m_iItemDefinitionIndex"]
    m_AttributeManager = Json["client.dll"]["classes"]["C_EconEntity"]["fields"]["m_AttributeManager"]

    m_vOldOrigin = Json["client.dll"]["classes"]["C_BasePlayerPawn"]["fields"]["m_vOldOrigin"]
    m_pWeaponServices = Json["client.dll"]["classes"]["C_BasePlayerPawn"]["fields"]["m_pWeaponServices"]

    m_bSpotted = Json["client.dll"]["classes"]["EntitySpottedState_t"]["fields"]["m_bSpotted"]
    m_bSpottedByMask = Json["client.dll"]["classes"]["EntitySpottedState_t"]["fields"]["m_bSpottedByMask"]

    m_bDormant = Json["client.dll"]["classes"]["CGameSceneNode"]["fields"]["m_bDormant"]
    m_vecAbsOrigin = Json["client.dll"]["classes"]["CGameSceneNode"]["fields"]["m_vecAbsOrigin"]

    m_nBombSite = Json["client.dll"]["classes"]["C_PlantedC4"]["fields"]["m_nBombSite"]
    m_bBeingDefused = Json["client.dll"]["classes"]["C_PlantedC4"]["fields"]["m_bBeingDefused"]
    m_flDefuseLength = Json["client.dll"]["classes"]["C_PlantedC4"]["fields"]["m_flDefuseLength"]
    m_flTimerLength = Json["client.dll"]["classes"]["C_PlantedC4"]["fields"]["m_flTimerLength"]

    m_hPawn = Json["client.dll"]["classes"]["CBasePlayerController"]["fields"]["m_hPawn"]
    m_modelState = Json["client.dll"]["classes"]["CSkeletonInstance"]["fields"]["m_modelState"]
    m_vecViewOffset = Json["client.dll"]["classes"]["C_BaseModelEntity"]["fields"]["m_vecViewOffset"]
    m_iClip1 = Json["client.dll"]["classes"]["C_BasePlayerWeapon"]["fields"]["m_iClip1"]
    m_Item = Json["client.dll"]["classes"]["C_AttributeContainer"]["fields"]["m_Item"]

    m_sSanitizedPlayerName = Json["client.dll"]["classes"]["CCSPlayerController"]["fields"]["m_sSanitizedPlayerName"]