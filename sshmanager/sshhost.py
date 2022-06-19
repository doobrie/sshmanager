import jsonpickle


class Host():
    def __init__(self, id, group, name, fullname) -> None:
        self.id = id
        self.group = group
        self.name = name
        self.fullname = fullname

    def get_id(self) -> int:
        return self.id

    def get_group(self) -> str:
        return self.group

    def get_name(self) -> str:
        return self.name

    def get_fullname(self) -> str:
        return self.fullname


class HostList:
    host_list = []

    def __init__(self) -> None:
        with open('hosts.txt', 'r') as input_file:
            json = input_file.readline()
            self.host_list = jsonpickle.decode(json)

    def add_host(self, host) -> None:
        self.host_list.append(host)

        json = jsonpickle.encode(self.get_hosts())
        with open('hosts.txt', 'w') as output_file:
            output_file.write(json)

    def get_hosts(self) -> list:
        return self.host_list

    def get_host(self, host_id) -> Host or None:
        for host in self.host_list:
            if host.get_id() == host_id:
                return host
        return None

    def get_host_ids(self) -> list:
        """Return a list of valid id's for the defined hosts

        Returns:
            list: List of id's starting at 1
        """
        return range(1, len(self.get_hosts())+1)
