"""
Algorithms and Data Structures in Python
========================================
Common algorithms and data structure implementations
"""

# Searching Algorithms
print("=== Searching Algorithms ===")

def linear_search(arr, target):
    """Linear search algorithm - O(n)"""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    """Binary search algorithm - O(log n) - requires sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test searching algorithms
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11

linear_result = linear_search(numbers, target)
binary_result = binary_search(numbers, target)

print(f"Array: {numbers}")
print(f"Target: {target}")
print(f"Linear search result: index {linear_result}")
print(f"Binary search result: index {binary_result}")

# Sorting Algorithms
print("\n=== Sorting Algorithms ===")

def bubble_sort(arr):
    """Bubble sort algorithm - O(n²)"""
    arr = arr.copy()  # Don't modify original
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Optimization: if no swaps, array is sorted
            break
    
    return arr

def selection_sort(arr):
    """Selection sort algorithm - O(n²)"""
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def insertion_sort(arr):
    """Insertion sort algorithm - O(n²)"""
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def merge_sort(arr):
    """Merge sort algorithm - O(n log n)"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    """Quick sort algorithm - O(n log n) average case"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Test sorting algorithms
unsorted = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
print(f"Original array: {unsorted}")
print(f"Bubble sort: {bubble_sort(unsorted)}")
print(f"Selection sort: {selection_sort(unsorted)}")
print(f"Insertion sort: {insertion_sort(unsorted)}")
print(f"Merge sort: {merge_sort(unsorted)}")
print(f"Quick sort: {quick_sort(unsorted)}")

# Stack Implementation
print("\n=== Stack Data Structure ===")

class Stack:
    """Stack implementation using list"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get stack size"""
        return len(self.items)
    
    def __str__(self):
        return f"Stack({self.items})"

# Test stack
stack = Stack()
print(f"Initial stack: {stack}")
print(f"Is empty: {stack.is_empty()}")

for i in [1, 2, 3, 4, 5]:
    stack.push(i)
    print(f"Pushed {i}: {stack}")

print(f"Peek: {stack.peek()}")
print(f"Size: {stack.size()}")

while not stack.is_empty():
    item = stack.pop()
    print(f"Popped {item}: {stack}")

# Queue Implementation
print("\n=== Queue Data Structure ===")

class Queue:
    """Queue implementation using list"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def front(self):
        """Return front item without removing"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get queue size"""
        return len(self.items)
    
    def __str__(self):
        return f"Queue({self.items})"

# Test queue
queue = Queue()
print(f"Initial queue: {queue}")

for item in ['A', 'B', 'C', 'D']:
    queue.enqueue(item)
    print(f"Enqueued {item}: {queue}")

print(f"Front: {queue.front()}")

while not queue.is_empty():
    item = queue.dequeue()
    print(f"Dequeued {item}: {queue}")

# Linked List Implementation
print("\n=== Linked List Data Structure ===")

class Node:
    """Node for linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Singly linked list implementation"""
    
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add element to end of list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Add element to beginning of list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """Delete first occurrence of data"""
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def find(self, data):
        """Find element in list"""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def size(self):
        """Get list size"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def display(self):
        """Display list elements"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Test linked list
ll = LinkedList()
print(f"Initial list: {ll.display()}")

for item in [1, 2, 3, 4, 5]:
    ll.append(item)
print(f"After appends: {ll.display()}")

ll.prepend(0)
print(f"After prepend 0: {ll.display()}")

print(f"Find 3: position {ll.find(3)}")
print(f"Find 10: position {ll.find(10)}")

ll.delete(3)
print(f"After delete 3: {ll.display()}")
print(f"List size: {ll.size()}")

# Binary Tree Implementation
print("\n=== Binary Tree Data Structure ===")

class TreeNode:
    """Node for binary tree"""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """Binary tree implementation"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """Insert data into binary search tree"""
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Helper method for insertion"""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def inorder_traversal(self):
        """In-order traversal (left, root, right)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for in-order traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Pre-order traversal (root, left, right)"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Helper method for pre-order traversal"""
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """Post-order traversal (left, right, root)"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Helper method for post-order traversal"""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
    
    def search(self, data):
        """Search for data in tree"""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Helper method for search"""
        if not node:
            return False
        
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

# Test binary tree
bt = BinaryTree()
values = [50, 30, 70, 20, 40, 60, 80]

for val in values:
    bt.insert(val)

print(f"Inserted values: {values}")
print(f"In-order traversal: {bt.inorder_traversal()}")
print(f"Pre-order traversal: {bt.preorder_traversal()}")
print(f"Post-order traversal: {bt.postorder_traversal()}")
print(f"Search for 40: {bt.search(40)}")
print(f"Search for 100: {bt.search(100)}")

# Hash Table Implementation
print("\n=== Hash Table Data Structure ===")

class HashTable:
    """Simple hash table implementation using chaining"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        """Simple hash function"""
        return hash(key) % self.size
    
    def put(self, key, value):
        """Insert key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return
        
        # Add new key-value pair
        bucket.append((key, value))
    
    def get(self, key):
        """Get value by key"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def keys(self):
        """Get all keys"""
        all_keys = []
        for bucket in self.table:
            for key, _ in bucket:
                all_keys.append(key)
        return all_keys
    
    def values(self):
        """Get all values"""
        all_values = []
        for bucket in self.table:
            for _, value in bucket:
                all_values.append(value)
        return all_values
    
    def display(self):
        """Display hash table contents"""
        result = {}
        for bucket in self.table:
            for key, value in bucket:
                result[key] = value
        return result

# Test hash table
ht = HashTable(5)

# Insert some data
data = [('apple', 5), ('banana', 3), ('orange', 8), ('grape', 12), ('kiwi', 7)]

for key, value in data:
    ht.put(key, value)

print(f"Hash table contents: {ht.display()}")
print(f"Get 'banana': {ht.get('banana')}")
print(f"All keys: {ht.keys()}")
print(f"All values: {ht.values()}")

ht.put('apple', 10)  # Update existing
print(f"After updating apple: {ht.display()}")

deleted_value = ht.delete('orange')
print(f"Deleted 'orange' (value: {deleted_value}): {ht.display()}")

# Graph Implementation
print("\n=== Graph Data Structure ===")

class Graph:
    """Graph implementation using adjacency list"""
    
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edge(self, from_vertex, to_vertex):
        """Add an edge between vertices"""
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        
        self.vertices[from_vertex].append(to_vertex)
    
    def get_vertices(self):
        """Get all vertices"""
        return list(self.vertices.keys())
    
    def get_edges(self, vertex):
        """Get edges from a vertex"""
        return self.vertices.get(vertex, [])
    
    def bfs(self, start_vertex):
        """Breadth-first search"""
        visited = set()
        queue = [start_vertex]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add unvisited neighbors to queue
                for neighbor in self.vertices.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    def dfs(self, start_vertex):
        """Depth-first search"""
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                for neighbor in self.vertices.get(vertex, []):
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_vertex)
        return result
    
    def display(self):
        """Display graph"""
        for vertex, edges in self.vertices.items():
            print(f"  {vertex} -> {edges}")

# Test graph
graph = Graph()

# Add vertices and edges
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('C', 'E')]

for from_v, to_v in edges:
    graph.add_edge(from_v, to_v)

print("Graph structure:")
graph.display()

print(f"BFS from A: {graph.bfs('A')}")
print(f"DFS from A: {graph.dfs('A')}")

print("\nAlgorithms and Data Structures demonstration complete!")