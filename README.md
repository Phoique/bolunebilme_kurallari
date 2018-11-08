# import
```python
import calculation as cal
```

# How to use? 
```python
number = 12
test = calculation.remainingCalculation(number)
print(test.all())
```

# What do these functions work for?
```python
number = 120
two(), # 120 => [1, 2, 0] => 0 % 2 = 0 
three(), # 120 => [1, 2, 0] => 1 + 2 + 0 = 3 => 3 % 3 = 0
four(), # 120 => [1, 2, 0] => 20 % 4 = 0
five(), # 120 => [1, 2, 0] => 0 or 5 => 0
eight(), # 120 => [1, 2, 0] => 120 % 8 => 0
nine(), # 120 => [1, 2, 0] => 1 + 2 + 0 = 3 => 3 % 3 = 3
ten(), # 120 => [1, 2, 0] => 0 => 0
eleven() # 120 => [1, 2, 0] => 1(–) 2(+) 0(–) => (2 - (1 + 0)) => 1 => 11 - 1 => 10
all() # Runs all functions
```