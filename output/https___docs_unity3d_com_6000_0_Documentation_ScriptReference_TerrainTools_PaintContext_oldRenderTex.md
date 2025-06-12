* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-oldRenderTexture.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).oldRenderTexture
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
[RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) oldRenderTexture; 
### Description
(Read Only) The value of RenderTexture.active at the time CreateRenderTargets is called.
[PaintContext.Cleanup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Cleanup.html) uses this value to restore the active RenderTexture to its original value. In some cases, it may be necessary to manually restore the RenderTexture before calling Cleanup:  
`RenderTexture.active = PaintContext.oldRenderTexture;`  
  
  
Additional resources: [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html), [PaintContext.Cleanup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Cleanup.html)
* * *
