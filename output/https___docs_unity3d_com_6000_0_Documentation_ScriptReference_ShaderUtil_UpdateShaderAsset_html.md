* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.UpdateShaderAsset.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).UpdateShaderAsset
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
public static void UpdateShaderAsset([AssetImporters.AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) context, [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader, string source, bool compileInitialShaderVariants); 
## Declaration
public static void UpdateShaderAsset([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader, string source, bool compileInitialShaderVariants); 
## Declaration
public static void UpdateShaderAsset([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader, string source); 
### Parameters
Parameter | Description  
---|---  
context | A context object that the asset system needs to register shader dependencies properly.  
source | A string that contains a shader written in [ShaderLab](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html) code.  
compileInitialShaderVariants | Set to true to compile the [ShaderLab](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html) code contained in the source string; otherwise false.  
shader | The [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) to update.  
### Description
Replaces the existing source code in the specified shader with the source code in the supplied string.
* * *
