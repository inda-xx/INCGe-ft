# Solution

Below are the solutions to the exercises described, with explanations suitable for students at different skill levels:

### Exercise 1: Analyzing Data from Arrays

#### Step-by-Step Solution

1. **Create an array of integers containing a set of temperature readings.**
   ```java
   int[] temperatures = {30, 32, 28, 35, 31, 33, 36, 29, 40, 27};
   ```

2. **Calculate the average temperature.**
   Here, we use a loop to sum all the temperature readings and then divide by the total number of readings to find the average.
   ```java
   double total = 0;
   for (int temp : temperatures) {
       total += temp;
   }
   double average = total / temperatures.length;
   System.out.println("Average Temperature: " + average);
   ```

3. **Use a loop to count occurrences of temperature values exceeding a threshold.**
   We'll use a threshold value, say 35, and count how many temperature readings exceed this value.
   ```java
   int threshold = 35;
   int count = 0;
   for (int temp : temperatures) {
       if (temp > threshold) {
           count++;
       }
   }
   System.out.println("Temperatures exceeding " + threshold + ": " + count);
   ```

### Exercise 2: Implementing a Custom Hashing Algorithm

#### Step-by-Step Solution

1. **Design a hashing algorithm to map strings to integers.**
   This example keeps it simple by using a base number and modular arithmetic.
   ```java
   int customHash(String input, int tableSize) {
       int hash = 0;
       int prime = 31; // A prime multiplier
       for (char c : input.toCharArray()) {
           hash = (hash * prime + c) % tableSize;
       }
       return hash;
   }
   ```

2. **Implement collision resolution using separate chaining.**
   We'll use an array of linked lists to handle collisions.
   ```java
   List<String>[] hashTable = new LinkedList[tableSize];
   for (int i = 0; i < tableSize; i++) {
       hashTable[i] = new LinkedList<>();
   }

   void insert(String key) {
       int index = customHash(key, hashTable.length);
       if (!hashTable[index].contains(key)) {
           hashTable[index].add(key);
       }
   }
   ```

3. **Test with datasets:**
   Demonstrate insertion and retrieval with different strings to test performance and collision resolution.
   ```java
   String[] keys = {"apple", "banana", "grape", "orange", "melon"};
   for (String key : keys) {
       insert(key);
   }

   // Display the hash table
   for (int i = 0; i < tableSize; i++) {
       System.out.println("Bucket " + i + ": " + hashTable[i]);
   }
   ```

### Exercise 3: Random Number Generation for Simulation

#### Step-by-Step Solution

1. **Generate a sequence of random numbers to simulate dice rolls.**
   Use a loop to simulate multiple dice rolls.
   ```java
   Random random = new Random();
   int numRolls = 100;
   int[] outcomes = new int[6]; // Index 0 for roll 1, index 5 for roll 6

   for (int i = 0; i < numRolls; i++) {
       int roll = random.nextInt(6) + 1;
       outcomes[roll - 1]++;
   }
   ```

2. **Simulate a simple game (e.g., rolling until you get a 6).**
   ```java
   int rolls = 0;
   int roll;
   do {
       roll = random.nextInt(6) + 1;
       rolls++;
   } while (roll != 6);
   System.out.println("Number of rolls to get a 6: " + rolls);
   ```

3. **Calculate the frequency distribution of the outcomes.**
   ```java
   for (int i = 0; i < outcomes.length; i++) {
       System.out.println("Frequency of " + (i + 1) + ": " + outcomes[i]);
   }
   ```

These solutions guide students through the basic manipulation of arrays, custom hashing, and random number generation, creating a comprehensive learning experience across varying complexity levels.