__author__ = 'bmbayad'


def binarySearch(search_array, key):
    # assuming that the array will be sorted

    lo = 0
    hi = len(search_array) - 1

    while lo <= hi:
        mid = lo + (hi - lo) / 2
        if key < search_array[mid]:
            hi = mid - 1
        elif key > search_array[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

def run():
    key = 5
    #search_array = [-1,-1,2, 3, 4, 5, 6,7]
    search_array = []
    with open("data/1Kints.txt") as f:
        for line in f:
            search_array.append(int(line.strip()))

    search_array.sort()


    idx = binarySearch(search_array, key)
    print "key: %d was found on index: %d" %(key,idx)


if __name__ == '__main__':
    run()
