// 1. Given a student class with the members and methods as follows, write a C++ test
// program (a.k.a. main function) to display names, courseNum and grades of 3 students
// who have appeared in the examination. Declare the class of name, courseNum. and
// grade. Create an array of class objects. Read and display the contents of the array.

// #include <iostream>
// using std::cout;
// using std::cin;
// #define MAX 10
// class student {
// private:
// char name[30];
// int courseNum;
// int total;
// float perc;
// public:
// void getDetails(void); //member function to get student's details
// void putDetails(void); //member function to print student's details
// };
// void student:: getDetails(void) //member function definition, outside of
// the class
// {
// cout << "Enter name: " ;
// cin >> name;
// cout << "Enter course number: ";
// cin >> courseNum;
// cout << "Enter total grades out of 500: ";
// cin >> total;
// perc=(float)total/500*100;
// }
// void student:: putDetails(void) //member function definition, outside of
// the class
// {
// cout << "Student details:\n";
// cout << "Name:"<< name << ",course Number:" << courseNum <<
// ",Total:" << total << ",Percentage:" << perc;
// }
// int main(void){
// //Write your program here
// return 0;
// }


// Answer:

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#define MAX 3

class student {
private:
    char name[30];
    int courseNum;
    int total;
    float perc;
public:
    void getDetails(void); //member function to get student's details
    void putDetails(void); //member function to print student's details
};

void student::getDetails(void) {
    cout << "Enter name: ";
    cin >> name;
    cout << "Enter course number: ";
    cin >> courseNum;
    cout << "Enter total grades out of 500: ";
    cin >> total;
    perc = (float)total / 500 * 100;
}

void student::putDetails(void) {
    cout << "Student details:\n";
    cout << "Name: " << name << ", Course Number: " << courseNum << ", Total: " << total << ", Percentage: " << perc << endl;
}

int main() {
    
    int numOfStudents;

    cout << "Enter total number of students: ";
    cin >> numOfStudents;
    
    
    student students[MAX];

    for (int i = 0; i < MAX; ++i) {
        cout << "Enter details of student " << i + 1 << ":\n";
        students[i].getDetails();
        cout << "\n";
    }

    for (int i = 0; i < MAX; ++i) {
        cout << "Details of student " << i + 1 << ":\n";
        students[i].putDetails();
        cout << endl;
    }

    return 0;
}

// Output :

// Enter total number of students: 3
// Enter details of student 1:
// Enter name: Karthik
// Enter course number: 1201
// Enter total grades out of 500: 456

// Enter details of student 2:
// Enter name: Mahesh
// Enter course number: 1202
// Enter total grades out of 500: 398

// Enter details of student 3:
// Enter name: Kiran
// Enter course number: 1203
// Enter total grades out of 500: 456

// Details of student 1:
// Student details:
// Name: Karthik, Course Number: 1201, Total: 456, Percentage: 91.2

// Details of student 2:
// Student details:
// Name: Mahesh, Course Number: 1202, Total: 398, Percentage: 79.6

// Details of student 3:
// Student details:
// Name: Kiran, Course Number: 1203, Total: 456, Percentage: 91.2

