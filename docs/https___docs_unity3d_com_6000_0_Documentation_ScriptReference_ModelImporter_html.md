* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html

# ModelImporter
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
### Description
Model importer lets you modify [model](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html) import settings from editor scripts.
Settings of this class match the ones exposed in [Mesh Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html).
### Properties
Property | Description  
---|---  
[addCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-addCollider.html) | Add mesh colliders to imported meshes.  
[animationCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-animationCompression.html) | Animation compression setting.  
[animationPositionError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-animationPositionError.html) | Allowed error of animation position compression.  
[animationRotationError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-animationRotationError.html) | Allowed error of animation rotation compression.  
[animationScaleError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-animationScaleError.html) | Allowed error of animation scale compression.  
[animationType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-animationType.html) | Animator generation mode.  
[animationWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-animationWrapMode.html) | The default wrap mode for the generated animation clips.  
[autoGenerateAvatarMappingIfUnspecified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-autoGenerateAvatarMappingIfUnspecified.html) | Generate auto mapping if no avatarSetup is provided when importing humanoid animation.  
[avatarSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-avatarSetup.html) | The Avatar generation of the imported model.  
[bakeAxisConversion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-bakeAxisConversion.html) | Computes the axis conversion on geometry and animation for Models defined in an axis system that differs from Unity's (left handed, Z forward, Y-up). When enabled, Unity transforms the geometry and animation data in order to convert the axis. When disabled, Unity transforms the root GameObject of the hierarchy in order to convert the axis.  
[bakeIK](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-bakeIK.html) | Bake Inverse Kinematics (IK) when importing.  
[clipAnimations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-clipAnimations.html) | Animation clips to split animation into. Additional resources: ModelImporterClipAnimation.  
[defaultClipAnimations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-defaultClipAnimations.html) | Generate a list of all default animation clip based on TakeInfo.  
[extraExposedTransformPaths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-extraExposedTransformPaths.html) | Animation optimization setting.  
[extraUserProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-extraUserProperties.html) | A list of default FBX properties to treat as user properties during OnPostprocessGameObjectWithUserProperties.  
[fileScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-fileScale.html) | Scaling factor used when useFileScale is set to true (Read-only).  
[generateAnimations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-generateAnimations.html) | Animation generation options.  
[generateSecondaryUV](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-generateSecondaryUV.html) | Generate secondary UV set for lightmapping.  
[globalScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-globalScale.html) | Global scale factor for importing.  
[humanDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-humanDescription.html) | The human description that is used to generate an Avatar during the import process.  
[humanoidOversampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-humanoidOversampling.html) | Controls how much oversampling is used when importing humanoid animations for retargeting.  
[importAnimatedCustomProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importAnimatedCustomProperties.html) | Import animated custom properties from file.  
[importAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importAnimation.html) | Import animation from file.  
[importBlendShapeDeformPercent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importBlendShapeDeformPercent.html) | Import BlendShapes deform percent.  
[importBlendShapeNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importBlendShapeNormals.html) | Blend shape normal import options.  
[importBlendShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importBlendShapes.html) | Controls import of BlendShapes.  
[importCameras](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importCameras.html) | Controls import of cameras. Basic properties like field of view, near plane distance and far plane distance can be animated.  
[importConstraints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importConstraints.html) | Import animation constraints.  
[importedTakeInfos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importedTakeInfos.html) | Generates the list of all imported take.  
[importLights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importLights.html) | Controls import of lights. Note that because light are defined differently in DCC tools, some light types or properties may not be exported. Basic properties like color and intensity can be animated.  
[importNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importNormals.html) | Vertex normal import options.  
[importTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importTangents.html) | Vertex tangent import options.  
[importVisibility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importVisibility.html) | Use visibility properties to enable or disable MeshRenderer components.  
[indexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-indexFormat.html) | Format of the imported mesh index buffer data.  
[isBakeIKSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-isBakeIKSupported.html) | Is Bake Inverse Kinematics (IK) supported by this importer.  
[isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-isReadable.html) | Are mesh vertices and indices accessible from script?  
[isTangentImportSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-isTangentImportSupported.html) | Is import of tangents supported by this importer.  
[isUseFileUnitsSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-isUseFileUnitsSupported.html) | Is useFileUnits supported for this asset.  
[keepQuads](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-keepQuads.html) | If this is true, any quad faces that exist in the mesh data before it is imported are kept as quads instead of being split into two triangles, for the purposes of tessellation. Set this to false to disable this behavior.  
[materialImportMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-materialImportMode.html) | Material creation options.  
[materialLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-materialLocation.html) | Material import location options.  
[materialName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-materialName.html) | Material naming setting.  
[materialSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-materialSearch.html) | Existing material search setting.  
[maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html) | The maximum number of bones per vertex stored in this mesh data.  
[meshCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-meshCompression.html) | Mesh compression setting.  
[meshOptimizationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-meshOptimizationFlags.html) | Options to control the optimization of mesh data during asset import.  
[minBoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-minBoneWeight.html) | Minimum bone weight to keep.  
[motionNodeName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-motionNodeName.html) | The path of the transform used to generation the motion of the animation.  
[normalCalculationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-normalCalculationMode.html) | Normal generation options for ModelImporter.  
[normalSmoothingAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-normalSmoothingAngle.html) | Smoothing angle (in degrees) for calculating normals.  
[normalSmoothingSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-normalSmoothingSource.html) | Source of smoothing information for calculation of normals.  
[optimizeBones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-optimizeBones.html) | Only import bones where they are connected to vertices.  
[optimizeGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-optimizeGameObjects.html) | Animation optimization setting.  
[optimizeMeshPolygons](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-optimizeMeshPolygons.html) | Optimize the order of polygons in the mesh to make better use of the GPUs internal caches to improve rendering performance.  
[optimizeMeshVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-optimizeMeshVertices.html) | Optimize the order of vertices in the mesh to make better use of the GPUs internal caches to improve rendering performance.  
[preserveHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-preserveHierarchy.html) | If true, always create an explicit Prefab root. Otherwise, if the model has a single root, it is reused as the Prefab root.  
[referencedClips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-referencedClips.html) | Returns the matching referenced clip assets for this model.  
[removeConstantScaleCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-removeConstantScaleCurves.html) | Removes constant animation curves with values identical to the object initial scale value.  
[resampleCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-resampleCurves.html) | If set to false, the importer will not resample curves when possible. Read more about animation curve resampling.Notes:- Some unsupported FBX features (such as PreRotation or PostRotation on transforms) will override this setting. In these situations, animation curves will still be resampled even if the setting is disabled. For best results, avoid using PreRotation, PostRotation and GetRotationPivot.- This option was introduced in Version 5.3. Prior to this version, Unity's import behaviour was as if this option was always enabled. Therefore enabling the option gives the same behaviour as pre-5.3 animation import.   
[secondaryUVAngleDistortion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-secondaryUVAngleDistortion.html) | Threshold for angle distortion (in degrees) when generating secondary UV.  
[secondaryUVAreaDistortion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-secondaryUVAreaDistortion.html) | Threshold for area distortion when generating secondary UV.  
[secondaryUVHardAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-secondaryUVHardAngle.html) | Hard angle (in degrees) for generating secondary UV.  
[secondaryUVMarginMethod](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-secondaryUVMarginMethod.html) | Method to use for handling margins when generating secondary UV.  
[secondaryUVMinLightmapResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-secondaryUVMinLightmapResolution.html) | The minimum lightmap resolution in texels per unit that the associated model is expected to have.  
[secondaryUVMinObjectScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-secondaryUVMinObjectScale.html) | The minimum object scale that the associated model is expected to have.  
[secondaryUVPackMargin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-secondaryUVPackMargin.html) | Margin to be left between charts when packing secondary UV.  
[skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-skinWeights.html) | Skin weights import options.  
[sortHierarchyByName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-sortHierarchyByName.html) | Sorts the gameObject hierarchy by name.  
[sourceAvatar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-sourceAvatar.html) | Imports the HumanDescription from the given Avatar.  
[strictVertexDataChecks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-strictVertexDataChecks.html) | Enables strict checks on imported vertex data.  
[swapUVChannels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-swapUVChannels.html) | Swap primary and secondary UV channels when importing.  
[transformPaths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-transformPaths.html) | Generates the list of all imported Transforms.  
[useFileScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-useFileScale.html) | Use FileScale when importing.  
[useFileUnits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-useFileUnits.html) | Detect file units and import as 1FileUnit=1UnityUnit, otherwise it will import as 1cm=1UnityUnit.  
[useSRGBMaterialColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-useSRGBMaterialColor.html) | When disabled, imported material albedo colors are converted to gamma space. This property should be disabled when using linear color space in Player rendering settings. The default value is true.  
[weldVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-weldVertices.html) | Combine vertices that share the same position in space.  
### Public Methods
Method | Description  
---|---  
[CreateDefaultMaskForClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.CreateDefaultMaskForClip.html) | Creates a mask that matches the model hierarchy, and applies it to the provided ModelImporterClipAnimation.  
[ExtractTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.ExtractTextures.html) | Extracts the embedded textures from a model file (such as FBX or SketchUp).  
[SearchAndRemapMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.SearchAndRemapMaterials.html) | Search the project for matching materials and use them instead of the internal materials.  
### Static Methods
Method | Description  
---|---  
[GetReferencedClipsForModelPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.GetReferencedClipsForModelPath.html) | Returns all the referenced clips matching the given model name.  
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
