print("FAILED LOGIN DETECTION\n")

failed_count = 0

with open("sample.log", "r") as file:
    logs = file.readlines()

for line in logs:
    if "Failed password" in line:
        print(line.strip())
        failed_count += 1

print("\nSUMMARY:")
print("Total failed logins:", failed_count)
