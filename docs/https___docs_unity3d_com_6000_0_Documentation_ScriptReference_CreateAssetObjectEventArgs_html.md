* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateAssetObjectEventArgs.html

# CreateAssetObjectEventArgs
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
A change of this type indicates that an asset object has been created. This happens for example when [Undo.RegisterCreatedObjectUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html) is used with an instance of an asset (e.g. [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)). Note that this only covers creation of asset objects in memory and not creation of new assets in the project on disk.
### Properties
Property | Description  
---|---  
[guid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateAssetObjectEventArgs-guid.html) | The GUID of the new asset.  
[instanceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateAssetObjectEventArgs-instanceId.html) | The instance ID of the modified asset.  
[scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateAssetObjectEventArgs-scene.html) | The Scene that contains the new asset. This is usually an invalid scene unless the asset is explicitly associated in a scene (e.g. RenderSettings).  
### Constructors
Constructor | Description  
---|---  
[CreateAssetObjectEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateAssetObjectEventArgs-ctor.html) | Constructs a new instance.  
* * *
