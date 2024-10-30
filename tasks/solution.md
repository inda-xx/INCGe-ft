# Solution

Below is a comprehensive solution to the exercises described. The solution is divided into two parts, one for each exercise, using Java.

### Exercise 1: Reading Data and Populating Data Structures Using Arrays

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class StudentDataProcessor {

    public static void main(String[] args) {
        String fileName = "students.txt";
        String[] studentNames = new String[100]; // Assumption: Max 100 students
        int[] studentScores = new int[100];
        int studentCount = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length == 2) {
                    String name = parts[0];
                    int score = Integer.parseInt(parts[1]);

                    studentNames[studentCount] = name;
                    studentScores[studentCount] = score;
                    studentCount++;
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }

        if (studentCount > 0) {
            double averageScore = calculateAverage(studentScores, studentCount);
            int highestScore = findHighestScore(studentScores, studentCount);
            int lowestScore = findLowestScore(studentScores, studentCount);

            System.out.println("Average Score: " + averageScore);
            System.out.println("Highest Score: " + highestScore + ", Student: " + studentNames[findIndex(studentScores, studentCount, highestScore)]);
            System.out.println("Lowest Score: " + lowestScore + ", Student: " + studentNames[findIndex(studentScores, studentCount, lowestScore)]);
        } else {
            System.out.println("No student data found.");
        }
    }

    private static double calculateAverage(int[] scores, int count) {
        int sum = 0;
        for (int i = 0; i < count; i++) {
            sum += scores[i];
        }
        return sum / (double) count;
    }

    private static int findHighestScore(int[] scores, int count) {
        int highest = Integer.MIN_VALUE;
        for (int i = 0; i < count; i++) {
            if (scores[i] > highest) {
                highest = scores[i];
            }
        }
        return highest;
    }

    private static int findLowestScore(int[] scores, int count) {
        int lowest = Integer.MAX_VALUE;
        for (int i = 0; i < count; i++) {
            if (scores[i] < lowest) {
                lowest = scores[i];
            }
        }
        return lowest;
    }

    private static int findIndex(int[] scores, int count, int score) {
        for (int i = 0; i < count; i++) {
            if (scores[i] == score) {
                return i;
            }
        }
        return -1;
    }
}
```

### Exercise 2: Implementing a Student Management System with HashMaps

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class StudentManagementSystem {

    private static Map<String, Integer> studentMap = new HashMap<>();

    public static void main(String[] args) {
        readDataFromFile("students.txt");

        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("Student Management System");
            System.out.println("1. View All Students");
            System.out.println("2. Add New Student");
            System.out.println("3. Remove Student");
            System.out.println("4. Update Student Score");
            System.out.println("5. Search Student");
            System.out.println("6. Exit");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // consume the newline

            switch (choice) {
                case 1:
                    viewAllStudents();
                    break;
                case 2:
                    addStudent(scanner);
                    break;
                case 3:
                    removeStudent(scanner);
                    break;
                case 4:
                    updateStudentScore(scanner);
                    break;
                case 5:
                    searchStudent(scanner);
                    break;
                case 6:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }

        scanner.close();
    }

    private static void readDataFromFile(String fileName) {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length == 2) {
                    String name = parts[0];
                    int score = Integer.parseInt(parts[1]);

                    studentMap.put(name, score);
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }
    }

    private static void viewAllStudents() {
        if (studentMap.isEmpty()) {
            System.out.println("No student records available.");
        } else {
            System.out.println("Student Records:");
            for (Map.Entry<String, Integer> entry : studentMap.entrySet()) {
                System.out.println("Name: " + entry.getKey() + ", Score: " + entry.getValue());
            }
        }
    }

    private static void addStudent(Scanner scanner) {
        System.out.print("Enter student name: ");
        String name = scanner.nextLine();
        System.out.print("Enter student score: ");
        int score = scanner.nextInt();
        scanner.nextLine(); // consume the newline

        if (studentMap.containsKey(name)) {
            System.out.println("Student already exists. Use update option to change the score.");
        } else {
            studentMap.put(name, score);
            System.out.println("Student added successfully.");
        }
    }

    private static void removeStudent(Scanner scanner) {
        System.out.print("Enter student name to remove: ");
        String name = scanner.nextLine();

        if (studentMap.remove(name) != null) {
            System.out.println("Student removed successfully.");
        } else {
            System.out.println("Student not found.");
        }
    }

    private static void updateStudentScore(Scanner scanner) {
        System.out.print("Enter student name to update: ");
        String name = scanner.nextLine();

        if (studentMap.containsKey(name)) {
            System.out.print("Enter new score: ");
            int score = scanner.nextInt();
            scanner.nextLine(); // consume the newline
            studentMap.put(name, score);
            System.out.println("Student score updated successfully.");
        } else {
            System.out.println("Student not found.");
        }
    }

    private static void searchStudent(Scanner scanner) {
        System.out.print("Enter student name to search: ");
        String name = scanner.nextLine();

        if (studentMap.containsKey(name)) {
            System.out.println("Name: " + name + ", Score: " + studentMap.get(name));
        } else {
            System.out.println("Student not found.");
        }
    }
}
```

### Explanation of the Code

#### Exercise 1

1. **File Reading**: We use `BufferedReader` wrapped around `FileReader` to read lines from the `students.txt` file.
2. **Data Storage**: We store names and scores in separate arrays (`studentNames` and `studentScores`).
3. **Data Processing**: We calculate the average, highest, and lowest scores using helper functions.
4. **Output Results**: We print the statistics including the names of the students with the highest and lowest scores.

#### Exercise 2

1. **HashMap Setup**: We create a `HashMap` to store names and scores.
2. **Data Integration and Management**: The `HashMap` is populated from the file and functions are implemented to manage the student records.
3. **User Interface**: A simple text-based interface allows users to interact with the system to perform operations like viewing, adding, removing, updating, and searching for students.
4. **File Reading**: Similar to Exercise 1, we read data from the file and populate the `HashMap`.

### Conclusion

This solution demonstrates effective use of arrays and hash maps for managing data typically encountered in real-world applications. The file handling with arrays in Exercise 1 sets the stage for more complex data management with hash maps in Exercise 2. By exploring and following Java documentation, one can gain insights into effective resource management and robust application development.