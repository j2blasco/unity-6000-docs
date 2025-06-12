* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings-defaultValue.html

#  [FilteringSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html).defaultValue
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
[Rendering.FilteringSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html) defaultValue; 
### Description
Creates a `FilteringSettings` struct that contains default values for all properties. With these default values, Unity does not perform any filtering.
To override values at the time that you create the struct, use the [FilteringSettings constructor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings-ctor.html).  
  
This example demonstrates the syntax for creating a default `FilteringSettings` struct with default values.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class FilteringSettingsExample
{
    public FilteringSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html) CreateFilteringSettings()
    {
        // Instantiate a FilteringSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html) struct with the default value
        // (i.e., perform no filtering)
        FilteringSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html) defaultFilteringSettings = FilteringSettings.defaultValue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings-defaultValue.html);  
  
        return defaultFilteringSettings;
    }
}

```

Additional resources: ScriptableRenderContext.DrawRenderers, [Creating a simple render loop in a custom render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/srp-creating-simple-render-loop.html).
* * *
