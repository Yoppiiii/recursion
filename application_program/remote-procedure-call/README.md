# Remote Procedure Call

## server.py

```bash
❯ python3 server.py
❯ Server is listening on port 8000...
❯ {'method': 'floor', 'params': [3.9], 'param_types': ['int'], 'id': 1}
```

## client.js

```bash
❯ node client.js
❯ Server is listening on port 8000...
❯　method:floor
❯ params:3.9
❯ { result: 3, result_type: [ 'int' ], id: 1 }
```

## List of methods
・floor(double x): Takes a decimal number x as input and rounds it down to the nearest integer, and returns the result as an integer.<br>
・nroot(int n, int x): Calculates the value of r in the equation rn = x.<br>
・reverse(string s): Takes a string s as input and returns a new string that is the reverse of the input string.<br>
・validAnagram(string str1, string str2): Takes two strings as input and returns a boolean value indicating whether the two input strings are anagrams of each other.<br>
・sort(string[] strArr): Takes an array of strings as input, sorts the array, and returns the sorted array of strings.<br>
