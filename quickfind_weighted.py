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
    pid_root = find(p)
    qid_root = find(q)
    print "\t %d--%d" %(pid_root,qid_root)

    if pid_root == qid_root: return

    if(settings.levelsArray[p] < settings.levelsArray[q]):
        settings.mainArray[p] = qid_root
        settings.levelsArray[q] += settings.levelsArray[p]
    else:
        settings.mainArray[q] = pid_root
        settings.levelsArray[p] += settings.levelsArray[q]

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
        print "(%d -- %d)" %(p,q)
        union(p, q)


def print_tree():
    print settings.mainArray


def run():
    load_setting()
    unionize()
    print_tree()


if __name__ == '__main__':
    run()
