run:
	python3 -m project.main

add_numbers:
	python3 -m project.module1.add_numbers

clean:
	@echo 'Removing logs'
	rm -rf data/logs/*