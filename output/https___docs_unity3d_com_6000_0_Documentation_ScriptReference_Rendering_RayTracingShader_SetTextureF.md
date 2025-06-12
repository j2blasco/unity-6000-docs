* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetTextureFromGlobal.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetTextureFromGlobal
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
public void SetTextureFromGlobal(int nameID, int globalTextureNameID); 
## Declaration
public void SetTextureFromGlobal(string name, string globalTextureName); 
### Parameters
Parameter | Description  
---|---  
nameID | The ID of the texture as given by Shader.PropertyToID.  
name | The name of the texture to bind.  
globalTextureName | The name of the global resource to bind to the RayTracingShader.  
globalTextureNameID | The ID of the global resource as given by Shader.PropertyToID.  
### Description
Binds a global texture to a [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).
The global texture must be previously set using [Shader.SetGlobalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalTexture.html).
* * *
