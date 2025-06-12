* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.html

# LightmapParameters
class in UnityEditor
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html "Go to LightmapParameters Component in the Manual")
### Description
Configures how Unity bakes lighting and can be assigned to a [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) instance or asset.
Note that Unity's built-in Lightmap Parameters Assets are read-only.  
  
Additional resources: [LightmapParameters.SetLightmapParametersForLightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.SetLightmapParametersForLightingSettings.html).
### Properties
Property | Description  
---|---  
[antiAliasingSamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-antiAliasingSamples.html) | The kernel width the lightmapper uses when sampling a lightmap texel.  
[AOAntiAliasingSamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.AOAntiAliasingSamples.html) | The maximum number of times to supersample a texel to reduce aliasing in AO.  
[AOQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.AOQuality.html) | The number of rays to cast for computing ambient occlusion.  
[backFaceTolerance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-backFaceTolerance.html) | The percentage of rays shot from a ray origin that must hit front faces to be considered usable.  
[bakedLightmapTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-bakedLightmapTag.html) | BakedLightmapTag is an integer that affects the assignment to baked lightmaps. Objects with different values for bakedLightmapTag are guaranteed to not be assigned to the same lightmap even if the other baking parameters are the same.  
[blurRadius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-blurRadius.html) | The radius (in texels) of the post-processing filter that blurs baked direct lighting.  
[clusterResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-clusterResolution.html) | Controls the resolution at which Enlighten Realtime Global Illumination stores and can transfer input light.  
[directLightQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-directLightQuality.html) | The number of rays used for lights with an area. Allows for accurate soft shadowing.  
[irradianceBudget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-irradianceBudget.html) | The amount of data used for Enlighten Realtime Global Illumination texels. Specifies how detailed view of the Scene a texel has. Small values mean more averaged out lighting.  
[irradianceQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-irradianceQuality.html) | The number of rays to cast for computing irradiance form factors.  
[isTransparent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-isTransparent.html) | If enabled, the object appears transparent during GlobalIllumination lighting calculations.  
[limitLightmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-limitLightmapCount.html) | If enabled, objects sharing the same lightmap parameters will be packed into LightmapParameters.maxLightmapCount lightmaps.  
[maxLightmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-maxLightmapCount.html) | The maximum number of lightmaps created for objects sharing the same lightmap parameters. This property is ignored if LightmapParameters.limitLightmapCount is false.  
[modellingTolerance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-modellingTolerance.html) | Maximum size of gaps that can be ignored for GI (multiplier on pixel size).  
[pushoff](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-pushoff.html) | The distance to offset the ray origin from the geometry when performing ray tracing, in modelling units. Unity applies the offset to all baked lighting: direct lighting, indirect lighting, environment lighting and ambient occlusion.  
[resolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-resolution.html) | The texel resolution per meter used for real-time lightmaps. This value is multiplied by LightingSettings.indirectResolution.  
[stitchEdges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-stitchEdges.html) | Whether pairs of edges should be stitched together.  
[systemTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-systemTag.html) | System tag is an integer identifier. It lets you force an object into a different Enlighten Realtime Global Illumination system even though all the other parameters are the same.  
### Public Methods
Method | Description  
---|---  
[AssignToLightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.AssignToLightingSettings.html) | Assignes itself to a LightingSettings instance or asset.  
### Static Methods
Method | Description  
---|---  
[GetLightmapParametersForLightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.GetLightmapParametersForLightingSettings.html) | Returns the assigned LightmapParameters for the specified LightingSettings.  
[SetLightmapParametersForLightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.SetLightmapParametersForLightingSettings.html) | Sets the LightmapParameters for the specified LightingSettings.  
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
