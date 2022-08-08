# Alg Language
## General-Purpose Programming Language

### Usage
First, download Alg [here](https://alglanguage.github.io/download) and unzip it.
Then, open Command Prompt and use the command:
```
alg filename.alg
```

### Example Program
```
int a = 11;
str name = "yoo";
bool isMale = True;
int num = 10 * 10 + 10;
str full_name = name + " " + name;
str gang;

(** This is a comment in Alg **)

for int x = 0 :: > 10 :: + 1 {
    print ("Hi");
}

if a == 11 {
	print "Perfect";
	if name != "yoo" {
		print "Not good";
	}
}
```
More examples are available in the examples folder.

### Built-In Functions, Keywords, & Datatypes
```
KEYWORDS = ["function","class","if","for","else","True","False","print","bool","int","str"]
BUILT_IN_FUNCTIONS = ["print"]
DATATYPE = ["bool","int","str"]
```
Also in constants.py

### Docs
Documentation and support for Alg is available [here](https://alglanguage.github.io/docs).
