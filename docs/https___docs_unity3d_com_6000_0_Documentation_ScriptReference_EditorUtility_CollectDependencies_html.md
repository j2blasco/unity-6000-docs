* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CollectDependencies.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).CollectDependencies
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
public static Object[] CollectDependencies(Object[] roots); 
### Description
Calculates and returns a list of all assets the assets listed in `roots` depend on.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorUtilityCollectDependencies.png)   
_Editor window that shows the next example._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CollectDependenciesExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    static GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) obj = null;  
  

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Collect Dependencies[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.html)")]
    static void Init()
    {
        // Get existing open window or if none, make a new one:
        CollectDependenciesExample window = (CollectDependenciesExample)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(CollectDependenciesExample));
        window.Show();
    }  
  
    void OnGUI()
    {
        obj = EditorGUI.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ObjectField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 20), "Find Dependency", obj, typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);  
  
        if (obj)
        {
            Object[] roots = new Object[] { obj };  
  
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 25, position.width - 6, 20), "Check Dependencies[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Dependencies.html)"))
                Selection.objects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-objects.html) = EditorUtility.CollectDependencies[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CollectDependencies.html)(roots);
        }
        else
            EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 25, position.width - 6, 20), "Missing:", "Select an object first");
    }  
  
    void OnInspectorUpdate()
    {
        Repaint();
    }
}

```

* * *
