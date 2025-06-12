* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.InspectorTitlebar.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).InspectorTitlebar
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
public static bool InspectorTitlebar(bool foldout, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetObj); 
## Declaration
public static bool InspectorTitlebar(bool foldout, Object[] targetObjs); 
### Parameters
Parameter | Description  
---|---  
foldout | The foldout state shown with the arrow.  
targetObj | The object (for example a component) or objects that the titlebar is for.  
### Returns
**bool** The foldout state selected by the user. 
### Description
Make an inspector-window-like titlebar.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/InspectorTitlebarUsage.png)   
_Create a custom inspector that shows the X,Y,Z,W quaternion components on the rotation._
```
// Create a custom transform inspector that shows the X,Y,Z,W
// quaternion components instead of the rotation angles.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class InspectorTitlebarExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool      fold = true;
    Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)   rotationComponents;
    Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) selectedTransform;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Inspector Titlebar")]
    static void Init()
    {
        var window = GetWindow(typeof(InspectorTitlebarExample));
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
The titlebar has an arrow for folding out, a help icon, and a settings menu that depends on the type of the object supplied.
* * *
