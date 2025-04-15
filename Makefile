build:
	python setup.py sdist

clean:
	ssh django@bpm-dev.malagasy.com "rm /opt/django/bpm/ticket_sim-*.tar.gz"

install:
	scp dist/ticket_sim-*.tar.gz django@bpm-dev.malagasy.com:/opt/django/bpm/
	ssh django@bpm-dev.malagasy.com "/opt/django/bpm/.env/bin/pip install --upgrade --force-reinstall /opt/django/bpm/ticket_sim-*.tar.gz"

deploy:
	ssh django@bpm-dev.malagasy.com "/opt/django/bpm/.env/bin/python /opt/django/bpm/manage.py collectstatic --no-input -l"
	ssh django@bpm-dev.malagasy.com "/opt/django/bpm/.env/bin/python /opt/django/bpm/manage.py migrate"
manage:
	ssh django@bpm-dev.malagasy.com "/opt/django/bpm/.env/bin/python /opt/django/bpm/manage.py ldap_sync"
	ssh django@bpm-dev.malagasy.com "/opt/django/bpm/.env/bin/python /opt/django/bpm/manage.py syncldapperms"
restart:
	ssh django@bpm-dev.malagasy.com "sudo systemctl stop django-bpm && sudo systemctl start django-bpm"
