# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        while 2 * i + 1 < n:
            k = i
            leftChild = 2 * i + 1
            rightChild = 2 * i + 2
            if leftChild <= n - 1 and data[leftChild] < data[k]:
                k = leftChild
            if rightChild <= n - 1 and data[rightChild] < data[k]:
                k = rightChild
            if i != k:
                swaps.append((i, k))
                c = data[i]
                data[i] = data[k]
                data[k] = c
                i = k
            else:
                break
    return swaps


def main():
    
    # Checks input method -> if I takes input from keyboard
    #                     -> if F takes input from a file
    input_method = input()

    if input_method.__contains__("I"):
        n = int(input())
        data = list(map(int, input().split()))
    
    elif input_method.__contains__("F"):
        file_name = input()
        if file_name.__contains__("a"):
            print("Input error")
            return
        try:
            with open("tests/" + file_name, "r") as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found")
            return

    else:
        print("Input error")
        return


    # Checks if lenght of data is the same as the said lenght
    assert len(data) == n, "n doesn't match the number of elements input"

    # Calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # Prints the number of swaps and each swap
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
