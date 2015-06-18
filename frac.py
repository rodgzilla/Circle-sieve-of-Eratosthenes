import sys
import pygame
from pygame import gfxdraw
from pygame import Color

pygame.init()
window_width = 900
window_height = 600
multiplier = 4
# Can be 1 or 2, the radius of each circle is divided by this value.
divisor = 1

def eratosthene(window, max_value):
    """Implementing the sieve of Eratosthenes:
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes. Whenever a
    multiple of a potential prime is crossed, draw a circle whose
    center depends on the multiple and whose radius depends on the
    prime number.

    """
    int_list = range(2, max_value + 1)
    primes = set(int_list)
    y = window_height / 2

    for n in int_list:
        if n in primes:
            i = 2 * n
            gfxdraw.circle(window, multiplier * n, y, (multiplier * n) / divisor, 
                           Color(129, 129, 129, 255))
            while i <= max_value:
                gfxdraw.circle(window, multiplier * i, y, (multiplier * n) / divisor, 
                               Color(129, 129, 129, 255))
                if i in primes:
                    primes.remove(i)
                i += n

if __name__ == '__main__':
    window = pygame.display.set_mode((window_width, window_height))

    eratosthene(window, 900)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
