* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.OSOpenFile.html

#  [CodeEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.html).OSOpenFile
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
public static bool OSOpenFile(string appPath, string arguments); 
### Parameters
Parameter | Description  
---|---  
appPath | The absolute path of the application to open.  
arguments | The arguments to be passed to the application. You must make sure any paths are quoted correctly for the current platform.  
### Description
Open an application with a quoted string of arguments.
This method is useful if you want to write a custom tool in the Unity Editor which launches a local application with arguments. The Unity Editor passes this request to the operating system's native support for opening applications. Note: Because the path and parameters you supply are passed directly on to the OS, you must ensure they are correctly quoted for the current platform. You can use [Application.platform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-platform.html) to detect the current platform.
* * *
