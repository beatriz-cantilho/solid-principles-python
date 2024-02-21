from good_srp.client import GithubClient
from good_srp.repo.parser import RepositoryParser
from good_srp.repo.reports_generator import ReportsGenerator
from good_srp.repo.reports.html_generator import HTMLGenerator
from good_srp.repo.reports.markdown_generator import MarkdownGenerator

if __name__ == '__main__':
    username = 'beatriz-cantilho'
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        repositories = RepositoryParser.parse(response['body'])
        markdown_report = ReportsGenerator.build(MarkdownGenerator, repositories)
        html_report = ReportsGenerator.build(HTMLGenerator, repositories)

        print(html_report)
        print(markdown_report)
    else:
        print(response['body'])
