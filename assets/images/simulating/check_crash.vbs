Set WshShell = WScript.CreateObject("WScript.Shell")

If WshShell.AppActivate("Internet Explorer") Then

    WshShell.SendKeys "{ESC}"
 
    WScript.Sleep 3000
Else
    WScript.Echo "Internet Explorer window not found"
End If
