def solution(bandage, health, attacks):
    continuous_success = 0
    attack_times = []
    damages = []
    cur_health = health 
    
    for i in range(len(attacks)):
        attack_times.append(attacks[i][0])
        damages.append(attacks[i][1])
    
    max_health = health
    t = 0
    maxtime = attacks[-1][0]

    while t <= maxtime:
        if t in attack_times:
            continuous_success = 0
            cur_health -= damages[attack_times.index(t)]
            if cur_health <= 0:
                return -1
        else:
            continuous_success += 1
            if continuous_success < bandage[0]:
                cur_health = min(cur_health + bandage[1], max_health)
            else:
                cur_health = min(cur_health + bandage[1] + bandage[2], max_health)
                continuous_success = 0
        t += 1

    return cur_health

# 테스트
print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])) # 5
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])) # -1
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])) # -1
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]])) # 3
