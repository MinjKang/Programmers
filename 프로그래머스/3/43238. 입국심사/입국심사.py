def solution(n, times):
    left = 1  # 최소 시간 (가장 빠른 경우)
    right = max(times) * n  # 최대 시간 (가장 느린 심사관이 n명을 혼자 심사하는 경우)
    answer = right

    while left <= right:
        mid = (left + right) // 2  # 현재 우리가 테스트할 시간

        # mid 시간 동안 심사할 수 있는 사람 수 계산
        total = sum(mid // time for time in times)

        if total >= n:
            answer = mid  # 현재 시간으로도 충분하므로 더 짧은 시간 시도
            right = mid - 1
        else:
            left = mid + 1  # 시간 부족하니 더 긴 시간 시도

    return answer
