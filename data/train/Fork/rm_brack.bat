cd C:\Users\fluke\Downloads\fork
setlocal enabledelayedexpansion
for %%a in (*.*) do (
set f=%%a
set f=!f:^(=!
set f=!f:^)=!
ren "%%a" "!f!"
)