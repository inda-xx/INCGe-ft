### Task Description

Exercise 1: Inventory Management System

Objective: Develop a program to manage product inventory, focusing on manipulating arrays and using loops to perform operations.

Description:
Students will implement an inventory management system for a small store. They will use arrays to store product information and loops to perform operations such as searching, adding, and removing products.

Tasks:
1. Initialize an array to store product names and quantities.
2. Write a loop to display all products and their quantities.
3. Implement functionality to add a new product to the inventory.
4. Use a loop to find and remove a product from the inventory.
5. Enhance the system to update the quantity of an existing product.

Hint Code Snippet:
```java
String[] products = new String[100];
int[] quantities = new int[100];

// Loop to display products
for (int i = 0; i < products.length; i++) {
    if (products[i] != null) {
        System.out.println(products[i] + ": " + quantities[i]);
    }
}
``` 

This exercise encourages problem-solving by simulating a real-world inventory management scenario, challenging students to manipulate arrays effectively using loops.