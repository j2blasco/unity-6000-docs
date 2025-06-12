* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ResolveAntiAliasedSurface.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).ResolveAntiAliasedSurface
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
## Declaration
public void ResolveAntiAliasedSurface(); 
## Declaration
public void ResolveAntiAliasedSurface([RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) target); 
### Parameters
Parameter | Description  
---|---  
target | The render texture to resolve into. If set, the target render texture must have the same dimensions and format as the source.  
### Description
Force an antialiased render texture to be resolved.
If an antialiased render texture has the [bindTextureMS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-bindTextureMS.html) flag set, it will not be automatically resolved. Sometimes, it's useful to have both the resolved and the unresolved version of the texture at different stages of the pipeline. If the target parameter is omitted, the render texture will be resolved into itself.
* * *
