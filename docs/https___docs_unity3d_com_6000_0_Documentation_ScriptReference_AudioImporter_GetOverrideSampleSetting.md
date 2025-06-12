* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.GetOverrideSampleSettings.html

#  [AudioImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html).GetOverrideSampleSettings
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
## Declaration
public [AudioImporterSampleSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html) GetOverrideSampleSettings([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) platformGroup); 
## Declaration
public [AudioImporterSampleSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html) GetOverrideSampleSettings(string platform); 
### Parameters
Parameter | Description  
---|---  
platformGroup | The platform for which to get the override settings.  
  
See [BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) for the complete list of options.  
platform | The platform for which to get the override settings.  
  
See [BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) for the complete list of options and type the desired platform enum name in the form of a string.  
### Returns
**AudioImporterSampleSettings** The override sample settings for the given platform. 
### Description
Return the current override settings for the given platform.
If there is no override for the passed platform, the default translated settings will be returned.  
  
The translated settings are the default settings to use for the given platform. For example on some platforms, the `compressionFormat` will be different to depending on different hardware decoders.  
  
Make sure to check [BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) for the names of the platforms.
```
// This script checks if the audio clip has override settings for a specific platform. 
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html). 
// Then, in the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Inspector, attach an AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) and set the platform you want to check the override settings for.   
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class AudioImporterExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Set your preferred platform and audio clip in the Inspector. 
    public BuildTargetGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) platformToCheck;
    public AudioClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) audioClip;  
  
    void Start()
    {
        string audioClipPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(audioClip);  
  
        // Get the AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html) for this audio file.
        AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html) audioImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(audioClipPath) as AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html);  
  
        if (audioImporter == null)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)($"No AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html) found for path: {audioClipPath}");
            return;
        }  
  
        // Check if there are override settings for your chosen platform.
        if (audioImporter.ContainsSampleSettingsOverride(platformToCheck))
        {
            // Get the override sample settings for your chosen platform.
            AudioImporterSampleSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html) sampleSettings = audioImporter.GetOverrideSampleSettings(platformToCheck);  
  
            // Log the platform-specific sample settings to the Console.
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Platform: {platformToCheck}");
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Compression Format: {sampleSettings.compressionFormat}");
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Quality: {sampleSettings.quality}");
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Load Type: {sampleSettings.loadType}");
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"No override sample settings found for {platformToCheck}.");
        }
    }
}
```

* * *
