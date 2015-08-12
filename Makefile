build: ship/tmp/ship.db
	python ship/ship.py

ship/tmp/ship.db: ship/tmp/
	touch ship/tmp/ship.db
	cd ship/tmp/
	python -c "from ship import init_db; init_db()"
	cd ../../

ship/tmp/:
	mkdir ship/tmp/
