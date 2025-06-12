* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset-excludedProperties.html

#  [Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html).excludedProperties
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
excludedProperties; 
### Description
List of properties to ignore when applying the Preset to an object.
Sets the list of properties or parent properties to ignore when applying the Preset to an object.
```
using UnityEngine;
using UnityEditor.Presets;  
  
static class PresetsExample
{
    public static bool ApplyToWithExclusion(Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) preset, Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target, string[] exclusion)
    {
        var current = preset.excludedProperties;
        preset.excludedProperties = exclusion;
        var success = preset.ApplyTo(target);
        preset.excludedProperties = current;
        return success;
    }  
  
    public static void ApplyTransformPresetWithoutPosition(Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) preset, Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target)
    {
        if (ApplyToWithExclusion(preset, target, new[] { "m_LocalPosition" }))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) has been applied and the position hasn't changed");
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) was not applied");
        }
    }
}

```

```
using UnityEngine;
using UnityEditor.Presets;  
  
static class PresetsExample
{
    public static bool ApplyOnlyTheYPosition(Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) preset, Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target)
    {
        var current = preset.excludedProperties;
        preset.excludedProperties = new[] { "m_LocalPosition.x", "m_LocalPosition.z" };
        var success = preset.ApplyTo(target, new[] { "m_LocalPosition" });
        preset.excludedProperties = current;
        return success;
    }
}

```

Note: If every properties get ignored on a Preset, ApplyTo will always return false. This is also the case when using ApplyTo(Object, string[]) and the specified list of properties to apply are all ignored.
```
using UnityEngine;
using UnityEditor.Presets;  
  
static class PresetsExample
{
    public static bool ApplyAlwaysReturnFalse(Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) preset, Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target)
    {
        var current = preset.excludedProperties;
        preset.excludedProperties = new[] { "m_LocalPosition" };
        var success = preset.ApplyTo(target, new[] { "m_LocalPosition" });  // always false because we try to apply only the ignored property.
        preset.excludedProperties = current;
        return success;
    }
}

```

* * *
