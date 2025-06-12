* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.AssignNewShaderToMaterial.html

#  [ShaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.html).AssignNewShaderToMaterial
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
public void AssignNewShaderToMaterial([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) oldShader, [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) newShader); 
### Parameters
Parameter | Description  
---|---  
material | The material the newShader should be assigned to.  
oldShader | Previous shader.  
newShader | New shader to assign to the material.  
### Description
This method is called when a new shader has been selected for a Material.
Can be used for setting up the new shader based on state from the previous shader. Ensure to call _base.AssignNewShaderToMaterial_ to actually set _material.shader_.
* * *
