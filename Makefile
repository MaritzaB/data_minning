reports: \
	reports/chapter01.pdf
	

.PHONY: \
	all \
	clean \
	format \
	tests

define renderLatex
    cd $(<D) && pdflatex $(<F)
	cd $(<D) && pdflatex $(<F)
	cd $(<D) && pdflatex $(<F)
endef

define lint
	pylint \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
		--function-naming-style=camelCase \
        ${1}
endef

reports/chapter01.pdf: reports/chapter01.tex
	$(renderLatex)


clean:
	rm --force reports/*.aux
	rm --force reports/*.bbl
	rm --force reports/*.blg
	rm --force reports/*.log
	rm --force reports/*.out
	rm --force reports/*.pdf
	rm --force reports/*.toc
	rm --force --recursive src/datasets/__pycache__
	rm --force --recursive src/DIC/__pycache__
	rm --force --recursive optics/__pycache__

format:
	black --line-length 80 src/*.py

linter:
	$(call lint, src)
	$(call lint, tests)

tests:
	pytest --verbose tests/
