* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.html

# ContentBuildInterface
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
Low level interface for building content for Unity.
Note: this class and its members exist to provide low-level support for the **Scriptable Build Pipeline** package. This is intended for internal use only; use the [Scriptable Build Pipeline package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html) to implement a fully featured build pipeline. You can install this via the [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html).
### Static Methods
Method | Description  
---|---  
[ArchiveAndCompress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.ArchiveAndCompress.html) | Create a Unity archive file, containing the content of one or more resource files.  
[CalculateBuildUsageTags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.CalculateBuildUsageTags.html) | Calculates the build usage of a set of objects.  
[CalculatePlayerDependenciesForGameManagers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.CalculatePlayerDependenciesForGameManagers.html) | Calculates dependency information for various internal Unity game manager classes.  
[CalculatePlayerDependenciesForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.CalculatePlayerDependenciesForScene.html) | Calculates the Scene dependency information.  
[CalculatePlayerSerializationHashForType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.CalculatePlayerSerializationHashForType.html) | Returns a unique hash for a given type's serialized layout.  
[GenerateAssetBundleBuilds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GenerateAssetBundleBuilds.html) | Returns an array of AssetBundleBuild structs that detail the current AssetBundle layout, as set through the Inspector and stored in the AssetDatabase.  
[GetGlobalUsageFromActiveScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GetGlobalUsageFromActiveScene.html) | Gets information about the lighting and render settings in the active scene.  
[GetGlobalUsageFromGraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GetGlobalUsageFromGraphicsSettings.html) | Returns the global usage information calculated by the Shader Stripping section of Graphics Settings.  
[GetPlayerAssetRepresentations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GetPlayerAssetRepresentations.html) | Returns a list of visible objects directly contained inside of an asset.  
[GetPlayerDependenciesForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GetPlayerDependenciesForObject.html) | Returns a list of objects referenced by an object.  
[GetPlayerDependenciesForObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GetPlayerDependenciesForObjects.html) | Returns a list of objects referenced by a set of objects.  
[GetPlayerObjectIdentifiersInAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GetPlayerObjectIdentifiersInAsset.html) | Returns a list of objects directly contained inside of an asset.  
[GetPlayerObjectIdentifiersInSerializedFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GetPlayerObjectIdentifiersInSerializedFile.html) | Returns a list of objects directly contained inside of a loose serialized file.  
[GetTypeForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GetTypeForObject.html) | Returns the System.Type of the ObjectIdentifier specified by objectID.  
[GetTypeForObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GetTypeForObjects.html) | Returns the System.Type of the ObjectIdentifiers and the referenced SerializeReference class types specified by objectIDs.  
[GetTypesForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.GetTypesForObject.html) | Returns the System.Type of the ObjectIdentifier and the referenced SerializeReference class types specified by objectID.  
[ObjectIsSupportedInBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.ObjectIsSupportedInBuild.html) | Returns True if the passed in target object is a valid runtime object.  
[StartProfileCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.StartProfileCapture.html) | Starts a profile capture to record content build profile events.  
[StopProfileCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.StopProfileCapture.html) | Returns an array of ContentBuildProfileEvent structs that contain information for each occuring event. Also stops the profile capture.  
[WriteGameManagersSerializedFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.WriteGameManagersSerializedFile.html) | Writes the current settings of internal Unity game manager classes to the 'globalgamemanagers' file on disk.  
[WriteSceneSerializedFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.WriteSceneSerializedFile.html) | Writes Scene objects to a serialized file on disk.  
[WriteSerializedFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.WriteSerializedFile.html) | Writes objects to a serialized file on disk.  
* * *
