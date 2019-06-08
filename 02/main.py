"""
#2 (Hard)
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

# brute force (but using no division)
def solution1(input):
    result = [1] * len(input)

    for idx1, value1 in enumerate(input):
        for idx2, value2 in enumerate(input):
            if idx1 == idx2:
                continue

            result[idx1] = result[idx1] * value2

    return result

# smarter than brute force (but with division)
def solution2(input):
    # compute product over all values
    product = 1
    for value in input:
        product = product * value

    # initialize array with all-values-product
    result = [product] * len(input)

    # divide each entry by value at their index
    for idx, value in enumerate(result):
        result[idx] = int(value / input[idx])

    return result

def main():
    data = [
        [[1, 2, 3, 4, 5], [120, 60, 40, 30, 24]],
        [[3, 2, 1], [2, 3, 6]]
    ]

    solutions = [
        solution1,
        solution2
    ]

    failedSolutions = set([])

    for dataEntry in data:
        input = dataEntry[0]
        expected = dataEntry[1]

        print("input: {}, expected: {}".format(str(input), str(expected)))

        for solution in solutions:
            result = solution(input)
            if result != expected:
                failedSolutions.add(solution)
            print("'{}': {}".format(solution.__name__, result))

        print()

    for failedSolution in failedSolutions:
        print("solution '{}' failed".format(failedSolution.__name__))

if __name__ == "__main__":
    main()