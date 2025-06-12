* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html

# Object
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Object.html "Go to Object Component in the Manual")
### Description
Base class for all objects Unity can reference.
UnityEngine.Object is the base class of all built-in Unity objects. Custom Unity Object types can be defined in scripts by deriving a new class from types like [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html), [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) and [ScriptedImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html).  
  
Any public variable you make that derives from Object gets shown in the inspector as a drop target, allowing you to set the value from the GUI.  
  
Typically scripts will use types derived from this class, for example [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) and [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html), so that the specific properties and methods for those types are exposed to the script. However, some APIs are designed to work with any Unity Object, so Object appears as a type in their signatures. For example [Resources.LoadAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAll.html), [EditorJsonUtility.ToJson](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorJsonUtility.ToJson.html) and [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).  
  
Sometimes an instance of Object can be in a detached state, where there is no underlying native object. This can happen if the instance references an native object that has been destroyed, or a missing Asset or missing type. Detached objects retain their InstanceID, but the object cannot be used to call methods or access properties. An object in this state will appear to be null, because of special implementations of operator ==, operator != and [Object.bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html). Because the object is not truly null, a call to **Object.ReferenceEquals(myobject, null)** will return false.  
  
The [null-conditional operator ](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/expressions#null-conditional-operator) (**?.**) and the [null-coalescing operator ](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/expressions#the-null-coalescing-operator)(**??**) are not supported with Unity Objects because they cannot be overridden to treat detached objects objects the same as null. It is only safe to use those operators in your scripts if there is certainty that the objects being checked are never in a detached state. 
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
