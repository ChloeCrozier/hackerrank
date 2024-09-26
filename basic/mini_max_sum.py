# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
def miniMaxSum(arr):
    min_val = arr[0]
    max_val = 0
    arr_sum = 0
    for elem in arr:
        arr_sum += elem
        if elem < min_val:
            min_val = elem
        if elem > max_val:
            max_val = elem
