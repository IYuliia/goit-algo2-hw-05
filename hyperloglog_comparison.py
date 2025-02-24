import time
import re
import mmh3
import math
from collections import defaultdict
from functools import lru_cache
from dataclasses import dataclass

class HyperLogLog:
    def __init__(self, p=5):
        self.p = p
        self.m = 1 << p
        self.registers = [0] * self.m
        self.alpha = self._get_alpha()
        self.small_range_correction = 5 * self.m / 2 

    def _get_alpha(self):
        if self.p <= 16:
            return 0.673
        elif self.p == 32:
            return 0.697
        else:
            return 0.7213 / (1 + 1.079 / self.m)

    def add(self, item):
        x = mmh3.hash(str(item), signed=False)
        j = x & (self.m - 1)
        w = x >> self.p
        self.registers[j] = max(self.registers[j], self._rho(w))

    def _rho(self, w):
        return len(bin(w)) - 2 if w > 0 else 32

    def count(self):
        Z = sum(2.0 ** -r for r in self.registers)
        E = self.alpha * self.m * self.m / Z
       
        if E <= self.small_range_correction:
            V = self.registers.count(0)
            if V > 0:
                return self.m * math.log(self.m / V)
        
        return E


def load_ip_addresses(filename):
    ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    ips = []
    try:
        with open(filename, "r") as file:
            for line in file:
                match = ip_pattern.search(line)
                if match:
                    ips.append(match.group())
    except FileNotFoundError:
        print("Error: File not found.")
    return ips


def exact_unique_count(ip_list):
    return len(set(ip_list))


def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, round(end - start, 4)


def run_comparison(log_file):
    ips = load_ip_addresses(log_file)

    exact_count, exact_time = measure_time(exact_unique_count, ips)

    hll = HyperLogLog(p=14)  
    for ip in ips:
        hll.add(ip)
    hll_count, hll_time = measure_time(lambda: hll.count())

    print("\nComparison Results:")
    print(f"{'':<25}{'Exact Count':<15}{'HyperLogLog':<15}")
    print(f"{'Unique Elements':<25}{exact_count:<15}{hll_count:<15}")
    print(f"{'Execution Time (sec)':<25}{exact_time:<15}{hll_time:<15}")

if __name__ == "__main__":
    log_file = "lms-stage-access.log"
    run_comparison(log_file)
