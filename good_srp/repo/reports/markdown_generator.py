class MarkdownGenerator:
    @classmethod
    def build(cls, repositories):
        items = ' '.join(
            f'**ID:** {repository.id} **NAME:** {repository.name} **STARS:** {repository.stars}\n'
            for repository in repositories)
        return f'##REPOSITORIES \n\n {items}'