
#### main.py

```python
#!/usr/bin/env python3
import random

def generate_orbit():
    # Generate random orbital parameters
    semi_major_axis = round(random.uniform(0.5, 10.0), 2)  # in Astronomical Units (AU)
    eccentricity = round(random.uniform(0, 0.9), 2)
    # Approximate orbital period using Kepler's Third Law (T^2 proportional to a^3, simplified)
    orbital_period = round(semi_major_axis ** 1.5, 2)  # in years
    return semi_major_axis, eccentricity, orbital_period

def main():
    print("Welcome to the Orbit Simulator!")
    print("Randomly generated orbital parameters:")
    semi_major_axis, eccentricity, orbital_period = generate_orbit()
    print(f"Semi-major Axis: {semi_major_axis} AU")
    print(f"Eccentricity: {eccentricity}")
    print(f"Orbital Period: {orbital_period} years")

if __name__ == "__main__":
    main()
