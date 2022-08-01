#!/usr/bin/env python3
"""
created: 2022-08-01 19:36:06
@author: seraph★776
contact: seraph776@gmail.com
"""



def validate_credit_card(card_number: str) -> bool:
    """This function validates a credit card number."""
    # 1. Change datatype to list[int]
    card_number = [int(num) for num in card_number]

    # 2. Remove the last digit:
    checkDigit = card_number.pop(-1)

    # 3. Reverse the remaining digits:
    card_number.reverse()

    # 4. Double digits at even indices
    card_number = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(card_number)]

    # 5. Subtract 9 at even indices if digit is over 9
    # (or you can add the digits)
    card_number = [num - 9 if idx % 2 == 0 and num >= 9
                   else num for idx, num in enumerate(card_number)]

    # 6. Add the checkDigit back to the list:
    card_number.append(checkDigit)

    # 7. Sum all digits:
    checkSum = sum(card_number)

    # 8. If checkSum is divisible by 10, it is valid.
    return checkSum % 10 == 0


if __name__ == '__main__':
    # American Express
    print(validate_credit_card('378282246310005'))  # True
    print(validate_credit_card('371449635398431'))  # True
    # American Express Corporate
    print(validate_credit_card('378734493671000'))  # True
    # Australian BankCard
    print(validate_credit_card('5610591081018250'))  # True
    # Diners Club
    print(validate_credit_card('30569309025904'))  # True
    print(validate_credit_card('38520000023237'))  # True
    # Discover
    print(validate_credit_card('6011111111111117'))  # True
    print(validate_credit_card('6011000990139424'))  # True
    # MasterCard
    print(validate_credit_card('5555555555554444'))  # True
    print(validate_credit_card('5105105105105100'))  # True
    # Visa
    print(validate_credit_card('4111111111111111'))  # True
    print(validate_credit_card('4012888888881881'))  # True

    # Invalid Credit Card Number
    print(validate_credit_card('7762888103111881'))  # False
    print(validate_credit_card('37612555227841800'))  # False
