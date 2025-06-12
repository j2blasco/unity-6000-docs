* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.html

# SpeedTreeImporter
class in UnityEditor
/
Inherits from:[AssetImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpeedTreeImporter.html "Go to SpeedTreeImporter Component in the Manual")
### Description
AssetImporter for importing SpeedTree model assets.
### Static Properties
Property | Description  
---|---  
[windQualityNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-windQualityNames.html) | Gets an array of name strings for wind quality value.  
### Properties
Property | Description  
---|---  
[alphaTestRef](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-alphaTestRef.html) | Gets and sets a default alpha test reference values.  
[animateCrossFading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-animateCrossFading.html) | Indicates if the cross-fade LOD transition, applied to the last mesh LOD and the billboard, should be animated.  
[bestWindQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-bestWindQuality.html) | Returns the best-possible wind quality on this asset (configured in SpeedTree modeler).  
[billboardTransitionCrossFadeWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-billboardTransitionCrossFadeWidth.html) | Proportion of the last 3D mesh LOD region width which is used for cross-fading to billboard tree.  
[castShadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-castShadows.html) | Gets and sets an array of booleans to enable shadow casting for each LOD.  
[castShadowsByDefault](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-castShadowsByDefault.html) | Gets and sets a boolean to toggle whether the imported SpeedTree casts shadows.  
[defaultBillboardShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-defaultBillboardShader.html) | Returns the default SpeedTree billboard shader for the active render pipeline, or null if the asset is a SpeedTree v8 asset.  
[defaultShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-defaultShader.html) | Returns the default SpeedTree shader for the active render pipeline (either v7 or v8 according to the asset version).  
[enableBump](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-enableBump.html) | Gets and sets an array of booleans to enable normal mapping for each LOD.  
[enableBumpByDefault](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-enableBumpByDefault.html) | Gets and sets a boolean to enable normal mapping on the imported SpeedTree model.  
[enableHue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-enableHue.html) | Gets and sets an array of booleans to enable hue variation effect for each LOD.  
[enableHueByDefault](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-enableHueByDefault.html) | Gets and sets a boolean to enable hue variation effect on the imported SpeedTree model.  
[enableSettingOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-enableSettingOverride.html) | Gets and sets an array of booleans to customize importer settings for a specific LOD.  
[enableSmoothLODTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-enableSmoothLODTransition.html) | Enables smooth LOD transitions.  
[enableSubsurface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-enableSubsurface.html) | Gets and sets an array of booleans to enable the subsurface scattering effect for each LOD (affects only SpeedTree v8 assets).  
[enableSubsurfaceByDefault](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-enableSubsurfaceByDefault.html) | Gets and sets a boolean to enable the subsurface scattering effect for the SpeedTree asset (affects only SpeedTree v8 assets).  
[fadeOutWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-fadeOutWidth.html) | Proportion of the billboard LOD region width which is used for fading out the billboard.  
[generateColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-generateColliders.html) | Gets and sets the boolean to toggle collider object generation during import.  
[generateRigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-generateRigidbody.html) | Gets and sets the boolean to toggle Rigidbody generation during import.  
[hasBillboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-hasBillboard.html) | Tells if there is a billboard LOD.  
[hasImported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-hasImported.html) | Tells if the SPM file has been previously imported.  
[hueVariation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-hueVariation.html) | Gets and sets a default hue variation color and amount (in alpha).  
[isV8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-isV8.html) | Returns true if the asset is a SpeedTree v8 asset.  
[LODHeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.LODHeights.html) | Gets and sets an array of floats of each LOD's screen height value.  
[mainColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-mainColor.html) | Gets and sets a default main color.  
[materialFolderPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-materialFolderPath.html) | Returns the folder path where generated materials will be placed in.  
[materialLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-materialLocation.html) | Material import location options.  
[receiveShadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-receiveShadows.html) | Gets and sets an array of booleans to enable shadow receiving for each LOD.  
[receiveShadowsByDefault](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-receiveShadowsByDefault.html) | Gets and sets a boolean to enable whether the SpeedTree asset receives shadows from other objects in your scene.  
[scaleFactor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-scaleFactor.html) | How much to scale the tree model compared to what is in the imported SpeedTree model file.  
[selectedWindQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-selectedWindQuality.html) | Gets and sets an integer corresponding to the SpeedTreeWind enum values. The value is clamped by SpeedTreeImporter.bestWindQuality internally.  
[useLightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-useLightProbes.html) | Gets and sets an array of booleans to enable Light Probe lighting for each LOD.  
[useLightProbesByDefault](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-useLightProbesByDefault.html) | Gets and sets a boolean to enable light probe lighting for the imported SpeedTree model.  
[windQualities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-windQualities.html) | Gets and sets an array of integers of the wind qualities on each LOD. Values will be clamped by SpeedTreeImporter.bestWindQuality internally.  
### Constructors
Constructor | Description  
---|---  
[SpeedTreeImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-ctor.html) | Construct a new SpeedTreeImporter object.  
### Public Methods
Method | Description  
---|---  
[GenerateMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.GenerateMaterials.html) | Generates all necessary materials under materialFolderPath. If Version Control is enabled please first check out the folder.  
[SearchAndRemapMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.SearchAndRemapMaterials.html) | Search the project for matching materials and use them instead of the internal materials.  
### Inherited Members
### Properties
Property | Description  
---|---  
[assetBundleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleName.html) | Get or set the AssetBundle name.  
[assetBundleVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleVariant.html) | Get or set the AssetBundle variant.  
[assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetPath.html) | The path name of the asset for this importer. (Read Only)  
[importSettingsMissing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-importSettingsMissing.html) | The value is true when no meta file is provided with the imported asset.  
[userData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-userData.html) | Get or set any user data.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[AddRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.AddRemap.html) | Map a sub-asset from an imported asset (such as an FBX file) to an external Asset of the same type.  
[GetExternalObjectMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetExternalObjectMap.html) | Gets a copy of the external object map used by the AssetImporter.  
[RemoveRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.RemoveRemap.html) | Removes an item from the map of external objects.  
[SaveAndReimport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SaveAndReimport.html) | Save asset importer settings if asset importer is dirty.  
[SetAssetBundleNameAndVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SetAssetBundleNameAndVariant.html) | Set the AssetBundle name and variant.  
[SupportsRemappedAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SupportsRemappedAssetType.html) | Checks if the AssetImporter supports remapping the given asset type.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[GetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html) | Retrieves the asset importer for the asset at path.  
[GetImportLog](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetImportLog.html) | Retrieves logs generated during the import of the asset at path.  
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
