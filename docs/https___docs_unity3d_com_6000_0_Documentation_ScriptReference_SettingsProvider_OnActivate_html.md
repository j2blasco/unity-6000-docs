* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.OnActivate.html

#  [SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html).OnActivate
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
public void OnActivate(string searchContext, [UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) rootElement); 
### Parameters
Parameter | Description  
---|---  
searchContext | Search context in the search box on the Settings window.  
rootElement | Root of the UIElements tree. If you add to this root, the SettingsProvider uses UIElements instead of calling [SettingsProvider.OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.OnGUI.html) to build the UI. If you do not add to this VisualElement, then you must use the IMGUI to build the UI.  
### Description
Use this function to implement a handler for when the user clicks on the Settings in the Settings window. You can fetch a settings Asset or set up UIElements UI from this function.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;  
  
class SimpleIMGUISettingsProvider : SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)
{
    SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) m_Settings;
    const string k_MyCustomSettingsPath = "Assets/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)/MyCustomSettings.asset";
    public SimpleIMGUISettingsProvider(string path, SettingsScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.html) scope = SettingsScope.User[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.User.html))
        : base(path, scope) {}  
  
    public override void OnActivate(string searchContext, VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) rootElement)
    {
        // Called when the user clicks on the MyCustom element in the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window
        m_Settings = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(k_MyCustomSettingsPath));
    }  
  
    public override void OnDeactivate()
    {
        // User selected another setting or closed the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window
        m_Settings = null;
    }  
  
    public override void OnGUI(string searchContext)
    {
        // Use IMGUI to display UI:
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_Settings.FindProperty("m_Number"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("My Number"));
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_Settings.FindProperty("m_SomeString"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Some string"));
        m_Settings.ApplyModifiedPropertiesWithoutUndo();
    }
}

```

This example shows how to build a SettingsProvider based on UIElements: you need to add any children to the rootElement passed to OnActivate.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;
using UnityEditor.UIElements;  
  
class SimpleUIElementsSettingsProvider : SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)
{
    SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) m_Settings;
    const string k_MyCustomSettingsPath = "Assets/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)/MyCustomSettings.asset";
    public SimpleUIElementsSettingsProvider(string path, SettingsScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.html) scope = SettingsScope.User[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.User.html))
        : base(path, scope) {}  
  
    public override void OnActivate(string searchContext, VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) rootElement)
    {
        // Called when the user clicks on the MyCustom element in the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window
        m_Settings = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(k_MyCustomSettingsPath));  
  
        // rootElement is a VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html). If you add any children to it, you are using UIElements to build the SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)
        var styleSheet = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<StyleSheet[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleSheet.html)>("Assets/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)/settings_ui.uss");
        rootElement.styleSheets.Add(styleSheet);
        var title = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)()
        {
            text = "Custom UI Elements"
        };
        title.AddToClassList("title");
        rootElement.Add(title);  
  
        rootElement.Add(new PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html)(m_Settings.FindProperty("m_SomeString")));
        rootElement.Add(new PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html)(m_Settings.FindProperty("m_Number")));  
  
        rootElement.Bind(m_Settings);
    }  
  
    public override void OnGUI(string searchContext)
    {
        // This function is never called since UIElements is drawing the UI.
    }
}

```

* * *
