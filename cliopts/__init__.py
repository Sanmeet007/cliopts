import getopt, sys
from typing import Callable


class CliArguments:
    def __init__(
        self, options: list[str], version: str = None, help: Callable = None
    ) -> None:
        self.__help = help
        self.__version = version
        self.__OPTS = {x[0]: x for x in options}
        self.SHORT_OPTS = ":".join(x[0] for x in options) + ":"
        self.LONG_OPTS = [opt + "=" for opt in options]

    def __get_args(self) -> dict[str, str]:
        cli_opts = {}

        try:
            if "--help" in sys.argv:
                if self.__help is not None:
                    self.__help()
                sys.exit()

            if "--version" in sys.argv:
                if self.__version is not None:
                    print(self.__version)
                sys.exit()

            cli_args = getopt.getopt(
                sys.argv[1:],
                shortopts=self.SHORT_OPTS,
                longopts=self.LONG_OPTS,
            )

        except getopt.GetoptError as cli_parse_err:
            print("InvalidOptionError : ", str(cli_parse_err))
            sys.exit()

        else:
            cli_opts = dict(cli_args[0])

        return cli_opts

    def __get_cli_args(self):
        args = self.__get_args()
        args = dict(args)
        for k in args:
            current_arg = args[k]

            if type(current_arg) == str and current_arg.isnumeric():
                args[k] = int(current_arg)
            elif type(current_arg) == str and (
                current_arg == "false"
                or current_arg == "true"
                or current_arg == "True"
                or current_arg == "False"
            ):
                args[k] = True if current_arg.lower() == "true" else False

        return args

    def __get_full_cli_args(self):
        fdict = {}
        rdict = self.__get_cli_args()
        keys = [
            (("-" + x), ("--" + y), ("--" + y + "="), y) for x, y in self.__OPTS.items()
        ]

        for k, v in rdict.items():
            for x in keys:
                if k in x:
                    fdict[x[3]] = v

        return fdict

    def todict(self):
        return self.__get_full_cli_args()
