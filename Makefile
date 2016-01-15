modules = users

all: flakes test

full_test:: run_unit_tests run_integration_tests run_acceptance_tests report html_report

test:: run_unit_tests run_integration_tests report

unit:: run_unit_tests report

ignore_test = manage.py,**/test*,venv/*,yacatecuhtli/settings/*

run_unit_tests:
	@echo "Running UNIT tests..."
	@coverage run --source=. --omit="${ignore_test}"\
		manage.py test -p"*.py" --testrunner test_runners.UnitRunner

run_integration_tests:
	@echo Running INTEGRATION tests...
	@coverage run --source=. --omit="${ignore_test}" -a\
		manage.py test -p"*.py" --testrunner test_runners.IntegrationRunner

run_acceptance_tests:
	@echo Running ACCEPTANCE tests...
	@coverage run --source=. --omit="${ignore_test}" -a\
		manage.py test -p"*.py" --testrunner test_runners.AcceptanceRunner

report:
	@coverage report

report_html: test
	@coverage html -d .html_coverage
	@nohup firefox .html_coverage/index.html > /dev/null &

clean:
	@rm -r .coverage .html_coverage

pep8:
	@pep8 --statistics ${modules}

flakes:
	@pyflakes ${modules}
