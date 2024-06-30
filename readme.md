# Cliopts Library

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cliopts)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cliopts)

The Cliopts Library is a Python library designed to simplify the process of parsing command-line arguments. It provides a straightforward and intuitive API, reducing the amount of code required for CLI argument parsing.

## Installation

To install the Cliopts Library, run the following command in your terminal (cmd, bash, PowerShell, etc.):

```bash
pip install cliopts
```

## Usage

To use the library in your code, follow these steps:

1. Import the `CliArguments` class from the `cliopts` module:

   ```python
   from cliopts import CliArguments
   ```

2. Create an instance of `CliArguments` and pass a list of argument names or a dictionary of argument names and their shorthand notations, along with optional parameters such as `options_desc` and `version`.

   Using a list of options:

   ```python
   args = CliArguments(
       options=["filename", "count", "verbose"],
       options_desc={
           "filename": "Specify the filename",
           "count": "Specify the count",
           "verbose": "Enable verbose output"
       },
       version="v1.0.0"
   )
   ```

   Using a dictionary of options with shorthand notations:

   ```python
   args = CliArguments(
       options={
           "filename": "f",
           "count": "c",
           "verbose": "v"
       },
       options_desc={
           "filename": "Specify the filename",
           "count": "Specify the count",
           "verbose": "Enable verbose output"
       },
       version="v1.0.0"
   )
   ```

3. Access the parsed command-line arguments as a dictionary using the `to_dict()` method:

   ```python
   print(args.to_dict())
   ```

   The `to_dict()` method returns a dictionary containing the parsed arguments.

4. Run your Python script and pass command-line arguments using the specified options and their shorthand notations:

   ```bash
   py test.py --filename="filename.txt" --count=5 --verbose=True
   py test.py -f "filename.txt" -c 5 -v True
   ```

   Replace `test.py` with the name of your script file and `filename.txt` with the desired value for the argument.

### Example

Let's consider an example to illustrate how to use the Cliopts Library. Suppose we are creating a Python script that takes a filename, count, and a verbose flag as input from the command line.

In `script.py` file:

```python
from cliopts import CliArguments

# Define the desired arguments: filename, count, verbose
args = CliArguments(
    options={
        "filename": "f",
        "count": "c",
        "verbose": "v"
    },
    options_desc={
        "filename": "Specify the filename",
        "count": "Specify the count",
        "verbose": "Enable verbose output"
    },
    version="v1.0.0"
)

print(args.to_dict())
```

In the command line:

```bash
py script.py --filename='/files/filename.txt' --count=5 --verbose=True
py script.py -f '/files/filename.txt' -c 5 -v True
```

The output of `args.to_dict()` will be:

```python
{
    "filename": "/files/filename.txt",
    "count": 5,
    "verbose": True
}
```

## CliArgument class params

### options

- **Type**: `Iterable[str] | dict[str, str]`
- **Description**: A list or dictionary of command-line options. If using a dictionary, the keys are the full option names and the values are their shorthand notations.

### options_desc

- **Type**: `dict[str, str]`
- **Optional**: Yes
- **Description**: A dictionary with descriptions for each option. Defaults to an empty dictionary.

### version

- **Type**: `str`
- **Optional**: Yes
- **Description**: The version of the program. Defaults to `None`.

### help

- **Type**: `(dict[str, str]) -> Any`
- **Optional**: Yes
- **Description**: A function to display help information. This function takes `options_desc` as its argument. If not provided, the default help function is triggered utilizing `options_desc`.

### throw_on_invalid_args

- **Type**: `bool`
- **Optional**: Yes
- **Description**: Whether to throw an error on invalid arguments. Defaults to `True`.

### name

- **Type**: `str`
- **Optional**: Yes
- **Description**: The name of the program. Defaults to `"python-program"`.

### desc

- **Type**: `str`
- **Optional**: Yes
- **Description**: The description of the program. Defaults to `None`.

## Default Help Function Output

If the `--help` flag is used, the default help function displays the following information:

```
Usage: python-program [options]

Options:
    filename : Specify the filename
    count : Specify the count
    verbose : Enable verbose output

--version : Show version
```

## Attach Version

If you want your script to return a version number when prompted with `--version`, you can easily achieve that by passing a version string as the `version` parameter when creating an instance of `CliArguments`.

Example in `script.py` file:

```python
from cliopts import CliArguments

args = CliArguments(
    options=["filename", "count", "verbose"],
    version="v1.0.0"
)
```

You can now check the script version using the following command:

```bash
py script.py --version
```

The output will be `v1.0.0`, matching the version parameter.

## Contact the Developer

For any inquiries or assistance, you can contact the developer at <ssanmeet123@gmail.com>. Feel free to reach out with any questions or feedback you may have.
