#include <iostream>
using namespace std;

int main() {
    // 6️⃣ Unreachable Code
    cout << "Before return statement." << endl;
    return 0;
    cout << "This will never execute." << endl;  // ❌ ERROR: Unreachable code
    return 0;
}