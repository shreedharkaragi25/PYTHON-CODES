
# 

durations = [12, 4, 8, 15, 3, 20]

total_time = sum(durations)
longest_video = max(durations)
average_duration = total_time / len(durations)

print("Total Watch Time:", total_time, "minutes")
print("Longest Video:", longest_video, "minutes")
print("Average Duration:", average_duration, "minutes")

print("Videos shorter than 5 minutes:")
for d in durations:
    if d < 5:
        print(d, "minutes")
        