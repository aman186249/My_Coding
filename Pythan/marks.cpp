#include <iostream>
using namespace std;
int main()
{
    int marks;

  cout << "Enter the student's marks (0-100): ";
  cin >> marks;

  if (marks < 0 || marks > 100) {
    cout << "Invalid marks. Please enter a number between 0 and 100." << endl;
  }

  // Determine grade
  string grade;
  if (marks < 50)
  {
    grade = "Fail";
  }
}
