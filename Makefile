DAY ?= 05


init:
	@mkdir day.$(DAY)
	@touch day.$(DAY)/sample.in
	@touch day.$(DAY)/puzzle.in
	@cp template.py day.$(DAY)/code.1.py

copy:
	@cp day.$(DAY)/code.1.py day.$(DAY)/code.2.py

test.1:
	@cd day.$(DAY) && python3 code.1.py

test.2:
	@cd day.$(DAY) && python3 code.2.py
