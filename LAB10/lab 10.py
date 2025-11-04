# read_athletes.py

# athletes.txt файлын ашу және оқу
with open("athletes.txt", "r") as file:
    scores = []  # ұпайларды сақтау үшін тізім
    print("🏅 Athletes and their performance:\n")

    for line in file:
        # Әр жолды аты мен ұпайына бөлу
        name, score = line.strip().split(", ")
        scores.append(int(score))
        print(f"{name} — {score} points")

    # Орташа ұпайды есептеу
    average = sum(scores) / len(scores)
    print(f"\n📊 Average score: {average:.2f}")

    # Ең үздік спортшыны табу
    max_score = max(scores)
    best_index = scores.index(max_score)

# Ең жоғары ұпай алған спортшыны көрсету
with open("athletes.txt", "r") as file:
    athletes = [line.strip().split(", ") for line in file]
    best_athlete = athletes[best_index][0]
    print(f"🏆 Best performer: {best_athlete} with {max_score} points!")
