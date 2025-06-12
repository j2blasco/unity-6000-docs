* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.IsSupported.html

#  [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).IsSupported
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html "Go to ComputeShader Component in the Manual")
## Declaration
public bool IsSupported(int kernelIndex); 
### Parameters
Parameter | Description  
---|---  
kernelIndex | Which kernel to query.  
### Returns
**bool** True if the specified compute kernel is able to run on the current end user device, false otherwise. 
### Description
Allows you to check whether the current end user device supports the features required to run the specified compute shader kernel.
The result of this call depends on which hardware requirements the compute shader in question is expected to rely on (as defined by the `#pragma require <requirement_a> <requirement_b> <requirement_c> ...` shader syntax). This method implicitly refers to the compute shader variant defined by the set of currently enabled shader keywords (the variant that would be run if [ComputeShader.Dispatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.Dispatch.html) were called instead). This means that when the source code of the shader in question contains per-keyword requirements defined using the '#pragma require KEYWORD_A KEYWORD_B ... : <requirement_a> <requirement_b> <requirement_c>...' syntax the result of [IsSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.IsSupported.html) might depend on which shader keywords are enabled.  
  
Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [Declaring and using shader keywords in HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html), [Targeting shader models and GPU features in HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html).
* * *
