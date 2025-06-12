* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteResult.html

# WriteResult
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
Struct containing the results from the ContentBuildPipeline.WriteSerialziedFile and ContentBuildPipeline.WriteSceneSerialziedFile APIs.
Note: this struct and its members exist to provide low-level support for the **Scriptable Build Pipeline** package. This is intended for internal use only; use the [Scriptable Build Pipeline package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html) to implement a fully featured build pipeline. You can install this via the [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html).
### Properties
Property | Description  
---|---  
[externalFileReferences](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteResult-externalFileReferences.html) | The collection of externally referenced files.  
[includedSerializeReferenceFQN](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteResult-includedSerializeReferenceFQN.html) | SerializeReference instances fully qualified name which were included in the serialized file.  
[includedTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteResult-includedTypes.html) | Types that were included in the serialized file.  
[resourceFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteResult-resourceFiles.html) | Collection of files written by the ContentBuildInterface.WriteSerializedFile or ContentBuildInterface.WriteSceneSerializedFile APIs.  
[serializedObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteResult-serializedObjects.html) | Collection of objects written to the serialized file.  
* * *
