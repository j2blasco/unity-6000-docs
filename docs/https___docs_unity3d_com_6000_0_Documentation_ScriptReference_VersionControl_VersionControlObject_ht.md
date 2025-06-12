* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html

# VersionControlObject
class in UnityEditor.VersionControl
/
Inherits from:[ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
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
The abstract base class for representing a version control system.
You can add support for a custom VCS by creating a new class derived from VersionControlObject and applying the [VersionControlAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlAttribute.html).
```
using UnityEditor.VersionControl;
using UnityEngine;  
  
[VersionControl("Custom")]
public class CustomVersionControlObject : VersionControlObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html)
{
    public override void OnActivate()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Custom VCS activated.");
    }  
  
    public override void OnDeactivate()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Custom VCS deactivated.");
    }
}

```

Using the example above, a new VCS option called _Custom_ will show up in Version Control settings window. You should only perform VCS operations when a VersionControlObject is activated. [OnActivate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.OnActivate.html) and [OnDeactivate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.OnDeactivate.html) methods are called on your class to notify your code about the change.  
  
Any persistent settings that must survive between Unity sessions (for example, the username or password) must be handled either by the underlying VCS, by using [EditorUserSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserSettings.html), or stored in a file. This is because the VersionControlObject is not serialized to disk and a new instance is created every time Unity starts up or when the VCS is activated.  
  
The VersionControlObject is derived from [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html). This makes [domain reloading](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html) handling simpler. You can add [OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) method to restore the state if needed.  
  
You can use [AssetModificationProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html) and [AssetPostprocessor.OnPostprocessAllAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessAllAssets.html) to get notifications from Unity when it wants to edit, add or remove assets.  
  
Additional resources: [VersionControlAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlAttribute.html), [VersionControlManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlManager.html), [EditorUserSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserSettings.html), [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html), [AssetModificationProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html), [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).
### Properties
Property | Description  
---|---  
[isConnected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject-isConnected.html) | Tests whether the VersionControlObject is connected to an underlying version control system.  
### Public Methods
Method | Description  
---|---  
[GetExtension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.GetExtension.html) | Gets optional extension object.  
[OnActivate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.OnActivate.html) | Called when your version control system is activated.  
[OnDeactivate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.OnDeactivate.html) | Called when your version control system is deactivated.  
[Refresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.Refresh.html) | Called when the cached state should be discarded and the new state should be retrieved from the underlying VCS.  
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
[CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html) | Creates an instance of a scriptable object.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
* * *
