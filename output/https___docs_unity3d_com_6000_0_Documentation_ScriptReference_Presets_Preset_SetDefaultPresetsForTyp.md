* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.SetDefaultPresetsForType.html

#  [Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html).SetDefaultPresetsForType
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
public static bool SetDefaultPresetsForType([Presets.PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html) type, DefaultPreset[] presets); 
### Parameters
Parameter | Description  
---|---  
type | A valid default [PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html).  
presets | An ordered list of [DefaultPreset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.DefaultPreset.html).  
### Returns
**bool** Returns true if the list was set as default. Returns false otherwise. 
### Description
Sets a default list of Presets with a filter for a specific [PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html).
Default Presets are stored in the PresetManager. Access Presets with a script, using this method and Preset.GetDefaultListForType, or from the [Preset Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PresetManager.html) window.
```
using UnityEditor.Presets;
using System.Linq;  
  
public static class PresetUility
{
    public static void InsertAsFirstDefault(Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) preset)
    {
        var type = preset.GetPresetType();
        if (type.IsValidDefault())
        {
            var list = Preset.GetDefaultPresetsForType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetDefaultPresetsForType.html)(type).ToList();
            list.Insert(0, new DefaultPreset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.DefaultPreset.html)(string.Empty, preset));
            Preset.SetDefaultPresetsForType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.SetDefaultPresetsForType.html)(type, list.ToArray());
        }
    }
}

```

* * *
