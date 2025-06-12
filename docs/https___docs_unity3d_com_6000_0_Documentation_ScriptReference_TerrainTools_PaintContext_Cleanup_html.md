* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Cleanup.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).Cleanup
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
public void Cleanup(bool restoreRenderTexture); 
### Parameters
Parameter | Description  
---|---  
restoreRenderTexture | When true, indicates that this function restores RenderTexture.active  
### Description
Releases the allocated resources of this PaintContext.
This function releases the `sourceRenderTexture` and `destinationRenderTexture`. When restoreRenderTexture is true, it also restores RenderTexture.active to the value saved as _oldRenderTexture. This function is called internally by [TerrainPaintUtility.EndPaintHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.EndPaintHeightmap.html), [TerrainPaintUtility.EndPaintTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.EndPaintTexture.html) and [TerrainPaintUtility.ReleaseContextResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.ReleaseContextResources.html). 
* * *
