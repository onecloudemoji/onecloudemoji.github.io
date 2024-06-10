Dim fso, inputFile, mutatedFile, content, i
Dim tags, allChars, tag, charIndex, longString
tags = Array("html", "head", "title", "base", "meta", "link", "style", "script", "noscript", "body", _
             "div", "span", "h1", "h2", "h3", "h4", "h5", "h6", "p", "hr", "pre", "blockquote", "ol", "ul", "li", _
             "dl", "dt", "dd", "a", "em", "strong", "small", "s", "cite", "q", "dfn", "abbr", "code", "var", _
             "samp", "kbd", "sub", "sup", "i", "b", "u", "bdo", "br", "img", "iframe", "embed", "object", "param", _
             "map", "area", "table", "caption", "colgroup", "col", "tbody", "thead", "tfoot", "tr", "td", "th", _
             "form", "label", "input", "button", "select", "optgroup", "option", "textarea", "fieldset", "legend", _
             "ins", "del")

Set fso = CreateObject("Scripting.FileSystemObject")
Set inputFile = fso.OpenTextFile("C:\fuzz\input\input.html", 1)
content = inputFile.ReadAll
inputFile.Close

Randomize

' Generate all characters (ASCII 0 to 255)
allChars = ""
For i = 0 To 255
    allChars = allChars & Chr(i)
Next

' Function to create a long string of a specific character
Function CreateLongString(character, length)
    Dim result, j
    result = ""
    For j = 1 To length
        result = result & character
    Next
    CreateLongString = result
End Function

' Get command line arguments
tag = WScript.Arguments(0)
charIndex = WScript.Arguments(1)

' Generate a long string of the current character
longString = CreateLongString(Mid(allChars, charIndex + 1, 1), 100)

' Insert the overflow string into the specified tag
If InStr(content, "<" & tag & " ") > 0 Then
    ' Handle tag attributes
    content = Replace(content, "<" & tag & " ", "<" & tag & " " & longString & " ", 1, -1, 1)
End If

If InStr(content, "</" & tag & ">") > 0 Then
    ' Handle content between opening and closing tags
    content = Replace(content, "<" & tag & ">", "<" & tag & ">" & longString, 1, -1, 1)
    content = Replace(content, "</" & tag & ">", longString & "</" & tag & ">", 1, -1, 1)
ElseIf InStr(content, "<" & tag & ">") > 0 Then
    ' Handle self-closing tags
    content = Replace(content, "<" & tag & ">", "<" & tag & " " & longString & ">", 1, -1, 1)
End If

' Write the mutated content to a new file
Set mutatedFile = fso.CreateTextFile("C:\fuzz\mutated\mutated_" & tag & "_" & charIndex & ".html", True)
mutatedFile.Write content
mutatedFile.Close

WScript.Echo "Mutated file for tag '" & tag & "' with character index " & charIndex & " created."
