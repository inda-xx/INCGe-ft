### Task Description

Exercise 1: Analyzing Text Data with HashMaps

**Subject:** File I/O and Collections  
**Difficulty:** Medium  
**Skills:** Using Documentation, File Reading, HashMap Manipulation

### Objective:

This exercise aims to enhance students' understanding of file I/O operations and the use of the `HashMap` class in Java by analyzing text data. It also emphasizes the importance of using documentation for understanding Java classes and libraries effectively.

### Instructions:

1. **Read and Explore Java Documentation:**
   - Navigate to the official Java documentation [Oracle Java API Docs](https://docs.oracle.com/en/java/javase/17/docs/api/index.html).
   - Familiarize yourself with the documentation for `HashMap`, `FileReader`, and `BufferedReader`.
   - Identify key methods and their use cases. Pay attention to examples provided and consider how they might be useful for this exercise.

2. **Set Up File Reading:**
   - Create a Java class named `TextAnalyzer`.
   - Set up a `BufferedReader` using `FileReader` to read from a provided text file, `data.txt`.
   - Ensure the file path is correctly specified, and handle IOExceptions using try-with-resources for resource management.

3. **Implement HashMap for Data Analysis:**
   - Initialize a `HashMap<String, Integer>` to keep track of word frequencies in the text file.
   - Read the file line-by-line, and for each word, update the frequency count in the `HashMap`.
   - Investigate and apply methods like `put()`, `getOrDefault()`, and `keySet()` for efficient operations.

4. **Enhance and Document Your Code:**
   - Use Java documentation and community resources to optimize your approach.
   - Comment your code to explain the logic and methods used, drawing connections to documentation insights.

5. **Test and Reflect:**
   - Print out the top 5 most frequent words and their counts.
   - Reflect on the performance and propose changes for handling larger datasets.

### Deliverables:

- A Java class file `TextAnalyzer.java` with implemented functionality.
- Documentation comments and a brief report detailing the approach and key learnings from the documentation.
- Output of the program showcasing the top 5 words with their frequencies.