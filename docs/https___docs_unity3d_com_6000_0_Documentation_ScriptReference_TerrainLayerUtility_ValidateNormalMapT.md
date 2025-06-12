* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayerUtility.ValidateNormalMapTextureUI.html

#  [TerrainLayerUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayerUtility.html).ValidateNormalMapTextureUI
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
public static void ValidateNormalMapTextureUI([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, bool normalMapTextureType); 
### Parameters
Parameter | Description  
---|---  
texture | The texture to validate.  
normalMapTextureType | The return value from the [CheckNormalMapTextureType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayerUtility.CheckNormalMapTextureType.html) method indicating whether the texture is imported as a normal map.  
### Description
Checks whether the texture is a valid TerrainLayer normal map texture. If it detects that the texture is not valid, it displays a warning message that identifies the issue.
A valid normal map texture must be correctly imported as a normal map, have [Repeat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.Repeat.html) wrap mode and mipmaps enabled.
* * *
