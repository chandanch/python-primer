import math
precipitation_level = 0

for level in range(1, 11):
    precipitation_level = math.ceil(level * 1.32)
    print(
        f"Stage: {level} Precipitation Level {precipitation_level}"
    )
