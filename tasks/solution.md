# Solution

Sure, let's work through the solution for the task given, which involves calculating the average temperature and identifying the hottest and coldest days from an array of daily temperatures representing a month's worth of data.

### Step-by-Step Solution:

1. **Create an array containing daily temperatures for 30 days.**
2. **Implement a loop to calculate the average temperature.**
3. **Identify the highest and lowest temperatures and their corresponding day indices.**

In Rust, we will make use of arrays, loops, and enumeration to achieve this task. Here's a complete implementation:

```rust
fn main() {
    // Step 1: Initialize an array containing 30 integers representing daily temperatures
    let temperatures = [
        10, 12, 8, 15, 11, 17, 9, 14, 10, 18, 21, 11, 16, 9, 7, 19, 20, 13, 14, 15,
        16, 18, 20, 21, 22, 19, 18, 17, 16, 15,
    ];

    // Step 2: Initialize variables for sum calculation and temperature tracking
    let mut sum = 0;
    let mut max_temp = temperatures[0];
    let mut min_temp = temperatures[0];
    let mut max_index = 0;
    let mut min_index = 0;

    // Step 3: Loop through the array to compute the sum, and track max and min temperatures
    for (i, &temp) in temperatures.iter().enumerate() {
        sum += temp;

        if temp > max_temp {
            max_temp = temp;
            max_index = i;
        }

        if temp < min_temp {
            min_temp = temp;
            min_index = i;
        }
    }

    // Calculate the average temperature
    let average_temp = sum as f64 / temperatures.len() as f64;

    // Print the results
    println!("Average temperature: {:.2}", average_temp);
    println!("Hottest day: Day {} with {}°C", max_index + 1, max_temp);
    println!("Coldest day: Day {} with {}°C", min_index + 1, min_temp);
}
```

### Explanation:

1. **Array Initialization:**
    ```rust
    let temperatures = [
        10, 12, 8, 15, 11, 17, 9, 14, 10, 18, 21, 11, 16, 9, 7, 19, 20, 13, 14, 15,
        16, 18, 20, 21, 22, 19, 18, 17, 16, 15,
    ];
    ```
    This array contains 30 temperature readings, simulating daily temperatures for a month.

2. **Variables Initialization for Analysis:**
    ```rust
    let mut sum = 0;
    let mut max_temp = temperatures[0];
    let mut min_temp = temperatures[0];
    let mut max_index = 0;
    let mut min_index = 0;
    ```
    - `sum` to keep a running total of temperatures for average calculation.
    - `max_temp` and `min_temp` to track highest and lowest temperatures.
    - `max_index` and `min_index` to store the day indices of the highest and lowest temperatures.

3. **Loop for Processing the Array:**
    ```rust
    for (i, &temp) in temperatures.iter().enumerate() {
        sum += temp;
        if temp > max_temp {
            max_temp = temp;
            max_index = i;
        }
        if temp < min_temp {
            min_temp = temp;
            min_index = i;
        }
    }
    ```
    - We iterate through the array using `.iter().enumerate()` to get both the index and the temperature.
    - `sum` is updated by adding the current temperature.
    - `max_temp` and `min_temp` along with their indices are updated when a new higher or lower temperature is found.

4. **Calculate and Output the Average Temperature:**
    ```rust
    let average_temp = sum as f64 / temperatures.len() as f64;
    println!("Average temperature: {:.2}", average_temp);
    println!("Hottest day: Day {} with {}°C", max_index + 1, max_temp);
    println!("Coldest day: Day {} with {}°C", min_index + 1, min_temp);
    ```
    - The average temperature is calculated by dividing `sum` by the length of the array and casting the result to `f64` for floating-point division.
    - The results are printed, with the day indices adjusted to be 1-based for human readability.

By following these steps and understanding each part of the code, students can gain practical experience in array manipulation, loop constructs, and basic data processing techniques in Rust.