#1006
'''
정답은 N ~ 2*N
1. 이어질수 있는 bridge 위치들 저장
2. 근처에 이웃수가 적은것부터 쭉 뺀다.
'''

def BOJ1006():
    N,W =map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    bridge_list = []
    #bridge_list 채우기
    for i in range(N):
        if (arr1[i] + arr1[i - 1] <= W):
            bridge_list.append([0,i])
        if (arr2[i] + arr2[i - 1] <= W):
            bridge_list.append([2, i])
        if (arr1[i - 1] + arr2[i - 1] <= W):
            bridge_list.append([1, i])

    #하나씩 삭제ㄱㄱ
    couple_count=0

    while(bridge_list):
        prev_bridge_list = bridge_list.copy()

        less_neighbor = 10 # 7~8을 넘을수 없다
        less_neighbor_list = []

        for a,b in bridge_list:
            neighbor_id = [[a,b]]

            for i,j in bridge_list:
                if (a - i)*(a - i) <=1 :
                    if (b - j)*(b - j) <= 1 and (a-i) != (b-j):
                        pass
                    elif (b - j - N)*(b - j - N) <= 1 and (a-i) != (b-j-N):
                        pass
                    elif (b - j + N)*(b - j + N) <= 1 and (a-i) != (b-j+N):
                        pass
                    else:
                        continue
                    neighbor_id.append([i,j])
                else :
                    continue

            if len(neighbor_id)==1 or len(neighbor_id)==2:
                couple_count= couple_count+1
                for i in neighbor_id:
                    if i in bridge_list:
                        bridge_list.remove(i)
            else :
                if len(neighbor_id)<less_neighbor:
                    less_neighbor = len(neighbor_id)
                    less_neighbor_list = neighbor_id

        if prev_bridge_list == bridge_list:
            couple_count = couple_count+1
            for i in less_neighbor_list:
                if i in bridge_list:
                    bridge_list.remove(i)

    print(2*N-couple_count)
    return




def main():
    T = int(input())
    while(T!=0):
        T = T-1
        BOJ1006()
    return

#if __name__ =="__main__":
main()