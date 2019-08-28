#include <iostream> // I/O Stream (cout, cin, etc.)
// #include <iomanip>  // I/O Manipulators (setw, setprecision, etc.)
#include <fstream>  // File I/O (ifstream, ofstream, etc.)
// #include <cmath>    // Give NAN among other math abilities
// #include <vector>   // Gives vectors

using namespace std;

// Define platform to hold terminal open on linux
#ifdef __linux__
    const string PLATFORM = "linux";
#elif _WIN32
    const string PLATFORM = "windows";
#else
    const string PLATFORM = "other";
#endif


int main() {

    cout << "Hello World!\n";

    if (PLATFORM == "linux"){ cin.get(); } // Keep terminal open on Linux
}
