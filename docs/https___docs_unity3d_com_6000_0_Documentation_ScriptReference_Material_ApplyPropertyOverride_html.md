* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.ApplyPropertyOverride.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).ApplyPropertyOverride
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
public void ApplyPropertyOverride([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) destination, string name, bool recordUndo); 
## Declaration
public void ApplyPropertyOverride([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) destination, int nameID, bool recordUndo); 
### Parameters
Parameter | Description  
---|---  
destination | The Material to which the Editor applies the override.  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | Property name, e.g. "_SrcBlend".  
recordUndo | Wheter the editor should record an undo operation for this action.  
### Description
Applies an override associated with a Material Variant to a target.
Sets the value of a property of this Material on a destination Material. The destination material must be an ancestor of this Material. After you apply an override, the Editor no longer marks the associated Property as overriden, and discards any change of the property on ancestors of this Material up to the destination Material. Note that this method is Editor-only.  
  
Additional resources: [Material.IsChildOf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsChildOf.html), [Material.IsPropertyOverriden](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsPropertyOverriden.html), [Material.RevertPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.RevertPropertyOverride.html).
* * *
