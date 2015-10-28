__author__ = 'bmbayad'


class Insertion(object):
    def __init__(self, array):
        self.array = array

    def sort(self):
        array_size = len(self.array)
        for i in range(1, array_size):
            j = i
            while j > 0:
                if self.array[j - 1] > self.array[j]:
                    self.swap(j - 1, j)
                j -= 1

    def swap(self, i, j):
        element = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = element


if __name__ == '__main__':
    insertion = Insertion([3, 1, 0, 5, 8, 2, 5, 7, 3, 1, 5])
    insertion.sort()
    print insertion.array
