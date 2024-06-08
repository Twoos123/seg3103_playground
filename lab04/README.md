Outline | Value
--------|-------
Course | SEG-3103
Date | June 10, 2024
Professor | Andrew Forward aforward@uottawa.ca
TA | Amirhossein Ghadami amirhossein.ghadami@uottawa.ca
Team | Asad Ali 300300354

# Commit 1: Test failure
I initiated a test with an intentionally incorrect expected value to verify its accuracy in assessing the relevant part of the code. Ensuring that the test was targeting the intended functionality was paramount.
![alt](https://user-images.githubusercontent.com/55165979/121284314-a8632f00-c8aa-11eb-928c-63344952c1f8.png)

# Commit 2: Fixed the failing test
Once I confirmed the test was appropriately aligned with the code segment under scrutiny, I corrected the expected value. This step was pivotal in ensuring the method's functionality for a 1x1 tictactoe grid was accurate.

# Comit 3: Adding more tests
In expanding the test suite, I incorporated scenarios for different grid configurations, including nx1, 1xn, and nxm grids. While executing these tests, some failures surfaced, indicating areas requiring attention.
![alt](https://user-images.githubusercontent.com/55165979/121284525-0132c780-c8ab-11eb-8bad-23f07a5f8a07.png)

# Commit 4: Fixing the method to support larger grids
Responding to the identified test failures, I proceeded to adjust the method to accommodate larger grid sizes. This adjustment aimed to ensure consistent and accurate outcomes across diverse grid dimensions.

# Commit 5+: Adding the remaining tests and refactoring the code
Expanding beyond the initial method, I extended the Tic class to encompass additional functionalities. This involved the introduction of a constructor capable of generating Tic objects based on specified or default grid dimensions. Renaming the method from emptyBoard() to toString(), I augmented the class with size() and showPositions() methods. Subsequent tests were crafted to validate these new functionalities, and the toString method was refined to align with the updated code structure.
