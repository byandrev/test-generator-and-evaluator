#include <bits/stdc++.h>
#define fastIO ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

void sortColors(vector<int> &nums)
{
    sort(nums.begin(), nums.end());

    cout << nums[0];
    for (int i = 1; i < nums.size(); i++)
    {
        cout << " " << nums[i];
    }

    cout << "\n";
}

int main() {
    int n;

    while (cin >> n) {
        vector<int> s;
        int aux;

        for (int i = 0; i < n; i++) {
            cin >> aux;
            s.push_back(aux);
        }

        sortColors(s);
    }

    return 0;
}