* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TileBaseEditor.RenderStaticPreview.html

#  [TileBaseEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TileBaseEditor.html).RenderStaticPreview
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
public [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) RenderStaticPreview(string assetPath, Object[] subAssets, int width, int height); 
### Parameters
Parameter | Description  
---|---  
assetPath | The asset to operate on.  
subAssets | An array of all Assets at assetPath.  
width | Width of the created texture.  
height | Height of the created texture.  
### Returns
**Texture2D** Generated texture or null. 
### Description
Creates a texture preview for rendering the [TileBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.TileBase.html) asset preview.
* * *
