* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetFloat.html

#  [EditorPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html).SetFloat
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
public static void SetFloat(string key, float value); 
### Parameters
Parameter | Description  
---|---  
key | Name of key to write float into.  
value | Float value to write into the storage.  
### Description
Sets the float value of the preference identified by `key`.
```
// Simple script that allows a float value to be editted
// in a slider. The final value is written into the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Preferences.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);  
  
public class SetFloatExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    static float floatValue = 0.0f;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Preferences SetFloat Example")]
    static void Init()
    {
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 100);
        SetFloatExample window = (SetFloatExample)EditorWindow.GetWindowWithRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html)(typeof(SetFloatExample), r);
        window.Show();
    }  
  
    void Awake()
    {
        floatValue = EditorPrefs.GetFloat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetFloat.html)("FloatExample", floatValue);
    }  
  
    void OnGUI()
    {
        floatValue = EditorGUILayout.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Slider.html)(floatValue, -1.0f, 1.0f);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Save float " + Convert.ToString(floatValue) + "?"))
        {
            EditorPrefs.SetFloat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetFloat.html)("FloatExample", floatValue);
        }
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Close"))
            this.Close();
    }
}

```

* * *
