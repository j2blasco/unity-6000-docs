* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.GetSourceTextureWidthAndHeight.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).GetSourceTextureWidthAndHeight
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html "Go to TextureImporter Component in the Manual")
## Declaration
public void GetSourceTextureWidthAndHeight(out int width, out int height); 
### Parameters
Parameter | Description  
---|---  
width | The source texture's width.  
height | The source texture's height.  
### Description
Gets the source texture's width and height.
Texture importer settings can affect the width and height of the imported texture. This method provides the source image's dimensions. This method throws an exception if the texture has not finished importing. For example, it would throw an exception if you called this method in an [AssetPostprocessor.OnPreprocessAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPreprocessAsset.html) callback. 
* * *
