* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html

# TerrainData
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
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
The TerrainData class stores heightmaps, detail mesh positions, tree instances, and terrain texture alpha maps.
The [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html) component links to the terrain data and renders it.
### Static Properties
Property | Description  
---|---  
[AlphamapTextureName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.AlphamapTextureName.html) | The name for the Terrain alpha map textures.  
[HolesTextureName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.HolesTextureName.html) | The name for the Terrain holes Texture.  
### Properties
Property | Description  
---|---  
[alphamapHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-alphamapHeight.html) | Height of the alpha map. (Read only.)  
[alphamapLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-alphamapLayers.html) | Number of alpha map layers.  
[alphamapResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-alphamapResolution.html) | The size of the alpha map in texels for either the width or the height.  
[alphamapTextureCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-alphamapTextureCount.html) | Returns the number of alphamap textures.  
[alphamapTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-alphamapTextures.html) | Alpha map textures used by the Terrain. Used by Terrain Inspector for undo.  
[alphamapWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-alphamapWidth.html) | Width of the alpha map.  
[baseMapResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-baseMapResolution.html) | Resolution of the base map used for rendering far patches on the terrain.  
[bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-bounds.html) | The local bounding box of the TerrainData object.  
[detailHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-detailHeight.html) | The resolution of the detail data stored in TerrainData.  
[detailPatchCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-detailPatchCount.html) | The number of patches along a terrain tile edge. This is squared to make a grid of patches.  
[detailPrototypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-detailPrototypes.html) | Contains the detail texture/meshes that the Terrain has.  
[detailResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-detailResolution.html) | Detail Resolution of the TerrainData.  
[detailResolutionPerPatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-detailResolutionPerPatch.html) | Detail Resolution of each patch. A larger value will decrease the number of batches used by detail objects.  
[detailScatterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-detailScatterMode.html) | Additional resources: DetailScatterMode  
[detailWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-detailWidth.html) | The resolution of the detail data stored in TerrainData.  
[enableHolesTextureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-enableHolesTextureCompression.html) | Enable the Terrain holes Texture compression.  
[heightmapResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-heightmapResolution.html) | The size of the heightmap in texels for both the width and height. When setting the heightmap resolution, Unity clamps the value to one of 33, 65, 129, 257, 513, 1025, 2049, or 4097.  
[heightmapScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-heightmapScale.html) | Returns a Vector3 where the x and z components are the size of each heightmap sample (i.e. the space between two neighboring heightmap samples), and the y component is the entire Terrain's height range in world space.  
[heightmapTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-heightmapTexture.html) | Returns the heightmap texture.  
[holesResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-holesResolution.html) | Returns the Terrain holes resolution for both the data and the Texture.  
[holesTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-holesTexture.html) | Returns the Terrain holes Texture.  
[maxDetailScatterPerRes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-maxDetailScatterPerRes.html) | The maximum value of each sample in the detail map of the terrain data.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-size.html) | The total size in world units of the terrain: width, height, and length.  
[terrainLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-terrainLayers.html) | Retrieves the terrain layers used by the current terrain.  
[treeInstanceCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-treeInstanceCount.html) | Returns the number of tree instances.  
[treeInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-treeInstances.html) | Contains the current trees placed in the terrain.  
[treePrototypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-treePrototypes.html) | The list of TreePrototypes available in the inspector.  
[wavingGrassAmount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-wavingGrassAmount.html) | Amount of waving grass in the terrain.  
[wavingGrassSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-wavingGrassSpeed.html) | Speed of the waving grass.  
[wavingGrassStrength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-wavingGrassStrength.html) | Strength of the waving grass in the terrain.  
[wavingGrassTint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData-wavingGrassTint.html) | Color of the waving grass that the terrain has.  
### Public Methods
Method | Description  
---|---  
[ComputeDetailCoverage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.ComputeDetailCoverage.html) | This function computes and returns the coverage (how many instances fit in a square unit) of a detail prototype, given its index.  
[ComputeDetailInstanceTransforms](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.ComputeDetailInstanceTransforms.html) | This function computes and returns an array of detail object transforms for the specified patch and the specified prototype. You can use this function to retrieve the exact same transform data the Unity engine uses for detail rendering.  
[CopyActiveRenderTextureToHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.CopyActiveRenderTextureToHeightmap.html) | Copies the specified part of the active RenderTexture to the Terrain heightmap texture.  
[CopyActiveRenderTextureToTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.CopyActiveRenderTextureToTexture.html) | Copies the specified part of the active RenderTexture to the Terrain texture.  
[DirtyHeightmapRegion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.DirtyHeightmapRegion.html) | Marks the specified part of the heightmap as dirty.  
[DirtyTextureRegion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.DirtyTextureRegion.html) | Marks the specified part of the Terrain texture as dirty.  
[GetAlphamaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetAlphamaps.html) | Returns the alpha map at a position x, y given a width and height.  
[GetAlphamapTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetAlphamapTexture.html) | Returns the alphamap texture at the specified index.  
[GetClampedDetailPatches](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetClampedDetailPatches.html) | Returns an array of detail patches, which are each identified by X-Z coordinates. Detail objects in the patches are clamped to the maximum count.  
[GetDetailLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetDetailLayer.html) | Returns a 2D array of the detail object density (i.e. the number of detail objects for this layer) in the specific location.  
[GetHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetHeight.html) | Calculates the height in world space units of a point on the heightmap. x and y are pixel coordinates in the heightmap, and the returned value does not take into account the heightmap's position.  
[GetHeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetHeights.html) | Gets an array of heightmap samples.  
[GetHoles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetHoles.html) | Gets an array of Terrain holes samples.  
[GetInterpolatedHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetInterpolatedHeight.html) | Gets an interpolated height at a point x,y. The x and y coordinates are clamped to [0, 1].  
[GetInterpolatedHeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetInterpolatedHeights.html) | Gets an array of terrain height values using the normalized x,y coordinates.  
[GetInterpolatedNormal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetInterpolatedNormal.html) | Get an interpolated normal at a given location.  
[GetMaximumHeightError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetMaximumHeightError.html) | Returns an array of tesselation maximum height error values per renderable terrain patch. The returned array can be modified and passed to OverrideMaximumHeightError.  
[GetPatchMinMaxHeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetPatchMinMaxHeights.html) | Returns an array of min max height values for all the renderable patches in a terrain. The returned array can be modified and then passed to OverrideMinMaxPatchHeights.  
[GetSteepness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetSteepness.html) | Gets the gradient of the terrain at point (x,y). The gradient's value is always positive.  
[GetSupportedLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetSupportedLayers.html) | Returns an array of all supported detail layer indices in the area.  
[GetTreeInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.GetTreeInstance.html) | Gets the tree instance at the specified index. It is used as a faster version of treeInstances[index] as this function doesn't create the entire tree instances array.  
[IsHole](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.IsHole.html) | Gets whether a certain point at x,y is a hole.  
[OverrideMaximumHeightError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.OverrideMaximumHeightError.html) | Override the maximum tessellation height error with user provided values. Note that the overriden values get reset when the terrain resolution is changed and stays unchanged when the terrain heightmap is painted or changed via script.  
[OverrideMinMaxPatchHeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.OverrideMinMaxPatchHeights.html) | Override the minimum and maximum patch heights for every renderable terrain patch. Note that the overriden values get reset when the terrain resolution is changed and stays unchanged when the terrain heightmap is painted or changed via script.  
[RefreshPrototypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.RefreshPrototypes.html) | Reloads all the values of the available prototypes (ie, detail mesh assets) in the TerrainData Object.  
[RemoveDetailPrototype](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.RemoveDetailPrototype.html) | Removes the detail prototype at the specified index.  
[SetAlphamaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetAlphamaps.html) | Assign all splat values in the given map area.  
[SetBaseMapDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetBaseMapDirty.html) | Marks the terrain data as dirty to trigger an update of the terrain basemap texture.  
[SetDetailLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetDetailLayer.html) | Sets the detail layer density map.  
[SetDetailResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetDetailResolution.html) | Sets the resolution of the detail map.  
[SetDetailScatterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetDetailScatterMode.html) | Sets the DetailScatterMode.  
[SetHeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHeights.html) | Sets an array of heightmap samples.  
[SetHeightsDelayLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHeightsDelayLOD.html) | Sets an array of heightmap samples.  
[SetHoles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHoles.html) | Sets an array of Terrain holes samples.  
[SetHolesDelayLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHolesDelayLOD.html) | Sets an array of Terrain holes samples.  
[SetTerrainLayersRegisterUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetTerrainLayersRegisterUndo.html) | This function sets the terrainLayers property, and in addition, registers the action to the Editor's undo stack.  
[SetTreeInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetTreeInstance.html) | Sets the tree instance with new parameters at the specified index. However, you cannot change TreeInstance.prototypeIndex and TreeInstance.position. If you change them, the method throws an ArgumentException.  
[SetTreeInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetTreeInstances.html) | Sets the Tree Instance array, and optionally snaps Trees onto the surface of the Terrain heightmap.  
[SyncHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SyncHeightmap.html) | Performs synchronization queued by previous calls to CopyActiveRenderTextureToHeightmap and DirtyHeightmapRegion, which makes the height data and LOD data used for tessellation up to date.  
[SyncTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SyncTexture.html) | Performs synchronization queued by previous calls to CopyActiveRenderTextureToTexture and DirtyTextureRegion, which makes CPU data of the Terrain textures up to date.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
