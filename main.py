from good_srp.client import GithubClient
from good_srp.repo.parser import RepositoryParser
from good_srp.repo.reports_generator import ReportsGenerator
from good_srp.repo.reports.html_generator import HTMLGenerator
from good_srp.repo.reports.markdown_generator import MarkdownGenerator
from good_srp.repo.reports.writer import ReportWriter
from good_srp.model_repo.member import Member
from good_srp.model_repo.manager import Manager
from good_srp.model_repo.owner import Owner

if __name__ == '__main__':
    username = 'beatriz-cantilho'
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        repositories = RepositoryParser.parse(response['body'])
        markdown_report = ReportsGenerator.build(MarkdownGenerator, repositories)
        html_report = ReportsGenerator.build(HTMLGenerator, repositories)

        ReportWriter.write(markdown_report)

        print(html_report)
        print(markdown_report)
    else:
        print(response['body'])

    member = Member('bcantilho', 'bcantilho@teste.com')
    manager = Manager('cantilho', 'bcantilho@manager.com')
    owner = Owner('cantilho', 'bcantilho@manager.com')

    print(member.members())
    print(owner.members())
    #print(manager.members()) #It won't work on purpose


    print(member.work())
    print(manager.work())
