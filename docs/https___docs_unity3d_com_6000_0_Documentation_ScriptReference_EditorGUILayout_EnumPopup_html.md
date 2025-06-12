* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EnumPopup.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).EnumPopup
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
public static Enum EnumPopup(Enum selected, params GUILayoutOption[] options); 
## Declaration
public static Enum EnumPopup(Enum selected, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static Enum EnumPopup(string label, Enum selected, params GUILayoutOption[] options); 
## Declaration
public static Enum EnumPopup(string label, Enum selected, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static Enum EnumPopup([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, Enum selected, params GUILayoutOption[] options); 
## Declaration
public static Enum EnumPopup([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, Enum selected, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static Enum EnumPopup([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, Enum selected, Func<Enum,bool> checkEnabled, bool includeObsolete, params GUILayoutOption[] options); 
## Declaration
public static Enum EnumPopup([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, Enum selected, Func<Enum,bool> checkEnabled, bool includeObsolete, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label in front of the field.  
selected | The enum option the field shows.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
includeObsolete | Set to true to include Enum values with ObsoleteAttribute. Set to false to exclude Enum values with ObsoleteAttribute.  
checkEnabled | Method called for each Enum value displayed. The specified method should return true if the option can be selected, false otherwise.  
### Returns
**Enum** The enum option that has been selected by the user. 
### Description
Make an enum popup selection field.
Takes the currently selected enum value as a parameter and returns the enum value selected by the user.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutEnumPopup.png)  
_Creates a primitive selected by the user._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
// Creates an instance of a primitive depending on the option selected by the user.  
  
public enum OPTIONS
{
    CUBE = 0,
    SPHERE = 1,
    PLANE = 2
}  
  
public class EditorGUILayoutEnumPopup : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    public OPTIONS op;
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) GUILayout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html) Enum Popup usage")]
    static void Init()
    {
        UnityEditor.EditorWindow window = GetWindow(typeof(EditorGUILayoutEnumPopup));
        window.Show();
    }  
  
    void OnGUI()
    {
        op = (OPTIONS)EditorGUILayout.EnumPopup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EnumPopup.html)("Primitive to create:", op);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Create"))
            InstantiatePrimitive(op);
    }  
  
    void InstantiatePrimitive(OPTIONS op)
    {
        switch (op)
        {
            case OPTIONS.CUBE:
                GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
                cube.transform.position = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
                break;
            case OPTIONS.SPHERE:
                GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) sphere = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Sphere.html));
                sphere.transform.position = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
                break;
            case OPTIONS.PLANE:
                GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) plane = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Plane.html));
                plane.transform.position = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
                break;
            default:
                Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Unrecognized Option");
                break;
        }
    }
}

```

* * *
