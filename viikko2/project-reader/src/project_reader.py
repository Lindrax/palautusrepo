from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed = toml.loads(content)

        license = parsed["tool"]["poetry"]['license']
        authors = parsed["tool"]["poetry"]['authors']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(parsed['tool']['poetry']['name'], parsed['tool']['poetry']['description'], license, authors, parsed['tool']['poetry']['dependencies'], parsed['tool']['poetry']['group']['dev']['dependencies'])
