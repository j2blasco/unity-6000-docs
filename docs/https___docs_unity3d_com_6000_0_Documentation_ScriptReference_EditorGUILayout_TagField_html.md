* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TagField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).TagField
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
public static string TagField(string tag, params GUILayoutOption[] options); 
## Declaration
public static string TagField(string tag, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static string TagField(string label, string tag, params GUILayoutOption[] options); 
## Declaration
public static string TagField(string label, string tag, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static string TagField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, string tag, params GUILayoutOption[] options); 
## Declaration
public static string TagField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, string tag, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label in front of the field.  
tag | The tag the field shows.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**string** The tag selected by the user. 
### Description
Make a tag selection field.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutTagField.png)   
_Assign tags on the selected GameObjects._
```
// Simple editor script that lets you set a tag for the selected GameObjects.
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class EditorGUILayoutTagField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    static string tagStr = "";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Set Tags For Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html)")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(EditorGUILayoutTagField));
        window.Show();
    }  
  
    void OnGUI()
    {
        tagStr = EditorGUILayout.TagField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TagField.html)("Tag for Objects:", tagStr);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Set Tag!"))
        {
            SetTags();
        }
    }  
  
    static void SetTags()
    {
        foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
        {
            go.tag = tagStr;
        }
    }
}

```

* * *
