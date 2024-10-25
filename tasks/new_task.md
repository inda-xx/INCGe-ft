### Task Description

### Exercise 1: Word Frequency Analyzer

**Subject: Arrays and Collections**

**Difficulty: Medium**

**Skills: Loops, File I/O, HashMap Manipulation**

---

#### Objective:

Students will learn to apply file reading techniques, use the `HashMap` class for data storage, and utilize documentation to understand Java libraries. This exercise simulates a real-world application of analyzing text data for word frequency, reinforcing critical thinking and problem-solving.

---

#### Description:

In this exercise, students will create a word frequency analyzer that reads a text file and calculates the frequency of each word. They'll use `HashMap` to store and manage word counts efficiently. This exercise emphasizes the importance of documentation and mastery of file I/O operations in Java.

---

#### Instructions:

1. **Setup:**

   - Create a Java project named `WordFrequencyAnalyzer`.
   - Prepare a text file, `input.txt`, containing sample text data.

2. **Task 1: File Reading and Stream Setup**
   
   - Set up a file path to `input.txt` and use `FileReader` and `BufferedReader` to efficiently read the file line by line.
   - Use the documentation to understand how `BufferedReader` enhances reading performance.

3. **Task 2: Populating the HashMap**
   
   - Split each line into words using appropriate methods (e.g., `split` on spaces or punctuation).
   - Use a `HashMap<String, Integer>` to track word frequencies. Initialize and update the map for each word encountered.

4. **Task 3: Exception Handling and Resource Management**
   
   - Implement try-with-resources to manage file streams and ensure resources are closed properly.
   - Handle potential exceptions, such as `FileNotFoundException` and `IOException`, to enhance robustness.

5. **Task 4: Analyzing and Displaying Results**
   
   - Iterate over the `HashMap` to display word frequencies in a readable format.
   - Sort the words by frequency and print the top N most frequent words.

6. **Documentation and Community Resources:**
   
   - Encourage students to navigate the official Java documentation to deepen their understanding of `HashMap` and I/O classes.
   - Explore community forums for additional insights and problem-solving strategies.

---

#### Evaluation Criteria:

- Correct setup and reading of the text file.
- Accurate implementation of the `HashMap` for counting word frequencies.
- Effective use of documentation and resources.
- Robust exception handling and resource management.
- Clear and correct output of word frequency analysis.

---

This exercise will enhance students' ability to integrate Java's file I/O and collection classes into practical applications, emphasizing documentation's role in mastering Java's libraries.