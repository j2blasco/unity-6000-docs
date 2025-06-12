* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsService.OpenUserPreferences.html

#  [SettingsService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsService.html).OpenUserPreferences
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
public static [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) OpenUserPreferences(string settingsPath); 
### Parameters
Parameter | Description  
---|---  
settingsPath | Settings path of the item to select (for example, 'Preferences/Keys' or 'Preferences/2D').  
### Returns
**EditorWindow** Returns an instance to the Settings window. 
### Description
Open the Preferences window with the specified settings item already selected.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
class MyCustomWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    void OnGUI()
    {
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Open my custom preference"))
        {
            SettingsService.OpenUserPreferences[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsService.OpenUserPreferences.html)("Preferences/MyCustomPref");
        }  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Open my custom project settings"))
        {
            SettingsService.OpenProjectSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsService.OpenProjectSettings.html)("Project/MyCustomSettings");
        }
    }
}

```

* * *
