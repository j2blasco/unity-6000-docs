* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html

# MonoScript
class in UnityEditor
/
Inherits from:[TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html)
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
Representation of Script assets.
This class represents C# files stored in the project.
### Public Methods
Method | Description  
---|---  
[GetClass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.GetClass.html) | Returns the System.Type object of the class implemented by this script.  
### Static Methods
Method | Description  
---|---  
[FromMonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.FromMonoBehaviour.html) | Returns the MonoScript object containing specified MonoBehaviour.  
[FromScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.FromScriptableObject.html) | Returns the MonoScript object containing specified ScriptableObject.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
[bytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-bytes.html) | The raw bytes of the text asset. (Read Only)  
[dataSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-dataSize.html) | The size of the text asset data in bytes. (Read Only)  
[text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-text.html) | The text contents of the file as a string. (Read Only)  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.GetData.html) | Gets raw text asset data.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.ToString.html) | Returns the contents of the TextAsset.  
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
