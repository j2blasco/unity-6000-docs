* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html

# Terrain
class in UnityEngine
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
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
The Terrain component renders the terrain.
### Static Properties
Property | Description  
---|---  
[activeTerrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-activeTerrain.html) | The active Terrain. This is a convenient function to get to the main Terrain in the Scene.  
[activeTerrains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-activeTerrains.html) | The active terrains in the Scene.  
[compressedHolesFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-compressedHolesFormat.html) | Graphics format of the Terrain holes Texture when it is compressed.  
[compressedHolesTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-compressedHolesTextureFormat.html) | Texture format of the Terrain holes Texture when it is compressed.  
[heightmapFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-heightmapFormat.html) | Graphics format of the Terrain heightmap.  
[heightmapRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-heightmapRenderTextureFormat.html) | RenderTextureFormat of the terrain heightmap.  
[holesFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-holesFormat.html) | Graphics format of the Terrain holes Texture when it is not compressed.  
[holesRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-holesRenderTextureFormat.html) | Render texture format of the Terrain holes Texture.  
[normalmapFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-normalmapFormat.html) | Graphics format of the Terrain normal map texture.  
[normalmapRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-normalmapRenderTextureFormat.html) | Render texture format of the Terrain normal map texture.  
[normalmapTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-normalmapTextureFormat.html) | Texture format of the Terrain normal map texture.  
### Properties
Property | Description  
---|---  
[allowAutoConnect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-allowAutoConnect.html) | Specifies if the terrain tile will be automatically connected to adjacent tiles.  
[bakeLightProbesForTrees](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-bakeLightProbesForTrees.html) | Whether to bake an array of internal light probes for Tree Editor trees (Editor only).  
[basemapDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-basemapDistance.html) | Heightmap patches beyond basemap distance will use a precomputed low res basemap.  
[bottomNeighbor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-bottomNeighbor.html) | Terrain bottom neighbor.  
[collectDetailPatches](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-collectDetailPatches.html) | Collect detail patches from memory.  
[deringLightProbesForTrees](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-deringLightProbesForTrees.html) | Removes ringing from light probes on Tree Editor trees (Editor only).  
[detailObjectDensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-detailObjectDensity.html) | Density of detail objects.  
[detailObjectDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-detailObjectDistance.html) | Detail objects will be displayed up to this distance.  
[drawHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-drawHeightmap.html) | Indicates whether Unity draws the Terrain geometry itself.  
[drawInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-drawInstanced.html) | Set to true to enable the terrain instance renderer. The default value is false.  
[drawTreesAndFoliage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-drawTreesAndFoliage.html) | Specify if terrain trees and details should be drawn. If disabled, this will also disable updates to renderer positions for trees and details. Tree and detail renderer positions will update again once this setting is re-enabled.  
[editorRenderFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-editorRenderFlags.html) | Controls what part of the terrain should be rendered.  
[enableHeightmapRayTracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-enableHeightmapRayTracing.html) | When this options is enabled, Terrain heightmap geometries will be added in acceleration structures used for Ray Tracing.  
[groupingID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-groupingID.html) | Grouping ID for auto connect.  
[heightmapMaximumLOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-heightmapMaximumLOD.html) | Limits the Terrain's maximum rendering resolution.  
[heightmapMinimumLODSimplification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-heightmapMinimumLODSimplification.html) | Limits how simplified the rendered terrain can be.  
[heightmapPixelError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-heightmapPixelError.html) | An approximation of how many pixels the terrain will pop in the worst case when switching lod.  
[ignoreQualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-ignoreQualitySettings.html) | When enabled, the terrain ignores the terrain overrides set in the QualitySettings.  
[keepUnusedRenderingResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-keepUnusedRenderingResources.html) | Defines whether Unity frees per-Camera rendering resources for the Terrain when those resources aren't in use after a certain number of frames.  
[leftNeighbor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-leftNeighbor.html) | The Terrain tile to the left, which is in the negative X direction.  
[lightmapIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-lightmapIndex.html) | The index of the baked lightmap applied to this terrain.  
[lightmapScaleOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-lightmapScaleOffset.html) | The UV scale & offset used for a baked lightmap.  
[materialTemplate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-materialTemplate.html) | The custom material Unity uses to render the Terrain.  
[normalmapTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-normalmapTexture.html) | Returns the normal map texture computed from sampling the heightmap. It is only used when terrain is rendered using instancing.  
[patchBoundsMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-patchBoundsMultiplier.html) | Set the terrain bounding box scale.  
[preserveTreePrototypeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-preserveTreePrototypeLayers.html) | Allows you to specify how Unity chooses the layer for tree instances.  
[realtimeLightmapIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-realtimeLightmapIndex.html) | The index of the realtime lightmap applied to this terrain.  
[realtimeLightmapScaleOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-realtimeLightmapScaleOffset.html) | The UV scale & offset used for a realtime lightmap.  
[reflectionProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-reflectionProbeUsage.html) | How reflection probes are used for terrain. See ReflectionProbeUsage.  
[renderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-renderingLayerMask.html) | Determines which rendering layers the Terrain renderer lives on.  
[rightNeighbor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-rightNeighbor.html) | The Terrain tile to the left, which is in the positive X direction.  
[shadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-shadowCastingMode.html) | Allows you to set the shadow casting mode for the terrain.  
[terrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-terrainData.html) | The Terrain Data that stores heightmaps, terrain textures, detail meshes and trees.  
[topNeighbor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-topNeighbor.html) | Terrain top neighbor.  
[treeBillboardDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-treeBillboardDistance.html) | Distance from the camera where trees will be rendered as billboards only.  
[treeCrossFadeLength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-treeCrossFadeLength.html) | Total distance delta that trees will use to transition from billboard orientation to mesh orientation.  
[treeDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-treeDistance.html) | The maximum distance at which trees are rendered.  
[treeLODBiasMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-treeLODBiasMultiplier.html) | The multiplier to the current LOD bias used for rendering LOD trees (i.e. SpeedTree trees).  
[treeMaximumFullLODCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-treeMaximumFullLODCount.html) | Maximum number of trees rendered at full LOD.  
[treeMotionVectorModeOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-treeMotionVectorModeOverride.html) | The motion vector rendering mode for all SpeedTree models painted on the terrain.   
### Public Methods
Method | Description  
---|---  
[AddTreeInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.AddTreeInstance.html) | Adds a tree instance to the terrain.  
[Flush](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.Flush.html) | Flushes any change done in the terrain so it takes effect.  
[GetClosestReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.GetClosestReflectionProbes.html) | Fills the list with reflection probes whose AABB intersects with terrain's AABB. Their weights are also provided. Weight shows how much influence the probe has on the terrain, and is used when the blending between multiple reflection probes occurs.  
[GetKeepUnusedCameraRenderingResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.GetKeepUnusedCameraRenderingResources.html) |   
[GetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.GetPosition.html) | Get the world space position of the terrain.  
[GetSplatMaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.GetSplatMaterialPropertyBlock.html) | Get the previously set splat material properties by copying to the dest MaterialPropertyBlock object.  
[SampleHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.SampleHeight.html) | Samples the height at the given position defined in world space, relative to the Terrain space.  
[SetKeepUnusedCameraRenderingResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.SetKeepUnusedCameraRenderingResources.html) | Defines whether Unity cleans up rendering resources for a given Camera during garbage collection.  
[SetNeighbors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.SetNeighbors.html) | Lets you set up the connection between neighboring Terrain tiles. This ensures LOD matches up on neighboring Terrain tiles.  
[SetSplatMaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.SetSplatMaterialPropertyBlock.html) | Set the additional material properties when rendering the terrain heightmap using the splat material.  
### Static Methods
Method | Description  
---|---  
[CreateTerrainGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.CreateTerrainGameObject.html) | Creates a Terrain including collider from TerrainData.  
[GetActiveTerrains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.GetActiveTerrains.html) | Populates a List of Terrains with the active Terrains in the Scene.  
[SetConnectivityDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.SetConnectivityDirty.html) | Marks the current connectivity status as invalid.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
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
