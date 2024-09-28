# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-two
def countingSort(arr):
    countedElems = [0] * 100
    for val in arr:
        countedElems[val] += 1
    return countedElems
