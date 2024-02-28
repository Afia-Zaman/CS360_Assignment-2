// 4. Create a class called MusicIns to contain three methods void string(void), void wind(void)
// and void perc(void). Each of these methods should initialize a member string type instrument array to contain the following
// a. Veena, guitar, sitar, sarod and mandolin under void string(void) method
// b. Flute, clarinet, saxophone, nadaswaram and piccolo under void wind(void) method
// c.Table, mridangam, bongos, drums and tambour under void perc(void) method.

// It should also have two methods called void get(void) and void show(void) to display the contents of the arrays initialized. 
// The void get(void) methods must display a menu as follows
// a. The values of instrument array within void string(void) method
// b. The values of instrument array within void wind(void) method
// c. The values of instrument array within void perc(void) method.After that, generate test program
// main.cpp to verify the above class

// Answer:

#include <iostream>
#include <string>
using namespace std;

class MusicIns {
private:
    string instruments[5];
public:
    void stringInstruments() {
        instruments[0] = "Veena";
        instruments[1] = "guitar";
        instruments[2] = "sitar";
        instruments[3] = "sarod";
        instruments[4] = "mandolin";
    }

    void windInstruments() {
        instruments[0] = "Flute";
        instruments[1] = "clarinet";
        instruments[2] = "saxophone";
        instruments[3] = "nadaswaram";
        instruments[4] = "piccolo";
    }

    void percInstruments() {
        instruments[0] = "Table";
        instruments[1] = "mridangam";
        instruments[2] = "bongos";
        instruments[3] = "drums";
        instruments[4] = "tambour";
    }

    void get() {
        cout << "Select the instrument type:\n";
        cout << "a. String instruments\n";
        cout << "b. Wind instruments\n";
        cout << "c. Percussion instruments\n";
        cout << "\n";

        char choice;
        cin >> choice;

        switch (choice) {
            case 'a':
                stringInstruments();
                break;
            case 'b':
                windInstruments();
                break;
            case 'c':
                percInstruments();
                break;
            default:
                cout << "Invalid choice." << endl;
                return;
        }
    }

    void show() {
        cout << "Instruments: ";
        for (int i = 0; i < 5; ++i) {
            cout << instruments[i] << ", ";
        }
        cout << endl;
    }
};

int main() {
    MusicIns music;

    cout << "String Instruments:" << endl;
    music.get();
    music.show();

    cout << "\nWind Instruments:" << endl;
    music.get();
    music.show();

    cout << "\nPercussion Instruments:" << endl;
    music.get();
    music.show();

    return 0;
}

// Output:

// String Instruments:
// Select the instrument type:
// a. String instruments
// b. Wind instruments
// c. Percussion instruments

// c
// Instruments: Table, mridangam, bongos, drums, tambour, 

// Wind Instruments:
// Select the instrument type:
// a. String instruments
// b. Wind instruments
// c. Percussion instruments

// b
// Instruments: Flute, clarinet, saxophone, nadaswaram, piccolo, 

// Percussion Instruments:
// Select the instrument type:
// a. String instruments
// b. Wind instruments
// c. Percussion instruments

// a
// Instruments: Veena, guitar, sitar, sarod, mandolin, 
