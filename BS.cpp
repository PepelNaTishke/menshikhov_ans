#include <iostream>
#include <cstdio>
#include <vector>
 
using namespace std;
const int MAX_VALUE = 1e9;
int k;
vector<int> C,L;
int x0, y0, x1, y1;
int dx, dy;
void input()
{
    cin>>x0>>y0>>x1>>y1>>k;
    C.resize(k);
    L.resize(k);
    for (int i=0;i<k;i++)
        cin>>L[i];
    for (int j=0;j<k;j++)
        cin>>C[j];
}
int _abs(int a)
{
    return (a<0) ? -a:a;
}
int minAmount = MAX_VALUE;
int curAmount;
bool isLast = false;
void rec(int pos, int curLen, int totalLen)
{
    if ((totalLen - curLen) % L[pos] == 0)
    {
        int lastAmount = _abs(totalLen - curLen) / L[pos];
        if (lastAmount <= C[pos])
        {
            if (isLast)
                minAmount = min(minAmount, curAmount + lastAmount);
            else
            {
                isLast = true;
                curAmount += lastAmount;
                C[pos] -= lastAmount;
 
                rec(0,0,dy);
 
                C[pos] += lastAmount;
                curAmount -= lastAmount;
                isLast = false;
            }
        }
    }
    if (pos == k-1)
        return;
    for (int x = -C[pos]; x <= C[pos]; x++)
    {
        C[pos]-= _abs(x);
        curAmount += _abs(x);
 
        rec(pos+1, curLen + x * L[pos], totalLen);
 
        curAmount -= _abs(x);
        C[pos] += _abs(x);
    }
}
 
void solve()
{
    dx = _abs(x0 - x1);
    dy = _abs(y0 - y1);
    // a*L[0] + b*L[1] + c*L[2] + d*L[3] = dx
    rec(0,0,dx);
    if (minAmount == MAX_VALUE)
        cout<<-1;
    else
        cout<<minAmount;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
 
    input();
    solve();
    return 0;
}
