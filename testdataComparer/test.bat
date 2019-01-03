@echo off
echo start > res.txt
for /l %%i in (1,1,200) do (
    if not exist %%i.in (
        goto final
    )
    echo now: %%i
    a.exe < %%i.in > out.txt
    fc out.txt %%i.out
    if errorlevel 1 (
        echo %%i false >> res.txt
    ) else (
        echo %%i true >> res.txt
    )
)
:final
del out.txt
