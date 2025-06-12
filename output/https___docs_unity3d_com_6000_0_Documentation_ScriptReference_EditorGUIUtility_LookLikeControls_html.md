* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.LookLikeControls.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).LookLikeControls
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
**Obsolete** LookLikeControls and LookLikeInspector modes are deprecated.Use EditorGUIUtility.labelWidth and EditorGUIUtility.fieldWidth to control label and field widths.
## Declaration
public static void LookLikeControls(float _labelWidth, float _fieldWidth); 
### Parameters
Parameter | Description  
---|---  
labelWidth | Width to use for prefixed labels.  
fieldWidth | Width of text entries.  
### Description
Make all [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html) look like regular controls.
This will make the default styles used by [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html) look like controls (e.g. [EditorGUI.Popup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Popup.html) becomes a full popup menu).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIUtilityLookLikeControls.png)  
_Editor window with "LookLikeControls" look._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  

// Simple editor window that shows the difference between
// Look like controls and look like inspector  
  
class LookLikeControlsInspector : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    int integer1 = 0;
    float float1 = 5.5f;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Look Like Controls - Inspector")]
    static void Init()
    {
        var window = GetWindow<LookLikeControlsInspector>();
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUIUtility.LookLikeInspector();
        EditorGUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextField.html)("Text Field:", "Hello There");
        EditorGUILayout.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntField.html)("Int Field:", integer1);
        EditorGUILayout.FloatField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.FloatField.html)("Float Field:", float1);
        EditorGUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Space.html)();
        EditorGUIUtility.LookLikeControls[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.LookLikeControls.html)();
        EditorGUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextField.html)("Text Field", "Hello There");
        EditorGUILayout.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntField.html)("Int Field:", integer1);
        EditorGUILayout.FloatField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.FloatField.html)("Float Field:", float1);
    }
}

```

* * *
