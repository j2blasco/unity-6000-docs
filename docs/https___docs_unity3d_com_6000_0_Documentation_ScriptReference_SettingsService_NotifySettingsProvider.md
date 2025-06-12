* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsService.NotifySettingsProviderChanged.html

#  [SettingsService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsService.html).NotifySettingsProviderChanged
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
public static void NotifySettingsProviderChanged(); 
### Description
Use this function to notify the SettingsService that a SettingsProvider changed.
The client managing the SettingsProvider should call this function when a SettingsProvider is added, removed, or modified and the Settings window needs to be refreshed.
```
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class MyCustomSettingsProcessor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    const string k_MyCustomSettingsPath = "Resources[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html)/MyCustomSettings.asset";
    static void OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths)
    {
        var settingsTouched = importedAssets.Any(a => a.Contains(k_MyCustomSettingsPath));
        settingsTouched = settingsTouched || deletedAssets.Any(a => a.Contains(k_MyCustomSettingsPath));
        settingsTouched = settingsTouched || movedAssets.Any(a => a.Contains(k_MyCustomSettingsPath));
        settingsTouched = settingsTouched || movedFromAssetPaths.Any(a => a.Contains(k_MyCustomSettingsPath));  
  
        if (settingsTouched)
        {
            // Notify the SettingsWindow that MyCustomSettings has been removed or added. This tells the SettingsWindow to Add/Remove
            // a new Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) section.
            SettingsService.NotifySettingsProviderChanged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsService.NotifySettingsProviderChanged.html)();
        }
    }
}

```

* * *
