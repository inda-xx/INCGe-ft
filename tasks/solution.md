# Solution

Sure, let's break down the solution for both tasks provided:

### Exercise 1: Building a Contact Management System

In this task, you'll build a simple contact management system using Java's `HashMap` for efficient contact storage, retrieval, and management. Here's how you can proceed:

#### Step-by-step Solution

1. **Define the `Contact` class:**
   - The `Contact` class should hold relevant contact information such as name, phone number, and optionally, email.

```java
public class Contact {
    private String name;
    private String phoneNumber;
    private String email;

    public Contact(String name, String phoneNumber, String email) {
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.email = email;
    }

    // Getters and setters
    public String getName() {
        return name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public String getEmail() {
        return email;
    }
    
    @Override
    public String toString() {
        return "Name: " + name + ", Phone: " + phoneNumber + ", Email: " + email;
    }
}
```

2. **Implement Contact Management System:**
   - Use a `HashMap` to store `Contact` objects with the contact's name as the key.

```java
import java.util.HashMap;
import java.util.Map;

public class ContactManagementSystem {
    private Map<String, Contact> contactMap;

    public ContactManagementSystem() {
        contactMap = new HashMap<>();
    }

    // Add a new contact
    public void addContact(Contact contact) {
        contactMap.put(contact.getName(), contact);
    }

    // Delete a contact
    public void deleteContact(String name) {
        contactMap.remove(name);
    }

    // Search for a contact
    public Contact searchContact(String name) {
        return contactMap.get(name);
    }

    // Display all contacts
    public void displayContacts() {
        for (Contact contact : contactMap.values()) {
            System.out.println(contact);
        }
    }

    // Test method with sample data
    public static void main(String[] args) {
        ContactManagementSystem cms = new ContactManagementSystem();
        cms.addContact(new Contact("John Doe", "123-456-7890", "john@example.com"));
        cms.addContact(new Contact("Jane Smith", "987-654-3210", "jane@example.com"));

        System.out.println("Search for John Doe: " + cms.searchContact("John Doe"));
        
        cms.displayContacts();

        cms.deleteContact("John Doe");
        cms.displayContacts();
    }
}
```

3. **Testing the System:**
   - Test with a large dataset by including additional methods to generate bulk test contacts and measure performance metrics if required.

### Exercise 2: Pathfinding with A*

For the second exercise, you'll implement the A* pathfinding algorithm, often used in games and robotics for finding the shortest path efficiently.

#### Step-by-step Solution

1. **Define the `Node` class:**
   - This class should contain fields for coordinates, costs, and links to parent nodes.

```java
import java.util.Objects;

public class Node {
    private int x;
    private int y;
    private int gCost; // Cost from start to current node
    private int hCost; // Heuristic cost from current node to goal
    private Node parent;

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getFCost() {
        return gCost + hCost;
    }

    // Getters, setters, hashCode, equals, etc.
    public void setGCost(int gCost) {
        this.gCost = gCost;
    }

    public void setHCost(int hCost) {
        this.hCost = hCost;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void setParent(Node parent) {
        this.parent = parent;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Node)) return false;
        Node node = (Node) obj;
        return x == node.x && y == node.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}
```

2. **Implement the A* Algorithm:**

```java
import java.util.*;

public class AStarPathfinding {
    private static final int[][] DIRECTIONS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    private static int calculateHeuristic(Node start, Node goal) {
        // Using Manhattan distance as the heuristic
        return Math.abs(start.getX() - goal.getX()) + Math.abs(start.getY() - goal.getY());
    }

    public static List<Node> findPath(Node start, Node goal, int[][] grid) {
        PriorityQueue<Node> openSet = new PriorityQueue<>(Comparator.comparingInt(Node::getFCost));
        Set<Node> closedSet = new HashSet<>();

        start.setGCost(0);
        start.setHCost(calculateHeuristic(start, goal));
        openSet.add(start);

        while (!openSet.isEmpty()) {
            Node current = openSet.poll();

            if (current.equals(goal)) {
                return reconstructPath(current);
            }

            closedSet.add(current);

            for (int[] direction : DIRECTIONS) {
                Node neighbor = new Node(current.getX() + direction[0], current.getY() + direction[1]);

                if (isInBounds(neighbor, grid) && !isBlocked(neighbor, grid) && !closedSet.contains(neighbor)) {
                    int tentativeGCost = current.getFCost() + 1; // Assume each move costs 1

                    if (tentativeGCost < neighbor.getFCost() || !openSet.contains(neighbor)) {
                        neighbor.setGCost(tentativeGCost);
                        neighbor.setHCost(calculateHeuristic(neighbor, goal));
                        neighbor.setParent(current);

                        if (!openSet.contains(neighbor)) {
                            openSet.add(neighbor);
                        }
                    }
                }
            }
        }

        return new ArrayList<>(); // No path found
    }

    private static List<Node> reconstructPath(Node node) {
        List<Node> path = new ArrayList<>();
        while (node != null) {
            path.add(node);
            node = node.parent;
        }
        Collections.reverse(path);
        return path;
    }

    private static boolean isInBounds(Node node, int[][] grid) {
        return node.getX() >= 0 && node.getX() < grid.length && node.getY() >= 0 && node.getY() < grid[0].length;
    }

    private static boolean isBlocked(Node node, int[][] grid) {
        return grid[node.getX()][node.getY()] == 1; // Assuming 1 represents an obstacle
    }
}
```

3. **Testing A* Pathfinding:**

   - You can test this algorithm by setting up a grid with obstacles and trying to find paths for different start and goal positions.
   - Ensure to modify heuristic calculations for diverse scenarios, like weighted terrain.

By delivering these implementations, students will gain comprehensive skills in using hash maps for efficient data management and implementing the popular A* algorithm for smart pathfinding.