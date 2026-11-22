# SCD-Group-5-Refactoring: Parrot Refactoring Kata (Python)

Refactoring of the [Parrot Refactoring Kata](https://github.com/codecop/Parrot-Refactoring-Kata) (Python version).
**Refactoring focus: Replace Type Code with Polymorphism.**

The legacy `Parrot` class branches on a type code in every method. We refactor it into an abstract `Parrot`
with `EuropeanParrot`, `AfricanParrot` and `NorwegianBlueParrot` subclasses created by a `create_parrot()` factory.
External behavior is unchanged, which is verified by characterization tests that pass before and after every refactoring.

Course: Software Construction and Development (SWEN-3113), KFUEIT

## Group Members
| Name | Roll No. |
|------|----------|
| Muhammad Hassaan | <swen241101011> |
| Ahmad bin Khalid | <swen241101014> |
| Zagham Ali | <swen241101021> |
| Inzemam Nawaz | <swen241101038> |

## How to Run
```bash
cd Python
python -m venv venv
venv\Scripts\activate        # Mac/Linux: source venv/bin/activate
pip install pytest
pytest -v
```

## Project Structure
- `Python/`: refactored source and tests
- `docs/baseline-analysis.md`: code smells and chosen refactorings
- `docs/design-model.png`: target UML class diagram

## Branching Strategy
- `main`: protected, releases only (changes via pull request)
- `develop`: integration branch
- `refactor/*`: one feature branch per refactoring, merged into `develop` by pull request

## Changelog
### v1.0.0
- Extracted magic numbers into constants
- Renamed unclear identifiers and simplified expressions
- Introduced `create_parrot()` factory method
- Replaced type-code conditionals with `Parrot` subclasses (polymorphism)
- Pushed type-specific fields down into the subclasses that use them
- Added characterization tests, baseline analysis and UML design model