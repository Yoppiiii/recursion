# File Manipulator Program

## Preparation
```bash
❯ echo this is test > testfile
❯ cat testfile

this is test
```

## reverse
```bash
❯ python3 main.py reverse testfile reversefile
❯ cat reversefile

tset si siht
```

## copy
```bash
❯ python3 main.py copy testfile copyfile
❯ cat copyfile

this is test
```

## duplicate-contents
```bash
❯ python3 main.py duplicate-contents testfile 3
❯ cat testfile

this is test
this is test
this is test
this is test
```

## replace-string
```bash
❯ python3 main.py replace-string testfile test "dog"
❯ cat testfile


this is dog
this is dog
this is dog
this is dog
```
