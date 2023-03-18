# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


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
            with open("test/" + file_name, "r") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found")
            return

    else:
        print("Input error")
        return


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n, "n doesn't match the number of elements input"

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
