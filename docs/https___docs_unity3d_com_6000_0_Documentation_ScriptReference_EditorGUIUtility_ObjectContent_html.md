* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.ObjectContent.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).ObjectContent
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
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) ObjectContent([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, Type type); 
### Description
Return a GUIContent object with the name and icon of an Object.
If the object is null, the icon will be picked according to type.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIUtilityObjectContent.png)  
_Object Content usage._
```
// Simple Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Script that shows the icons of Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html),
// rigidbody and GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in 3 buttons.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ObjectContentExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ObjectContent usage")]
    static void Init()
    {
        ObjectContentExample window = (ObjectContentExample)GetWindow(typeof(ObjectContentExample));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUILayout.PrefixLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PrefixLabel.html)("Select a type:");
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)(EditorGUIUtility.ObjectContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.ObjectContent.html)(null, typeof(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html))).image))
            DoSomething("Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)");
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)(EditorGUIUtility.ObjectContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.ObjectContent.html)(null, typeof(Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html))).image))
            DoSomething("RigidBody");
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)(EditorGUIUtility.ObjectContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.ObjectContent.html)(null, typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))).image))
            DoSomething("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)");
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Close"))
            this.Close();
    }  
  
    private void DoSomething(string obj)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Hello there " + obj + "!");
    }
}

```

* * *
