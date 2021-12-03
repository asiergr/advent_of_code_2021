def main():
    with open("./../inputs/day2.txt", "r") as file:
        instructions = file.readlines()

    forward = 0
    horizontal = 0

    for instruction in instructions:
        direction, val = instruction.split()
        val = int(val)
        if direction == "forward":
            forward += val
        elif direction == "down":
            horizontal += val
        elif direction == "up":
            horizontal -= val
    pt1 = forward * horizontal

    forward = 0
    horizontal = 0
    aim = 0

    for instruction in instructions:
        direction, val = instruction.split()
        val = int(val)
        if direction == "forward":
            forward += val
            horizontal += val * aim
        elif direction == "down":
            aim += val
        elif direction == "up":
            aim -= val
    pt2 = forward * horizontal
    return pt1, pt2


if __name__ == "__main__":
    print(main())

