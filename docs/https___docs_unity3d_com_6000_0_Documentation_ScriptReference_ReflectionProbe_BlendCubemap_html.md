* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.BlendCubemap.html

#  [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html).BlendCubemap
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html "Go to ReflectionProbe Component in the Manual")
## Declaration
public static bool BlendCubemap([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) dst, float blend, [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) target); 
### Parameters
Parameter | Description  
---|---  
src | Cubemap to blend from.  
dst | Cubemap to blend to.  
blend | Blend weight.  
target | RenderTexture which will hold the result of the blend.  
### Returns
**bool** Returns trues if cubemaps were blended, false otherwise. 
### Description
Utility method to blend 2 cubemaps into a target render texture.
* * *
