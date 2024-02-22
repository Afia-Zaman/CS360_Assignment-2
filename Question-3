// 3. While exercising, you can use a heart rate monitor to see that your heart rate stays within
// a safe range suggested by your trainers and doctors. According to the American
// Heart Association (AHA) (www.americanheart.org/presenter.jhtml?identifier=4736),
// the formula for calculating your maximum heart rate in beats per minute is 220 minus
// your age in years. Your target heart rate is a range that is 50-85% of your maximum
// heart rate. [Note: These formulas are estimates provided by the AHA. Maximum and
// target heart rates may vary based on the health, fitness and gender of the individual.
// Always consult a physician or qualified health care professional before beginning or
// modifying an exercise program.]. Create a class called HeartRates. The class attributes
// should include the person’s first name, last name and date of birth (consisting of
// separate attributes for the month, day and year of birth). Your class should have a
// constructor that receives this data as parameters. For each attribute provide set and get
// functions. The class also should include a function getAge that calculates and returns the
// person’s age (in years), a function getMaxiumumHeartRate that calculates and returns
// the person’s maximum heart rate and a function getTargetHeartRate that calculates and
// returns the person’s target heart rate. Since you do not yet know how to obtain the
// current date from the computer, function getAge should prompt the user to enter the
// current month, day and year before calculating the person’s age. Write an application
// that prompts for the person’s information, instantiates an object of class HeartRates and
// prints the information from that object—including the person’s first name, last name and
// date of birth—then calculates and prints the person’s age in (years), maximum heart rate
// and target-heart-rate range.


// Answer:

#include <iostream>
#include <string>
#include <ctime>

class HeartRates {
public:
    // Constructor
    HeartRates(const std::string &first, const std::string &last, int m, int d, int y)
        : firstName(first), lastName(last), birthMonth(m), birthDay(d), birthYear(y) {}

    // Getters and Setters for first name
    void setFirstName(const std::string &first) {
        firstName = first;
    }
    std::string getFirstName() const {
        return firstName;
    }

    // Getters and Setters for last name
    void setLastName(const std::string &last) {
        lastName = last;
    }
    std::string getLastName() const {
        return lastName;
    }

    //implementing setters and getters for birthMonth, birthDay, and birthYear

    //calculate age
    int getAge(int currentYear, int currentMonth, int currentDay) const {
        int age = currentYear - birthYear;
        if (birthMonth > currentMonth || (birthMonth == currentMonth && birthDay > currentDay))
            age--;
        return age;
    }

    //calculate maximum heart rate
    int getMaximumHeartRate() const {
        //pass currentYear, currentMonth, and currentDay to getAge() here
        return 220 - getAge(2024, 2, 23); // Assuming today's date is 2024-02-23
    }

    // calculate target heart rate
    void getTargetHeartRate(int &targetMin, int &targetMax) const {
        int maxRate = getMaximumHeartRate();
        targetMin = static_cast<int>(maxRate * 0.50);
        targetMax = static_cast<int>(maxRate * 0.85);
    }

private:
    std::string firstName;
    std::string lastName;
    int birthMonth;
    int birthDay;
    int birthYear;
};

int main() {
    std::string firstName, lastName;
    int birthMonth, birthDay, birthYear;
    int currentMonth, currentDay, currentYear;

    std::cout << "Enter first name: ";
    std::cin >> firstName;
    std::cout << "Enter last name: ";
    std::cin >> lastName;
    std::cout << "Enter birth month, day, and year: ";
    std::cin >> birthMonth >> birthDay >> birthYear;
    std::cout << "Enter current month, day, and year: ";
    std::cin >> currentMonth >> currentDay >> currentYear;

    HeartRates person(firstName, lastName, birthMonth, birthDay, birthYear);

    std::cout << "\nPerson's Information:\n"
              << "Name: " << person.getFirstName() << " " << person.getLastName() << "\n"
              << "Date of Birth: " << birthMonth << "/" << birthDay << "/" << birthYear << "\n";

    int age = person.getAge(currentYear, currentMonth, currentDay);
    std::pair<int, int> targetHeartRate;
    person.getTargetHeartRate(targetHeartRate.first, targetHeartRate.second);

    std::cout << "\nAdditional Information:\n"
              << "Age: " << age << " years\n"
              << "Maximum Heart Rate: " << person.getMaximumHeartRate() << " bpm\n"
              << "Target Heart Rate Range: " << targetHeartRate.first << " bpm - "
              << targetHeartRate.second << " bpm\n";

    return 0;
}

// Output - 
// Enter first name: Afia 
// Enter last name: Zaman
// Enter birth month, day, and year: 06 22 2004
// Enter current month, day, and year: 02 23 2024

// Person's Information:
// Name: Afia Zaman
// Date of Birth: 6/22/2004

// Additional Information:
// Age: 19 years
// Maximum Heart Rate: 201 bpm
// Target Heart Rate Range: 100 bpm - 170 bpm


