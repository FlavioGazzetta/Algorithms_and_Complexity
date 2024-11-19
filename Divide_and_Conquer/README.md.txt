# Majority Element Finder

This Python program implements an algorithm to find the **majority element** in an array. A majority element is an element that appears more than \( n/2 \) times in the array, where \( n \) is the length of the array. If no such element exists, the program returns `-1`.

---

## How It Works

The algorithm iterates through the array, counting occurrences of each element. If an element's count exceeds \( n/2 \), it is returned as the majority element. Otherwise, the function returns `-1`.

### **Core Algorithm**
1. For each element in the array:
   - Count how many times it appears in the array.
2. If an element's count exceeds \( n/2 \):
   - Return that element as the majority element.
3. If no element satisfies this condition:
   - Return `-1`.

---

## Example Usage

### **Input**
```python
x1 = [1, 2, 3, 4, 3, 2, 2, 2, 2, 2, 2, 3, 2, 1, 2, 3]
x2 = [8, 9, 10, 10]
