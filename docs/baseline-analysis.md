# Baseline Analysis: Parrot Refactoring Kata (Python)

Group 5. Refactoring focus: Replace Type Code with Polymorphism.

## Code smells and planned refactorings
| # | Code smell | Location | Fowler refactoring | Branch |
|---|------------|----------|--------------------|--------|
| 1 | Magic numbers (12.0, 9.0, 24.0) | `_base_speed`, `_load_factor`, `_compute_base_speed_for_voltage` | Replace Magic Number with Symbolic Constant | refactor/extract-constants |
| 2 | Unclear names; needless list inside `min([...])` | `type_of_parrot`, `_compute_base_speed_for_voltage` | Rename Method/Variable; Simplify Expression | refactor/rename-and-cleanup |
| 3 | Callers must know the type code; unknown type silently returns `None` | `Parrot(...)` constructor | Introduce Factory Method (with explicit error) | refactor/factory-method |
| 4 | Type-code `match` repeated in `speed()` and `cry()`; adding a type edits every method (Open/Closed violation) | `speed()`, `cry()` | Replace Type Code with Subclasses; Replace Conditional with Polymorphism | refactor/polymorphism |
| 5 | Fields used by only one type (`number_of_coconuts`, `voltage`, `nailed`) | `__init__` | Push Down Field | refactor/push-down-fields |

## Characterization tests
`Python/test_parrot.py` (kata) and `Python/test_characterization.py` (ours) cover `speed()`
and `cry()` for every parrot type and boundary values. All 25 tests pass on the legacy code
and must pass after every refactoring.

## Target design
See `design-model.png`: abstract `Parrot` with `EuropeanParrot`, `AfricanParrot` and
`NorwegianBlueParrot` subclasses, created by a `create_parrot()` factory.