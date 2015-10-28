__author__ = 'bmbayad'


class Selection(object):

    def __init__(self,array):
        self.array = array

    def sort(self):
        array_size = len(self.array)
        for i in range(array_size):
            min = i
            for j in range(i+1,array_size):
                if self.array[j] < self.array[min]:
                    min = j

            self.swap(i, min)

    def swap(self,i,j):
        element = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = element

if __name__ == '__main__':
    selection = Selection([3, 1, 0, 5, 8, 2])
    selection.sort()
    print selection.array