# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
from .packets import Default


class Model(Default):
    """
    A model is an object that can be serialized and sent over the network, but 
    that can be saved into the SQL database used by the server.
    """

    def build(self, dct):
        self.build_default(dct)
        return dct

    def parse(self, dct):
        self.parse_default(dct)
        return self

    def __repr__(self):
        """
        Return a textual representation of the object. It will mainly be used
        for pretty-printing into the console.
        """
        attrs = u", ".join(
            [
                u"{}={}".format(key, val)
                for key, val in Default.attrs(self.__dict__).items()
            ]
        )
        return u"{}({})".format(self.__class__.__name__, attrs)


class Project(Model):
    """
    IDBs are organized into projects, binaries and snapshots. A project contains all
    the files associated to a given topic, CVE, malware, etc. that we want to 
    group together to ease differentiating from another research topic.
    """

    def __init__(self, name, date):
        super(Project, self).__init__()
        self.name = name
        self.date = date


class Binary(Model):
    """
    IDBs are organized into projects, binaries and snapshots. A binary regroups
    multiples revisions of an IDB. It has a name, the hash of the input file,
    the path to the input file, the type of the input file and the date of the
    snapshot creation.
    """

    def __init__(self, project_name, name, hash, file, type, date):
        super(Binary, self).__init__()
        self.project_name = project_name
        self.name = name
        self.hash = hash
        self.file = file
        self.type = type
        self.date = date


class Snapshot(Model):
    """
    IDBs are organized into projects, binaries and snapshots. A snapshot corresponds to
    a revision of an IDB. It has a binary, a name, a date of creation, and a
    current tick (events) count.
    """

    def __init__(self, project_name, binary, name, date, tick=0):
        super(Snapshot, self).__init__()
        self.project_name = project_name
        self.binary = binary
        self.name = name
        self.date = date
        self.tick = tick
