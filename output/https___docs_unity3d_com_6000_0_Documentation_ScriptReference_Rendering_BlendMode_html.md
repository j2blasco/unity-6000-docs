* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.html

# BlendMode
enumeration
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
### Description
Blend mode for controlling the blending.
The blend mode is set separately for source and destination, and it controls the blend factor of each component going into the blend equation. It is also possible to set the blend mode for color and alpha components separately. Note: the blend modes are ignored if logical blend operations or advanced OpenGL blend operations are in use.
### Properties
Property | Description  
---|---  
[Zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.Zero.html) | Blend factor is (0, 0, 0, 0).  
[One](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.One.html) | Blend factor is (1, 1, 1, 1).  
[DstColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.DstColor.html) | Blend factor is (Rd, Gd, Bd, Ad).  
[SrcColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.SrcColor.html) | Blend factor is (Rs, Gs, Bs, As).  
[OneMinusDstColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.OneMinusDstColor.html) | Blend factor is (1 - Rd, 1 - Gd, 1 - Bd, 1 - Ad).  
[SrcAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.SrcAlpha.html) | Blend factor is (As, As, As, As).  
[OneMinusSrcColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.OneMinusSrcColor.html) | Blend factor is (1 - Rs, 1 - Gs, 1 - Bs, 1 - As).  
[DstAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.DstAlpha.html) | Blend factor is (Ad, Ad, Ad, Ad).  
[OneMinusDstAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.OneMinusDstAlpha.html) | Blend factor is (1 - Ad, 1 - Ad, 1 - Ad, 1 - Ad).  
[SrcAlphaSaturate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.SrcAlphaSaturate.html) | Blend factor is (f, f, f, 1); where f = min(As, 1 - Ad).  
[OneMinusSrcAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.OneMinusSrcAlpha.html) | Blend factor is (1 - As, 1 - As, 1 - As, 1 - As).  
* * *
