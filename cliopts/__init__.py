import getopt, sys, re
from typing import Callable
from collections.abc import Iterable


class CliArguments:

    def __init__(
        self,
        options: Iterable[str] | dict[str, str],
        options_desc: dict[str, str] = {},
        version: str = None,
        help: Callable = None,
        throw_on_invalid_args=True,
        name="python-program",
    ) -> None:
        """
        A class to handle command-line arguments for a Python program.

        Attributes:
            options (Iterable[str] | dict[str, str]): A list or dictionary of command-line options.
            options_desc (dict[str, str], optional): A dictionary with descriptions for each option. Defaults to an empty dictionary.
            version (str, optional): The version of the program. Defaults to None.
            help ((dict[str, str], optional): A function to display help information. If not provided, the default help function is triggerd using `options_desc`.
            throw_on_invalid_args (bool, optional): Whether to throw an error on invalid arguments. Defaults to True.
            name (str, optional): The name of the program. Defaults to "python-program".

        Example:
            >>> def custom_help(options_desc):
            ...     for option, desc in options_desc.items():
            ...         print(f"{option}: {desc}")

            >>> cli_args = CliArguments(
            ...     options=["foo", "bar"],
            ...     options_desc={"foo": "foo desc here", "bar": "bar desc here"},
            ...     version="1.0.0",
            ...     help=custom_help,
            ...     throw_on_invalid_args=True,
            ...     name="my-program"
            ... )
        """

        self.__options_desc = options_desc
        self.__name = name
        self.throw_on_invalid_args = throw_on_invalid_args
        if help is not None:
            self.__help = help
        else:
            self.__help = self.__default_help

        self.__version = version
        self.__OPTS = {
            k: v
            for (k, v) in zip(
                self.__build_short_opts(options),
                self.__build_long_opts(options),
            )
        }

        self.SHORT_OPTS = [x for x in self.__OPTS.keys()]
        self.LONG_OPTS = [opt + "=" for opt in self.__OPTS.values()]

    def __default_help(self, options_desc):
        print(f"Usage : {self.__name} [options]\n")
        print("Options:")
        for i, (k, v) in enumerate(self.__OPTS.items(), 1):
            print(f"\t -{k} {v} : {options_desc.get(v , f'argument {i}')}")

        print("")
        print("--version : Show version")
        print("")

    def __build_long_opts(self, opts: Iterable[str] | dict[str, str]):
        if type(opts) == dict:
            return [opt for opt in opts.keys()]

        elif hasattr(opts, "__iter__"):
            return [opt for opt in opts]

    def __build_short_opts(self, opts: Iterable[str] | dict[str, str]):
        if type(opts) == dict:
            return tuple(map(lambda x: x[0], opts.values()))

        elif hasattr(opts, "__iter__"):
            return tuple(map(lambda x: x[0], opts))

    def __get_args(self) -> dict[str, str]:
        cli_opts = {}

        try:
            if "--help" in sys.argv:
                if self.__help is not None:
                    self.__help(self.__options_desc)
                sys.exit()

            if "--version" in sys.argv:
                if self.__version is not None:
                    print(self.__version)
                sys.exit()

            cli_args = getopt.getopt(
                sys.argv[1:],
                shortopts=":".join(self.SHORT_OPTS) + ":",
                longopts=self.LONG_OPTS,
            )

        except getopt.GetoptError as cli_parse_err:
            if self.throw_on_invalid_args:
                raise InvalidOptionError(f"{cli_parse_err.args}")

        else:
            cli_opts = dict(cli_args[0])

        return cli_opts

    def __parse_types(self) -> dict[str, (str | bool | int | float)]:
        args = self.__get_args()
        args = dict(args)
        for k in args:
            current_arg = args[k]

            if type(current_arg) == str:
                if re.match(r"^-?\d+(?:\.\d+)$", current_arg) is not None:
                    args[k] = float(current_arg)
                elif current_arg.isnumeric():
                    args[k] = int(current_arg)

            elif type(current_arg) == str and (
                current_arg == "false"
                or current_arg == "true"
                or current_arg == "True"
                or current_arg == "False"
            ):
                args[k] = True if current_arg.lower() == "true" else False

        return args

    def __build_args_dict(self):
        final_dict = {}
        parsed_dict = self.__parse_types()
        keys = [
            (("-" + x), ("--" + y), ("--" + y + "="), y) for x, y in self.__OPTS.items()
        ]

        for k, v in parsed_dict.items():
            for x in keys:
                if k in x:
                    final_dict[x[3]] = v

        return final_dict

    def to_dict(self) -> dict[str, (str | int | float | bool)]:
        """
        Parses and converts the arguments passed to the Python program to a Python dictionary.

        Example:
            >>> cli_args = CliArguments(...)
            >>> args_dict = cli_args.to_dict()
        """

        if not hasattr(self, "__cached_dic"):
            self.__cached_dict = self.__build_args_dict()
        return self.__cached_dict

    @staticmethod
    def is_camel_case(s: str):
        """
        Checks if a given string is in camelCase format.

        Args:
            s (str): The string to be checked.

        Returns:
            bool: True if the string is in camelCase format, False otherwise.

        """
        return (
            re.match(
                r"^[a-z][a-z0-9]*(([A-Z][a-z0-9]+)*[A-Z]?|([a-z0-9]+[A-Z])*|[A-Z])$",
                s,
            )
            is not None
        )

    @staticmethod
    def is_pascal_case(s: str):
        """
        Checks if a given string is in PascalCase format.

        Args:
            s (str): The string to be checked.

        Returns:
            bool: True if the string is in PascalCase format, False otherwise.

        """
        return (
            re.match(
                r"^[A-Z](([a-z0-9]+[A-Z]?)*)$",
                s,
            )
            is not None
        )


class InvalidOptionError(Exception):
    pass
