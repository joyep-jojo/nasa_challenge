# SDET-test

## Instructions
1. Install libraries using `pip install -r requirements.txt`
2. Run command `pytest -n 4 --capture=tee-sys` (this will execute the 4 tests in differents threads)
3. Check `pytest_html_report.html`

![alt text](example-report.JPG)
[example_report](https://joyep-jojo.github.io/nasa_challenge/report/pytest_html_report.html#dashboard)

*Notes*

* You can also create a virtual env and follow the same steps
* Time spent: 5 hours
## Challenge
Create pilot Java test framework for testing NASA's open API.

NASA has an open API: https://api.nasa.gov/index.html#getting-started. It grants access to different features e.g: Astronomy Picture of the Day, Mars Rover Photos, etc.

We would like to test different scenarios that the API offers:
1. Retrieve the first 10 Mars photos made by "Curiosity" on 1000 Martian sol.
2. Retrieve the first 10 Mars photos made by "Curiosity" on Earth date equal to 1000 Martian sol.
3. Retrieve and compare the first 10 Mars photos made by "Curiosity" on 1000 sol and on Earth date equal to 1000 Martian sol.
4. Validate that the amounts of pictures that each "Curiosity" camera took on 1000 Mars sol is not greater than 10 times the amount taken by other cameras on the same date.

## Instructions
You will need to fork the repository and build the solution in Github **publicly**. Once you are finished, let HR know and share a link to your fork or a Zip file with your solution and the URL of the repository.

Implementation deadline is 3 days. Please let us know the time that you spent to achieve the task.


