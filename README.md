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

### Skipping tests

`unittest` provides a mechanism for skipping tests, conditionally or
unconditionally.

It uses the following decorators for implementing the skipping
mechanism:

-  `unittest.skip(reason)`: Unconditionally skips the
decorated test. reason should describe why the test is
being skipped.
- `unittest.skipIf(condition, reason)`: Skips the
decorated test if condition is true.
- `unittest.skipUnless(condition, reason)`: Skips the
decorated test unless condition is true.
- `unittest.expectedFailure()`: Marks the test as an
expected failure. If the test fails when it runs, the test is
not counted as a failure.

### assertRaises()

The `assertRaises()` method is used to check if the code block raises the
exception mentioned in assertRaises(). If the code raises the exception
then the test passes; otherwise, it fails. 
