* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html

# AudioImporterSampleSettings
struct in UnityEditor
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
This structure contains a collection of settings used to define how an AudioClip should be imported.
Unity uses this structure with the [AudioImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html) to define how to import and load the [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) within the Scene. This is useful if you want to change the import settings of a group of audio clips to the same settings programmatically. You can also change these in the Inspector of the audio clip.
```
// This script creates a custom menu item. If you click this item, it reimports the audio files
// (from a certain directory) with new import settings. The settings contain overrides for 
// multiple platforms (Default, Standalone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Standalone.html), and Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html)).   
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class AudioImporterSampleSettingsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Tools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html)/Apply Audio Overrides for Multiple Platforms")]
    public static void ApplyOverrides()
    {
        // Path to your audio files. Place your audio files in the following directory.
        string folderPath = "Assets/Sounds"; 
        // Find all audio clips in this folder. 
        string[] guids = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t:AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html)", new[] { folderPath });  
  
        // Loop through the audio clips in the folder. 
        foreach (string guid in guids)
        {
            string assetPath = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid);
            // Get the importer for this audio file. 
            AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html) importer = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html);  
  
            // Change settings for the default platform. 
            AudioImporterSampleSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html) defaultSettings = new AudioImporterSampleSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html)
            {
                loadType = AudioClipLoadType.DecompressOnLoad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClipLoadType.DecompressOnLoad.html),
                compressionFormat = AudioCompressionFormat.PCM[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCompressionFormat.PCM.html),
                sampleRateSetting = AudioSampleRateSetting.PreserveSampleRate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSampleRateSetting.PreserveSampleRate.html),
                sampleRateOverride = 44100,
                quality = 1.0f
            };
            importer.defaultSampleSettings = defaultSettings;  
  
            // Set override settings for Standalone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Standalone.html) platform. 
            AudioImporterSampleSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html) standaloneSettings = new AudioImporterSampleSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html)
            {
                loadType = AudioClipLoadType.CompressedInMemory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClipLoadType.CompressedInMemory.html), 
                compressionFormat = AudioCompressionFormat.Vorbis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCompressionFormat.Vorbis.html), 
                sampleRateSetting = AudioSampleRateSetting.OptimizeSampleRate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSampleRateSetting.OptimizeSampleRate.html),
                quality = 0.5f
            };
            importer.SetOverrideSampleSettings(BuildTargetGroup.Standalone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.Standalone.html), standaloneSettings);  
  
            // Set override settings for the Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html) platform. 
            AudioImporterSampleSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html) androidSettings = new AudioImporterSampleSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html)
            {
                loadType = AudioClipLoadType.Streaming[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClipLoadType.Streaming.html), 
                compressionFormat = AudioCompressionFormat.ADPCM[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCompressionFormat.ADPCM.html), 
                sampleRateSetting = AudioSampleRateSetting.OptimizeSampleRate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSampleRateSetting.OptimizeSampleRate.html),
                quality = 0.6f 
            };
            importer.SetOverrideSampleSettings(BuildTargetGroup.Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.Android.html), androidSettings);  
  

            // Reimport the audio file with new changes. 
            AssetDatabase.ImportAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html)(assetPath, ImportAssetOptions.ForceUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImportAssetOptions.ForceUpdate.html));
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Successfully applied overrides for: {assetPath}");
        }
    }
}

```

### Properties
Property | Description  
---|---  
[compressionFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings-compressionFormat.html) | CompressionFormat defines the compression type that the audio file is encoded to. Different compression types have different performance and audio artifact characteristics.  
[loadType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings-loadType.html) | LoadType defines how the imported AudioClip data should be loaded.  
[preloadAudioData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings-preloadAudioData.html) | Preloads audio data of the clip when the clip asset is loaded. When this flag is off, scripts have to call AudioClip.LoadAudioData() to load the data before the clip can be played. Properties like length, channels and format are available before the audio data has been loaded.  
[quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings-quality.html) | Audio compression quality (0-1)Amount of compression. The value roughly corresponds to the ratio between the resulting and the source file sizes.  
[sampleRateOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings-sampleRateOverride.html) | Target sample rate to convert to when samplerateSetting is set to OverrideSampleRate.  
[sampleRateSetting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings-sampleRateSetting.html) | Defines how the sample rate is modified (if at all) of the importer audio file.  
* * *
