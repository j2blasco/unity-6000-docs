* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SetMaterial.html

#  [CanvasRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.html).SetMaterial
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
public void SetMaterial([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int index); 
## Declaration
public void SetMaterial([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture); 
### Parameters
Parameter | Description  
---|---  
material | Material for rendering.  
texture | Material texture overide.  
index | Material index.  
### Description
Set the material for the canvas renderer. If a texture is specified then it will be used as the 'MainTex' instead of the material's 'MainTex'. Additional resources: [CanvasRenderer.materialCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer-materialCount.html), [CanvasRenderer.SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanvasRenderer.SetTexture.html).
* * *
