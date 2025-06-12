* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsPropertyLockedByAncestor.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).IsPropertyLockedByAncestor
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
public bool IsPropertyLockedByAncestor(string name); 
## Declaration
public bool IsPropertyLockedByAncestor(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | Property name, e.g. "_SrcBlend".  
### Returns
**bool** Returns true if the property you pass in is locked by any of ancestor of this material. Otherwise, returns false. 
### Description
Checks whether a property is locked by any of ancestor of this material.
If a property is locked by an ancestor of the material, any change to the property on this Material will not have any effect until the property is unlocked by the ancestor. Note that this method is Editor-only.  
  
Additional resources: [Material.SetPropertyLock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetPropertyLock.html).
* * *
