* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginFadeGroup.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).BeginFadeGroup
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
public static bool BeginFadeGroup(float value); 
### Parameters
Parameter | Description  
---|---  
value | A value between 0 and 1, 0 being hidden, and 1 being fully visible.  
### Returns
**bool** If the group is visible or not. 
### Description
Begins a group that can be be hidden/shown and the transition will be animated.
  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutBeginFadeGroup.gif)   
_Fade Group_
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.AnimatedValues;  
  
public class MyWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    AnimBool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimBool.html) m_ShowExtraFields;
    string m_String;
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) m_Color = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
    int m_Number = 0;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/My Window")]
    static void Init()
    {
        MyWindow window = (MyWindow)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(MyWindow));
    }  
  
    void OnEnable()
    {
        m_ShowExtraFields = new AnimBool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimBool.html)(true);
        m_ShowExtraFields.valueChanged.AddListener(Repaint);
    }  
  
    void OnGUI()
    {
        m_ShowExtraFields.target = EditorGUILayout.ToggleLeft[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ToggleLeft.html)("Show extra fields", m_ShowExtraFields.target);  
  
        //Extra block that can be toggled on and off.
        if (EditorGUILayout.BeginFadeGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginFadeGroup.html)(m_ShowExtraFields.faded))
        {
            EditorGUI.indentLevel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-indentLevel.html)++;
            EditorGUILayout.PrefixLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PrefixLabel.html)("Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)");
            m_Color = EditorGUILayout.ColorField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ColorField.html)(m_Color);
            EditorGUILayout.PrefixLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PrefixLabel.html)("Text");
            m_String = EditorGUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextField.html)(m_String);
            EditorGUILayout.PrefixLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PrefixLabel.html)("Number");
            m_Number = EditorGUILayout.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntSlider.html)(m_Number, 0, 10);
            EditorGUI.indentLevel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-indentLevel.html)--;
        }  
  
        EditorGUILayout.EndFadeGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndFadeGroup.html)();
    }
}

```

* * *
