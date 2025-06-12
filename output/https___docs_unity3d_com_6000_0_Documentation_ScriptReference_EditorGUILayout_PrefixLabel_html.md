* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PrefixLabel.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).PrefixLabel
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
public static void PrefixLabel(string label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) followingStyle = "Button"); 
## Declaration
public static void PrefixLabel(string label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) followingStyle, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) labelStyle); 
## Declaration
public static void PrefixLabel([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) followingStyle = "Button"); 
## Declaration
public static void PrefixLabel([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) followingStyle, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) labelStyle); 
### Parameters
Parameter | Description  
---|---  
label | Label to show to the left of the control.  
### Description
Make a label in front of some control.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SimplePrefixLabelUsage.png)   
_Simple window that shows the prefix label._  
  
Note that most editor controls already have built-in optional labels that can be specified as one of the parameters. PrefixLabel can be used when there is no such built-in label available, or when you're creating your own editor control from scratch.  
  
[PrefixLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PrefixLabel.html) also ensures that when the label is clicked, the linked control will get keyboard focus (if the control supports keyboard focus). The label is automatically linked to the following control coming after it.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ExampleClass : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    static int ammo = 0;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Prefix Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) Usage")]
    static void Init()
    {
        ExampleClass window = (ExampleClass)GetWindow(typeof(ExampleClass));
        window.Show();
    }  
  
    public void OnGUI()
    {
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        EditorGUILayout.PrefixLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PrefixLabel.html)("Ammo");
        ammo = EditorGUILayout.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntField.html)(ammo);
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();
    }
}

```

* * *
