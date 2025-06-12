* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.ApplyTo.html

#  [Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html).ApplyTo
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
public bool ApplyTo([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) target); 
## Declaration
public bool ApplyTo([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) target, string[] selectedPropertyPaths); 
### Parameters
Parameter | Description  
---|---  
target | The target object that will be updated with the Preset serialized values.  
selectedPropertyPaths | Optional list of property names that are applied to the target.  
### Returns
**bool** Returns true if the target object was successfully updated by the Preset, false otherwise. 
### Description
Applies this Preset to the target object.
* * *
