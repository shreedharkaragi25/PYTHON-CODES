
# Pattern Compression

data = [1, 1, 1, 2, 2, 3, 3, 3]

compressed = []
count = 1

for i in range(1, len(data)):
    if data[i] == data[i - 1]:
        count += 1
    else:
        compressed.append((data[i - 1], count))
        count = 1

# Add last element
compressed.append((data[-1], count))

print("Compressed Output:", compressed)