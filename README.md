# NSGA-II Implementation in Python

This python program implements the NSGA-II algorithm developed by K. Deb et.al. for any desired number of objectives, generations & parameters. Tested on all ZDT & DTLZ series problems.

## Getting Started

The program runs on both Linux & Windows. You may simply download/clone the source or use the relevant files as subroutines to your code. You may also install it as a pip package using
'''
pip3 install -e /path/pynsga-ii
'''


### Prerequisites

With a working internet connection, the above pip command will install all prerequisites automatically. The very basic requirements are matplotlib, numpy. More requirements may be added with updates.

### Using the Package

To run the optimization code from source code, follow these steps:

*  Define your objectives in the file ''' pynsga-ii/operations/evaluate.py '''
*  Open optimizer.py & define all specifications in '''main()'''
*  For proper visualization, edit the '''plot''' method (won't work for more than 2 objectives)
*  Run optimizer.py/main() target

The program generates the pareto data & plots it in case of two objectives. The results, i.e. points on the pareto are also generated in a text file in the same directory.


## Resources

* [NSGA-II](https://ieeexplore.ieee.org/document/996017/) - The Non-Dominated Sorting Genetic Algorithm


## Feedback

There's definitely a lot of work that needs to be done in this code for easier usability. I welcome suggestions & discussions by raising issues in the repo, or contacting me through neelotpalnag@gmail.com


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

