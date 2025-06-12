* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.RegisterMaterial.html

#  [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html).RegisterMaterial
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
public [Rendering.BatchMaterialID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchMaterialID.html) RegisterMaterial([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material); 
### Parameters
Parameter | Description  
---|---  
material | Unity Material.  
### Returns
**BatchMaterialID** BatchRendererGroup Material ID. 
### Description
Registers a Material in `BatchRendererGroup` and returns its `BatchMaterialID`. Each registration of a specific Material increases its number of owners by 1.
* * *
