// 1. Modify class GradeBook as follows:
// a. Include a second-string data member that represents the course instructor’s name.
// b. Provide a set function to change the instructor’s name and a get function to retrieve it.
// c. Modify the constructor to specify course name and instructor name parameters.
// d. Modify function displayMessage to output the welcome message and course name,
// then the string "This course is presented by: " followed by the instructor’s name.
// Use your modified class in main function that demonstrates the class’s new capabilities.
// #include <string>
// class GradeBook{
// public:
// explicit GradeBook( std::string ); // constructor initialize courseName
// void setCourseName( std::string ); // sets the course name
// std::string getCourseName() const; // gets the course name
// void displayMessage() const; // displays a welcome message
// private:
// std::string courseName; // course name for this GradeBook
// }; // end class GradeBook
// #include <iostream>
// using namespace std;
// GradeBook::GradeBook( string name ):courseName( name ){}
// void GradeBook::setCourseName( string name ){
// courseName = name;}
// string GradeBook::getCourseName() const{return courseName;}
// void GradeBook::displayMessage() const{
// cout << "Welcome to the grade book for\n" << getCourseName()
// << "!" << endl;}


// Answer:


#include <iostream>
#include <string>
using namespace std;

class GradeBook {
public:
    explicit GradeBook(std::string, std::string); 
    void setCourseName(std::string); 
    void setInstructorName(std::string); 
    std::string getCourseName() const; 
    std::string getInstructorName() const; 
    void displayMessage() const; 
    
private:
    std::string courseName;
    std::string instructorName; 
};

GradeBook::GradeBook(std::string course, std::string instructor)
    : courseName(course), instructorName(instructor) {}

void GradeBook::setCourseName(std::string name) {
    courseName = name;
}

void GradeBook::setInstructorName(std::string name) {
    instructorName = name;
}

std::string GradeBook::getCourseName() const {
    return courseName;
}

std::string GradeBook::getInstructorName() const {
    return instructorName;
}

void GradeBook::displayMessage() const {
    std::cout << "Welcome to the grade book for\n" << getCourseName()
              << "!\nThis course is presented by: " << getInstructorName() << std::endl;
}

int main() {
    GradeBook gb("C and C++", "Mr. Alex Yang");
    gb.displayMessage();
    cout << "\n";
    
    
    gb.setCourseName("C and C++ Lab");
    gb.setInstructorName("Mr. Alex Yang");
    gb.displayMessage();

    return 0;
}

// Output -
// Welcome to the grade book for C and C++!
// This course is presented by: Mr. Alex Yang

// Welcome to the grade book for C and C++ Lab!
// This course is presented by: Mr. Alex Yang

