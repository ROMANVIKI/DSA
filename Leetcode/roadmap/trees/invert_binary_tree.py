# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sol = []
        if not root:
            return root
        
        queue = deque([root])

        while queue:
            current = queue.popleft()

            current.left, current.right = current.right, current.left
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root
       









Here's an explanation of the code you provided to invert a binary tree. I'll walk through each part of the code, explaining the purpose and expected output at each step using a sample binary tree:

### Sample Tree
To illustrate, let’s use this binary tree as the input:

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

### Code Explanation
```python
# Import deque for efficient queue operations
from collections import deque

# Definition of the Solution class containing the invertTree method
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sol = []  # Unused variable; this does not affect the solution.

        # Step 1: Check if the root is None (an empty tree)
        if not root:
            return root
```

- **Explanation**: If the `root` is `None`, meaning the tree is empty, the function immediately returns `None`. For our example tree, `root` is not `None`, so we proceed to the next part of the code.

---

```python
        # Step 2: Initialize a queue with the root node
        queue = deque([root])
```

- **Explanation**: Here, we initialize a `deque` queue and add the root node to it. This queue will help us perform a **level-order traversal** (breadth-first search) of the tree.
- **Queue State**: `[4]`

---

```python
        # Step 3: Start a loop that will continue until the queue is empty
        while queue:
            # Step 4: Remove the current node from the left end of the queue
            current = queue.popleft()
```

- **Explanation**: We enter a loop that continues as long as the queue is not empty. The `popleft()` operation removes the node from the left end of the queue, making it the `current` node for processing.
- **Current Node**: `4`
- **Queue State After popleft()**: `[]`

---

```python
            # Step 5: Swap the left and right children of the current node
            current.left, current.right = current.right, current.left
```

- **Explanation**: We swap the left and right children of `current`. This effectively inverts the `current` node's children.
- **Effect**:
    - For `current = 4`, the left child (`2`) and right child (`7`) are swapped.
- **Tree State After Swap**:
    ```
         4
       /   \
      7     2
     / \   / \
    6   9 1   3
    ```

---

```python
            # Step 6: If the left child exists, add it to the queue
            if current.left:
                queue.append(current.left)
```

- **Explanation**: If the `current` node has a left child, we add it to the queue. After the swap, `current.left` is now `7`.
- **Queue State After Append**: `[7]`

---

```python
            # Step 7: If the right child exists, add it to the queue
            if current.right:
                queue.append(current.right)
```

- **Explanation**: If the `current` node has a right child, we add it to the queue. After the swap, `current.right` is now `2`.
- **Queue State After Append**: `[7, 2]`

---

```python
        # Loop continues, processing each node in the queue (7 and 2 in this case)
```

The loop continues for the remaining nodes (`7` and `2`) in the queue. The algorithm proceeds as follows:

1. **Process `current = 7`**:
   - Swap `7`'s children: `6` and `9` are swapped.
   - **Tree State**:
     ```
         4
       /   \
      7     2
     / \   / \
    9   6 1   3
     ```
   - **Queue State** After Appending Children: `[2, 9, 6]`

2. **Process `current = 2`**:
   - Swap `2`'s children: `1` and `3` are swapped.
   - **Tree State**:
     ```
         4
       /   \
      7     2
     / \   / \
    9   6 3   1
     ```
   - **Queue State** After Appending Children: `[9, 6, 3, 1]`

3. **Process `current = 9`, `6`, `3`, and `1`**:
   - All of these nodes are leaf nodes (they have no children), so no swaps are needed, and no additional nodes are added to the queue.

---

```python
        # Step 8: Return the root of the inverted tree
        return root
```

- **Explanation**: Once the queue is empty (indicating that all nodes have been processed and inverted), we return the root of the inverted tree.

### Final Inverted Tree
After completing all iterations, the final inverted tree looks like this:

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

### Summary
- **Input**: A binary tree represented by `root`.
- **Output**: The same tree structure with all left and right children swapped at each level.
  
This code effectively mirrors the binary tree using a level-order traversal. Each node’s children are swapped, resulting in the final inverted structure.


    
