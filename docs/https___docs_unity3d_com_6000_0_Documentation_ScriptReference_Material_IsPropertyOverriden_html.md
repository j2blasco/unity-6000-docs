* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsPropertyOverriden.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).IsPropertyOverriden
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
## Declaration
public bool IsPropertyOverriden(string name); 
## Declaration
public bool IsPropertyOverriden(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | Property name, e.g. "_SrcBlend".  
### Returns
**bool** Returns true if the property you pass in is overriden by this material. Otherwise, returns false. 
### Description
Checks whether a property is overriden by this material.
This method is Editor-only.  
  
Additional resources: [Material.ApplyPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.ApplyPropertyOverride.html), [Material.RevertPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.RevertPropertyOverride.html).
* * *
