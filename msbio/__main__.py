import time
import msbio
import click
import pprint
from rich.console import Console

# ! Console
console = Console()

# ! Other Methods
def log(chap: str, chap_style: str, msg: str) -> None:
    console.print(f"\[[{chap_style}]{chap.upper().center(8)}[/{chap_style}]]: {msg}")

def info(msg: str):
    log("info", "green", msg)

# ! Main Method
def main(
    from_filepath: str,
    to_filepath: str,
    type_checking: bool
) -> None:
    with open(from_filepath, "rb") as file:
        start_load_time = time.time()
        data = msbio.load(file)
        end_load_time = time.time()
    info(f"[#5f00ff]Load time[/#5f00ff] > {round(end_load_time-start_load_time, 3)} [yellow]second(s)[/yellow]")
    info(f"Type checking is {'[green]enabled[/green]' if type_checking else '[red]disabled[/red]'}.")
    with open(to_filepath, "wb") as file:
        start_dump_time = time.time()
        msbio.dump(data, file, type_checking=type_checking)
        end_dump_time = time.time()
    info(f"[#5f00ff]Dump time[/#5f00ff] > {round(end_dump_time-start_dump_time, 3)} [yellow]second(s)[/yellow]")
    info("Writing 'log.txt'...")
    with open("log.txt", "wb") as file:
        file.write(pprint.pformat(data).encode())
    info("Done!")

# ! CLI Main Method
@click.command
@click.argument(
    "from_filepath", type=click.Path(True, True, False)
)
@click.argument(
    "to_filepath", type=click.Path(False, True, False)
)
@click.option(
    "--no-type-cheking", "-ntp", "type_checking",
    is_flag=True, default=True,
    help="Disabling type checking before writing."
)
def cli_main(from_filepath: str, to_filepath: str, type_checking: bool):
    try:
        main(from_filepath, to_filepath, type_checking)
    except:
        console.print_exception(word_wrap=True, show_locals=True)

# ! Start
if __name__ == "__main__":
    cli_main()