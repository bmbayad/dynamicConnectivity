import settings

__author__ = 'bmbayad'


def load_setting():
    settings.setup()


def connected(p, q):
    """
    Checks whether the two nodes p and q are connected
    :param p: p is the first ID
    :param q: q is the second ID
    :return: return True if p and q share the same ID
    """

    if settings.mainArray[p] == settings.mainArray[q]:
        return True
    else:
        return False


def union(p, q):
    """
    Connects the nodes p and q
    :param p: the first node
    :param q: the second node
    :return:
    """
    pid = settings.mainArray[p]
    qid = settings.mainArray[q]

    for idx, val in enumerate(settings.mainArray):
        if val == pid:
            settings.mainArray[idx] = qid


def find(p):
    pass


def count():
    return settings.size


def unionize():
    for item in settings.unions:
        p = item[0]
        q = item[1]
        if not connected(p, q):
            union(p, q)


def print_tree():
    print settings.mainArray


def run():
    load_setting()
    unionize()
    print_tree()


if __name__ == '__main__':
    run()
