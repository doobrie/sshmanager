import os
import argparse
from sshhost import Host


from rich.console import Console
from rich.prompt import IntPrompt
from rich.table import Table

from sshhost import HostList


def add_host():
    print('Adding host')
    host_name = input('Host name: ')
    host_group = input('Host group: ')
    host_address = input('Host address: ')
    new_host = Host(host_group, host_name, host_address)


def parse_args():
    parser = argparse.ArgumentParser(
        prog='sshmanager', description='SSH Manager.')

    parser.add_argument('-a',
                        '--add',
                        action='store',
                        help='add a new ssh host')
    args = parser.parse_args()
    print(args.add)
    if (args.add):
        add_host()
    else:
        show_hosts()


def show_hosts():
    table = Table(title="SSH Hosts")
    host_list = HostList()
    hosts = host_list.get_hosts()

    table.add_column("Id", justify="right", style="white", no_wrap=True)
    table.add_column("Host", style="cyan", no_wrap=True)
    table.add_column("Group", style="magenta")
    table.add_column("Full Host Name", style="green")

    for host in hosts:
        table.add_row(str(host.get_id()), host.get_name(),
                      host.get_group(), host.get_fullname())

    console = Console()
    console.print(table)

    host_ids = host_list.get_host_ids()
    host_id = IntPrompt.ask("Select a host id", choices=[
        "{:0d}".format(x) for x in host_ids])

    selected_host = host_list.get_host(host_id)
    print(f'ssh {selected_host.get_address()}')
    os.system(f'ssh {selected_host.get_address()}')


if __name__ == '__main__':
    parse_args()
