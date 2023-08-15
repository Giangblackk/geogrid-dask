"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """GeoGrid Dask."""


if __name__ == "__main__":
    main(prog_name="geogrid-dask")  # pragma: no cover
