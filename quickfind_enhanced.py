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
    pid_root = find(settings.mainArray[p])
    qid_root = find(settings.mainArray[q])

    if pid_root == qid_root: return

    settings.mainArray[pid_root] = qid_root

def find(p):
    while( p != settings.mainArray[p]):
        p = settings.mainArray[p]
    return  settings.mainArray[p]


def count():
    return settings.size


def unionize():
    for item in settings.unions:
        p = find(item[0])
        q = find(item[1])
        union(p, q)


def print_tree():
    print settings.mainArray


def run():
    load_setting()
    unionize()
    print_tree()


if __name__ == '__main__':
    run()
