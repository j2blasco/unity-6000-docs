* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.InspectorTitlebar.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).InspectorTitlebar
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
public static bool InspectorTitlebar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool foldout, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetObj, bool expandable); 
## Declaration
public static bool InspectorTitlebar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, bool foldout, Object[] targetObjs, bool expandable); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the titlebar.  
foldout | The foldout state shown with the arrow.  
targetObj | The object (for example a component) that the titlebar is for.  
targetObjs | The objects that the titlebar is for.  
expandable | Whether this editor should display a foldout arrow in order to toggle the display of its properties.  
### Returns
**bool** The foldout state selected by the user. 
### Description
Makes an inspector-window-like titlebar.
The titlebar has a foldout arrow, a help icon, and a settings menu that depends on the type of the object supplied.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIInspectorTitlebar.png)  
_Inspector titlebar in an Editor Window._
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) window that shows the detailed rotation (X,Y,Z and W components),
// the position in 3D space and position in Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) space of the selected
// transform.  
  
class CustomTransformInspector : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool showing = true;
    Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) rotationComp;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) detailed inspector")]
    static void Init()
    {
        CustomTransformInspector window = (CustomTransformInspector)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(CustomTransformInspector));
        window.Show();
    }  
  
    void OnInspectorUpdate()
    {
        Repaint();
    }  
  
    void OnGUI()
    {
        var currObj = Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html);  
  
        showing = EditorGUI.InspectorTitlebar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.InspectorTitlebar.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, position.width, 20), showing, currObj, showing);
        if (showing)
        {
            if (currObj)
            {
                currObj.position = EditorGUI.Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector3Field.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 15, position.width - 6, 20),
                    "Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) in 3D Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html):",
                    currObj.position);  
  
                EditorGUI.Vector2Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector2Field.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 50, position.width - 6, 20),
                    "Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) in Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html):",
                    Camera.main.WorldToScreenPoint(currObj.position));  
  
                rotationComp = EditorGUI.Vector4Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector4Field.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 85, position.width - 6, 20),
                    "Detailed Rotation:",
                    QuaternionToVector4(currObj.localRotation));
                currObj.localRotation = ConvertToQuaternion(rotationComp);  
  
                currObj.localScale = EditorGUI.Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector3Field.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 120, position.width - 6, 20),
                    "Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html):",
                    currObj.localScale);
            }
            else
            {
                EditorGUI.DropShadowLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DropShadowLabel.html)(
                    new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 15, position.width, 20),
                    "Select an Object to inspect");
            }
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
}

```

* * *
## Declaration
public static void InspectorTitlebar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, Object[] targetObjs); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the titlebar.  
targetObjs | The objects that the titlebar is for.  
### Description
Makes an inspector-window-like titlebar.
* * *
