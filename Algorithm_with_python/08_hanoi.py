def hanoi(n, from_pos, to_pos, aux_pos):
    if n==1:
        print(from_pos,"->", to_pos)
        return

    hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos,"->", to_pos)

    hanoi(n-1, aux_pos, to_pos, from_pos)


hanoi(2,1,3,2)   

# n=1 일때 3번 기둥에 도착했다는 뜻 이전에는 -1씩 감소하면서 2번기둥으로 이동해야 함.