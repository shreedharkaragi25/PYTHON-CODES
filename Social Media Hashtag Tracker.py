
# Social Media Hashtag Tracker

hashtags = ["#fun", "#python", "#fun", "#code", "#python"]

# Frequency of each hashtag
frequency = {}

for tag in hashtags:
    if tag in frequency:
        frequency[tag] += 1
    else:
        frequency[tag] = 1

print("Frequency of each hashtag:")
for tag in frequency:
    print(tag, ":", frequency[tag])

# Most repeated hashtag
max_count = max(frequency.values())
for tag in frequency:
    if frequency[tag] == max_count:
        print("Most Repeated Hashtag:", tag)
        break

# Unique hashtags
print("Unique Hashtags:", list(frequency.keys()))

# Remove duplicates
no_duplicates = []
for tag in hashtags:
    if tag not in no_duplicates:
        no_duplicates.append(tag)

print("Hashtags after removing duplicates:", no_duplicates)