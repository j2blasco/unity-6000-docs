* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.ParseArgument.html

#  [CodeEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.html).ParseArgument
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public static string ParseArgument(string arguments, string path, int line, int column); 
### Parameters
Parameter | Description  
---|---  
arguments | The string that contains the template arguments to parse.  
path | The file path to open.  
line | The Line number to place the cursor.  
column | The column number that represents where on the line to place the cursor.  
### Returns
**string** Returns the `arguments` parameter with replacements based on the values passed in to the method. 
### Description
Parse a string using the rules defined under [External Tools](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html).
* * *
