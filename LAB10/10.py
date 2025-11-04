# task3_athletes.py

try:
    # Файлды оқу
    with open("athletes.txt", "r") as file:
        athletes = file.readlines()

except FileNotFoundError:
    # Файл жоқ болса
    print("Error: File 'athletes.txt' not found! Please create it first.")

else:
    # Файл сәтті оқылды
    print("File read successfully!\n")
    print("🏅 Current list of athletes:\n")
    for line in athletes:
        print(line.strip())

    # Жаңа спортшы қосу
    try:
        name = input("\nEnter athlete name: ")
        score = int(input("Enter athlete score: "))  # сан болуы керек
        with open("athletes.txt", "a") as file:
            file.write(f"\n{name}, {score}")
        print("\nRecord added successfully!")

    except ValueError:
        # Егер сан енгізілмесе
        print("Error: Score must be a number!")

finally:
    print("\nProgram completed.")


