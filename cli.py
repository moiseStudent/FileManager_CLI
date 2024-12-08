#!/usr/bin/env python3

import click
import os
from fileManager import FileManager

fm = FileManager()

### Command Group
@click.group()
def cli():
    """
    .:File Manager v0:.
    """
    pass

@cli.command()
@click.option('--path', required=True, help='Directory path to organize files by their extensions.')
def sortfiles(path):
    """Organize files by their extensions."""
    click.echo(fm.organize_files(path))

if __name__ == '__main__':
    cli()

"""
* shebang agregado para ejecutar con python3
* Formas de ejecutar el Script CLI, asegurate de tener instalado click
* >>> python3 cli.py [Funcion] --[parametro] valor_del_parametro
* >>> python3 cli.py despedir --nombre moises
* >>> Adiós, moises!

"""