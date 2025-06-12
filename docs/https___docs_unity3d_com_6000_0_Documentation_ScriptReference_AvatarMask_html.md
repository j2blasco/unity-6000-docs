* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.html

# AvatarMask
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AvatarMask.html "Go to AvatarMask Component in the Manual")
### Description
AvatarMask is used to mask out humanoid body parts and transforms.
They can be used when importing animation or in an animator controller layer.
### Properties
Property | Description  
---|---  
[transformCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask-transformCount.html) | Number of transforms.  
### Constructors
Constructor | Description  
---|---  
[AvatarMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask-ctor.html) | Creates a new AvatarMask.  
### Public Methods
Method | Description  
---|---  
[AddTransformPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.AddTransformPath.html) | Adds a transform path into the AvatarMask.  
[GetHumanoidBodyPartActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.GetHumanoidBodyPartActive.html) | Returns true if the humanoid body part at the given index is active.  
[GetTransformActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.GetTransformActive.html) | Returns true if the transform at the given index is active.  
[GetTransformPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.GetTransformPath.html) | Returns the path of the transform at the given index.  
[RemoveTransformPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.RemoveTransformPath.html) | Removes a transform path from the AvatarMask.  
[SetHumanoidBodyPartActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.SetHumanoidBodyPartActive.html) | Sets the humanoid body part at the given index to active or not.  
[SetTransformActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.SetTransformActive.html) | Sets the tranform at the given index to active or not.  
[SetTransformPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.SetTransformPath.html) | Sets the path of the transform at the given index.  
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
