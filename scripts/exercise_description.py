import os
import sys
import openai


def generate_with_retries(client, messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="ft:gpt-4o-2024-08-06:kexjobbars:third-times-the-charm:AM0eLhOv",
                messages=messages
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating task description: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
    return None

def parse_exercise_details(details):
    if details:
        parts = details.split(",")
        difficulty = parts[0].strip()
        skills = parts[1].strip() if len(parts) > 1 else "None"
        subject = parts[2].strip() if len(parts) > 2 else "No subject provided"
        return difficulty, skills, subject
    return None, None, None

def generate_task_description(api_key, number_of_exercises, language, programming_language, *exercise_details):
    if not api_key:
        print("Error: OpenAI API key is missing.")
        sys.exit(1)

    openai.api_key = api_key

    # Prepare modular prompts for each exercise considering difficulty level, language, and skill maps
    exercise_details_formatted = []
    for i, details in enumerate(exercise_details):
        difficulty, skills, subject = parse_exercise_details(details)
        if difficulty and skills and subject:
            prompt_section = f"Exercise {i+1}: Subject: {subject}, Difficulty: {difficulty}, Skills: {skills}\n\n"
            if difficulty == "simple":
                prompt_section += (
                    "Focus on introductory concepts for beginners using basic applications of the skills. "
                    "Encourage understanding of foundational concepts in programming, especially for language: {programming_language}.\n"
                )
            elif difficulty == "medium":
                prompt_section += (
                    "This exercise should push students to apply their skills in moderately challenging scenarios. "
                    "Include tasks that involve real-world applications, encouraging problem-solving in {programming_language}.\n"
                )
            elif difficulty == "hard":
                prompt_section += (
                    "Challenge students to solve complex problems that require deeper knowledge of the specified skills. "
                    "The tasks should simulate industry-level complexity, especially suited for {programming_language} applications.\n"
                )
            elif difficulty == "v.hard":
                prompt_section += (
                    "The exercise should be highly challenging, combining multiple skills to solve complex, multi-step problems. "
                    "Designed for advanced students, it should demand a deep understanding of {programming_language} in practical applications.\n"
                )

            exercise_details_formatted.append(prompt_section)

    if not exercise_details_formatted:
        print("No valid exercises were provided.")
        sys.exit(1)

    # Modular prompt that integrates the learning goals and skill maps
    messages = [
        {
            "role": "system",
            "content": (
                "You are an experienced programming instructor creating a set of exercises for a university-level programming lab. "
                "These exercises should be challenging, pedagogically valuable, and focused on skill development in the specified programming language."
                "Provide very brief code snippets in the exercise as small hints and guides in the chosen language. The snippets should in no way reveal the answer but provide a slight structure to tackle the task."
            )
        },
        {
            "role": "user",
            "content": f"Create {number_of_exercises} exercises in {programming_language}."
                       "Each exercise should follow the provided details:\n\n" +
                       "\n".join(exercise_details_formatted) +
                       "\n\nDesign these exercises to be challenging and to encourage the students to apply critical thinking and problem-solving skills."
        }
    ]

    task_description = generate_with_retries(openai, messages)
    if not task_description:
        print("Failed to generate task description.")
        sys.exit(1)

    # Write the task description to a markdown file
    with open("tasks/new_task.md", "w") as f:
        f.write(f"### Task Description\n\n")
        f.write(task_description)

    print("Task description generated successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: exercise_description.py <api_key> <number_of_exercises> <language> <programming_language> <exercise_1_details> [<exercise_2_details> ...]")
        sys.exit(1)

    api_key = sys.argv[1]
    number_of_exercises = sys.argv[2]
    language = sys.argv[3]
    programming_language = sys.argv[4]
    exercise_details = sys.argv[5:]

    generate_task_description(api_key, number_of_exercises, language, programming_language, *exercise_details)
