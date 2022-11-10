from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        py_obj = tomli.loads(content)
        name = py_obj['tool']['poetry']['name']
        descr = py_obj['tool']['poetry']['description']
        dependencies = py_obj['tool']['poetry']['dependencies']
        dev_dependencies = py_obj['tool']['poetry']['dev-dependencies']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, descr, dependencies, dev_dependencies)
