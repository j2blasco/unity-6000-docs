* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetBool.html

#  [EditorPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html).GetBool
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
public static bool GetBool(string key); 
## Declaration
public static bool GetBool(string key, bool defaultValue = false); 
### Description
Returns the value corresponding to `key` in the preference file if it exists.
If it doesn't exist, it will return `defaultValue`.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorPrefsBool.png)  
_Round rotations/positions and remember the active option._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class EditorPrefsBoolExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool showRoundPosition = true;
    bool showRoundRotation = true;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Round positions-rotations")]
    static void Init()
    {
        EditorPrefsBoolExample window = (EditorPrefsBoolExample)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(EditorPrefsBoolExample), true, "My Empty Window");
        window.Show();
    }  
  
    void OnGUI()
    {
        showRoundPosition = EditorGUILayout.BeginToggleGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginToggleGroup.html)("Round Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)", showRoundPosition);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Round Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)!"))
            DoRoundPosition();
        EditorGUILayout.EndToggleGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndToggleGroup.html)();
        showRoundRotation = EditorGUILayout.BeginToggleGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginToggleGroup.html)("Round Rotation", showRoundRotation);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Round Rotation!"))
            DoRoundRotation();
        EditorGUILayout.EndToggleGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndToggleGroup.html)();
    }  
  
    void DoRoundPosition()
    {
        foreach (Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) t in Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html))
            t.localPosition = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Round[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Round.html)(t.localPosition.x),
                Mathf.Round[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Round.html)(t.localPosition.z),
                Mathf.Round[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Round.html)(t.localPosition.y));
    }  
  
    void DoRoundRotation()
    {
        foreach (Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) t in Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html))
            t.rotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(
                new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Round[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Round.html)(t.eulerAngles.x / 45f) * 45f,
                    Mathf.Round[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Round.html)(t.eulerAngles.y / 45f) * 45f,
                    Mathf.Round[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Round.html)(t.eulerAngles.z / 45f) * 45f));
    }  
  
    void OnFocus()
    {
        if (EditorPrefs.HasKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.HasKey.html)("ShowRoundPosition"))
            showRoundPosition = EditorPrefs.GetBool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetBool.html)("ShowRoundPosition");
        if (EditorPrefs.HasKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.HasKey.html)("ShowRoundRotation"))
            showRoundPosition = EditorPrefs.GetBool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetBool.html)("ShowRoundRotation");
    }  
  
    void OnLostFocus()
    {
        EditorPrefs.SetBool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetBool.html)("ShowRoundPosition", showRoundPosition);
        EditorPrefs.SetBool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetBool.html)("ShowRoundRotation", showRoundRotation);
    }  
  
    void OnDestroy()
    {
        EditorPrefs.SetBool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetBool.html)("ShowRoundPosition", showRoundPosition);
        EditorPrefs.SetBool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetBool.html)("ShowRoundRotation", showRoundRotation);
    }
}

```

* * *
