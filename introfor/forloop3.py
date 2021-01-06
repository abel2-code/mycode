#!/usr/bin/env python3

peak = 5

for i in range(1, peak * 2):
    stars = -abs(peak - i) + peak
    print("* " * stars)
