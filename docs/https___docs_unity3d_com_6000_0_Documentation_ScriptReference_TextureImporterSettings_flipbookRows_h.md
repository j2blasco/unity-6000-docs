* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-flipbookRows.html

#  [TextureImporterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html).flipbookRows
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
flipbookRows; 
### Description
The number of rows in the source image for a Texture2DArray or Texture3D.
When Unity imports a texture with a [textureShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-textureShape.html) of [TextureImporterShape.Texture2DArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterShape.Texture2DArray.html) or [TextureImporterShape.Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterShape.Texture3D.html), it divides the source image into cells. Each cell is imported into its own layer or depth slice of the resulting texture. You can set the number of cells using the [flipbookColumns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-flipbookColumns.html) and [flipbookRows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings-flipbookRows.html) settings.
* * *
