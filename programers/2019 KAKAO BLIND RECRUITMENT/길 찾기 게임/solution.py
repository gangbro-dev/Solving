def solution(nodeinfo):
    numnode = dict()
    i = 1
    for node in nodeinfo:
        numnode[tuple(node)] = i
        i += 1
    new_nodeinfo = sorted(nodeinfo, key=lambda x: x[1], reverse=True)
    tree = list()
    while

    return answer