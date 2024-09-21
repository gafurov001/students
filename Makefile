mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
csu:
	python3 manage.py createsuperuser
cr:
	python3 manage.py migrate django_celery_results
cel:
	celery -A root worker -l INFO
flower:
	celery -A root.celery.app flower --port=5001
beat:
	celery -A root beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
