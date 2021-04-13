import math

# https://math.stackexchange.com/questions/2978564/find-all-solutions-to-the-system-x-equiv-1-pmod-4-x-equiv-0-pmod-3-and
with open("day13.in") as f:
    lines = f.read().split("\n")

departure = int(lines[0])
buses = lines[1].split(",")
departure_time = []
for bus in buses:
    if bus == "x":
        departure_time.append(10000000000)
    else:
        departure_time.append((int(bus) - departure % int(bus)) % int(bus))

# print(departure_time)
minimum = min(departure_time)
index = departure_time.index(minimum)

print("part 1: ", int(buses[index]) * minimum)

print(len(buses))
# part 2:

bus_time = [
    (int(bus_id), offset) for offset, bus_id in enumerate(buses) if bus_id != "x"
]
print(bus_time)

time = 100
n = 1
for bus_id, offset in bus_time:
    while (time + offset) % bus_id != 0:
        time += n
    n = n * bus_id
print(time)
