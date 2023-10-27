#include <stdio.h>

int sumDigits(int number[], int start, int end) {
    int sum = 0;
    for (int i = start; i < end; i++) {
        sum += number[i];
    }
    return sum;
}

int countLuckyNumbers(int n) {
    int count = 0;
    int digits[n];
    int half = n / 2;

    for (int i = 0; i < n; i++) {
        digits[i] = 0;
    }

    while (1) {
        int leftSum = sumDigits(digits, 0, half);
        int rightSum = sumDigits(digits, half, n);
        if (leftSum == rightSum) {
            count++;
        }

        int carry = 1;
        for (int i = n - 1; i >= 0; i--) {
            digits[i] += carry;
            if (digits[i] == 10) {
                digits[i] = 0;
                carry = 1;
            } else {
                carry = 0;
                break;
            }
        }

        if (carry == 1) {
            break;
        }
    }

    return count;
}

int main() {
    int n;
    printf("Sonning uzunligini kiriting: ");
    scanf("%d", &n);

    int luckyCount = countLuckyNumbers(n);
    printf("Omadli chipta sonlarining soni: %d\n", luckyCount);

    return 0;
}