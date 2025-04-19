def solution(id_list, report, k):
    # report에서 지목된 사람 count
    # id_list랑 user name 비교
    # 같으면, warn_person count
    # 이미 했으면 count X
    dict = {}
    for i in id_list:
        dict[i] = 0

    # 신고 중복 제거
    report = list(set(report))

    # 신고당한 횟수 세기
    count_dict = {}
    for r in report:
        user, warn_person = r.split(' ')
        if warn_person not in count_dict:
            count_dict[warn_person] = 1
        else:
            count_dict[warn_person] += 1

    banned = []
    for i in count_dict:
        if count_dict[i] >= k:
            banned.append(i)

    for r in report:
        user, warn_person = r.split(' ')
        if warn_person in banned:
            dict[user] += 1

    answer = []
    for i in id_list:
        answer.append(dict[i])

    return answer
        
        
        