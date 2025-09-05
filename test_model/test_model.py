# 외부 데이터
base_skill_dmg = {
    "플레인 차지드라이브": 1839,
    "플레인 스펠": 373,
    "스칼렛 차지드라이브": 2118,
    "스칼렛 스펠": 1105,
    "거스트 차지드라이브": 2418,
    "거스트 스펠": 924,
    "어비스 차지드라이브": 3850,
    "어비스 스펠": 144,
    "지워지지 않는 상처": 2958,
    "채워지지 않는 굶주림": 3451,
    "걷잡을 수 없는 혼돈": 5316,
    "멈출 수 없는 충동": 2190,
    "멈출 수 없는 본능": 2778,
    "돌아오는 증오": 2898,
    "황홀한 구속": 36340,
    "끝없는 고통": 41400,
    "끝나지 않는 악몽": 2658,
    "끝나지 않는 흉몽": 2688,
    "다가오는 죽음": 906 + 266
    # 인피니티 스펠 19레벨 기준 다가오는 죽음 133%p 상승.
    # 공격횟수 포함한 총 %데미지 기준이므로 133%p * 2 = 266%p
    # 이 상승량을 따로 기재함.
}
mastery_core_1 = {
    "플레인 차지드라이브VI": {
        "max_dmg": 3615,
        "dmg_up": 42
    },
    "플레인 스펠VI": {
        "max_dmg": 1610,
        "dmg_up": 20
    },
    "스칼렛 차지드라이브VI": {
        "max_dmg": 4530,
        "dmg_up": 54
    },
    "스칼렛 스펠VI": {
        "max_dmg": 2375,
        "dmg_up": 30
    },
    "거스트 차지드라이브VI": {
        "max_dmg": 5250,
        "dmg_up": 66
    },
    "거스트 스펠VI": {
        "max_dmg": 1980,
        "dmg_up": 24
    },
    "어비스 차지드라이브VI": {
        "max_dmg": 7894,
        "dmg_up": 102
    },
    "어비스 스펠VI": {
        "max_dmg": 302,
        "dmg_up": 4
    },
    "깨어난 심연": {
        "max_dmg": 4380,
        "dmg_up": 48
    }
}
mastery_core_2 = {
    "지워지지 않는 상처VI": {
        "max_dmg": 8040,
        "dmg_up": 102
    },
    "채워지지 않는 굶주림VI": {
        "max_dmg": 9268,
        "dmg_up": 112
    },
    "걷잡을 수 없는 혼돈VI": {
        "max_dmg": 14220,
        "dmg_up": 168
    },
    "멈출 수 없는 충동": {
        "max_dmg": 2450,
        "dmg_up": 55
    },
    "멈출 수 없는 본능": {
        "max_dmg": 2940,
        "dmg_up": 66
    },
    "돌아오는 증오VI": {
        "max_dmg": 480,
        "dmg_up": 16
    }
}
mastery_core_3 = {
    "돌아오는 증오VI": {
        "max_dmg": 8320,
        "dmg_up": 96
    },
    "황홀한 구속VI": {
        "max_dmg": 82200,
        "dmg_up": 920
    },
    "끝없는 고통VI": {
        "max_dmg": 66330,
        "dmg_up": 630
    }
}
mastery_core_4 = {
    "잊혀지지 않는 악몽VI": {
        "max_dmg": 6685,
        "dmg_up": 84
    },
    "잊혀지지 않는 흉몽VI": {
        "max_dmg": 6797,
        "dmg_up": 84
    },
    "다가오는 죽음": {
        "max_dmg": 120,
        "dmg_up": 4
    }
}
mastery_core_list = [mastery_core_1, mastery_core_2, mastery_core_3, mastery_core_4]
mastery_core_cost = [50, 15, 18, 20, 23, 25, 28, 30, 33, 100,
                     40, 45, 50, 55, 60, 65, 70, 75, 80, 175,
                     85, 90, 95, 100, 105, 110, 115, 120, 125, 250]

def input_data(core):
    while(True):
        sum_rate = 0

        for core_idx in range(4):
            while(True):
                try:
                    # 사용자로부터 마스터리 코어별 현재 레벨을 입력받음.
                    cur_level = int(input("현재 마스터리 코어" + str(core_idx + 1) + "의 현재 레벨을 입력하세요: "))

                    # 입력된 마스터리 코어별 현재 레벨이 정상적인 데이터인지 확인함.
                    if(1 <= cur_level and cur_level <= 30):
                        core[core_idx]["cur_level"] = cur_level

                        for skill_name in mastery_core_list[core_idx].keys():
                            # 현재 레벨 기준 스킬 %데미지 저장함.
                            core[core_idx]["skill"][skill_name]["cur_dmg"] = (mastery_core_list[core_idx][skill_name]["max_dmg"]
                                                                - mastery_core_list[core_idx][skill_name]["dmg_up"] * (30 - cur_level))
                            # 현재 레벨 기준 스킬 %데미지에 기본 스킬 %데미지 합산함.
                            for base_skill in base_skill_dmg.keys():
                                if(skill_name == base_skill):
                                    core[core_idx]["skill"][skill_name]["cur_dmg"] += base_skill_dmg[base_skill]
                            
                            # 입력된 마스터리 코어별 현재 레벨이 최대 레벨인지 확인함.
                            if(cur_level == 30):
                                core[core_idx]["skill"][skill_name]["dmg_up"] = 0
                            else:
                                core[core_idx]["skill"][skill_name]["dmg_up"] = mastery_core_list[core_idx][skill_name]["dmg_up"]
                            
                            while(True):
                                try:
                                    # 사용자로부터 스킬별 점유율을 입력받음.
                                    rate = float(input(skill_name + "의 점유율을 입력하세요: "))
                                    
                                    # 입력된 스킬별 점유율이 정상적인 데이터인지 확인함.
                                    if(rate >= 0):
                                        # 스킬별 점유율 저장함.
                                        core[core_idx]["skill"][skill_name]["rate"] = rate
                                        sum_rate = rate
                                        break
                                except ValueError:
                                    print("입력된 정보(점유율)가 잘못되었습니다.")
                        break
                    else:
                        print("입력된 정보(현재 레벨)가 잘못되었습니다.")

                except ValueError:
                    print("입력된 정보(현재 레벨)가 잘못되었습니다.")
        
        # 입력된 스킬별 점유율 합산이 100을 초과하는지 확인함.
        if(sum_rate > 100):
            print("입력된 정보(점유율 합산)가 잘못되었습니다.")
        else:
            break
    return core
def test_data(core):
    # 입력될 데이터를 리스트 타입으로 저장함.
    cur_level = [19, 9, 9, 9]
    rate = [[3.84, 1.63, 0.54, 0.27, 0.89, 0.32, 0.89, 0.35, 11.51],
            [1.61, 1.93, 1.99, 0.61, 1.51, 12.14],
            [12.14, 2.32, 2.0],
            [0.96, 8.42, 27.1]]

    for core_idx in range(4):
        # 마스터리 코어별 현재 레벨 저장함.
        core[core_idx]["cur_level"] = cur_level[core_idx]
        rate_idx = 0

        for skill_name in mastery_core_list[core_idx].keys():
            # 마스터리 코어 별 현재 레벨 기준 스킬 %데미지 저장함.
            core[core_idx]["skill"][skill_name]["cur_dmg"] = (mastery_core_list[core_idx][skill_name]["max_dmg"]
                                              - mastery_core_list[core_idx][skill_name]["dmg_up"] * (30 - cur_level[core_idx]))
            # 현재 레벨 기준 스킬 %데미지에 기본 스킬 %데미지 합산함.
            for base_skill_name in base_skill_dmg.keys():
                if(skill_name == base_skill_name):
                    core[core_idx]["skill"][skill_name]["cur_dmg"] += base_skill_dmg[base_skill_name]
            
            # 입력될 마스터리 코어별 현재 레벨이 최대 레벨인지 확인함.
            if(cur_level == 30):
                core[core_idx]["skill"][skill_name]["dmg_up"] = 0
            else:
                core[core_idx]["skill"][skill_name]["dmg_up"] = mastery_core_list[core_idx][skill_name]["dmg_up"]
            
            # 스킬별 점유율 저장함.
            core[core_idx]["skill"][skill_name]["rate"] = rate[core_idx][rate_idx]
            rate_idx += 1
    return core
def adj_dmg(core):
    for core_idx in range(4):
        for comp_core_idx in range(core_idx + 1, 4):
            # core_idx & comp_core_idx: 0 & 1, 2, 3 / 1 & 2, 3 / 2 & 3
            # 서로 다른 마스터리 코어이면서 동일한 스킬을 추출함.
            common_skill = core[core_idx]["skill"].keys() & core[comp_core_idx]["skill"].keys()

            for skill_name in common_skill:
                # 두 마스터리 코어의 현재 레벨 기준 스킬 %데미지를 합산함.
                new_cur_dmg = core[core_idx]["skill"][skill_name]["cur_dmg"] + core[comp_core_idx]["skill"][skill_name]["cur_dmg"]
                core[core_idx]["skill"][skill_name]["cur_dmg"] = new_cur_dmg
                core[comp_core_idx]["skill"][skill_name]["cur_dmg"] = new_cur_dmg
    return core
def cost_eff(cur_price, cost_cnt):
    # 재화 효율을 계산함.
    return 1000000 / (cur_price * cost_cnt)
def calc_enh_eff(core):
    # 재화 시세를 저장함.
    cur_price = 550

    for core_idx in range(4):
        for skill_name in core[core_idx]["skill"].keys():    
            skill_name = core[core_idx]["skill"][skill_name]

            # 1레벨 상승 시 최종데미지 상승율을 구하기 위해서 현재 레벨을 확인함.
            if(core[core_idx]["cur_level"] != 30):
                # 재화 소모량, 데미지 상승율을 저장함.
                cost_cnt = mastery_core_cost[core[core_idx]["cur_level"]]
                dmg_up_rate = skill_name["dmg_up"] / skill_name["cur_dmg"]

                # 최종데미지 상승율을 합산함.
                core[core_idx]["dmg_up"]["final_dmg_per_level"] += skill_name["rate"] * dmg_up_rate
                core[core_idx]["dmg_up"]["final_dmg_per_level_per_10b"] += (cost_eff(cur_price, cost_cnt)
                                                                            * skill_name["rate"] * dmg_up_rate)
    
            # 5레벨 상승 시 평균 최종데미지 상승율을 구하기 위해서 현재 레벨을 확인함.
            if(core[core_idx]["cur_level"] + 4 <= 30):
                # 평균 재화 소모량, 평균 데미지 상승율을 저장함.
                avg_cost_cnt = sum(mastery_core_cost[core[core_idx]["cur_level"]:core[core_idx]["cur_level"] + 5]) / 5
                tempA = skill_name["dmg_up"]
                tempB = skill_name["cur_dmg"]
                avg_dmg_up_rate = ((tempA / tempB + tempA / (tempB + tempA) + tempA / (tempB + 2 * tempA)
                                    + tempA / (tempB + 3 * tempA) + tempA / (tempB + 4 * tempA)) / 5)
                
                # 평균 최종데미지 상승율을 합산함.
                core[core_idx]["dmg_up"]["avg_final_dmg_per_5level"] += skill_name["rate"] * avg_dmg_up_rate
                core[core_idx]["dmg_up"]["avg_final_dmg_per_5level_per_10b"] += (cost_eff(cur_price, avg_cost_cnt)
                                                                                 * skill_name["rate"] * avg_dmg_up_rate)

    return core
def recommend_enh(core):
    all_final_dmg_per_10b_list = []

    # 한 리스트에 마스터리 코어별로 1레벨 상승 시 100억당 최종데미지 상승율, 5레벨 상승 시 100억당 평균 최종데미지 상승율을 저장함.
    for core_idx in range(4):
        all_final_dmg_per_10b_list.append(core[core_idx]["dmg_up"]["final_dmg_per_level_per_10b"])
        all_final_dmg_per_10b_list.append(core[core_idx]["dmg_up"]["avg_final_dmg_per_5level_per_10b"])
    
    max_idx = 0
    max_final_dmg_per_10b = 0

    # 최종데미지 상승율을 저장한 리스트에서 최댓값일 때의 인덱스와 최댓값을 찾음.
    for idx, final_dmg_per_10b in enumerate(all_final_dmg_per_10b_list):
        if(final_dmg_per_10b > max_final_dmg_per_10b):
            max_idx = idx
            max_final_dmg_per_10b = final_dmg_per_10b

    # 최댓값일 때의 인덱스와 최댓값으로 가장 효율 좋은 마스터리 코어 번호 및 강화 횟수를 유추함.
    if(max_final_dmg_per_10b == 0):
        return 0, 0
    
    best_core_idx = max_idx // 2

    if(max_idx % 2 == 0):
        enh_cnt = 1
    else:
        enh_cnt = 5
    return best_core_idx, enh_cnt
def print_result(core, best_core_idx, enh_cnt):
    # 강화할 스킬이 있다면, 스킬 이름 및 추천 레벨 및 최종데미지 상승율을 출력함.
    if(enh_cnt != 0):
        print(f"마스터리 코어{best_core_idx + 1}", end=" ")
        print(str(core[best_core_idx]["cur_level"] + enh_cnt) + "레벨 달성 시")

        if(enh_cnt == 1):
            print("1레벨 상승 시 최종데미지 상승율", end=" ")
            print(round(core[best_core_idx]["dmg_up"]["final_dmg_per_level"], 3))
            print("1레벨 상승 시 100억당 최종데미지 상승율", end=" ")
            print(round(core[best_core_idx]["dmg_up"]["final_dmg_per_level_per_10b"], 3))
        else:
            print("5레벨 상승 시 평균 최종데미지 상승율", end=" ")
            print(round(core[best_core_idx]["dmg_up"]["avg_final_dmg_per_5level"], 3))
            print("5레벨 상승 시 100억당 평균 최종데미지 상승율", end=" ")
            print(round(core[best_core_idx]["dmg_up"]["avg_final_dmg_per_5level_per_10b"], 3))
        return True
    else:
        return False
def new_rate(rate, adj_rate, is_up):
    # 마스터리 코어 레벨이 상승했나에 따라 새로운 점유율을 다르게 적용함.
    if(is_up):
        return rate * (1 + adj_rate) / (1 + rate * adj_rate / 100)
    else:
        return rate / (1 + adj_rate / 100)
def final_dmg_reset(core_idx):
    # 최종데미지 상승율을 0으로 초기화함.
    core_idx["dmg_up"]["final_dmg_per_level"] = 0
    core_idx["dmg_up"]["final_dmg_per_level_per_10b"] = 0
    core_idx["dmg_up"]["avg_final_dmg_per_5level"] = 0
    core_idx["dmg_up"]["avg_final_dmg_per_5level_per_10b"] = 0
    return core_idx
def adj_rate(core, best_core_idx, enh_cnt):
    # 강화한 마스터리 코어 점유율 상승량(%p)의 합산을 0으로 초기화함.
    sum_rate_up = 0

    # 강화한 마스터리 코어의 점유율 조정함.
    for skill_name in core[best_core_idx]["skill"].keys():
        skill_name = core[best_core_idx]["skill"][skill_name]

        if(enh_cnt == 1):
            dmg_up_rate = skill_name["dmg_up"] / skill_name["cur_dmg"]
            sum_rate_up += new_rate(skill_name["rate"], dmg_up_rate, True) - skill_name["rate"]
            skill_name["rate"] = new_rate(skill_name["rate"], dmg_up_rate, True)
            skill_name["cur_dmg"] += skill_name["dmg_up"]
        else:
            tempA = skill_name["dmg_up"]
            tempB = skill_name["cur_dmg"]
            dmg_up_rate = (tempA / tempB + tempA / (tempB + tempA) + tempA / (tempB + 2 * tempA)
                           + tempA / (tempB + 3 * tempA) + tempA / (tempB + 4 * tempA))
            sum_rate_up += new_rate(skill_name["rate"], dmg_up_rate, True) - skill_name["rate"]
            skill_name["rate"] = new_rate(skill_name["rate"], dmg_up_rate, True)
            skill_name["cur_dmg"] += skill_name["dmg_up"] * 5
        
        if(core[best_core_idx]["cur_level"] + enh_cnt >= 30):
            skill_name["dmg_up"] = 0
    
    # 강화한 마스터리 코어의 현재 레벨 상승 및 최종데미지 상승율을 0으로 초기화함.
    core[best_core_idx]["cur_level"] += enh_cnt
    core[best_core_idx] = final_dmg_reset(core[best_core_idx])

    # 나머지 마스터리 코어의 점유율 조정 및 최종데미지 상승율을 0으로 초기화함.
    for core_idx in range(4):
        if(core_idx != best_core_idx):
            for skill_name in core[core_idx]["skill"].keys():
                skill_name = core[core_idx]["skill"][skill_name]
                skill_name["rate"] = new_rate(skill_name["rate"], sum_rate_up, False)
            
            core[core_idx] = final_dmg_reset(core[core_idx])
    return core
def align_core_data(core):
    for core_idx in range(4):
        for comp_core_idx in range(core_idx + 1, 4):
            # core_idx & comp_core_idx: 0 & 1, 2, 3 / 1 & 2, 3 / 2 & 3
            # 서로 다른 마스터리 코어이면서 동일한 스킬을 추출함.
            common_skill = core[core_idx]["skill"].keys() & core[comp_core_idx]["skill"].keys()

            for skill_name in common_skill:
                # 동일한 스킬의 현재 레벨 기준 %데미지가 다른지 확인함.
                if(core[core_idx]["skill"][skill_name]["cur_dmg"] != core[comp_core_idx]["skill"][skill_name]["cur_dmg"]):
                    # 높은 쪽의 점유율을 기준으로 현재 레벨 기준 스킬 %데미지와 점유율을 갱신함.
                    if(core[core_idx]["skill"][skill_name]["rate"] > core[comp_core_idx]["skill"][skill_name]["rate"]):
                        core[comp_core_idx]["skill"][skill_name]["cur_dmg"] = core[core_idx]["skill"][skill_name]["cur_dmg"]
                        core[comp_core_idx]["skill"][skill_name]["rate"] = core[core_idx]["skill"][skill_name]["rate"]
                    else:
                        core[core_idx]["skill"][skill_name]["cur_dmg"] = core[comp_core_idx]["skill"][skill_name]["cur_dmg"]
                        core[core_idx]["skill"][skill_name]["rate"] = core[comp_core_idx]["skill"][skill_name]["rate"]
    return core