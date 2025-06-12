* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html

# LightingSettings
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html "Go to LightingSettings Component in the Manual")
### Description
An object containing settings for precomputing lighting data, that Unity can serialize as a [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html).
When the Unity Editor precomputes lighting data for a Scene that uses the Baked Global Illumination system or the Enlighten Realtime Global Illumination system, it uses settings from a `LightingSettings` object. The same `LightingSettings` object can be assigned to more than one Scene, which makes it possible to share settings across multiple Scenes.  
  
The following example shows how to create a `LightingSettings` object and assign it to the active Scene using the [Lightmapping.lightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-lightingSettings.html) API:
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CreateLightingSettingsExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Create Lighting Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Settings.html)")]
    static void CreateExampleLightingSettings()
    {
        // Create an instance of LightingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html)
        LightingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) lightingSettings = new LightingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html)();  
  
        // Configure the LightingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) object
        lightingSettings.albedoBoost = 8.0f;  
  
        // Assign the LightingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) object to the active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
        Lightmapping.lightingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-lightingSettings.html) = lightingSettings;
    }
}

```

The following example shows how to create a `LightingSettings` object, and save it to disk as a Lighting Settings Asset using the [AssetDatabase.CreateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html) API.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CreateLightingSettingsExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Create Lighting Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Settings.html)")]
    static void SaveExampleLightingSettingsToDisk()
    {
        // Create an instance of LightingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html)
        LightingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) lightingSettings = new LightingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html)();  
  
        // Configure the LightingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) object
        lightingSettings.albedoBoost = 8.0f;  
  
        // Save it to your Project, using the .lighting extension
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(lightingSettings, "Assets/ExampleLightingSettings.lighting");
    }
}

```

Additional resources: [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html).
### Properties
Property | Description  
---|---  
[albedoBoost](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-albedoBoost.html) | The intensity of surface albedo throughout the Scene when considered in lighting calculations. This value influences the energy of light at each bounce. (Editor only).  
[ao](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-ao.html) | Whether to apply ambient occlusion to lightmaps. (Editor only).  
[aoExponentDirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-aoExponentDirect.html) | Determines the degree to which direct lighting is considered when calculating ambient occlusion in lightmaps. (Editor only).  
[aoExponentIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-aoExponentIndirect.html) | Sets the contrast of ambient occlusion that Unity applies to indirect lighting in lightmaps. (Editor only).  
[aoMaxDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-aoMaxDistance.html) | The distance that a ray travels before Unity considers it to be unoccluded when calculating ambient occlusion in lightmaps. (Editor only).  
[bakedGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-bakedGI.html) | Whether to enable the Baked Global Illumination system for this Scene.  
[denoiserTypeAO](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-denoiserTypeAO.html) | Determines the type of denoising that the Progressive Lightmapper applies to ambient occlusion in lightmaps. (Editor only).  
[denoiserTypeDirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-denoiserTypeDirect.html) | Determines the denoiser that the Progressive Lightmapper applies to direct lighting. (Editor only).  
[denoiserTypeIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-denoiserTypeIndirect.html) | Determines the denoiser that the Progressive Lightmapper applies to indirect lighting. (Editor only).  
[directionalityMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-directionalityMode.html) | Determines whether the lightmapper should generate directional or non-directional lightmaps. (Editor only).  
[directSampleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-directSampleCount.html) | Specifies the number of samples the Progressive Lightmapper uses for direct lighting calculations. (Editor only).  
[environmentImportanceSampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-environmentImportanceSampling.html) | Determines whether Progressive Lightmappers use importance sampling when they sample environment lighting while baking.  
[environmentSampleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-environmentSampleCount.html) | Specifies the number of samples the Progressive Lightmapper uses when sampling indirect lighting from the skybox. (Editor only).  
[extractAO](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-extractAO.html) | Whether the Progressive Lightmapper extracts Ambient Occlusion to a separate lightmap. (Editor only).  
[filteringAtrousPositionSigmaAO](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-filteringAtrousPositionSigmaAO.html) | Specifies the threshold the Progressive Lightmapper uses to filter direct light stored in the lightmap when using the A-Trous filter. (Editor only).  
[filteringAtrousPositionSigmaDirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-filteringAtrousPositionSigmaDirect.html) | Specifies the threshold the Progressive Lightmapper uses to filter the indirect lighting component of the lightmap when using the A-Trous filter. (Editor only).  
[filteringAtrousPositionSigmaIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-filteringAtrousPositionSigmaIndirect.html) | Specifies the radius the Progressive Lightmapper uses to filter the ambient occlusion component in the lightmap when you use the Gaussian filter. (Editor only).  
[filteringGaussianRadiusAO](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-filteringGaussianRadiusAO.html) | Specifies the radius the Progressive Lightmapper uses to filter the direct lighting component of the lightmap when you use the Gaussian filter. (Editor only).  
[filteringGaussianRadiusDirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-filteringGaussianRadiusDirect.html) | Specifies the radius the Progressive Lightmapper uses to filter the indirect lighting component of the lightmap when you use the Gaussian filter. (Editor only).  
[filteringGaussianRadiusIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-filteringGaussianRadiusIndirect.html) | Specifies the method that the Progressive Lightmapper uses to reduce noise in lightmaps. (Editor only).  
[filteringMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-filteringMode.html) | Specifies the filter type that the Progressive Lightmapper uses for ambient occlusion. (Editor only).  
[filterTypeAO](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-filterTypeAO.html) | Specifies the filter kernel that the Progressive Lightmapper uses for ambient occlusion. (Editor only).  
[filterTypeDirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-filterTypeDirect.html) | Specifies the filter kernel that the Progressive Lightmapper uses for the direct lighting. (Editor only).  
[filterTypeIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-filterTypeIndirect.html) | Specifies whether the Editor calculates the final global illumination light bounce at the same resolution as the baked lightmap.  
[indirectResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-indirectResolution.html) | Defines the number of texels that Enlighten Realtime Global Illumination uses per world unit when calculating indirect lighting. (Editor only).  
[indirectSampleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-indirectSampleCount.html) | Specifies the number of samples the Progressive Lightmapper uses for indirect lighting calculations. (Editor only).  
[indirectScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-indirectScale.html) | Multiplies the intensity of of indirect lighting in lightmaps. (Editor only).  
[lightmapCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-lightmapCompression.html) | The level of compression the Editor uses for lightmaps.  
[lightmapMaxSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-lightmapMaxSize.html) | The maximum size in pixels of an individual lightmap texture. (Editor only).  
[lightmapPadding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-lightmapPadding.html) | Sets the distance (in texels) between separate UV tiles in lightmaps. (Editor only).  
[lightmapper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-lightmapper.html) | Determines which backend to use for baking lightmaps in the Baked Global Illumination system. (Editor only).  
[lightmapResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-lightmapResolution.html) | Defines the number of texels to use per world unit when generating lightmaps.  
[lightProbeSampleCountMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-lightProbeSampleCountMultiplier.html) | Specifies the number of samples to use for Light Probes relative to the number of samples for lightmap texels. (Editor only).  
[maxBounces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-maxBounces.html) | Stores the maximum number of bounces the Progressive Lightmapper computes for indirect lighting. (Editor only)  
[minBounces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-minBounces.html) | Stores the minimum number of bounces the Progressive Lightmapper computes for indirect lighting. (Editor only)  
[mixedBakeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-mixedBakeMode.html) | Sets the MixedLightingMode that Unity uses for all Mixed Lights in the Scene. (Editor only).  
[prioritizeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-prioritizeView.html) | Whether the Progressive Lightmapper prioritizes baking visible texels within the frustum of the Scene view. (Editor only).  
[realtimeEnvironmentLighting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-realtimeEnvironmentLighting.html) | Determines the lightmap that Unity stores environment lighting in.  
[realtimeGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-realtimeGI.html) | Whether to enable the Enlighten Realtime Global Illumination system for this Scene.  
[respectSceneVisibilityWhenBakingGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings-respectSceneVisibilityWhenBakingGI.html) | When Unity is precomputing or baking Global Illumination, respect the Scene Visibility setting of a [[GameObject] with a MeshRenderer or Terrain component.  
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
