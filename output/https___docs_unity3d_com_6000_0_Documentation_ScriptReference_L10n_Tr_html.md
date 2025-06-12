* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/L10n.Tr.html

#  [L10n](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/L10n.html).Tr
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
public static string Tr(string str); 
### Parameters
Parameter | Description  
---|---  
str | Original text, basically English.  
### Returns
**string** Localized text. 
### Description
This function referes a po file like ja.po as an asset. Asmdef and [assembly: UnityEditor.Localization] is needed.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// This is not an editor script.
public class MyScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {}  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyScript))]
public class MyScriptInspector : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    MyScript m_Target = null;
    void OnEnable()
    {
        m_Target = target as MyScript;
    }  
  
    public override void OnInspectorGUI()
    {
        base.OnInspectorGUI();
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)(L10n.Tr[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/L10n.Tr.html)("Cancel"));
    }
}

```

* * *
