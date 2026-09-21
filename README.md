[README.md](https://github.com/user-attachments/files/32490223/README.md)
# Velocity & Acceleration Calculator

A simple command-line script that calculates either velocity or
acceleration from a distance and time input.

## How it works

1. Prompts you for:
   - **Distance travelled** (in meters)
   - **Time taken** (in seconds)
   - **Quantity** you want: `A` for acceleration or `V` for velocity
2. Calculates:
   - `velocity = distance / time`
   - `acceleration = velocity / time`
3. Prints the result rounded to 2 decimal places, with the correct unit
   (`M/S` for velocity, `M/S^2` for acceleration).

## Usage

```bash
python "quantity calculation (velocity and acceleration).py"
```

Example run:
```
Enter distance travelled: 100
enter time taken: 10
enter quantity, acceleration(A) or velocity(V): V
your answer is: 10.0M/S
```

## Notes / things to be aware of

- **Input is case-sensitive.** Typing `a` or `v` (lowercase) will fall
  through to the "please enter either A or V" message instead of
  calculating anything — and since `unit` and `answer` are never set in
  that case, the final `print` line will actually crash with a
  `NameError`. If you want lowercase to work too, compare against
  `quantity.upper()` instead of `quantity` directly.
- **Acceleration here is derived, not directly measured** — it's
  calculated as `velocity / time`, which assumes you started from rest
  (0 initial velocity) and accelerated uniformly over the full time
  period. It isn't a general-purpose acceleration formula.
- No input validation for non-numeric distance/time — entering
  non-numbers will crash the script with a `ValueError`.

## Possible improvements

- Fix the invalid-input case so it doesn't crash.
- Accept lowercase `a`/`v`.
- Let the user separately provide initial and final velocity for a more
  general acceleration calculation.
