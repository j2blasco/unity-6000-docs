* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.html

# SpriteAtlasAsset
class in UnityEditor.U2D
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
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
SpriteAtlasAsset stores inputs for generating SpriteAtlas and generates atlas textures on Import.
### Properties
Property | Description  
---|---  
[isVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset-isVariant.html) | Checks whether the Sprite Atlas Importer set the Sprite Atlas as a Variant.  
### Public Methods
Method | Description  
---|---  
[Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.Add.html) | Add an array of Assets to the packable objects list.  
[GetMasterAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.GetMasterAtlas.html) | Gets the Master Sprite Atlas for the given Variant Sprite Atlas.  
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.Remove.html) | Removes objects from the Atlas's packable objects list.  
[SetIsVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.SetIsVariant.html) | Sets whether this Sprite Atlas is a Variant or not.  
[SetMasterAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.SetMasterAtlas.html) | Sets an Atlas to be the Master Atlas.  
[SetScriptablePacker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.SetScriptablePacker.html) | Sets the ScriptablePacker ScriptableObject to SpriteAtlasAsset so custom packing can be implemented.  
### Static Methods
Method | Description  
---|---  
[Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.Load.html) | Loads SpriteAtlasAsset at the given path. File extension of SpriteAtlasAsset is *.spriteatlasv2.  
[Save](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.Save.html) | Saves SpriteAtlasAsset to disk. File extension of SpriteAtlasAsset is *.spriteatlasv2.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
