.PHONY: build run test clean

run:
	flask --app src/main.py --debug run
