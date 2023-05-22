#include<iostream>
#include<string>

const int MIN_ID = 1;
const int MAX_ID = 100000;
const int MIN_TEAM = 1;
const int MAX_TEAM = 5;
const int MIN_SCORE = 1;
const int MAX_SCORE = 5;


struct Soldier                                          // 병사 하나의 구조체
{
    int ID;
    int team;
    Soldier *prev;
    Soldier *next;
} soldier[MAX_ID + 1];                                  // 최대 수의 병사만큼 선언해둔다. 이렇게 하면 ID를 이용해서 참조 가능하다.

struct Team                                             // 팀 하나의 구조체
{
    Soldier head;                                       // 링크드리스트 헤드로 사용할 임의의 주소값용 노드(내부 내용은 없음)
    Soldier tail;                                       // 링크드리스트 백으로 사용할 임의의 주소값용 노드(내부 내용은 없음)

    void initialize()                                   // 초기화
    {
        link(&head, &tail);                             // 헤드와 테일을 이어둔다(빈 링크드리스트라는 뜻)
    }

    static void link(Soldier *front, Soldier *back)     // 프론트와 백을 잇는다.(프론트의 다음 = 백, 백의 이전 = 프론트)
    {
        front->next = back;
        back->prev = front;
    }

    static void erase(Soldier *node)                    // 한 노드의 프론트와 백을 잇는다. 그 노드는 링크드리스트에서 사라지게 된다.(프론트 -> 노드 -> 백 에서 프론트 -> 백으로 변함) 생성된 병사기록은 삭제되지 않지만 찾기 어려움
    {
        link(node->prev, node->next);
    }

    void insert(Soldier *node)                          // 프론트와 백 사이에 한 노드를 잇는다. 그 노드는 링크드리스트의 원소로 추가된다.(프론트->백 에서 프론트->노드->백 으로 변환)
    {
        link(tail.prev, node);
        link(node, &tail);
    }

    bool isEmpty()                                      // head의 next가 tail의 주소값이라면, 이는 링크드리스트가 비었다는 의미이다.
    {
        return (head.next == &tail);
    }

    void splice(Team *list)                             // 
    {
        if (list->isEmpty())                            // 빈 링크드리스트라면, 생략
            return;
        link(tail.prev, list->head.next);               
        /* 
        현재 리스트의 마지막 값 뒤에 가져올 리스트의 첫번째 값을 잇는다
        현재 리스트 헤드 -> 현재 원소들... -> 가져온 리스트의 원소들... ->가져온 리스트의 테일
        이때, 현재 리스트의 테일과, 가져온 리스트의 헤드는 잘못된 위치를 참조하고 있다.
        */ 
        
        link(list->tail.prev, &tail);
        /* 
        가져온 리스트의 마지막값과, 현재 리스트의 테일을 잇는다
        현재 리스트 헤드 -> 현재 원소들.... -> 가져온 리스트의 원소들... -> 현재 리스트의 테일
        결과적으로 현재 리스트 원소들 뒤로 새로운 링크드 리스트가 추가된다.
        하지만, 가져온 리스트의 헤드와 테일에는 아직 잘못된 위치를 참조하고 있다.
        */                   
        list->initialize();                             // 가져온 리스트를 초기화한다. 잘못된 위치가 사라지고, 빈 링크드 리스트가 된다.
    }
} team[MAX_TEAM + 1][MAX_SCORE + 1];                    // 각 팀을 생성하고, 그 팀의 점수별 병사들을 모아서 점수마다 링크드 리스트를 생성.



void init()
{
    for (int i = MIN_TEAM; i <= MAX_TEAM; i++)
        for (int j = MIN_SCORE; j <= MAX_SCORE; j++)
            team[i][j].initialize();
}

void hire(int mID, int mTeam, int mScore)
{
    soldier[mID].ID = mID;
    soldier[mID].team = mTeam;
    team[mTeam][mScore].insert(soldier + mID);
}

void fire(int mID)
{
    Team::erase(soldier + mID);
}

void updateSoldier(int mID, int mScore)
{
    Team::erase(soldier + mID);
    team[soldier[mID].team][mScore].insert(soldier + mID);
}

void updateTeam(int mTeam, int mChangeScore)
{
    if (mChangeScore > 0)
    {
        for (int i = MAX_SCORE - 1; i >= MIN_SCORE; i--)
        {
            int newScore = i + mChangeScore;
            if (newScore > MAX_SCORE)
                newScore = MAX_SCORE;
            team[mTeam][newScore].splice(&team[mTeam][i]);
        }
    }
    else if (mChangeScore < 0)
    {
        for (int i = MIN_SCORE + 1; i <= MAX_SCORE; i++)
        {
            int newScore = i + mChangeScore;
            if (newScore < MIN_SCORE)
                newScore = MIN_SCORE;
            team[mTeam][newScore].splice(&team[mTeam][i]);
        }
    }
}

int bestSoldier(int mTeam)
{
    Team *maxScoreGroup;
    for (int i = MAX_SCORE; i >= MIN_SCORE; i--)
    {
        if (!team[mTeam][i].isEmpty())
        {
            maxScoreGroup = &team[mTeam][i];
            break;
        }
    }

    int maxId = MIN_ID - 1;
    Soldier *maxScoreSoldier = maxScoreGroup->head.next;    // 링크드리스트 첫 병사
    while (maxScoreSoldier != &(maxScoreGroup->tail))       // 처음부터 끝까지 한바퀴 순회하면서 최대값 찾기
    {
        if (maxId < maxScoreSoldier->ID)                    // 최대값 찾으면 저장          
            maxId = maxScoreSoldier->ID;
        maxScoreSoldier = maxScoreSoldier->next;
    }
    return maxId;                                           // 저장한 최대값 반환
}