# Unit Testing in Python

This project contains two main packages: `mypackage` for development code and `test` for testing code.

## Coding Conventions for `unittest`

To enable automatic test discovery in your project directory, it is essential to follow specific coding and naming conventions for your test code. The examples in this book consistently adhere to these conventions.

### Key Conventions

- **Test File Structure**: All test files must be either modules or packages that can be imported from the project's top-level directory.
- **Starting Point**: Test discovery begins from the current directory by default.
- **Filename Pattern**: By default, test discovery looks for files matching the pattern `test*.py`.

### Common Assertions

Here’s a summary of the most commonly used assertions in the `unittest` framework along with their purposes:

| Method                        | Checks That                     |
|-------------------------------|----------------------------------|
| `assertEqual(a, b)`          | `a == b`                        |
| `assertNotEqual(a, b)`       | `a != b`                        |
| `assertTrue(x)`              | `bool(x) is True`              |
| `assertFalse(x)`             | `bool(x) is False`             |
| `assertIs(a, b)`             | `a is b`                       |
| `assertIsNot(a, b)`          | `a is not b`                   |
| `assertIsNone(x)`            | `x is None`                    |
| `assertIsNotNone(x)`         | `x is not None`                |
| `assertIn(a, b)`             | `a in b`                       |
| `assertNotIn(a, b)`          | `a not in b`                   |
| `assertIsInstance(a, b)`     | `isinstance(a, b)`             |
| `assertNotIsInstance(a, b)`  | `not isinstance(a, b)`         |
| `assertAlmostEqual(a, b)`    | `round(a-b, 7) == 0`           |
| `assertNotAlmostEqual(a, b)`  | `round(a-b, 7) != 0`           |
| `assertGreater(a, b)`        | `a > b`                        |
| `assertGreaterEqual(a, b)`   | `a >= b`                       |
| `assertLess(a, b)`           | `a < b`                        |
| `assertLessEqual(a, b)`      | `a <= b`                       |
| `assertRegexpMatches(s, r)`   | `r.search(s)`                  |
| `assertNotRegexpMatches(s, r)`| `not r.search(s)`              |
| `assertItemsEqual(a, b)`     | `sorted(a) == sorted(b)`       |
| `assertDictContainsSubset(a, b)`| All key/value pairs in `a` exist in `b`|

### Comparison Methods

These methods are used to compare various types of data structures:

| Method                          | Used to Compare   |
|----------------------------------|------------------|
| `assertMultiLineEqual(a, b)`    | Strings          |
| `assertSequenceEqual(a, b)`      | Sequences        |
| `assertListEqual(a, b)`          | Lists            |
| `assertTupleEqual(a, b)`         | Tuples           |
| `assertSetEqual(a, b)`           | Sets or frozensets|
| `assertDictEqual(a, b)`          | Dictionaries     |

---
