# Cuenca Challenge Instructions

Here's the programming problem: https://en.wikipedia.org/wiki/Eight_queens_puzzle

These are the different aspect of the project you can work on (in order):
1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens
2. iterate over N and store the solutions in postgres using SQLAlchemy
3. write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest
4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)
5. setup Travis CI (or similar) for your public GitHub repo to run the tests automatically

You don't need to go through all of the steps, but there should be instructions on how I can run the code. I mainly want to see how you approach a problem and your coding style. There are multiple steps so you have the option to show me different skills. It's up to you.

Please commit everything in a public GitHub repo and use python3.

You can borrow from an existing solution—except for Google's. If you borrow from someone else's code, please cite where you got the code and be ready to explain how the code works.

## Instalation

Install python library dependencies with `pip3` using the requirements file.

	$ pip3 install -r requirements.txt

## Generate and edit the configuration file

Configure your database access

	$ cp challenge.conf
	$ nano challenge.conf
	  postgresql:
       host: 127.0.0.1
       port: 5432
       name: name_db
       user: user1
       password: passwd

# Use the code n-queens to see the solutions by entering a number of Queens

Run the script `python3 run.py --help`

```
usage: run.py [-h] [-q QUEENS]

optional arguments:
  -h, --help            show this help message and exit
  -q QUEENS, --queens QUEENS
                        number of queens

```

# Test

Run the script to check tests:

	$ pytest test_n_queens.py

I coloqued three tests, one that does not pass the test and the other two that do

# Deployment as container

The project can be used within a container.

Run the bash script:

	$ ./deploy.sh

Run the following command:

	$ docker run --rm -it  ubuntu:20.04

To configure database and user may use the commands next:

	$ su - postgres
	$ service postgresql restart
	$ createdb cuenca
	$ psql
	$ ALTER USER postgres WITH PASSWORD '123456';
	$ \q
	$ exit

Then we are located in the folder challenge and run the next command:

	$ python3 run.py -q <number_of_queens>

When executing this command, when passing a number of queens, the value is stored in the solutions_n_queens table that will be created in the `cuenca` database when executing the script

## Challenge Solution by

* **José Nicolielly** - - [jcnil](https://github.com/jcnil/ChallengeCuenca)

