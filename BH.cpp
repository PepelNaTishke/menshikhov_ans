#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int MAX_SIZE = 110;
const int FREE = 0;
const int USED = 7;
int n, m;
vector<vector<int>> mas;

void input()
{
    cin >> m >> n;
    mas = vector<vector<int>>(n + 4, vector<int>(m + 4, 0));

    char str[MAX_SIZE];
    for (int i = 2; i < n + 2; i++)
    {
        scanf("%s", str);
        for (int j = 2; j < m + 2; j++)
            mas[i][j] = (str[j - 2] == '*' ? USED : FREE);
    }
}

struct point
{
    int x, y;
    point() {}
    point(int X, int Y) { x = X; y = Y; }
};

int moveX[4] = {0, -1, 0, 1};
int moveY[4] = {-1, 0, 1, 0};
vector<int> holes;
vector<int> squares;

bool correct(int x, int y)
{
    if (x < 0 || y < 0) return false;
    if (x == n + 4 || y == m + 4) return false;
    return true;
}

int bfs1(int X, int Y, vector<vector<int>>& one, int& minX, int& maxX, int& minY, int& maxY)
{
    int S = 1;
    mas[X][Y] = FREE;
    one[X][Y] = USED;
    minX = min(minX, X); maxX = max(maxX, X);
    minY = min(minY, Y); maxY = max(maxY, Y);

    queue<point> q;
    q.push(point(X, Y));
    while (!q.empty())
    {
        point cur = q.front(); q.pop();
        for (int i = 0; i < 4; i++)
        {
            int x = cur.x + moveX[i];
            int y = cur.y + moveY[i];
            if (correct(x, y) && mas[x][y] == USED)
            {
                minX = min(minX, x); maxX = max(maxX, x);
                minY = min(minY, y); maxY = max(maxY, y);
                S++;
                mas[x][y] = FREE;
                one[x][y] = USED;
                q.push(point(x, y));
            }
        }
    }
    return S;
}

void prepare(vector<vector<int>>& one, int minX, int maxX, int minY, int maxY)
{
    for (int i = minX - 1; i <= maxX + 1; i++)
    {
        one[i][minY - 1] = FREE; one[i][minY - 2] = USED;
        one[i][maxY + 1] = FREE; one[i][maxY + 2] = USED;
    }
    for (int i = minY - 1; i <= maxY + 1; i++)
    {
        one[minX - 1][i] = FREE; one[minX - 2][i] = USED;
        one[maxX + 1][i] = FREE; one[maxX + 2][i] = USED;
    }
}

void bfs2(vector<vector<int>>& one, int x, int y)
{
    one[x][y] = USED;
    queue<point> q;
    q.push(point(x, y));
    while (!q.empty())
    {
        point cur = q.front(); q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = cur.x + moveX[i];
            int ny = cur.y + moveY[i];
            if (one[nx][ny] == FREE)
            {
                one[nx][ny] = USED;
                q.push(point(nx, ny));
            }
        }
    }
}

int findHoles(vector<vector<int>>& one, int minX, int maxX, int minY, int maxY)
{
    int holesAmount = -1;
    for (int i = minX - 1; i <= maxX + 1; i++)
        for (int j = minY - 1; j <= maxY + 1; j++)
            if (one[i][j] == FREE)
            {
                bfs2(one, i, j);
                holesAmount++;
            }
    return holesAmount;
}

void solve()
{
    vector<vector<int>> one(n + 4, vector<int>(m + 4, FREE));

    for (int i = 2; i < n + 2; i++)
    {
        for (int j = 2; j < m + 2; j++)
        {
            if (mas[i][j] == USED)
            {
                for (int p = 0; p < n + 4; p++)
                    one[p].assign(one[p].size(), FREE);

                int minX = i, maxX = i;
                int minY = j, maxY = j;
                int curS = bfs1(i, j, one, minX, maxX, minY, maxY);
                prepare(one, minX, maxX, minY, maxY);
                int holesAmount = findHoles(one, minX, maxX, minY, maxY);

                if (holesAmount != 0)
                {
                    holes.push_back(holesAmount);
                    squares.push_back(curS);
                }
            }
        }
    }

    if (holes.empty())
    {
        cout << 0;
        return;
    }

    int pos = max_element(holes.begin(), holes.end()) - holes.begin();
    int maxHoles = holes[pos];
    int minSquare = squares[pos];

    for (int i = 0; i < (int)squares.size(); i++)
        if (holes[i] == maxHoles)
            minSquare = min(minSquare, squares[i]);

    cout << minSquare;
}

int main()
{
    input();
    solve();
    return 0;
}
