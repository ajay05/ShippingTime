build: tmp/ship.db
	python ship.py

tmp/ship.db: tmp/
	touch tmp/ship.db
	cd tmp/
	python -c "from ship import init_db; init_db()"
	cd ../

tmp/:
	mkdir tmp/
