__author__ = 'bmbayad'


class Shell(object):
    def __init__(self, array):
        self.array = array

    def sort(self):
        array_size = len(self.array)
        h = 1
        while h < (array_size / 3):
            h = 3 * h + 1
        print h
        while h >= 1:

            for i in range(h, array_size):
                j = i
                while j >= h:
                    print j
                    if self.array[j - h] > self.array[j]:
                        print "swapping %d %d %d" % (h, (j - h), j)
                        self.swap(j - h, j)
                    j -= h
            h /= 3

    def swap(self, i, j):
        element = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = element


if __name__ == '__main__':
    shell = Shell(
        [3, 1, 0, 5, 8, 2, 5, 7, 3])
    shell.sort()
    print shell.array
