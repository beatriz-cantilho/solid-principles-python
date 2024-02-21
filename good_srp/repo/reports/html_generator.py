class HTMLGenerator:
    @classmethod
    def build(cls, repositories):
        items = ' '.join(
            f'<strong>ID: </strong>{repository.id} <strong>NAME: </strong>{repository.name} <strong>STARS: </strong>{repository.stars}\n'
            for repository in repositories)
        return f'<p>{items}</p>'
