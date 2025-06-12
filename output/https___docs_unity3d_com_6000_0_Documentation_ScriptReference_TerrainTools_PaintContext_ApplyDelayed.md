* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ApplyDelayedActions.html

#  [PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html).ApplyDelayedActions
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
public static void ApplyDelayedActions(); 
### Description
Flushes the delayed actions created by PaintContext heightmap and alphamap modifications.
Expensive updates that would cause performance issues during painting and sculpting are deferred until the user finishes interacting with them. [PaintContext.ScatterAlphamap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterAlphamap.html) creates a delayed action to rebuild basemap LOD textures. [PaintContext.ScatterHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterHeightmap.html) creates a delayed action to rebuild collision, physics, pixel error metrics, visibility bounding boxes, and grass, tree, and detail positions. ApplyDelayedActions will immediately apply these delayed actions. ApplyDelayedActions is called automatically on mouse button up, and when the terrain inspector is closed (OnDisable). 
* * *
