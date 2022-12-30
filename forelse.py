import math
precipitation_level = 0

for level in range(1, 11):
    precipitation_level = math.ceil(level * 1.32)
    if precipitation_level > 10:
        print("*** Exceeded more than 10*****")
        break
    print(
        f"Stage: {level} Precipitation Level {precipitation_level}"
    )

else:
    print("Precipitation level did not exceed more than 10!")
