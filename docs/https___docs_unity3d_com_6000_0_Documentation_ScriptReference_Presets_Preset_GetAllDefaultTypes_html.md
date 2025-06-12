* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetAllDefaultTypes.html

#  [Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html).GetAllDefaultTypes
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
public static PresetType[] GetAllDefaultTypes(); 
### Description
Returns all the [PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html) that have at least one [DefaultPreset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.DefaultPreset.html) entry in the default Presets list.
Use this method to gather all existing [DefaultPreset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.DefaultPreset.html) and all [Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) used as default in a project.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Presets;
using UnityEngine;  
  
public static class PresetExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Presets Example/Log All Default Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html)")]
    public static void LogDefaultPreset()
    {
        var defaultTypes = Preset.GetAllDefaultTypes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetAllDefaultTypes.html)();
        foreach (var defaultType in defaultTypes)
        {
            var defaults = Preset.GetDefaultPresetsForType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetDefaultPresetsForType.html)(defaultType);
            foreach (var defaultPreset in defaults)
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Default - Filter:{defaultPreset.filter}, Enabled:{defaultPreset.enabled}, Name:{defaultPreset.preset.name}", defaultPreset.preset);
            }
        }
    }
}

```

* * *
