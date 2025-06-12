* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteCommand.html

# WriteCommand
class in UnityEditor.Build.Content
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
Container for holding information about a serialized file to be written.
Note: this class and its members exist to provide low-level support for the **Scriptable Build Pipeline** package. This is intended for internal use only; use the [Scriptable Build Pipeline package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html) to implement a fully featured build pipeline. You can install this via the [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html).
### Properties
Property | Description  
---|---  
[fileName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteCommand-fileName.html) | Final file name on disk of the serialized file.  
[internalName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteCommand-internalName.html) | Internal name used by the loading system for a serialized file.  
[serializeObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteCommand-serializeObjects.html) | List of objects and their order contained inside a serialized file.  
### Constructors
Constructor | Description  
---|---  
[WriteCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteCommand-ctor.html) | Default constructor for an empty WriteCommand.  
* * *
