build: tmp/ship.db
	python ship.py

tmp/ship.db: tmp/
	touch tmp/ship.db
	python -c "from ship import init_db; init_db()"

tmp/:
	mkdir tmp/

clean:
	rm -rf tmp/

test:
	cd tests/; python _run_all_tests.py
