* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.HasShaderDefine.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).HasShaderDefine
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
public static bool HasShaderDefine([Rendering.GraphicsTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTier.html) tier, [Rendering.BuiltinShaderDefine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderDefine.html) defineHash); 
### Description
Returns true if shader define was set when compiling shaders for current [GraphicsTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTier.html). Graphics Tiers are only available in the Built-in Render Pipeline.
* * *
## Declaration
public static bool HasShaderDefine([Rendering.BuiltinShaderDefine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderDefine.html) defineHash); 
### Description
Returns true if shader define was set when compiling shaders for a given [GraphicsTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTier.html). Graphics Tiers are only available in the Built-in Render Pipeline.
* * *
