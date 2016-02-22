![alt text](https://travis-ci.org/andela-aomondi/amity-roomalloc.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/andela-aomondi/amity-roomalloc/badge.svg?branch=develop)](https://coveralls.io/github/andela-aomondi/amity-roomalloc?branch=develop)

# AMITY ROOM ALLOCATION SYSTEM

This is a system created to allocate rooms randomly for Andela's
Amity Campus. 

### Running the code
1. Open your terminal
2. Run `git clone https://github.com/andela-aomondi/amity-roomalloc.git`
3. `cd` into `amity-roomalloc`
4. Run `pip install -r requirements.txt` to install all dependencies.
5. Run `python populate.py` to create the database
6. Run `python allocate.py allocate test.txt` to allocate rooms using the sample file.
7. Run `python allocate.py get allocations` to see a list of all the allocations in the database.
8. Run `python allocate.py print allocations` to print all allocations to text file `allocations.txt`
9. Run `python allocate.py print allocations <roomname>` to show the members of a given room on screen
10. To depopulate the system, run `python allocate.py depopulate`

### Running Tests
Run command `nosetests` in the project root folder