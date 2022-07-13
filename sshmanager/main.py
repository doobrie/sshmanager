import argparse
import os
import sys

from rich.console import Console
from rich.prompt import IntPrompt
from rich.table import Table

from sshhost import Host
from sshhost import HostList


GROUP_POSITION = 0
NAME_POSITION = 1
ADDRESS_POSITION = 2


def add_host(args):
    """ Add a new host

    Args:
        args: List(str) containig details of the new host.
              args[0] = Group Name
              args[1] = Host name
              args[2] = Host address
    """
    print(
        f'Adding host "{args[NAME_POSITION]}" to group "{args[GROUP_POSITION]}" at "{args[ADDRESS_POSITION]}"')
    new_host = Host(args[GROUP_POSITION],
                    args[NAME_POSITION], args[ADDRESS_POSITION])
    host_list = HostList()
    host_list.add_host(new_host)


def parse_args():
    """ Parse the application arguments and act accordingly by adding a host or showing all hosts.
    """
    parser = argparse.ArgumentParser(
        prog='sshmanager', description='SSH Manager.')

    parser.add_argument('-a',
                        '--add',
                        type=str,
                        nargs=3,
                        help='add a new ssh host (group name address)')
    args = parser.parse_args()
    if (args.add):
        add_host(args.add)
    else:
        show_hosts()


def show_hosts():
    """ Show the stored hosts and allow the user to select one.
    """
    table = Table(title="SSH Hosts")
    host_list = HostList()
    hosts = host_list.get_hosts()

    table.add_column("Id", justify="right", style="white", no_wrap=True)
    table.add_column("Host", style="cyan", no_wrap=True)
    table.add_column("Group", style="magenta")
    table.add_column("Host Address", style="green")

    for host in hosts:
        table.add_row(str(host.get_id()), host.get_name(),
                      host.get_group(), host.get_address())

    console = Console()
    console.print(table)

    host_ids = host_list.get_host_ids()
    try:
        host_id = IntPrompt.ask("Select a host id", choices=[
            "{:0d}".format(x) for x in host_ids])
    except KeyboardInterrupt:
        sys.exit()

    selected_host = host_list.get_host(host_id)
    if selected_host:
        print(f'ssh {selected_host.get_address()}')
        os.system(f'ssh {selected_host.get_address()}')
    else:
        print('Invalid selection.')


if __name__ == '__main__':
    parse_args()
