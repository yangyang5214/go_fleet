> 回文数 https://leetcode-cn.com/problems/palindrome-number/

### 字符串

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        length = len(s)
        for index in range(length // 2):
            if s[index] != s[length - index - 1]:
                return False
        return True
```

### 反转一半

```python

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数
        if x < 0:
            return False
        # 特殊处理
        if x == 0:
            return True
        # 以 0 结尾
        if x % 10 == 0:
            return False
        r = 0
        while True:
            temp = x % 10
            r = r * 10 + temp
            x = x // 10
            # len(x) 是奇数的情况，多算一步
            if x <= r:
                break
        # r // 10 == x 奇数的情况
        return r == x or r // 10 == x
```



