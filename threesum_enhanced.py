__author__ = 'bmbayad'
import binarySearch
import timeit


def threesum(threesum_array):
    length = len(threesum_array)
    count = 0
    for i in range(length):
        for j in range(i + 1, length):
            idx = binarySearch.binarySearch(threesum_array[j + 1:], -(threesum_array[i] + threesum_array[j]))
            if idx != -1:
                count += 1

    print "%d matches were found" % count;


def run():
    threesum_array = []
    with open("data/1Kints.txt") as f:
        for line in f:
            threesum_array.append(int(line.strip()))

    threesum_array.sort()
    t = timeit.Timer(lambda: threesum(threesum_array))
    print "enhanced 3-sum took: %d secs" % t.timeit(number=1)


if __name__ == '__main__':
    run()
