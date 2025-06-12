* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Space.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).Space
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
public static void Space(); 
## Declaration
public static void Space(float width); 
## Declaration
public static void Space(float width, bool expand); 
### Parameters
Parameter | Description  
---|---  
width | The width of the empty space. Use this for horizontal layout.  
expand | Option passed to enable or disable horizontal expansion.  
### Description
Make a small space between the previous control and the following.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/InspectorTitlebarUsageSpace.png)   
_Custom inspector that shows the X,Y,Z,W quaternion components of a transform._
```
// Create a custom transform inspector that shows the X,Y,Z,W quaternion components
// instead of the rotation angles.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class EditorGUILayoutSpaceField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool fold = true;
    Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) rotationComponents;
    Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) selectedTransform;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) between controls")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(EditorGUILayoutSpaceField));
        window.Show();
    }  
  
    void OnGUI()
    {
        if (Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
        {
            selectedTransform = Selection.activeGameObject.transform;
            fold = EditorGUILayout.InspectorTitlebar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.InspectorTitlebar.html)(fold, selectedTransform);
            if (fold)
            {
                selectedTransform.position =
                    EditorGUILayout.Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector3Field.html)("Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)", selectedTransform.position);
                EditorGUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Space.html)();  
  
                rotationComponents =
                    EditorGUILayout.Vector4Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector4Field.html)("Detailed Rotation",
                        QuaternionToVector4(selectedTransform.localRotation));  
  
                EditorGUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Space.html)();
                selectedTransform.localScale =
                    EditorGUILayout.Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Vector3Field.html)("Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html)", selectedTransform.localScale);
            }
            selectedTransform.localRotation = ConvertToQuaternion(rotationComponents);
            EditorGUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Space.html)();
        }
    }  
  
    Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) ConvertToQuaternion(Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) v4)
    {
        return new Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)(v4.x, v4.y, v4.z, v4.w);
    }  
  
    Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) QuaternionToVector4(Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) q)
    {
        return new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)(q.x, q.y, q.z, q.w);
    }  
  
    void OnInspectorUpdate()
    {
        this.Repaint();
    }
}

```

* * *
