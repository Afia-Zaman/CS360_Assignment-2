// 3. Write a class called Rectangle that has floating point data members'length and width. The class has the following member functions:
// void setlength(float) to set the length data member; void setwidth(float)to set the width data member;float perimeter(void)to calculate
// and return the perimeter of the rectangle; float area(void)to calculate and return the area of the rectangle; void show(void)to display the
// length and width of the rectangle; int sameArea(Rectangle)that has one parameter of type Rectangle, and sameArea returns 1 if the two
// Rectangles have the same area, otherwiese returns 0 if they don't.
// a. Create Rectangle class first
// b. Write main function to create two rectangle objects. Set the length and width of the first rectangle to 5 and 2.5, and set the
// length and width of the second rectangle to 5 and 18.9. Display each rectangle and its area and perimeter.
// c. Check whether the two Rectangles have the same area and print a message indicating the result. Set the length and width of the first
// rectangle to 15 and 6.3. Display each Rectangle and its area and perimeter again. Again, verify whether the two
// Rectangles have the same area and print a message indicating the result

// Answer:

#include <iostream>
using namespace std;

class Rectangle {
private:
    float length;
    float width;
public:
    void setLength(float l) {
        length = l;
    }

    void setWidth(float w) {
        width = w;
    }

    float perimeter() {
        return 2 * (length + width);
    }

    float area() {
        return length * width;
    }

    void show() {
        cout << "Length: " << length << ", Width: " << width << endl;
    }

    int sameArea(Rectangle r) {
        return (area() == r.area()) ? 1 : 0;
    }
};

int main() {
    Rectangle rect1, rect2;

    // length and width of the first rectangle
    rect1.setLength(5);
    rect1.setWidth(2.5);

    // length and width of the second rectangle
    rect2.setLength(5);
    rect2.setWidth(18.9);

    cout << "Rectangle 1:" << endl;
    rect1.show();
    cout << "Area: " << rect1.area() << endl;
    cout << "Perimeter: " << rect1.perimeter() << endl;


    cout << "Rectangle 2:" << endl;
    rect2.show();
    cout << "Area: " << rect2.area() << endl;
    cout << "Perimeter: " << rect2.perimeter() << endl;

    // Checking if the two rectangles have the same area
    if (rect1.sameArea(rect2))
        cout << "Both rectangles have the same area." << endl;
    else
        cout << "Both rectangles do not have the same area." << endl;

    // Modify the dimensions of the first rectangle
    rect1.setLength(15);
    rect1.setWidth(6.3);

   
    cout << "\nRectangle 1 (after modification):" << endl;
    rect1.show();
    cout << "Area: " << rect1.area() << endl;
    cout << "Perimeter: " << rect1.perimeter() << endl;

    // Checking if the two rectangles have the same area after modification
    if (rect1.sameArea(rect2))
        cout << "Both rectangles have the same area." << endl;
    else
        cout << "Both rectangles do not have the same area." << endl;

    return 0;
}

// Output:

// Rectangle 1:
// Length: 5, Width: 2.5
// Area: 12.5
// Perimeter: 15
// Rectangle 2:
// Length: 5, Width: 18.9
// Area: 94.5
// Perimeter: 47.8
// Both rectangles do not have the same area.

// Rectangle 1 (after modification):
// Length: 15, Width: 6.3
// Area: 94.5
// Perimeter: 42.6
// Both rectangles have the same area.



