* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.html

# PaintContext
class in UnityEngine.TerrainTools
/
Implemented in:[UnityEngine.TerrainModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.TerrainModule.html)
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
The context for a paint operation that may span multiple connected Terrain tiles.
This class is used to apply an edit operation to an area of Terrain that may span multiple Terrain tiles. A PaintContext may be used to edit heightmap or splatmap data, and may also be used to gather normal data in read-only mode (you cannot write to normals, because they are derived from the heightmap).  
  
A PaintContext will calculate the relevant regions on each Terrain, and collect the original data into a single sourceRenderTarget. Your edit operation can then read from sourcerenderTarget, and write the modified data to destinationRenderTarget. Once you have applied your edit operation, the PaintContext can also write the modified data in destinationRenderTarget back to each Terrain, ensuring no seams between them.  
  
The simplest way to use a PaintContext is through the helper functions in TerrainPaintUtility:  
[TerrainPaintUtility.BeginPaintHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.BeginPaintHeightmap.html), [TerrainPaintUtility.EndPaintHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.EndPaintHeightmap.html), [TerrainPaintUtility.BeginPaintTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.BeginPaintTexture.html), [TerrainPaintUtility.EndPaintTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.EndPaintTexture.html), [TerrainPaintUtility.CollectNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.CollectNormals.html) and [TerrainPaintUtility.ReleaseContextResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtility.ReleaseContextResources.html).  
  
You can also use PaintContext more directly through its member functions. In general, they are used in the following order:  
1) Constructor, [PaintContext.CreateFromBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.CreateFromBounds.html) - Construct a PaintContext with a target Terrain and a region to edit  
2) [PaintContext.CreateRenderTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.CreateRenderTargets.html) - Create the source and destination RenderTargets  
3) [PaintContext.GatherHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherHeightmap.html), [PaintContext.GatherAlphamap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherAlphamap.html), [PaintContext.GatherNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherNormals.html) - Read from Terrain tiles into sourceRenderTarget  
4) Apply editing operations, reading from sourceRenderTarget, and writing to destinationRenderTarget  
5) [PaintContext.ScatterHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterHeightmap.html), [PaintContext.ScatterAlphamap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterAlphamap.html) - Write from destinationRenderTarget into Terrain tiles (optional)  
6) [PaintContext.Cleanup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Cleanup.html) - Destroy RenderTarget resources (required if you call CreateRenderTargets)  
7) [PaintContext.ApplyDelayedActions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ApplyDelayedActions.html) - Apply any delayed actions that perform expensive updates  
  
  
Additional resources: [TerrainPaintTool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintTool_1.html)
### Static Properties
Property | Description  
---|---  
[kNormalizedHeightScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-kNormalizedHeightScale.html) | Unity uses this value internally to transform a [0, 1] height value to a texel value, which is stored in TerrainData.heightmapTexture.  
### Properties
Property | Description  
---|---  
[destinationRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-destinationRenderTexture.html) | (Read Only) RenderTexture that an edit operation writes to modify the data.  
[heightWorldSpaceMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-heightWorldSpaceMin.html) | The minimum height of all Terrain tiles that this PaintContext touches in world space.  
[heightWorldSpaceSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-heightWorldSpaceSize.html) | The height range (from Min to Max) of all Terrain tiles that this PaintContext touches in world space.  
[oldRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-oldRenderTexture.html) | (Read Only) The value of RenderTexture.active at the time CreateRenderTargets is called.  
[originTerrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-originTerrain.html) | (Read Only) The Terrain used to build the PaintContext.  
[pixelRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-pixelRect.html) | (Read Only) The pixel rectangle that this PaintContext represents.  
[pixelSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-pixelSize.html) | (Read Only) The size of a PaintContext pixel in terrain units (as defined by originTerrain.)  
[sourceRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-sourceRenderTexture.html) | (Read Only) Render target that stores the original data from the Terrain tiles.  
[targetTextureHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-targetTextureHeight.html) | (Read Only) The height of the target terrain texture. This is the resolution for a single Terrain.  
[targetTextureWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-targetTextureWidth.html) | (Read Only) The width of the target terrain texture. This is the resolution for a single Terrain.  
[terrainCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-terrainCount.html) | (Read Only) The number of Terrain tiles in this PaintContext.  
### Constructors
Constructor | Description  
---|---  
[PaintContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext-ctor.html) | Creates a new PaintContext, to edit a target texture on a Terrain, in a region defined by pixelRect.  
### Public Methods
Method | Description  
---|---  
[Cleanup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Cleanup.html) | Releases the allocated resources of this PaintContext.  
[CreateRenderTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.CreateRenderTargets.html) | Creates the sourceRenderTexture and destinationRenderTexture.  
[Gather](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Gather.html) | Gathers user-specified Texture data into sourceRenderTexture.  
[GatherAlphamap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherAlphamap.html) | Gathers the alphamap information into sourceRenderTexture.  
[GatherHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherHeightmap.html) | Gathers the heightmap information into sourceRenderTexture.  
[GatherHoles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherHoles.html) | Gathers the Terrain holes information into sourceRenderTexture.  
[GatherNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GatherNormals.html) | Gathers the normal information into sourceRenderTexture.  
[GetClippedPixelRectInRenderTexturePixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GetClippedPixelRectInRenderTexturePixels.html) | Retrieves the clipped pixel rectangle for a Terrain, relative to the PaintContext render textures.  
[GetClippedPixelRectInTerrainPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GetClippedPixelRectInTerrainPixels.html) | Retrieves the clipped pixel rectangle for a Terrain.  
[GetTerrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.GetTerrain.html) | Retrieves a Terrain from the PaintContext.  
[Scatter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.Scatter.html) | Applies an edited PaintContext by copying modifications back to user-specified RenderTextures for the source Terrain tiles.  
[ScatterAlphamap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterAlphamap.html) | Applies an edited alphamap PaintContext by copying modifications back to the source Terrain tiles.  
[ScatterHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterHeightmap.html) | Applies an edited heightmap PaintContext by copying modifications back to the source Terrain tiles.  
[ScatterHoles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ScatterHoles.html) | Applies an edited Terrain holes PaintContext by copying modifications back to the source Terrain tiles.  
### Static Methods
Method | Description  
---|---  
[ApplyDelayedActions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.ApplyDelayedActions.html) | Flushes the delayed actions created by PaintContext heightmap and alphamap modifications.  
[CreateFromBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintContext.CreateFromBounds.html) | Constructs a PaintContext that you can use to edit a texture on a Terrain, in the region defined by boundsInTerrainSpace and extraBorderPixels.  
* * *
