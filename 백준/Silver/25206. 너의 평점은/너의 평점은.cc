#include <iostream>

using namespace std;

double gradeToNum(string grade) {
    double num = 0;
    if (grade == "A+") num = 4.5;
    else if (grade == "A0") num = 4.0;
    else if (grade == "B+") num = 3.5;
    else if (grade == "B0") num = 3.0;
    else if (grade == "C+") num = 2.5;
    else if (grade == "C0") num = 2.0;
    else if (grade == "D+") num = 1.5;
    else if (grade == "D0") num = 1.0;
    else if (grade == "F") num = 0.0;
    return num;
}

int main() {
    string subject, grade; double credit = 0; double sum = 0; int totalCredit = 0;
    for (int i = 0; i < 20; i++) {
        cin >> subject >> credit >> grade;
        sum += gradeToNum(grade) * credit;
        if (grade != "P") totalCredit += credit;
    }
    cout << sum / totalCredit << "\n";
    return 0;

    
}