* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.IsValid.html

#  [PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html).IsValid
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
## Declaration
public bool IsValid(); 
### Returns
**bool** Returns true if the [PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html) is valid. Returns false otherwise. 
### Description
Checks whether a [PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html) corresponds with a valid native or managed class.
A PresetType is invalid when a MonoScript has been removed from the project, or the file containing a MonoBehaviour has been renamed and no longer matches the class name, or the type is explicitely excluded using [ExcludeFromPresetAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExcludeFromPresetAttribute.html).
* * *
