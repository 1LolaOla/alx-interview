#!/usr/bin/python3

def canUnlockAll(boxes):
    if not isinstance(boxes, list):
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    queue = [0]  # Start with the first box

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]
        for key in keys:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

# Example usage
if __name__ == "__main__":
    boxes = [[1], [2], [3], []]
    print(canUnlockAll(boxes))  # Output: True
