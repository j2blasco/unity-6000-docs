* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.IsEditorTargetAPreset.html

#  [Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html).IsEditorTargetAPreset
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
public static bool IsEditorTargetAPreset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) target); 
### Description
Returns true if the given target is a temporary UnityEngine.Object instance created from inside a PresetEditor.
This method has to be used from inside a CustomEditor in order to change what values are being displayed in the context of a Preset. Some CustomEditors, like the ones for global settings, are being mixed with serialized values that can be part of a Preset and global values shared between projects that are not serializable. In a Preset inspector, those global values should be hidden or at least disabled because changing them in the Preset would in fact change them globally.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Presets;
using UnityEditor.UIElements;
using UnityEngine;
using UnityEngine.UIElements;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(SomeSettings))]
class SomeSettingsEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public override VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreateInspectorGUI()
    {
        var root = new VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)();  
  
        // create UI for serialized data
        var aFloat = new PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html)(serializedObject.FindProperty("m_AFloat"));
        root.Add(aFloat);  
  
        // We are adding another field with an EditorPref data that we want to be excluded from the Preset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) UI.
        if (!Preset.IsEditorTargetAPreset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.IsEditorTargetAPreset.html)(target))
        {
            var global = new FloatField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FloatField.html)("Global Pref");
            global.value = EditorPrefs.GetFloat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetFloat.html)("SomeGlobalSetting", 0.0f);
            global.RegisterCallback<ChangeEvent<float>>(evt => EditorPrefs.SetFloat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetFloat.html)("SomeGlobalSetting", evt.newValue));
            root.Add(global);
        }  
  
        return root;
    }
}  
  
class SomeSettings : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public float m_AFloat;
}

```

* * *
