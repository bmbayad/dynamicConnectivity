__author__ = 'bmbayad'


def threesum(threesum_array):
    length = len(threesum_array)
    count = 0
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if threesum_array[i] + threesum_array[j] + threesum_array[k] == 0:
                    count += 1
    print count;


def run():
    threesum_array = []
    with open("data/1Kints.txt") as f:
        for line in f:
            threesum_array.append(int(line.strip()))

    import timeit
    t = timeit.Timer(lambda: threesum(threesum_array))
    print t.timeit(number=1)


if __name__ == '__main__':
    run()

