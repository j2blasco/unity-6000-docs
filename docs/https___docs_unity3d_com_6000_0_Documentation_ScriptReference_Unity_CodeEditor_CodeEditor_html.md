* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.html

# CodeEditor
class in Unity.CodeEditor
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
### Description
Handles interaction with the code editor.
### Static Properties
Property | Description  
---|---  
[CurrentEditorPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.CurrentEditorPath.html) | The path to the external code editor that Unity uses used to open script assets.  
[Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.Editor.html) | A singleton instance of CodeEditor. The Unity Editor references this instance to handle code editor callbacks.  
### Properties
Property | Description  
---|---  
[CurrentCodeEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.CurrentCodeEditor.html) | Returns the current IExternalCodeEditor instance for the code editor.  
[CurrentInstallation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.CurrentInstallation.html) | Returns the current CodeEditor.Installation instance for the code editor.  
### Public Methods
Method | Description  
---|---  
[GetCodeEditorForPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.GetCodeEditorForPath.html) | Each registered code editor package has an instance of IExternalCodeEditor. This method invokes IExternalCodeEditor.TryGetInstallationForPath on that instance. It returns the first instance that returns a valid installation.  
[GetFoundScriptEditorPaths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.GetFoundScriptEditorPaths.html) | Collects all installations from registered instances of IExternalCodeEditor. This is done using IExternalCodeEditor.Installations.  
[GetInstallationForPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.GetInstallationForPath.html) | Each registered code editor package has an instance of IExternalCodeEditor. This method invokes IExternalCodeEditor.TryGetInstallationForPath on that instance. It finds the first instance that returns a valid installation, and returns the installation.  
[SetCodeEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.SetCodeEditor.html) | Sets the path to the code editor that Unity uses to open script assets.  
### Static Methods
Method | Description  
---|---  
[OSOpenFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.OSOpenFile.html) | Open an application with a quoted string of arguments.  
[ParseArgument](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.ParseArgument.html) | Parse a string using the rules defined under External Tools.  
[QuoteForProcessStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.QuoteForProcessStart.html) | Quotes a string to pass to Process.Start as a single argument, and appends it to this string builder.  
[Register](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.Register.html) | Register an instance of IExternalCodeEditor to use when populating Preferences/External Tools menu. Calls ref::Initialize if you select the instance.  
[Unregister](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.Unregister.html) | Remove an instance of IExternalCodeEditor from the list of registered code editors. Calls ref::Initialize if you select the instance.  
* * *
