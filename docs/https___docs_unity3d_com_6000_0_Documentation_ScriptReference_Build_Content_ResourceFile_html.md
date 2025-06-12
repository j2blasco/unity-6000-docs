* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ResourceFile.html

# ResourceFile
struct in UnityEditor.Build.Content
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
Details about a specific file written by the [ContentBuildInterface.WriteSerializedFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.WriteSerializedFile.html) or [ContentBuildInterface.WriteSceneSerializedFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.WriteSceneSerializedFile.html) APIs.
Note: this struct and its members exist to provide low-level support for the **Scriptable Build Pipeline** package. This is intended for internal use only; use the [Scriptable Build Pipeline package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html) to implement a fully featured build pipeline. You can install this via the [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html).
### Properties
Property | Description  
---|---  
[fileAlias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ResourceFile-fileAlias.html) | Internal name used by the loading system for a resource file.  
[fileName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ResourceFile-fileName.html) | Path to the resource file on disk.  
[serializedFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ResourceFile-serializedFile.html) | Bool to determine if this resource file represents serialized Unity objects (serialized file) or binary resource data.  
* * *
