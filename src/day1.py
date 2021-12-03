def main():
    with open("./../inputs/day1.txt", "r") as file:
        nums = [int(n) for n in file.readlines()]

    inc_cnt = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            inc_cnt += 1

    l, r = 0, 2
    s = nums[0] + nums[1] + nums[2]
    window_cnt = 0
    while r < len(nums) - 1:
        prev = s
        s -= nums[l]
        l += 1
        r += 1
        s += nums[r]

        if s > prev:
            window_cnt += 1
    return inc_cnt, window_cnt


if __name__ == "__main__":
    print(main())

