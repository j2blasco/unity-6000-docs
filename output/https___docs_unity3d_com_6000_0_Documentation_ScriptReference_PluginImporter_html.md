* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html

# PluginImporter
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
Represents a plugin importer.
### Properties
Property | Description  
---|---  
[DefineConstraints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.DefineConstraints.html) | Allows you to specify a list of #define directives which controls whether your plug-in should be included.  
[isNativePlugin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter-isNativePlugin.html) | Is plugin native or managed? Note: C++ libraries with CLR support are treated as native plugins, because Unity cannot load such libraries. You can still access them via P/Invoke.  
[isPreloaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter-isPreloaded.html) | Is a native plugin loaded during startup or on demand?  
### Constructors
Constructor | Description  
---|---  
[PluginImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter-ctor.html) | Constructor.  
### Public Methods
Method | Description  
---|---  
[ClearSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.ClearSettings.html) | Clear all plugin settings and set the compatability with Any Platform to true.  
[GetCompatibleWithAnyPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetCompatibleWithAnyPlatform.html) | Checks whether a plugin is flagged as being compatible with Any Platform.  
[GetCompatibleWithEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetCompatibleWithEditor.html) | Is plugin compatible with editor.  
[GetCompatibleWithPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetCompatibleWithPlatform.html) | Is plugin compatible with specified platform.  
[GetEditorData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetEditorData.html) | Returns editor specific data for specified key.  
[GetExcludeEditorFromAnyPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetExcludeEditorFromAnyPlatform.html) | Is Editor excluded when Any Platform is set to true.  
[GetExcludeFromAnyPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetExcludeFromAnyPlatform.html) | Is platform excluded when Any Platform set to true.  
[GetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetIcon.html) | Gets the custom icon to associate with a MonoScript at import time.  
[GetIsOverridable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetIsOverridable.html) | Identifies whether or not this plugin will be overridden if a plugin of the same name is placed in your project folder.  
[GetPlatformData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetPlatformData.html) | Get platform specific data.  
[SetCompatibleWithAnyPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetCompatibleWithAnyPlatform.html) | Sets compatibility with Any Platform.  
[SetCompatibleWithEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetCompatibleWithEditor.html) | Sets compatibility with any editor.  
[SetCompatibleWithPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetCompatibleWithPlatform.html) | Sets compatibility with the specified platform.  
[SetEditorData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetEditorData.html) | Sets editor specific data.  
[SetExcludeEditorFromAnyPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetExcludeEditorFromAnyPlatform.html) | Exclude Editor from compatible platforms when Any Platform is set to true.  
[SetExcludeFromAnyPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetExcludeFromAnyPlatform.html) | Exclude platform from compatible platforms when Any Platform is set to true.  
[SetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetIcon.html) | Sets the custom icon to associate with a MonoScript imported by a managed plugin.  
[SetIncludeInBuildDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetIncludeInBuildDelegate.html) | Setting the delegate function to be called by ShouldIncludeInBuild.  
[SetPlatformData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetPlatformData.html) | Sets platform specific data.  
[ShouldIncludeInBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.ShouldIncludeInBuild.html) | Identifies whether or not this plugin should be included in the current build target.  
### Static Methods
Method | Description  
---|---  
[GetAllImporters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetAllImporters.html) | Returns all plugin importers for all platforms.  
[GetImporters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetImporters.html) | Returns all plugin importers for specfied platform.  
### Delegates
Delegate | Description  
---|---  
[IncludeInBuildDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.IncludeInBuildDelegate.html) | Delegate to be used with SetIncludeInBuildDelegate.  
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
