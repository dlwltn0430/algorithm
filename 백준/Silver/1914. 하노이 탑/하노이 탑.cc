#include <iostream>
#include <cmath>
#include <string>

using namespace std;

void hanoi(int n, int from, int to, int by) {
    if (n == 1) cout << from << " " << to << "\n";
    else {
        hanoi(n - 1, from, by, to);
        cout << from << " " << to << "\n";
        hanoi(n - 1, by, to, from);
    }
}

int main() {
    int n;
    cin >> n;
    string x = to_string(pow(2, n));
    x = x.substr(0, x.find('.'));
    x[x.length() - 1] -= 1;
    cout << x << "\n";
    if (n <= 20) hanoi(n, 1, 3, 2);
    return 0;
}