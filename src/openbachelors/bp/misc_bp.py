from fastapi import APIRouter
from fastapi import Request

from ..const.json_const import true, false, null
from ..const.filepath import CONFIG_JSON, VERSION_JSON, ACTIVITY_TABLE
from ..util.const_json_loader import const_json_loader
from ..util.player_data import player_data_decorator
from ..util.battle_log_logger import log_battle_log_if_necessary

router = APIRouter()


@router.post("/deepSea/branch")
@player_data_decorator
async def deepSea_branch(player_data, request: Request):
    request_json = await request.json()

    for branch in request_json["branches"]:
        tech_tree_id = branch["techTreeId"]
        branch_id = branch["branchId"]

        player_data["deepSea"]["techTrees"][tech_tree_id]["branch"] = branch_id

    response = {}
    return response


@router.post("/act25side/battleStart")
@player_data_decorator
async def act25side_battleStart(player_data, request: Request):
    request_json = await request.json()

    stage_id = request_json["stageId"]
    player_data.extra_save.save_obj["cur_stage_id"] = stage_id

    response = {
        "result": 0,
        "battleId": "00000000-0000-0000-0000-000000000000",
        "apFailReturn": 0,
        "isApProtect": 0,
        "inApProtectPeriod": false,
        "notifyPowerScoreNotEnoughIfFailed": false,
    }
    return response


@router.post("/act25side/battleFinish")
@player_data_decorator
async def act25side_battleFinish(player_data, request: Request):
    request_json = await request.json()

    log_battle_log_if_necessary(player_data, request_json["data"])

    response = {
        "result": 0,
        "apFailReturn": 0,
        "expScale": 1.2,
        "goldScale": 1.2,
        "rewards": [],
        "firstRewards": [],
        "unlockStages": [],
        "unusualRewards": [],
        "additionalRewards": [],
        "furnitureRewards": [],
        "overrideRewards": [],
        "alert": [],
        "suggestFriend": false,
        "pryResult": [],
        "itemReturn": [],
    }
    return response


@router.post("/charm/setSquad")
@player_data_decorator
async def charm_setSquad(player_data, request: Request):
    request_json = await request.json()

    player_data["charm"]["squad"] = request_json["squad"]

    response = {}
    return response


@router.post("/car/confirmBattleCar")
@player_data_decorator
async def car_confirmBattleCar(player_data, request: Request):
    request_json = await request.json()

    player_data["car"]["battleCar"] = request_json["car"]

    response = {}
    return response


@router.post("/retro/typeAct20side/competitionStart")
@player_data_decorator
async def retro_typeAct20side_competitionStart(player_data, request: Request):
    request_json = await request.json()
    response = {
        "result": 0,
        "battleId": "00000000-0000-0000-0000-000000000000",
    }
    return response


@router.post("/retro/typeAct20side/competitionFinish")
@player_data_decorator
async def retro_typeAct20side_competitionFinish(player_data, request: Request):
    request_json = await request.json()

    log_battle_log_if_necessary(player_data, request_json["data"])

    response = {
        "performance": 0,
        "expression": 0,
        "operation": 0,
        "total": 0,
        "level": "SS",
        "isNew": false,
    }
    return response


@router.post("/trainingGround/battleStart")
@player_data_decorator
async def trainingGround_battleStart(player_data, request: Request):
    request_json = await request.json()
    response = {
        "result": 0,
        "battleId": "00000000-0000-0000-0000-000000000000",
    }
    return response


@router.post("/trainingGround/battleFinish")
@player_data_decorator
async def trainingGround_battleFinish(player_data, request: Request):
    request_json = await request.json()

    log_battle_log_if_necessary(player_data, request_json["data"])

    response = {
        "result": 0,
        "firstRewards": [],
    }
    return response


@router.post("/medal/setCustomData")
@player_data_decorator
async def medal_setCustomData(player_data, request: Request):
    request_json = await request.json()

    custom_data = request_json["data"]

    player_data["medal"]["custom"]["customs"]["1"] = custom_data

    response = {}
    return response


@router.post("/firework/savePlateSlots")
@player_data_decorator
async def firework_savePlateSlots(player_data, request: Request):
    request_json = await request.json()

    player_data["firework"]["plate"]["slots"] = request_json["slots"]

    response = {}
    return response


@router.post("/firework/changeAnimal")
@player_data_decorator
async def firework_changeAnimal(player_data, request: Request):
    request_json = await request.json()

    player_data["firework"]["animal"]["select"] = request_json["animal"]

    response = {
        "animal": request_json["animal"],
    }
    return response


@router.post("/activity/enemyDuel/singleBattleStart")
@player_data_decorator
async def activity_enemyDuel_singleBattleStart(player_data, request: Request):
    request_json = await request.json()

    response = {
        "result": 0,
        "battleId": "00000000-0000-0000-0000-000000000000",
    }
    return response


@router.post("/activity/enemyDuel/singleBattleFinish")
@player_data_decorator
async def activity_enemyDuel_singleBattleFinish(player_data, request: Request):
    request_json = await request.json()

    log_battle_log_if_necessary(player_data, request_json["activityId"])

    activity_id = request_json["activityId"]
    activity_table = const_json_loader[ACTIVITY_TABLE]

    rank_lst = [
        {"id": "1", "rank": 1, "score": 262900, "isPlayer": 1},
    ]

    for npc_id, npc_obj in activity_table["activity"]["ENEMY_DUEL"][activity_id][
        "npcData"
    ]:
        if len(rank_lst) >= 8:
            break
        rank_lst.append(
            {"id": npc_id, "rank": 2, "score": 0, "isPlayer": 0},
        )

    response = {
        "result": 0,
        "choiceCnt": {"skip": 0, "normal": 5, "allIn": 5},
        "commentId": "Comment_Operation_1",
        "isHighScore": false,
        "rankList": rank_lst,
        "bp": 0,
        "dailyMission": {"add": 0, "reward": 0},
    }
    return response


@router.post("/activity/vecBreakV2/battleStart")
@player_data_decorator
async def activity_vecBreakV2_battleStart(player_data, request: Request):
    request_json = await request.json()

    response = {
        "result": 0,
        "battleId": "00000000-0000-0000-0000-000000000000",
    }
    return response


@router.post("/activity/vecBreakV2/battleFinish")
@player_data_decorator
async def activity_vecBreakV2_battleFinish(player_data, request: Request):
    request_json = await request.json()

    log_battle_log_if_necessary(player_data, request_json["data"])

    response = {
        "result": 0,
        "msBefore": 0,
        "msAfter": 0,
        "unlockStages": [],
        "suggestFriend": false,
        "finTs": 1700000000,
    }
    return response


@router.post("/vecBreakV2/getSeasonRecord")
@player_data_decorator
async def vecBreakV2_getSeasonRecord(player_data, request: Request):
    request_json = await request.json()

    response = {
        "seasons": {},
    }
    return response


def get_vec_break_v2_defense_buff_id(activity_id, stage_id):
    activity_table = const_json_loader[ACTIVITY_TABLE]

    defense_buff_id = activity_table["activity"]["VEC_BREAK_V2"][activity_id][
        "defenseDetailDict"
    ][stage_id]["buffId"]

    return defense_buff_id


@router.post("/activity/vecBreakV2/defendBattleStart")
@player_data_decorator
async def activity_vecBreakV2_defendBattleStart(player_data, request: Request):
    request_json = await request.json()

    activity_id = request_json["activityId"]
    stage_id = request_json["stageId"]

    defense_buff_id = get_vec_break_v2_defense_buff_id(activity_id, stage_id)

    defense_buff_id_lst = player_data["activity"]["VEC_BREAK_V2"][activity_id][
        "activatedBuff"
    ].copy()
    if defense_buff_id not in defense_buff_id_lst:
        defense_buff_id_lst.append(defense_buff_id)
    player_data["activity"]["VEC_BREAK_V2"][activity_id]["activatedBuff"] = (
        defense_buff_id_lst
    )

    player_data["activity"]["VEC_BREAK_V2"][activity_id]["defendStages"][stage_id][
        "defendSquad"
    ] = [{"charInstId": i["charInstId"]} for i in request_json["squad"]["slots"]]

    response = {
        "result": 0,
        "battleId": "00000000-0000-0000-0000-000000000000",
    }
    return response


@router.post("/activity/vecBreakV2/defendBattleFinish")
@player_data_decorator
async def activity_vecBreakV2_defendBattleFinish(player_data, request: Request):
    request_json = await request.json()

    log_battle_log_if_necessary(player_data, request_json["data"])

    response = {
        "msBefore": 0,
        "msAfter": 0,
        "finTs": 1700000000,
    }
    return response


@router.post("/activity/vecBreakV2/setDefend")
@player_data_decorator
async def activity_vecBreakV2_setDefend(player_data, request: Request):
    request_json = await request.json()

    activity_id = request_json["activityId"]
    stage_id = request_json["stageId"]

    defense_buff_id = get_vec_break_v2_defense_buff_id(activity_id, stage_id)

    defense_buff_id_lst = player_data["activity"]["VEC_BREAK_V2"][activity_id][
        "activatedBuff"
    ].copy()
    if defense_buff_id in defense_buff_id_lst:
        defense_buff_id_lst.remove(defense_buff_id)
    player_data["activity"]["VEC_BREAK_V2"][activity_id]["activatedBuff"] = (
        defense_buff_id_lst
    )

    player_data["activity"]["VEC_BREAK_V2"][activity_id]["defendStages"][stage_id][
        "defendSquad"
    ] = []

    response = {}
    return response


@router.post("/activity/vecBreakV2/changeBuffList")
@player_data_decorator
async def activity_vecBreakV2_changeBuffList(player_data, request: Request):
    request_json = await request.json()

    activity_id = request_json["activityId"]

    player_data["activity"]["VEC_BREAK_V2"][activity_id]["activatedBuff"] = (
        request_json["buffList"]
    )

    response = {}
    return response


@router.post("/activity/bossRush/battleStart")
@player_data_decorator
async def activity_bossRush_battleStart(player_data, request: Request):
    request_json = await request.json()

    response = {
        "result": 0,
        "battleId": "00000000-0000-0000-0000-000000000000",
        "apFailReturn": 0,
        "isApProtect": 0,
        "inApProtectPeriod": false,
        "notifyPowerScoreNotEnoughIfFailed": false,
    }
    return response


@router.post("/activity/bossRush/battleFinish")
@player_data_decorator
async def activity_bossRush_battleFinish(player_data, request: Request):
    request_json = await request.json()

    log_battle_log_if_necessary(player_data, request_json["data"])

    response = {
        "result": 0,
        "apFailReturn": 0,
        "expScale": 0,
        "goldScale": 0,
        "rewards": [],
        "firstRewards": [],
        "unlockStages": [],
        "unusualRewards": [],
        "additionalRewards": [],
        "furnitureRewards": [],
        "alert": [],
        "suggestFriend": false,
        "pryResult": [],
        "wave": 3,
        "milestoneBefore": 0,
        "milestoneAdd": 0,
        "isMileStoneMax": true,
        "tokenAdd": 0,
        "isTokenMax": true,
    }
    return response


@router.post("/activity/bossRush/relicSelect")
@player_data_decorator
async def activity_bossRush_relicSelect(player_data, request: Request):
    request_json = await request.json()

    player_data["activity"]["BOSS_RUSH"][request_json["activityId"]]["relic"][
        "select"
    ] = request_json["relicId"]

    response = {}
    return response


@router.post("/activity/enemyDuel/startMatch")
@player_data_decorator
async def activity_enemyDuel_startMatch(player_data, request: Request):
    request_json = await request.json()

    player_data.extra_save.save_obj["enemyDuel_activityId"] = request_json["activityId"]
    player_data.extra_save.save_obj["enemyDuel_modeId"] = request_json["modeId"]

    response = {
        "result": 0,
    }
    return response


@router.post("/activity/enemyDuel/queryMatch")
@player_data_decorator
async def activity_enemyDuel_queryMatch(player_data, request: Request):
    request_json = await request.json()

    if request_json["needLeave"]:
        response = {
            "result": 1,
            "team": null,
        }
    else:
        multiplayer_addr = const_json_loader[CONFIG_JSON]["multiplayer_addr"]
        response = {
            "result": 0,
            "team": {
                "teamId": "some_team_id",
                "serverAddress": multiplayer_addr,
                "serverToken": "some_server_token",
            },
            "playerCnt": 8,
        }
    return response


@router.post("/activity/enemyDuel/multiBattleStart")
@player_data_decorator
async def activity_enemyDuel_multiBattleStart(player_data, request: Request):
    request_json = await request.json()

    response = {
        "result": 0,
    }
    return response


@router.post("/activity/enemyDuel/multiBattleFinish")
@player_data_decorator
async def activity_enemyDuel_multiBattleFinish(player_data, request: Request):
    request_json = await request.json()

    response = {
        "result": 0,
        "choiceCnt": {"skip": 0, "normal": 5, "allIn": 5},
        "commentId": "Comment_Operation_1",
        "isHighScore": false,
        "rankList": [
            {"id": "1", "rank": 1, "score": 262900, "isPlayer": 1},
            {
                "id": "100",
                "rank": 2,
                "score": 0,
                "isPlayer": 1,
                "playerBrief": {
                    "nickName": "Undergraduate",
                    "uid": "100",
                    "avatar": {"type": "ICON", "id": "avatar_def_01"},
                    "nickNumber": "1234",
                    "nameCardStyle": {
                        "componentOrder": [
                            "module_sign",
                            "module_assist",
                            "module_medal",
                        ],
                        "skin": {
                            "selected": "nc_rhodes_default",
                            "state": {},
                            "tmpl": {},
                        },
                        "misc": {"showDetail": true, "showBirthday": false},
                    },
                },
            },
        ],
        "bp": 0,
        "dailyMission": {"add": 0, "reward": 0},
    }
    return response
