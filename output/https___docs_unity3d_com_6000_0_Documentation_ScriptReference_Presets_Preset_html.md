* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html

# Preset
class in UnityEditor.Presets
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
A Preset contains default values for an Object.
The Preset class contains the type of the Object used to create it and a list of each serialized property/value pair of this Object. It can be used to store informations from any serializable Object in the Editor and apply them back to this Object or any other Object of the same type. Presets can also be saved as Assets using the .preset extension in order to.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Presets;
using UnityEngine;  
  
public static class PresetUsageExample
{
    // This method uses a Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) to copy the serialized values from the source to the target and return true if the copy succeed.
    public static bool CopyObjectSerialization(Object source, Object target)
    {
        Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) preset = new Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html)(source);
        return preset.ApplyTo(target);
    }  
  
    // This method creates a Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) from a given Object and save it as an asset in the project.
    public static void CreatePresetAsset(Object source, string name)
    {
        Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) preset = new Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html)(source);
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(preset, "Assets/" + name + ".preset");
    }
}

```

### Properties
Property | Description  
---|---  
[excludedProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset-excludedProperties.html) | List of properties to ignore when applying the Preset to an object.  
[PropertyModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.PropertyModifications.html) | Returns a copy of the PropertyModification array owned by this Preset.  
### Constructors
Constructor | Description  
---|---  
[Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset-ctor.html) | Constructs a new Preset from a given Object.  
### Public Methods
Method | Description  
---|---  
[ApplyTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.ApplyTo.html) | Applies this Preset to the target object.  
[CanBeAppliedTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.CanBeAppliedTo.html) | Returns true if this Preset can be applied to the target Object.  
[DataEquals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.DataEquals.html) | Determines if the target object has the same serialized values as the Preset.  
[GetPresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetPresetType.html) | Returns the PresetType of this Preset.  
[GetTargetFullTypeName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetTargetFullTypeName.html) | Returns a human readable string of this Preset's target fulltype, including namespace.  
[GetTargetTypeName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetTargetTypeName.html) | Returns a human readable string of this Preset's target type.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.IsValid.html) | Returns true if the Preset type of this Preset is valid.  
[UpdateProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.UpdateProperties.html) | Updates this Preset's properties from the given Object's values. The given Object's type must match this Preset's type.  
### Static Methods
Method | Description  
---|---  
[GetAllDefaultTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetAllDefaultTypes.html) | Returns all the PresetType that have at least one DefaultPreset entry in the default Presets list.  
[GetDefaultPresetsForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetDefaultPresetsForObject.html) | Gets the ordered list of Presets that set its default values when applied to the target.  
[GetDefaultPresetsForType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetDefaultPresetsForType.html) | Gets an ordered list of DefaultPreset based on the specified PresetType.  
[IsEditorTargetAPreset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.IsEditorTargetAPreset.html) | Returns true if the given target is a temporary UnityEngine.Object instance created from inside a PresetEditor.  
[RemoveFromDefault](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.RemoveFromDefault.html) | Remove the Preset type from having default values in the project.  
[SetDefaultPresetsForType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.SetDefaultPresetsForType.html) | Sets a default list of Presets with a filter for a specific PresetType.  
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
