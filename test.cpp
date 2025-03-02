#include <iostream>
using namespace std;

int main() {
    // 1️⃣ Uninitialized Pointer (Segmentation Fault)
    int* p;
    *p = 10;  // ❌ ERROR: Dereferencing an uninitialized pointer

    // 2️⃣ Infinite Loop
    for(int i = 0; i < 5; i--) {  // ❌ ERROR: Loop condition always true
        cout << "Looping forever..." << endl;
    }

    // 3️⃣ Array Out of Bounds
    int arr[5];
    arr[10] = 42;  // ❌ ERROR: Accessing index outside of array size

    // 4️⃣ Uninitialized Variable
    int x;
    if (x == 5) {  // ❌ ERROR: Using an uninitialized variable
        cout << "Uninitialized variable used!" << endl;
    }

    // 5️⃣ Memory Leak
    int* ptr = new int[5];
    delete ptr;  // ❌ ERROR: Should use delete[] for arrays

    // 6️⃣ Unreachable Code
    cout << "Before return statement." << endl;
    return 0;
    cout << "This will never execute." << endl;  // ❌ ERROR: Unreachable code

    // 7️⃣ Double Free
    int* q = (int*)malloc(4);
    free(q);
    free(q);  // ❌ ERROR: Freeing memory twice
}
