* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.OnInspectorUpdate.html

#  [SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html).OnInspectorUpdate
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
public void OnInspectorUpdate(); 
### Description
OnInspectorUpdate is called at 10 frames per second to give the inspector a chance to update. See [EditorWindow.OnInspectorUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnInspectorUpdate.html) for more details.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
public static class PresetManagerHelper
{
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreatePresetManagerProvider()
    {
        var provider = AssetSettingsProvider.CreateProviderFromAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.CreateProviderFromAssetPath.html)(
            "Project/Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) Manager", "ProjectSettings/PresetManager.asset");
        provider.inspectorUpdateHandler += () =>
        {
            // When PresetManager is updated from the inspector, check to see if we need to update the Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) View.
            if (provider.settingsEditor != null &&
                provider.settingsEditor.serializedObject.UpdateIfRequiredOrScript())
            {
                provider.Repaint();
            }
        };
        return provider;
    }
}

```

* * *
