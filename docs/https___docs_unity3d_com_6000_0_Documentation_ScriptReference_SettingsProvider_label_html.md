* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-label.html

#  [SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html).label
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
label; 
### Description
Gets or sets the display name of the SettingsProvider as it appears in the Settings window. If not set, the Settings window uses last token of [SettingsProvider.settingsPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-settingsPath.html) instead.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;  
  
class SettingsProviderExamples
{
    void CreateVariousSettingsProviders()
    {
        // New Project setting that appears in its own root section (MyOwnSection) and not grouped under all the core settings.
        var p = new SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)("MyOwnSection/MySettings", SettingsScope.Project[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.Project.html));
        // here p.label == "MySettings"  
  
        // First parameter is a unique id used to place the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) in the tree view.
        // If a label is specified, this becomes the display name of the SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html).
        var p2 = new SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)("MyOwnSection/MySettingsOfDoom", SettingsScope.Project[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.Project.html))
        {
            label = "A more proper Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) Name"
        };  
  
        // Second parameter is the Scope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Scope.html) of the SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html). It determines whether this SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) appears in the
        // Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window (used for Project settings specified with SettingsScope.Project[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.Project.html))
        // or if it appears in the Preferences window (when specified with SettingsScope.User[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.User.html))
        var p3 = new SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)("Preferences/Multi touch", SettingsScope.User[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.User.html));
    }
}

```

* * *
