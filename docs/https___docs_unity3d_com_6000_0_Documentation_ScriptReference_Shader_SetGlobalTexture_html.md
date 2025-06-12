* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalTexture.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).SetGlobalTexture
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html "Go to Shader Component in the Manual")
## Declaration
public static void SetGlobalTexture(string name, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) value); 
## Declaration
public static void SetGlobalTexture(int nameID, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) value); 
## Declaration
public static void SetGlobalTexture(string name, [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) value, [Rendering.RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html) element); 
## Declaration
public static void SetGlobalTexture(int nameID, [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) value, [Rendering.RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html) element); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
value | The texture to set.  
element | Optional parameter that specifies the type of data to set from the RenderTexture.  
### Description
Sets a global texture property for all shaders.
Global properties are used if a shader needs them but the material does not have them defined (for example, if the shader does not expose them in `Properties` block).  
  
Usually this is used if you have a set of custom shaders that all use the same "global" texture (for example, custom diffuse-lighting cubemap). Then you can set the global property from script and don't have to setup the same texture in all materials.  
  
By specifying a `RenderTextureSubElement`, you can indicate which type of data to set from the RenderTexture. The possible options are: [RenderTextureSubElement.Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Color.html), [RenderTextureSubElement.Depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Depth.html), and [RenderTextureSubElement.Stencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.Stencil.html).  
  
Additional resources: [SetGlobalColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalColor.html), [SetGlobalFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetGlobalFloat.html); [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) class, [ShaderLab documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html), [RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html).
* * *
