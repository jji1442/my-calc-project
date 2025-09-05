# 내부 데이터
mastery_core_1 = {
    "cur_level": 0,
    "dmg_up": {
        "final_dmg_per_level": 0,
        "final_dmg_per_level_per_10b": 0,
        "avg_final_dmg_per_5level": 0,
        "avg_final_dmg_per_5level_per_10b": 0
    },
    "skill": {
        "플레인 차지드라이브VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "플레인 스펠VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "스칼렛 차지드라이브VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "스칼렛 스펠VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "거스트 차지드라이브VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "거스트 스펠VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "어비스 차지드라이브VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "어비스 스펠VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "깨어난 심연": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        }
    }
}
mastery_core_2 = {
    "cur_level": 0,
    "dmg_up": {
        "final_dmg_per_level": 0,
        "final_dmg_per_level_per_10b": 0,
        "avg_final_dmg_per_5level": 0,
        "avg_final_dmg_per_5level_per_10b": 0
    },
    "skill": {
        "지워지지 않는 상처VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "채워지지 않는 굶주림VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "걷잡을 수 없는 혼돈VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "멈출 수 없는 충동": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "멈출 수 없는 본능": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "돌아오는 증오VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        }
    }
}
mastery_core_3 = {
    "cur_level": 0,
    "dmg_up": {
        "final_dmg_per_level": 0,
        "final_dmg_per_level_per_10b": 0,
        "avg_final_dmg_per_5level": 0,
        "avg_final_dmg_per_5level_per_10b": 0
    },
    "skill": {
        "돌아오는 증오VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "황홀한 구속VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "끝없는 고통VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        }
    }
}
mastery_core_4 = {
    "cur_level": 0,
    "dmg_up": {
        "final_dmg_per_level": 0,
        "final_dmg_per_level_per_10b": 0,
        "avg_final_dmg_per_5level": 0,
        "avg_final_dmg_per_5level_per_10b": 0
    },
    "skill": {
        "잊혀지지 않는 악몽VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "잊혀지지 않는 흉몽VI": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        },
        "다가오는 죽음": {
            "cur_dmg": 0,
            "dmg_up": 0,
            "rate": 0
        }
    }
}
mastery_core_list = [mastery_core_1, mastery_core_2, mastery_core_3, mastery_core_4]

import test_model

# 메인 함수
# input_data는 실제 사용자 입력을 위한 함수입니다.
# test_data는 반복되는 사용자 입력을 리스트화하여 다른 함수를 빠르게 테스트하기 위한 임시 함수입니다.
#mastery_core_list = test_model.input_data(mastery_core_list)
mastery_core_list = test_model.test_data(mastery_core_list)
mastery_core_list = test_model.adj_dmg(mastery_core_list)

# 아래의 for문은 간략한 결과를 보기 위한 반복문입니다.
#for test_cnt in range(5):
while(True):
    mastery_core_list = test_model.calc_enh_eff(mastery_core_list)
    best_core_idx, enh_cnt = test_model.recommend_enh(mastery_core_list)
    if(not test_model.print_result(mastery_core_list, best_core_idx, enh_cnt)):
        break
    test_model.adj_rate(mastery_core_list, best_core_idx, enh_cnt)
    mastery_core_list = test_model.align_core_data(mastery_core_list)
