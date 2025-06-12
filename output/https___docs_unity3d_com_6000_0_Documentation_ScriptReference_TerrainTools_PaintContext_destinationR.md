* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-destinationRenderTexture.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).destinationRenderTexture
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
[RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) destinationRenderTexture; 
### Description
(Read Only) RenderTexture that an edit operation writes to modify the data.
This RenderTexture stores the modified data represented by a PaintContext. A terrain tool will typically read from `sourceRenderTexture`, modify the data, and write to `destinationRenderTexture`. The Scatter functions ([PaintContext.ScatterHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterHeightmap.html) or [PaintContext.ScatterAlphamap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterAlphamap.html)) read from `destinationRenderTexture` to distribute the modified data back to the source Terrain tiles. `destinationRenderTexture` is created by [PaintContext.CreateRenderTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.CreateRenderTargets.html), with size and format matching `sourceRenderTexture`.  
  
Additional resources: [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html), [PaintContext.sourceRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-sourceRenderTexture.html). 
* * *
