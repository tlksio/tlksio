.PHONY: runserver
runserver:
	python manage.py runserver vps123446.vps.ovh.ca:8080

.PHONY: clean
clean:
	find . -name "__pycache__" -exec rm -rf "{}" \;
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	rm -rf .coverage

.PHONY: distclean
distclean: clean
	rm -rf db.sqlite3

.PHONY: deps-upgrade
deps-upgrade:
	pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

.PHONY: deps
deps: deps-upgrade
	pip install -r requirements.txt
	pip freeze > requirements.txt

.PHONY: shell
shell:
	python manage.py shell

.PHONY: test
test:
	python manage.py test --keepdb -v2

.PHONY: cover
cover:
	coverage run --source=tlksio,talks manage.py test
	coverage report

.PHONY: migrate
migrate:
	python manage.py makemigrations
	python manage.py migrate

.PHONY: uwsgi
uwsgi:
	/usr/local/bin/uwsgi --chdir=/home/raul/tlksio \
		--module=wsgi:application \
		--master --pidfile=/tmp/project-master.pid \
		--socket :8080 \
		--processes=5 \
		--max-requests=5000 \
		--vacuum \
		--home=/home/raul/tlksio/env
		# --http 127.0.0.1:8080
		# daemonize=/home/raul/tlksio/yourproject.log


