* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html

# TextAsset
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html "Go to TextAsset Component in the Manual")
### Description
Represents a raw text or binary file asset.
You can use raw text files in your project as assets and get their contents through this class. For more information, see [text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-text.html).  
  
You can access the file as a raw byte array to access data from binary files. For more information on how to access data from binary files, see [bytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-bytes.html) and [GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.GetData.html).  
  
For more information about importing text or binary files into your project as Text Assets, see [Text Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html).
### Properties
Property | Description  
---|---  
[bytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-bytes.html) | The raw bytes of the text asset. (Read Only)  
[dataSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-dataSize.html) | The size of the text asset data in bytes. (Read Only)  
[text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-text.html) | The text contents of the file as a string. (Read Only)  
### Constructors
Constructor | Description  
---|---  
[TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-ctor.html) | Creates a new TextAsset with specified text contents.  
### Public Methods
Method | Description  
---|---  
[GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.GetData.html) | Gets raw text asset data.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.ToString.html) | Returns the contents of the TextAsset.  
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
