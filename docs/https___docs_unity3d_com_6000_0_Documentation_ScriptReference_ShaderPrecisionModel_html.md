* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderPrecisionModel.html

# ShaderPrecisionModel
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
Options for the shader precision model.
This enumeration allows you to change two things: the default sampler precision and the definition of `half`.  
  
The default sampler precision is only relevant to samplers that don't explicitly declare a precision. For example, `sampler2D` uses the default precision, but `sampler2D_float` uses full precision regardless of the default precision.  
  
Regarding the shader type `half`, it is defined as either `float` or `min16float` (see [SL-DataTypesAndPrecision](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-DataTypesAndPrecision.html)). For the purpose of uploading data to buffers, including constant buffers, the size and alignment is 4 bytes in both cases. 
### Properties
Property | Description  
---|---  
[PlatformDefault](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderPrecisionModel.PlatformDefault.html) | Use the target platform defaults. The default sampler precision is half precision on mobile targets and full precision elsewhere. Also, shader type half is defined as min16float on mobile targets and float elsewhere.  
[Unified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderPrecisionModel.Unified.html) | Use full sampler precision by default, and explicitly declare when you want to use lower precision. Refer to SL-DataTypesAndPrecision for more information. In addition, half is defined as min16float on all platforms. This sets BuiltinShaderDefine.UNITY_UNIFIED_SHADER_PRECISION_MODEL when Unity compiles shaders.  
* * *
