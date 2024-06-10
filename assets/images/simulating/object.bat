@echo off
setlocal enabledelayedexpansion

REM Create directories if they don't exist
if not exist C:\fuzz\input mkdir C:\fuzz\input
if not exist C:\fuzz\mutatedobj mkdir C:\fuzz\mutatedobj
if not exist C:\fuzz\crashesobj mkdir C:\fuzz\crashesobj

REM Copy sample input to input directory (if not already present)
if not exist C:\fuzz\input\input.html copy C:\fuzz\sample_input.html C:\fuzz\input\input.html

set count=0
set maxCount=126

REM Loop through all tags
for %%t in (html head title base meta link style script noscript body div span h1 h2 h3 h4 h5 h6 p hr pre blockquote ol ul li dl dt dd a em strong small s cite q dfn abbr code var samp kbd sub sup i b u bdo br img iframe embed object param map area table caption colgroup col tbody thead tfoot tr td th form label input button select optgroup option textarea fieldset legend ins del) do (
    REM Loop through all characters
    for /l %%c in (0,1,%maxCount%) do (
        REM echo Fuzzing tag %%t with character index %%c

        REM Mutate the input file
        cscript //nologo C:\fuzz\object.vbs %%t %%c
        if %ERRORLEVEL% neq 0 (
            echo Mutation script failed!
            goto :eof
        )
        echo Mutation complete.

        REM Check if the mutated file was created
        if not exist C:\fuzz\mutatedobj\mutated_%%t_%%c.html (
            echo Mutated file not found!
            goto :eof
        )

        REM Run Internet Explorer with the mutated file
        start "" "C:\Program Files\Internet Explorer\iexplore.exe" file:///C:/fuzz/mutatedobj/mutated_%%t_%%c.html
        echo IE execution started.

        REM Wait for a short period to allow IE to process the file
        ping -n 15 127.0.0.1 > nul
	

        REM Check for the crash dialog using VBScript
        cscript //nologo C:\fuzz\check_crash.vbs
        
	taskkill /IM iexplore.exe /F >nul 2>&1
		
		if !errorlevel! neq 0 (
			echo IE crashed, saving mutated file.
            		copy C:\fuzz\mutatedobj\mutated_%%t_%%c.html C:\fuzz\crashesobj\crash_%%t_%%c.html
		) else (
			echo IE did not crash.
		)
		
        set /a count+=1
        if %count% geq 1000 goto :done
    )
)
:done
echo Fuzzing completed.
endlocal
