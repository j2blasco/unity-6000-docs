* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.CreateComputeShaderAsset.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).CreateComputeShaderAsset
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
public static [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) CreateComputeShaderAsset([AssetImporters.AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) context, string source); 
### Parameters
Parameter | Description  
---|---  
context | The context object the asset system uses to register shader dependencies.  
source | The string that contains a shader written in HLSL code.  
### Description
Creates a new [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) object from the provided source code string. You can use this method alongside the [ScriptedImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html) to create custom compute shader generation tools in the Editor.
* * *
