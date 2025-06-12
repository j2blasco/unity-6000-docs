* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.CreateRenderTargets.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).CreateRenderTargets
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
public void CreateRenderTargets([RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) colorFormat); 
### Parameters
Parameter | Description  
---|---  
colorFormat | Render Texture format.  
### Description
Creates the `sourceRenderTexture` and `destinationRenderTexture`.
The render textures are created at a resolution matching the current [PaintContext.pixelRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-pixelRect.html), using the specified [RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html).  
  
This function is called internally by [TerrainPaintUtility.BeginPaintHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.BeginPaintHeightmap.html), [TerrainPaintUtility.BeginPaintTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.BeginPaintTexture.html) and [TerrainPaintUtility.CollectNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.CollectNormals.html).  
  
Additional resources: [PaintContext.destinationRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-destinationRenderTexture.html), [PaintContext.sourceRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-sourceRenderTexture.html)
* * *
