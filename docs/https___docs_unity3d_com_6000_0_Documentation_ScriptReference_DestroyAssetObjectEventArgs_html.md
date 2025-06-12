* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyAssetObjectEventArgs.html

# DestroyAssetObjectEventArgs
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
A change of this type indicates that an asset object has been destroyed. This happens for example when [Undo.DestroyObjectImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.DestroyObjectImmediate.html) is used with an instance of an asset (e.g. [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)). Note that this only covers destruction of asset objects in memory and not deletion of assets in the project on disk.
### Properties
Property | Description  
---|---  
[guid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyAssetObjectEventArgs-guid.html) | The GUID of the removed asset.  
[instanceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyAssetObjectEventArgs-instanceId.html) | The instance ID of the modified asset.  
[scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyAssetObjectEventArgs-scene.html) | The scene that contained the asset. This is usually an invalid scene unless the asset is explicitly associated in a scene (e.g. RenderSettings).  
### Constructors
Constructor | Description  
---|---  
[DestroyAssetObjectEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyAssetObjectEventArgs-ctor.html) | Constructs a new instance.  
* * *
