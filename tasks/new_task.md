### Task Description

### Exercise 1: Temperature Data Analysis with Arrays

**Objective:**  
Develop skills in using arrays and loops to process and analyze numerical data.

**Description:**  
In this exercise, students will work with an array representing daily temperature readings over a month. The goal is to analyze this data by calculating both the average temperature and identifying the hottest and coldest days. This exercise simulates real-world data processing tasks encountered in climate research and monitoring.

**Requirements:**  
1. Create an array containing 30 integers representing daily temperatures.
2. Implement a loop to calculate the average temperature.
3. Identify the highest and lowest temperatures and their corresponding day indices.

**Hints:**  
- Use a `for` loop to iterate through the array and accumulate the sum for average calculation.
- Track the maximum and minimum temperatures along with their indices during the iteration.

```rust
let temperatures = [10, 12, 8, 15, // ... more data for 30 days];
let mut sum = 0;
let mut max_temp = temperatures[0];
let mut min_temp = temperatures[0];
for (i, temp) in temperatures.iter().enumerate() {
    sum += temp;
    if *temp > max_temp {
        max_temp = *temp;
        // Save index for hottest day
    }
    if *temp < min_temp {
        min_temp = *temp;
        // Save index for coldest day
    }
}
```

**Outcome:**  
By completing this exercise, students will enhance their ability to manipulate arrays and loops in Rust, preparing them for more complex data processing challenges.