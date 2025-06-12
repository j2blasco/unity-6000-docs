* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.GetFoundScriptEditorPaths.html

#  [CodeEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.html).GetFoundScriptEditorPaths
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
public Dictionary<string,string> GetFoundScriptEditorPaths(); 
### Returns
**Dictionary <string,string>** A Dictionary that maps names to editor paths. 
### Description
Collects all installations from registered instances of [IExternalCodeEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.IExternalCodeEditor.html). This is done using [IExternalCodeEditor.Installations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.IExternalCodeEditor.Installations.html).
* * *
