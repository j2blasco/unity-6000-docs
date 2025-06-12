* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeAssetObjectPropertiesEventArgs.html

# ChangeAssetObjectPropertiesEventArgs
struct in UnityEditor
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
A change of this type indicates that a property of an asset object in memory has changed. This happens for example when [Undo.RecordObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html) is used with an instance of an asset (e.g. [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)). Note that this only covers changes to asset objects in memory and not changes to assets in the project on disk.
### Properties
Property | Description  
---|---  
[guid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeAssetObjectPropertiesEventArgs-guid.html) | The GUID of the changed asset.  
[instanceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeAssetObjectPropertiesEventArgs-instanceId.html) | The instance ID of the modified asset.  
[scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeAssetObjectPropertiesEventArgs-scene.html) | The Scene that contains the modified asset. This is usually an invalid scene unless the asset is explicitly associated in a scene (e.g. RenderSettings).  
### Constructors
Constructor | Description  
---|---  
[ChangeAssetObjectPropertiesEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeAssetObjectPropertiesEventArgs-ctor.html) | Constructs a new instance.  
* * *
