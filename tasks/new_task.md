### Task Description

Exercise 1: Subject: Building a Contact Management System, Difficulty: medium, Skills: Hash maps

Description:
In this exercise, students will create a contact management system using hash maps to store and retrieve contact information efficiently. This task simulates real-world applications of data storage and retrieval.

Objective:
- Implement a system to add, delete, and search contacts.
- Utilize hash maps for fast lookup operations.

Code Snippet:
```java
Map<String, Contact> contactMap = new HashMap<>();
// Add a new contact
contactMap.put("John Doe", new Contact("John Doe", "123-456-7890"));
// Retrieve contact information
Contact contact = contactMap.get("John Doe");
```

Task Breakdown:
1. Define a `Contact` class with necessary fields.
2. Implement methods to add, delete, and search contacts using a hash map.
3. Test the system's efficiency with a dataset of 1000+ contacts.

---

Exercise 2: Subject: Pathfinding with A*, Difficulty: hard, Skills: A*

Description:
In this exercise, students will implement the A* algorithm to find the shortest path in a grid-based map, a common challenge in game development and robotics.

Objective:
- Develop an understanding of A* and heuristic-based search.
- Implement the algorithm to solve dynamic pathfinding problems.

Code Snippet:
```java
PriorityQueue<Node> openSet = new PriorityQueue<>(new NodeComparator());
Set<Node> closedSet = new HashSet<>();
// Initialize start and goal nodes
Node start = new Node(startX, startY);
Node goal = new Node(goalX, goalY);
// Add start node to open set
openSet.add(start);
```

Task Breakdown:
1. Define the `Node` class and create a heuristic function.
2. Implement the A* algorithm to explore paths and update scores.
3. Adjust the heuristic for different scenarios, such as weighted terrains.