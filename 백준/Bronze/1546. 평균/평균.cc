#include <iostream>

using namespace std;

int main() {
	int n;
	int max = -1;
	
	cin >> n;
	int score[n];
	
	for (int i = 0; i < n; i++) {
		cin >> score[i];
		if (max < score[i]) max = score[i];
	}
	//cout << max << '\n';
	double fake_score[n];
	double sum = 0;
	double avg;
	
	for (int i = 0; i < n; i++) {
		fake_score[i] = (double)score[i] / max * 100;
		sum += fake_score[i];
	}
	avg = sum / n;
	
	cout << fixed;
	cout.precision(2);
	cout << avg;
	return 0;
}