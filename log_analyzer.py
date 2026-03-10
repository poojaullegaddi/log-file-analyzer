info = warning = error = 0
errors = []

with open("sample_log.txt", "r") as file:
    for line in file:

        if "INFO" in line:
            info += 1

        elif "WARNING" in line:
            warning += 1

        elif "ERROR" in line:
            error += 1
            errors.append(line)

print("INFO:", info)
print("WARNING:", warning)
print("ERROR:", error)

print("\nError Logs:")
for e in errors:
    print(e)