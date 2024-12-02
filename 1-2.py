with open('input/1-1-left.txt', 'r') as file:
    left = list(set(
        int(line.strip())
        for line in file
        if line.strip().isdigit()
    ))

with open('input/1-1-right.txt', 'r') as file:
    right = list(
        int(line.strip())
        for line in file
        if line.strip().isdigit()
    )

total = 0
for left_val in left:
    total += left_val * right.count(left_val)

print(f'Total: {total}')