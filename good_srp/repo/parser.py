import sys

sys.path.append('/home/cantilho/Documentos/Cursos/SOLID/code/good_srp/model_repo')
from good_srp.model_repo.repository import Repository


class RepositoryParser:
    @classmethod
    def parse(cls, response):
        repositories = []
        for i in range(len(response)):
            repository = response[i]
            repository = Repository(repository["id"], repository["name"], repository["stargazers_count"])
            repositories.append(repository)
        return repositories
