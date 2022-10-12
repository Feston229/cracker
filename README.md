# Simple sha256 cracking tool

A simple python script that will try to get key for given sha256 hash


## Getting Started

These instructions will get you a copy of the project up and running on your local machine

### Usage

Clone the repository
```
git clone https://github.com/Feston229/cracker.git
```

Navigate into the `cracker` directory
```
cd cracker
```

Install dependensies
```
pipenv install
```

Run the script
```
python3 cracker.py -s d339f720de1fd92a672df9ef19a8cdbda6171cbf33fcd35ad95c46f8aebaf628 -l 4 -a ln
```
The program can accept a number of command line arguments:
```
$ python3 cracker.py --help
usage: cracker.py [-h] -s HASH -l LENGTH [-a {l,n,u,ln,un,lu,lun}] [-f FIRST]

Multiprocessing tool for cracking sha256 hash

options:
  -h, --help            show this help message and exit
  -s HASH, --hash HASH  sha256 raw hash
  -l LENGTH, --length LENGTH
                        length of plain text
  -a {l,n,u,ln,un,lu,lun}, --alpha {l,n,u,ln,un,lu,lun}
                        alphabet for cracking: l -> letters lowercase n -> numbers u -> letters uppercase ln ->
                        lowercase + numbers un -> uppercase + numbers lu -> lowercase + uppercase lun -> lowercase
                        + uppercase + numbers default -> ln
  -f FIRST, --first FIRST
                        first letters
```
only hash and length are required

###  Output
```
$ python3 cracker.py -s d339f720de1fd92a672df9ef19a8cdbda6171cbf33fcd35ad95c46f8aebaf628 -l 4 -a ln
Iterating...
Found key -> lora
```


## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details