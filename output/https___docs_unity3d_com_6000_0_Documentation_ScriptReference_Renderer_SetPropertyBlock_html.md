* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.SetPropertyBlock.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).SetPropertyBlock
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
public void SetPropertyBlock([MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties); 
## Declaration
public void SetPropertyBlock([MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties, int materialIndex); 
### Parameters
Parameter | Description  
---|---  
properties | Property block with values you want to override.  
materialIndex | The index of the Material you want to override the parameters of. The index ranges from 0 to Renderer.sharedMaterials.Length-1.  
### Description
Lets you set or clear per-renderer or per-material parameter overrides.
This is recommended when only a few properties of a Material are different per object. This is more memory efficient than having one complete distinct Material per object.  
  
You can also provide a Material index (from 0 to Renderer.materials.Length-1). In this case, only parameters of that Material are set. If there is both a per-renderer and a per-material block, only the per-Material block is used.  
  
To disable any of per-Renderer or per-Material overrides, pass null as the property’s argument.  
  
Additional resources: [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html), [GetPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.GetPropertyBlock.html).
* * *
