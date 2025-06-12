* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainInspectorUtility.TerrainShaderValidationGUI.html

#  [TerrainInspectorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainInspectorUtility.html).TerrainShaderValidationGUI
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
public static void TerrainShaderValidationGUI([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material); 
### Parameters
Parameter | Description  
---|---  
material | The Material to validate.  
### Description
Checks whether a Material is compatible with Terrain.
This method determines whether a Material is intended for Terrain use. If the Material is incompatible with Terrain, Unity displays a warning message that lets you know where to find a shader that is compatible with Terrain. It also explains how you can use the `TerrainCompatible` tag to suppress this warning message. 
* * *
