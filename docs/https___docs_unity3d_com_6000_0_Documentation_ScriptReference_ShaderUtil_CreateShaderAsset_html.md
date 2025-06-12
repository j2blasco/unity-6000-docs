* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.CreateShaderAsset.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).CreateShaderAsset
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
public static [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) CreateShaderAsset([AssetImporters.AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) context, string source, bool compileInitialShaderVariants); 
## Declaration
public static [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) CreateShaderAsset(string source, bool compileInitialShaderVariants); 
## Declaration
public static [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) CreateShaderAsset(string source); 
### Parameters
Parameter | Description  
---|---  
context | A context object that the asset system needs to register shader dependencies properly.  
source | A string that contains a shader written in [ShaderLab](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html) code.  
compileInitialShaderVariants | Set to true to compile the [ShaderLab](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html) code contained in the source string; otherwise false.  
### Description
Creates a new [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) object from the provided source code string. You can use this method alongside the [ScriptedImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html) to create custom shader generation tools in the Editor.
* * *
