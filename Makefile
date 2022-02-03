.PHONY: main clean FORCE

main: TreeLogo.png

TreeLogo.pdf: FORCE
	latexmk -pdflatex='lualatex -halt-on-error -file-line-error -interaction=errorstopmode' -pdf TreeLogo.tex

%.png:	%.pdf
	pdftoppm -png $< $*
	mv $*-1.png $@

clean:
	latexmk -pdf -C
