
def main():
    with open("1.in", "r") as f:
        data = f.readlines()

    # get first and last integer in each line and concatenate them
    total = 0
    for i in range(len(data)):
        first = 0
        last = 0
        for j, char in enumerate(data[i]):
            if ord('0') <= ord(char) <= ord('9'):
                first = int(char)
                break
            # Check if this is the end of a number
            try:
                if data[i][j-2:j+1] == "one":
                    first = 1
                    break
                elif data[i][j-2:j+1] == "two":
                    first = 2
                    break
                elif data[i][j-2:j+1] == "six":
                    first = 6
                    break
                elif data[i][j-3:j+1] == "four":
                    first = 4
                    break
                elif data[i][j-3:j+1] == "five":
                    first = 5
                    break
                elif data[i][j-3:j+1] == "nine":
                    first = 9
                    break
                elif data[i][j-4:j+1] == "three":
                    first = 3
                    break
                elif data[i][j-4:j+1] == "seven":
                    first = 7
                    break
                elif data[i][j-4:j+1] == "eight":
                    first = 8
                    break
            except IndexError:
                pass
        for j in range(len(data[i])-1, -1, -1):
            char = data[i][j]
            if ord('0') <= ord(char) <= ord('9'):
                last = int(char)
                break
            # Check if this is the end of a number
            try:
                if data[i][j:j+3] == "one":
                    last = 1
                    break
                elif data[i][j:j+3] == "two":
                    last = 2
                    break
                elif data[i][j:j+3] == "six":
                    last = 6
                    break
                elif data[i][j:j+4] == "four":
                    last = 4
                    break
                elif data[i][j:j+4] == "five":
                    last = 5
                    break
                elif data[i][j:j+4] == "nine":
                    last = 9
                    break
                elif data[i][j:j+5] == "three":
                    last = 3
                    break
                elif data[i][j:j+5] == "seven":
                    last = 7
                    break
                elif data[i][j:j+5] == "eight":
                    last = 8
                    break
            except IndexError:
                pass

        # print(data[i], first, last)
        data[i] = 10 * first + last
        total += data[i]
    # print the result
    print(total)


if __name__ == '__main__':
    main()