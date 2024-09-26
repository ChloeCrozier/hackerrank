# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
def timeConversion(s):
    hour = int(s[0:2])
    if s[-2:] == 'PM':
        if hour < 12:
            s = str(hour + 12) + s[2:]
    else:
        if hour == 12:
            s = '00' + s[2:]
    return s[:-2]
