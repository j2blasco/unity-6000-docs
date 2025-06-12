* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginBuildTargetSelectionGrouping.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).BeginBuildTargetSelectionGrouping
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
public static [BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) BeginBuildTargetSelectionGrouping(); 
### Description
Begin a build target grouping and get the selected BuildTargetGroup back.
  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/BuildTargetGroupExampleExtended.png)   
_Build Target Selection Group_
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class BuildTargetGroupExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Begin-End BuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) Grouping")]
    static void Init()
    {
        BuildTargetGroupExample window =
            (BuildTargetGroupExample)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(BuildTargetGroupExample), true,
                "My Custom Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Window");
        window.Show();
    }  
  
    void OnGUI()
    {
        BuildTargetGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) selectedBuildTargetGroup = EditorGUILayout.BeginBuildTargetSelectionGrouping[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginBuildTargetSelectionGrouping.html)();
        if (selectedBuildTargetGroup == BuildTargetGroup.Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.Android.html))
        {
            EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html) specific things");
        }  
  
        if (selectedBuildTargetGroup == BuildTargetGroup.Standalone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.Standalone.html))
        {
            EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Standalone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Standalone.html) specific things");
        }  
  
        EditorGUILayout.EndBuildTargetSelectionGrouping[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndBuildTargetSelectionGrouping.html)();
    }
}

```

* * *
