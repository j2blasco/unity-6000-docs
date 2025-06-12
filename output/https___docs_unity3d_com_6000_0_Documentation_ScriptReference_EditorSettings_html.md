* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings.html

# EditorSettings
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
### Description
User settings for Unity Editor.
Use EditorSettings to apply Editor Project Settings to your Unity Project. You can control settings such as version control, streaming settings, and Asset serialization.  
  
Additional resources: [Editor Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html)
### Static Properties
Property | Description  
---|---  
[assetNamingUsesSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-assetNamingUsesSpace.html) | Controls whether to insert a space before a number in duplicated Asset names.  
[assetPipelineMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-assetPipelineMode.html) | Select the assetpipeline mode.  
[asyncShaderCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-asyncShaderCompilation.html) | Enable asynchronous Shader compilation in Game and Scene view.  
[cacheServerDownloadBatchSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerDownloadBatchSize.html) | Controls the size of the batches used when making cacheserver download requests.  
[cacheServerEnableAuth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEnableAuth.html) | Toggle whether to enable authentication to cache server.  
[cacheServerEnableDownload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEnableDownload.html) | Toggle whether to enable downloading from cache server.  
[cacheServerEnableTls](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEnableTls.html) | Toggle whether to enable TLS encryption to cache server.  
[cacheServerEnableUpload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEnableUpload.html) | Toggle whether to enable uploading from cache server.  
[cacheServerEndpoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerEndpoint.html) | Cache server endpoint IP address  
[cacheServerMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerMode.html) | Select cache server mode  
[cacheServerNamespacePrefix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerNamespacePrefix.html) | Sets the namespace prefix to use for the cache server.  
[cacheServerValidationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerValidationMode.html) | Select Accelerator server validation mode.  
[cachingShaderPreprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cachingShaderPreprocessor.html) | This property is now obsolete. Unity always uses the Caching Shader Preprocessor.  
[enableTextureStreamingInEditMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-enableTextureStreamingInEditMode.html) | Enable texture mipmap streaming system when in Edit Mode.  
[enableTextureStreamingInPlayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-enableTextureStreamingInPlayMode.html) | Enable texture mipmap streaming system when in Play Mode.  
[enterPlayModeOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-enterPlayModeOptions.html) | Determines the state of the Enter Play Mode Options in the Unity Editor.  
[enterPlayModeOptionsEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-enterPlayModeOptionsEnabled.html) | Determines whether the Enter Play Mode Options are enabled in the Unity Editor or not.  
[gameObjectNamingDigits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-gameObjectNamingDigits.html) | Indicates the amount of digits to use for the numbers in a duplicated GameoObject's name.  
[gameObjectNamingScheme](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-gameObjectNamingScheme.html) | Indicates which naming scheme to use for duplicated GameObjects.  
[lineEndingsForNewScripts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-lineEndingsForNewScripts.html) | Determines what line endings to use in a new C# file created in the Editor.  
[prefabModeAllowAutoSave](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-prefabModeAllowAutoSave.html) | Allow Auto Save in Prefab Mode for this project.  
[prefabRegularEnvironment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-prefabRegularEnvironment.html) | Allows you to specify a Scene to use as the editing environment for Prefabs.  
[prefabUIEnvironment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-prefabUIEnvironment.html) | Allows you to specify a Scene to use as the editing environment for UI Prefabs.  
[projectGenerationRootNamespace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-projectGenerationRootNamespace.html) | Controls which root namespace gets written into the c# .csproj projects that Unity generates.  
[projectGenerationUserExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-projectGenerationUserExtensions.html) | Controls list of extensions of files that will be included in the c# .csproj projects that Unity generates.  
[referencedClipsExactNaming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-referencedClipsExactNaming.html) | Controls which referenced clips an humanoid rig is able to update when using @convention files.  
[refreshImportMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-refreshImportMode.html) | Controls the Editor's use of parallel processes when it imports assets during an asset database refresh, for this project.  
[serializeInlineMappingsOnOneLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-serializeInlineMappingsOnOneLine.html) | Forces Unity to write references and similar YAML structures on one line, which reduces version control noise.  
[shadowmaskStitching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-shadowmaskStitching.html) | Apply seam stitching to Shadowmask Lightmaps.  
[spritePackerPaddingPower](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-spritePackerPaddingPower.html) | Power of 2 value to add a boundary (padding) to Sprites packed to the Atlas (Legacy Sprite Packer).  
[unityRemoteCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-unityRemoteCompression.html) | Gets or sets compression method used for Unity Remote screen stream.  
[unityRemoteDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-unityRemoteDevice.html) | Gets or sets device ID used for Unity Remote feature.  
[unityRemoteJoystickSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-unityRemoteJoystickSource.html) | Gets or sets joystick source used in editor when Unity Remote is connected.  
[unityRemoteResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-unityRemoteResolution.html) | Gets or sets resolution used for Unity Remote screen stream.  
[useLegacyProbeSampleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-useLegacyProbeSampleCount.html) | Enable the legacy fixed sample counts for baking Light Probes with Progressive Lightmapper.  
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
