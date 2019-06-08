"""
#1 (Easy)
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# unoptimized brute force
def solution1(k, numbers):
    for (idx1, number1) in enumerate(numbers):
        for (idx2, number2) in enumerate(numbers):
            # don't check the same value again
            if idx1 == idx2:
                continue

            if number1 + number2 == k:
                return True
    return False

# optimized brute force
def solution2(k, numbers):
    for idx1, number1 in enumerate(numbers):
        # second loop can skip all previously checked items
        for number2 in numbers[idx1+1:]:
            if number1 + number2 == k:
                return True
    return False

# one pass solution with a hash set
def solution3(k, numbers):
    restSet = set([])
    for number in numbers:
        if number in restSet:
            return True

        restSet.add(k - number)

    return False

def main():
    data = [
        [True, 17, [10, 15, 3, 7]],         # True: 10 + 7
        [False, 17, [10, 15, 3, 8]],        # False
        [True, 11, [10, 15, 3, 8, 1]],      # True: 3 + 8, 10 + 1
        [True, 18, [10, 15, 3, 8, 1]],      # True: 15 + 3
        [False, 20, [10, 3, 8, 1]],         # False: 10 + 10 should not work
    ]

    solutions = [
        solution1,
        solution2,
        solution3
    ]

    failedSolutions = set([])

    for dataEntry in data:
        expected = dataEntry[0]
        k = dataEntry[1]
        numbers = dataEntry[2]

        print("k: {}, numbers: {}, expected: {}".format(str(k), str(numbers), str(expected)))

        for solution in solutions:
            result = solution(k, numbers)
            if result != expected:
                failedSolutions.add(solution)
            print("'{}': {}".format(solution.__name__, result))

        print()

    for failedSolution in failedSolutions:
        print("solution '{}' failed".format(failedSolution.__name__))

if __name__ == "__main__":
    main()
