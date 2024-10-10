# Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.
import random # importing random module
# creating list for days and moods
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]
times = ["morning", "afternoon", "evening"]         
# iterate through days, time and moods and print mood for each day and time
for day in days:
    for time in times:
        mood = random.choice(moods)
        print(f"On {day}, at {time}, I am feeling {mood}.") 