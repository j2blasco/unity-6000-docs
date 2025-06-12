* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.html

# BlendOp
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
Blend operation.
The blend operation that is used to combine the pixel shader output with the render target. This can be passed through Material.SetInt() to change the blend operation during runtime.  
  
Note that the logical operations are only supported in Gamma (non-sRGB) colorspace, on DX11.1 hardware running on DirectX 11.1 runtime.  
  
Advanced OpenGL blend operations are supported only on hardware supporting either GL_KHR_blend_equation_advanced or GL_NV_blend_equation_advanced and may require use of [GL.RenderTargetBarrier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.RenderTargetBarrier.html). In addition, the shaders that are used with the advanced blend operations must have a UNITY_REQUIRE_ADVANDED_BLEND(mode) declaration in the shader code where mode is one of the blend operations or "all_equations" for supporting all advanced blend operations (see the KHR_blend_equation_advanced spec for other values).
### Properties
Property | Description  
---|---  
[Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Add.html) | Add (s + d).  
[Subtract](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Subtract.html) | Subtract.  
[ReverseSubtract](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.ReverseSubtract.html) | Reverse subtract.  
[Min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Min.html) | Min.  
[Max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Max.html) | Max.  
[LogicalClear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalClear.html) | Logical Clear (0).  
[LogicalSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalSet.html) | Logical SET (1) (D3D11.1 only).  
[LogicalCopy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalCopy.html) | Logical Copy (s) (D3D11.1 only).  
[LogicalCopyInverted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalCopyInverted.html) | Logical inverted Copy (!s) (D3D11.1 only).  
[LogicalNoop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalNoop.html) | Logical No-op (d) (D3D11.1 only).  
[LogicalInvert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalInvert.html) | Logical Inverse (!d) (D3D11.1 only).  
[LogicalAnd](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalAnd.html) | Logical AND (s & d) (D3D11.1 only).  
[LogicalNand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalNand.html) | Logical NAND !(s & d). D3D11.1 only.  
[LogicalOr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalOr.html) | Logical OR (s | d) (D3D11.1 only).  
[LogicalNor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalNor.html) | Logical NOR !(s | d) (D3D11.1 only).  
[LogicalXor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalXor.html) | Logical XOR (s XOR d) (D3D11.1 only).  
[LogicalEquivalence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalEquivalence.html) | Logical Equivalence !(s XOR d) (D3D11.1 only).  
[LogicalAndReverse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalAndReverse.html) | Logical reverse AND (s & !d) (D3D11.1 only).  
[LogicalAndInverted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalAndInverted.html) | Logical inverted AND (!s & d) (D3D11.1 only).  
[LogicalOrReverse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalOrReverse.html) | Logical reverse OR (s | !d) (D3D11.1 only).  
[LogicalOrInverted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.LogicalOrInverted.html) | Logical inverted OR (!s | d) (D3D11.1 only).  
[Multiply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Multiply.html) | Multiply (Advanced OpenGL blending).  
[Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Screen.html) | Screen (Advanced OpenGL blending).  
[Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Overlay.html) | Overlay (Advanced OpenGL blending).  
[Darken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Darken.html) | Darken (Advanced OpenGL blending).  
[Lighten](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Lighten.html) | Lighten (Advanced OpenGL blending).  
[ColorDodge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.ColorDodge.html) | Color dodge (Advanced OpenGL blending).  
[ColorBurn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.ColorBurn.html) | Color burn (Advanced OpenGL blending).  
[HardLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.HardLight.html) | Hard light (Advanced OpenGL blending).  
[SoftLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.SoftLight.html) | Soft light (Advanced OpenGL blending).  
[Difference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Difference.html) | Difference (Advanced OpenGL blending).  
[Exclusion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.Exclusion.html) | Exclusion (Advanced OpenGL blending).  
[HSLHue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.HSLHue.html) | HSL Hue (Advanced OpenGL blending).  
[HSLSaturation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.HSLSaturation.html) | HSL saturation (Advanced OpenGL blending).  
[HSLColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.HSLColor.html) | HSL color (Advanced OpenGL blending).  
[HSLLuminosity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.HSLLuminosity.html) | HSL luminosity (Advanced OpenGL blending).  
* * *
