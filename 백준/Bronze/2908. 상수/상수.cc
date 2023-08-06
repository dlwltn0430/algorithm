#include <iostream>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int a_reverse = (a % 100 % 10) * 100 + (a % 100 / 10) * 10 + a / 100;
    int b_reverse = (b % 100 % 10) * 100 + (b % 100 / 10) * 10 + b / 100;
    cout << max(a_reverse, b_reverse) << "\n";
    return 0;
}