* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html

# PresetType
struct in UnityEditor.Presets
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
Stores a type to which a Preset can be applied.
Only classes that inherit from UnityEngine.Object are represented by a PresetType.  
  
This structure is used instead of Type because some native C++ types in Unity are not exposed to managed C# for optimization reasons.
### Public Methods
Method | Description  
---|---  
[GetManagedTypeName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.GetManagedTypeName.html) | Retrieves a human readable namespace and the name of the target class, regardless of whether it's a managed C# class or a native C++ class.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.IsValid.html) | Checks whether a PresetType corresponds with a valid native or managed class.  
[IsValidDefault](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.IsValidDefault.html) | Checks whether a PresetType can be used within the DefaultPreset system.  
* * *
