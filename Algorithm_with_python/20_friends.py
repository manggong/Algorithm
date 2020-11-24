def friends(g, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop()
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)



fr = {
    'kim': ['yang', 'jung', 'moon'],
    'yang': ['kim', 'ji', 'hwan'],
    'ji': ['kim'],
    'jung':['kim'],
    'moon': ['kim'],
    'hwan': ['kim']
}

friends(fr,'kim')