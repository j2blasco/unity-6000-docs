* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TextureGenerator.GenerateTexture.html

#  [TextureGenerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TextureGenerator.html).GenerateTexture
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
public static [AssetImporters.TextureGenerationOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TextureGenerationOutput.html) GenerateTexture([AssetImporters.TextureGenerationSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TextureGenerationSettings.html) settings, NativeArray<Color> colorBuffer); 
## Declaration
public static [AssetImporters.TextureGenerationOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TextureGenerationOutput.html) GenerateTexture([AssetImporters.TextureGenerationSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TextureGenerationSettings.html) settings, NativeArray<Color32> colorBuffer); 
### Parameters
Parameter | Description  
---|---  
settings | Settings use for generating [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) and [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).  
colorBuffer | Color buffer for generating [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) and [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).  
### Returns
**TextureGenerationOutput** Result of the generation. 
### Description
Generates [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) and [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) Assets based on the settings provided.
* * *
