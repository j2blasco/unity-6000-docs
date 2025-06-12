* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html

# AudioImporter
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
Use this class to modify [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) import settings from editor scripts.
Use these settings to ensure all or a subset of your audio files have the same import settings. You can also edit these settings in the [Audio Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html) Inspector.   
  
Additional resources: [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html)  
  

```
// This script adds a new menu item to the Unity Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html). Select the menu item to change the settings of and reimport audio from a certain folder.   
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;   
  
public class AudioImporterExample
{
    // Creates a new menu item in Unity Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html). 
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Tools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html)/Reimport sounds with new settings")]
    public static void SetAllToAmbisonic()
    {
        // Put the audio that you want to change in this directory. 
        string folderPath = "Assets/Sounds";  
  
        // Find all AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) assets in the specified folder.
        string[] guids = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t:AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html)", new[] { folderPath });  
  
        foreach (string guid in guids)
        {
            // Get the paths to the audio clips. 
            string assetPath = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid);  
  
            // Get the AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html) for this audio clip.
            AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html) importer = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html);
            if (importer != null)
            {
                // Change the importer settings. 
                importer.ambisonic = true;
                importer.loadInBackground = true; 
                importer.forceToMono = false;
                // Reimport the asset to apply changes.
                AssetDatabase.ImportAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html)(assetPath, ImportAssetOptions.ForceUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImportAssetOptions.ForceUpdate.html)); 
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Changed '{assetPath}' settings.");
             }
        }
    }
}

```

### Properties
Property | Description  
---|---  
[ambisonic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter-ambisonic.html) | Enable this property to treat the audio clip as ambisonic.  
[defaultSampleSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter-defaultSampleSettings.html) | The default sample settings for the AudioClip importer.  
[forceToMono](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter-forceToMono.html) | Force audioclips to mono sound type, so all audio plays through a single channel.  
[loadInBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter-loadInBackground.html) | Corresponding to the "Load In Background" flag in the AudioClip inspector, when this flag is set, the loading of the clip will happen delayed without blocking the main thread.  
### Public Methods
Method | Description  
---|---  
[ClearSampleSettingOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.ClearSampleSettingOverride.html) | Clears the sample settings override for the given platform.  
[ContainsSampleSettingsOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.ContainsSampleSettingsOverride.html) | Returns whether the sample settings for a specified build target are currently overridden.  
[GetOverrideSampleSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.GetOverrideSampleSettings.html) | Return the current override settings for the given platform.  
[SetOverrideSampleSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.SetOverrideSampleSettings.html) | Sets the override sample settings for the given platform.  
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
