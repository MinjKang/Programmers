def solution(priorities, location):
    pri_dict = {i: p for i, p in enumerate(priorities)}
    order = list(pri_dict.keys())
    count = 0

    while order:
        now_idx = order.pop(0)
        now_pri= pri_dict[now_idx]
        print(now_idx, now_pri, order)

        high = False 
        for i in order:
            if pri_dict[i] > now_pri:
                high = True
                break

        if high:
            order.append(now_idx)
        else:
            count += 1
            if now_idx == location:
                return count