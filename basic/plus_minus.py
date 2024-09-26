# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
def plusMinus(arr):
    length = len(arr)
    positive, negative = 0, 0
    
    for elem in arr:
        if elem > 0:
            positive += 1
        elif elem < 0:
            negative += 1
    
    print(round(positive/length, 6))
    print(round(negative/length, 6))
    print(round((length - positive - negative)/length, 6))
