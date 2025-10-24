# Roman to Integer

**Problem:**  
Convert a Roman numeral to an integer.  

Roman numerals are represented by the following seven symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Typically, Roman numerals are written largest to smallest from left to right. However, some numerals use **subtractive notation**:  
- I can be placed before V (5) and X (10) to make 4 and 9.  
- X can be placed before L (50) and C (100) to make 40 and 90.  
- C can be placed before D (500) and M (1000) to make 400 and 900.

**Example 1:**  
Input: s = "III"  
Output: 3  

**Example 2:**  
Input: s = "IV"  
Output: 4  

**Example 3:**  
Input: s = "LVIII"  
Output: 58  
Explanation: L = 50, V = 5, III = 3  

**Example 4:**  
Input: s = "MCMXCIV"  
Output: 1994  
Explanation: M = 1000, CM = 900, XC = 90, IV = 4

**Constraints:**  
- 1 <= s.length <= 15  
- s contains only the characters ('I','V','X','L','C','D','M')  
- It is guaranteed that s is a valid Roman numeral in the range [1, 3999]

**Link:** [LeetCode Problem 13](https://leetcode.com/problems/roman-to-integer/)
