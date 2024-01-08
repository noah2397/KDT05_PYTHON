import numpy as np
from scipy.sparse import dok_matrix
n_players = 20
team_size = 4
max_iterations = 10000
count_2=0
count_23=800
def update_adjacency_matrix(adjacency_matrix, team_membership, ex='-'):
    global count_2,count_23
    count_2=0
    total_weight=0
    for i in range(n_players):
        for j in range(i + 1, n_players):
            if team_membership[i] == team_membership[j]:
                if adjacency_matrix[i,j]==2 :
                    count_2+=1
                if ex=='-' :
                    adjacency_matrix[i, j] -= 1
                    adjacency_matrix[j, i] -= 1
                    if adjacency_matrix[i,j] > 0 :
                        total_weight+=(adjacency_matrix[i,j]+3)**10
                    else :
                        total_weight+=0
                else :
                    adjacency_matrix[i, j] += 1
                    adjacency_matrix[j, i] += 1
    if ex=='-' :
        return adjacency_matrix, total_weight
    else :
        return adjacency_matrix

def create_random_teams(n_players, team_size):
    return np.random.permutation(n_players) % (n_players // team_size)

def optimize_teams(n_players, team_size, adjacency_matrix, members):
    min_weight = 0
    best_team_membership = None
    global count_2, count_23
    for _ in range(max_iterations):
        team_membership = create_random_teams(n_players, team_size)
        #print(team_membership)
        adjacency_matrix, total_weight = update_adjacency_matrix(adjacency_matrix, team_membership)
        adjacency_matrix = update_adjacency_matrix(adjacency_matrix, team_membership, ex="+")
        if total_weight > min_weight and count_2 < count_23-5:
            min_weight = total_weight
            best_team_membership = team_membership
    adjacency_matrix = update_adjacency_matrix(adjacency_matrix, team_membership)
    return min_weight, best_team_membership

def print_teams(team_membership, members):
    teams = [[] for _ in range(5)]
    for i, member in enumerate(members):
        teams[team_membership[i]].append(member)

    for i, team in enumerate(teams, start=1):
        print(f"팀{i} : {team}")

def main():
    global count_2, count_23
    members = ["옥영신","권혁원","권오영","고우석","김문섭","양현우","이승민","김규량","우승연","이시명","변주영",
               "임소영","이화은","김동현","전진우","이윤서","이현길","명노아","손예림","박희진"]

    adjacency_matrix = dok_matrix((n_players, n_players), dtype=int)
    for i in range(n_players):
        for j in range(i + 1, n_players):
                adjacency_matrix[i, j] = 2
                adjacency_matrix[j, i] = 2
    for i in range(15):
        min_weight, best_team_membership = optimize_teams(n_players, team_size, adjacency_matrix, members)

        print("최적화 팀 생성:")
        print_teams(best_team_membership, members)
        print(adjacency_matrix.toarray())
        print(f"팀 가중치 (가중치 최소값 {min_weight})")
        count_23=count_2

if __name__ == "__main__":
    main()
