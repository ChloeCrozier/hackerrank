# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two
def lonelyinteger(a):
    seen = {}
    for elem in a:
        if elem in seen:
            seen[elem] += 1
        else:
            seen[elem] = 1
    for key, val in seen.items():
        if val == 1:
            return key
