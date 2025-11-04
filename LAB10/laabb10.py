# append_athletes.py

# Қолданушыдан жаңа спортшының аты мен ұпайын сұраймыз
name = input("Enter athlete name: ")
score = input("Enter athlete score: ")

# Файлға қосу (append режимі)
with open("athletes.txt", "a") as file:
    file.write(f"\n{name}, {score}")

print("\nRecord added successfully!\n")

# Енді жаңартылған файл мазмұнын шығару
print("🏅 Updated list of athletes:\n")

with open("athletes.txt", "r") as file:
    for line in file:
        print(line.strip())
