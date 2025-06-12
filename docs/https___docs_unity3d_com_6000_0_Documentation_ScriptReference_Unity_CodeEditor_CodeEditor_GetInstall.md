* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.GetInstallationForPath.html

#  [CodeEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.html).GetInstallationForPath
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
public [Unity.CodeEditor.CodeEditor.Installation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.Installation.html) GetInstallationForPath(string editorPath); 
### Parameters
Parameter | Description  
---|---  
editorPath | The absolute path to an executable.  
### Returns
**Installation** An [Installation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.Installation.html) representation of the path. 
### Description
Each registered code editor package has an instance of [IExternalCodeEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.IExternalCodeEditor.html). This method invokes [IExternalCodeEditor.TryGetInstallationForPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.IExternalCodeEditor.TryGetInstallationForPath.html) on that instance. It finds the first instance that returns a valid installation, and returns the installation.
* * *
