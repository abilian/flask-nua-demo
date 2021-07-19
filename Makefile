.PHONY:
run:
	poetry run gunicorn app:app

.PHONY:
clean:
	rm -rf __pycache__
