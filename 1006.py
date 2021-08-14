#1006
'''
정답은 N ~ 2*N
1. 주변에 합쳐서 100이내로 할 수 없는것들은 미리 빼둔다.
2. 근처에 이웃수가 1인것부터 쭉 뺀다.
'''

def BOJ1006():
    N,W =map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    bridge = [[0 for _ in range(N)] for _ in range (3)]
    bridge_list = []
    #bridge 를 채운다.
    for i in range(N):
        if (arr1[i] + arr1[i - 1] <= W):
            bridge[0][i] = 1
            bridge_list.append([0,i])
        if (arr2[i] + arr2[i - 1] <= W):
            bridge[2][i] = 1
            bridge_list.append([2, i])
        if (arr1[i - 1] + arr2[i - 1] <= W):
            bridge[1][i] = 1
            bridge_list.append([1, i])
    #위에서부터 하나씩 삭제ㄱㄱ
    couple_count=0
    while(bridge_list):
        for a,b in bridge_list:
            neighbor = 0
            neighbor_id = []
            if a-1>=0 and b-1>=0 and bridge[a-1][b-1]==1:
                neighbor = neighbor + 1
                neighbor_id = [a-1,b-1]
            if a - 1 >= 0 and bridge[a - 1][b] == 1:
                neighbor = neighbor + 1
                neighbor_id = [a - 1,b]
            if b - 1 >= 0 and bridge[a][b - 1] == 1:
                neighbor_id = [a - 1, b - 1]
            if a + 1 < N and b + 1 < N and bridge[a + 1][b + 1] == 1:
                neighbor = neighbor + 1
                neighbor_id = [a + 1, b + 1]
            if a + 1 < N and bridge[a + 1][b] == 1:
                neighbor = neighbor + 1
                neighbor_id = [a + 1, b]
            if b + 1 < N and bridge[a][b + 1] == 1:
                neighbor = neighbor + 1
                neighbor_id = [a, b + 1]
            if neighbor==0 or neighbor==1:
                couple_count= couple_count+1
                bridge_list.remove([a,b])
                if neighbor_id:
                    bridge_list.remove(neighbor_id)
    print(couple_count)




def main():
    T = int(input())
    while(T!=0):
        T = T-1
        BOJ1006()

if __name__ =="__main__":
    main()