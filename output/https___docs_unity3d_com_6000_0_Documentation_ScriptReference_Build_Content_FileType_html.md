* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.FileType.html

# FileType
enumeration
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
Enum description of the type of file an object comes from.
Note: this enum and its values exist to provide low-level support for the **Scriptable Build Pipeline** package. This is intended for internal use only; use the [Scriptable Build Pipeline package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html) to implement a fully featured build pipeline. You can install this via the [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html).
### Properties
Property | Description  
---|---  
[NonAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.FileType.NonAssetType.html) | Object is contained in file not currently tracked by the AssetDatabase.  
[DeprecatedCachedAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.FileType.DeprecatedCachedAssetType.html) | Object is contained in a very old format. Currently unused.  
[SerializedAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.FileType.SerializedAssetType.html) | Object is contained in a standard asset file type located in the Assets folder.  
[MetaAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.FileType.MetaAssetType.html) | Object is contained in the imported asset meta data located in the Library folder.  
* * *
