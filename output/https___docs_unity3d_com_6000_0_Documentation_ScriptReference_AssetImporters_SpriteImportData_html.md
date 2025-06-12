* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SpriteImportData.html

# SpriteImportData
struct in UnityEditor.AssetImporters
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
Struct that represents how [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) asset should be generated when calling [TextureGenerator.GenerateTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TextureGenerator.GenerateTexture.html).
### Properties
Property | Description  
---|---  
[alignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SpriteImportData-alignment.html) | Pivot value represented by SpriteAlignment.  
[border](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SpriteImportData-border.html) | Border value for the generated Sprite.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SpriteImportData-name.html) | Name for the generated Sprite.  
[outline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SpriteImportData-outline.html) | Sprite Asset creation uses this outline when it generates the Mesh for the Sprite. If this is not given, SpriteImportData.tesselationDetail will be used to determine the mesh detail.  
[pivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SpriteImportData-pivot.html) | Pivot value represented in Vector2.  
[rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SpriteImportData-rect.html) | Position and size of the Sprite in a given texture.  
[spriteID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SpriteImportData-spriteID.html) | An identifier given to a Sprite. Use this to identify which data was used to generate that Sprite.  
[tessellationDetail](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SpriteImportData-tessellationDetail.html) | Controls mesh generation detail. This value will be ignored if SpriteImportData.ouline is provided.  
* * *
