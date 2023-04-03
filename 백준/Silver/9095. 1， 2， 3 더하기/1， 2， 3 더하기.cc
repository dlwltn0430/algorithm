#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t, n;
    vector<int> v(12, 0);
    v[1] = 1;
    v[2] = 2;
    v[3] = 4;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        for (int i = 4; i <= n; i++) {
            v[i] = v[i - 3] + v[i - 2] + v[i - 1];
        }
        cout << v[n] << "\n";
    }
    return 0;
}