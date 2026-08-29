pdflatex -jobname=respuestas_guia_4 respuestas_guia_4.tex
echo "2 seconds wait"
sleep 2
rm respuestas_guia_4.aux
rm respuestas_guia_4.log
rm respuestas_guia_4.fdb_latexmk
rm respuestas_guia_4.fls
