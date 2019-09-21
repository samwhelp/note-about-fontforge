

default: help
.PHONY: default


help:
	@echo Usage:
	@echo

	@echo $$ make [Target]

	@echo
	@echo
	@echo Example:
	@echo

	@echo $$ make help

	@echo
	@echo $$ make prepare

	@echo
	@echo $$ make svg-export
	@echo $$ make svg-import

	@echo
	@echo $$ make font-install
	@echo $$ make font-remove

	@echo
.PHONY: help




prepare:
	@./prepare.sh
.PHONY: prepare




svg-export:
	@./svg-export.sh
.PHONY: svg-export


svg-import:
	@./svg-import.sh
.PHONY: svg-import




font-install:
	@./font-install.sh
.PHONY: font-install


font-remove:
	@./font-remove.sh
.PHONY: font-remove
