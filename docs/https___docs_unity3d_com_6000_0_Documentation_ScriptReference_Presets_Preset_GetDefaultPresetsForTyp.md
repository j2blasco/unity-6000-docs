* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.GetDefaultPresetsForType.html

#  [Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html).GetDefaultPresetsForType
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
public static DefaultPreset[] GetDefaultPresetsForType([Presets.PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html) type); 
### Parameters
Parameter | Description  
---|---  
type | A valid default [PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html).  
### Returns
**DefaultPreset[]** Returns a list of [DefaultPreset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.DefaultPreset.html) from the PresetManager that match the specified [PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html). 
### Description
Gets an ordered list of [DefaultPreset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.DefaultPreset.html) based on the specified [PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html).
See also [Preset.SetDefaultPresetsForType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.SetDefaultPresetsForType.html).
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
