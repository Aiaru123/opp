# Task 4: Custom Exception Example

# Custom exception
class LowScoreError(Exception):
    pass


try:
    # Қолданушыдан спортшының ұпайын сұрау
    score = int(input("Enter athlete score: "))

    # Егер ұпай 5-тен төмен болса (мысалы, спортшылар үшін минималды 5)
    if score < 5:
        raise LowScoreError("Score too low! Athlete failed.")

    print("Score accepted.")

except LowScoreError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Error: Score must be a number!")
