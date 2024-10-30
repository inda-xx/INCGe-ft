### Task Description

Exercise 1: Analyzing Text File Data with HashMaps

**Subject:** Arrays  
**Difficulty:** Medium  
**Skills:** Loops  

**Objective:**  
In this exercise, students will read data from a text file, process it using arrays and HashMaps, and output meaningful statistics. This task simulates a common real-world scenario of data processing and analysis.

**Description:**  
Students will work with a text file containing product sales data. They must read the file, analyze sales per product, and store results in a HashMap. This exercise reinforces reading data efficiently and using HashMaps for data analysis.

**Instructions:**  

1. **Read the File:**
   - Set up the file path and read the file line by line using `BufferedReader`.
   - Extract product names and sales figures from each line.

   ```java
   BufferedReader reader = new BufferedReader(new FileReader("sales.txt"));
   String line;
   while ((line = reader.readLine()) != null) {
       // Process line
   }
   ```

2. **Process Data:**
   - Use an array to store and update sales figures for each product.
   - Implement a loop to iterate through the data and populate the array.

   ```java
   String[] productData = line.split(",");
   String productName = productData[0];
   int sales = Integer.parseInt(productData[1]);
   ```

3. **Store Results in a HashMap:**
   - Create a `HashMap` to map product names to total sales.
   - Update the map with cumulative sales for each product.

   ```java
   HashMap<String, Integer> salesMap = new HashMap<>();
   salesMap.put(productName, salesMap.getOrDefault(productName, 0) + sales);
   ```

4. **Output Statistics:**
   - Iterate over the `HashMap` to print total sales for each product.
   - Use loops to analyze and display data patterns.

   ```java
   for (Map.Entry<String, Integer> entry : salesMap.entrySet()) {
       System.out.println(entry.getKey() + ": " + entry.getValue());
   }
   ```

**Expected Outcomes:**  
By completing this exercise, students will develop skills in file I/O, data manipulation with arrays, and using HashMaps for efficient data processing. They will also enhance their ability to navigate and leverage documentation to implement these solutions.