build: app/tmp/ship.db
	cd app/; python ship.py

app/tmp/ship.db: app/tmp/
	touch app/tmp/ship.db
	cd app/; python -c "from ship import init_db; init_db()"

app/tmp/:
	mkdir app/tmp/

clean:
	rm -rf app/tmp/

test:
	cd app/tests/; python _run_all_tests.py
