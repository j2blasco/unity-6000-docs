* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.OnTitleBarGUI.html

#  [SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html).OnTitleBarGUI
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
public void OnTitleBarGUI(); 
### Description
Use this function to override drawing the title for the SettingsProvider using IMGUI. This allows you to add custom UI (such as a toolbar button) next to the title. [AssetSettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) uses this mecanism to display the "add to preset" and the "help" buttons.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;
using EditorStyles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles.html) = UnityEditor.EditorStyles;  
  
class SimpleIMGUISettingsProvider : SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)
{
    SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) m_Settings;
    const string k_MyCustomSettingsPath = "Assets/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)/MyCustomSettings.asset";
    public SimpleIMGUISettingsProvider(string path, SettingsScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.html) scope = SettingsScope.User[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.User.html))
        : base(path, scope) {}  
  
    public override void OnGUI(string searchContext)
    {
        // Use IMGUI to display UI:
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_Settings.FindProperty("m_Number"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("My Number"));
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_Settings.FindProperty("m_SomeString"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Some string"));
        m_Settings.ApplyModifiedPropertiesWithoutUndo();
    }  
  
    public override void OnTitleBarGUI()
    {
        // This button appears right after the Title of the currently selected SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html):
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Help[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.html)!", EditorStyles.miniButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-miniButton.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("You are on your own.");
        }
    }
}

```

* * *
