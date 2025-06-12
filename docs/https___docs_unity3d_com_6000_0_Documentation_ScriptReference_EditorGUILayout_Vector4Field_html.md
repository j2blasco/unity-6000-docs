* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector4Field.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).Vector4Field
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
public static [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) Vector4Field(string label, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) value, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Label to display above the field.  
value | The value to edit.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**Vector4** The value entered by the user. 
### Description
Make an X, Y, Z & W field for entering a [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ModifyQuaternionDirectly.png)   
_Modify X,Y,Z and W values directly of a GameObject._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ModifyQuaternionDirectly : UnityEditor.EditorWindow
{
    Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) quat;
    public Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) value;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Modify internal Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)")]
    static void Init()
    {
        ModifyQuaternionDirectly window = (ModifyQuaternionDirectly)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(ModifyQuaternionDirectly), true, "My Empty Window");
        window.Show();
    }  
  
    void OnGUI()
    {
        value = EditorGUILayout.Vector4Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector4Field.html)("Components:", value);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Capture Rotation"))
            value = QuaternionToVector4(Selection.activeTransform.rotation);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Close"))
            this.Close();
    }  
  
    static Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) QuaternionToVector4(Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rot)
    {
        return new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(rot.x, rot.y, rot.z, rot.w);
    }
}

```

* * *
