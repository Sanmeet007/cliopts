# Cliargs Library

The Cliargs Library is a Python library designed to simplify the process of parsing command line arguments. It provides a straightforward and intuitive API, reducing the amount of code required for cli argument parsing.

## Installation

To install the Cliargs Library, run the following command in your terminal (cmd, bash, powershell, etc.):

```bash
pip install cliargs
```

## Usage

To use the library in your code, follow these steps:

1. Import the `CliArguments` class from the `cliargs` module:

   ```python
   from cliargs import CliArguments
   ```

2. Create an instance of `CliArguments` and pass a list of argument names as a parameter:

   ```python
   args = CliArguments(["options"])
   ```

3. Access the parsed command line arguments as a dictionary using the `todict()` method:

   ```python
   print(args.todict())
   ```

   The `todict()` method returns a dictionary containing the parsed arguments.

4. Run your Python script and pass command line arguments using the specified options:

   ```bash
   py test.py --filename="filename"
   py test.py -f filename
   py test.py --f="filename"
   ```

   Replace `test.py` with the name of your script file and `filename` with the desired value for the argument.

### Example

Let's consider an example to illustrate how to use the Cliargs Library. Suppose we are creating a Python script that takes a filename as input from the command line.

In `script.py` file:

```python
from cliargs import CliArguments

# Define the desired arguments: filepath, count, boolean
args = CliArguments(["filepath", "count", "boolean"]) 

print(args.todict())
```

In the command line:

```bash
py script.py -f '/files/filename.txt' -c 5 -b True 
```

The output of `args.todict()` will be:

```python
{
    "filepath": "/files/filename.txt",
    "count" : 5,
    "boolean": True
}
```

## Attach Version

If you want your script to return a version number when prompted with `--version`, you can easily achieve that by passing a version string as the second parameter when creating an instance of `CliArguments`.

Example in `script.py` file:

```python
from cliargs import CliArguments

args = CliArguments(["options"], "v1.0.0")
```

You can now check the script version using the following command:

```bash
py script.py --version
```

The output will be `v1.0.0`, matching the second parameter.

## Attach Help Function

If you want your script to run a help program  when prompted with `--help`, you can easily achieve that by passing a help_function , callable as the third parameter when creating an instance of `CliArguments`.

Example in `script.py` file:

```python
from cliargs import CliArguments

def help_function(): 
   print("HELP STRING")

args = CliArguments(["options"], "v1.0.0"  , help_function)
```

You can now run a help function using the following command:

```bash
py script.py --help
```

The output will be `HELP STRING`, matching the output of function passed as third parameter.

## Contact the Developer

For any inquiries or assistance, you can contact the developer at <ssanmeet123@gmail.com>. Feel free to reach out with any questions or feedback you may have.
