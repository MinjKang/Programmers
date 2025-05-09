n = int(input())
times = list(map(int, input().split()))

times.sort()

waiting_time = 0
total_waiting_time = 0

for t in times:
    waiting_time += t
    total_waiting_time += waiting_time

print(total_waiting_time)