rem ---------------------------------------
rem  Generate PNGs from dot and move them
rem  to the png folder
rem ---------------------------------------

for %%f in (*.dot) do (
    dot -Tpng -O %%~f
)

mv *.png png\
