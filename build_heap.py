# python3

def build_heap(data):
    swaps = []
    n = len(data)
    # Starts the loop by looking at the last element of array and going backwards
    for i in range(n // 2, -1, -1):
        # Loop checks if the element has a left child also considering that it could have a right child
        while 2 * i + 1 < n:
            j = i
            leftChild = 2 * i + 1
            rightChild = 2 * i + 2
            # Checks if the child exists and is smaller in value than parent
            # The smallest child in value gets assigned to variable j
            if leftChild <= n - 1 and data[leftChild] < data[j]:
                j = leftChild
            if rightChild <= n - 1 and data[rightChild] < data[j]:
                j = rightChild
            # Checks that parent and child aren't equal
            # Registers the swap into a list and performs the swap 
            if i != j:
                swaps.append((i, j))
                data[i],data[j] = data[j],data[i]
                i = j
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
