# Create a frozen set named frozen_set containing elements "hello", "world".
frozen_set = frozenset({'hello', 'world'})

# Try to add "!" to frozen_set. What happens?
frozen_set.add('!')

# Create a normal set named normal_set containing elements "let's", "learn".
normal_set = {"let's", "learn"}

# Try to add frozen_set to normal_set. Why does it work? Explain.
normal_set = normal_set.add(frozen_set)

# Prin[dictionary_examples.py](collections%2Fdictionary_examples.py)t normal_set.
print(normal_set)