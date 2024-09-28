# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-two
def diagonalDifference(arr):
    topDownSum = 0
    bottomUpSum = 0
    length = len(arr[0])
    for i in range(0, len(arr)):
        topDownSum += arr[i][i]
        bottomUpSum += arr[length - i - 1][i]
    return abs(topDownSum - bottomUpSum)
