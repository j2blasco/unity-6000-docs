* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.CurveField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).CurveField
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
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ranges); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ranges); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ranges); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
label | Optional label to display in front of the field.  
value | The curve to edit.  
color | The color to show the curve with.  
ranges | Optional rectangle that the curve is restrained within.  
### Returns
**AnimationCurve** The curve edited by the user. 
### Description
Makes a field for editing an [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUICurveField.png)   
_Curve field in an Editor Window._
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class EditorGUICurveField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curveX = AnimationCurve.Linear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Linear.html)(0, 0, 1, 0);
    AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curveY = AnimationCurve.Linear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Linear.html)(0, 0, 1, 1);
    AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curveZ = AnimationCurve.Linear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Linear.html)(0, 0, 1, 0);  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Curve Field demo")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(EditorGUICurveField));
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 400, 199);
        window.Show();
    }  
  
    void OnGUI()
    {
        curveX = EditorGUI.CurveField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.CurveField.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 50),
            "Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) on X", curveX);
        curveY = EditorGUI.CurveField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.CurveField.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 56, position.width - 6, 50),
            "Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) on Y", curveY);
        curveZ = EditorGUI.CurveField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.CurveField.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 109, position.width - 6, 50),
            "Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) on Z", curveZ);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 163, position.width - 6, 30), "Generate Curve"))
            AddCurveToSelectedGameObject();
    }  
  
    // A GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with the FollowAnimationCurve script must be selected
    void AddCurveToSelectedGameObject()
    {
        if (Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
        {
            FollowAnimationCurve comp  =
                Selection.activeGameObject.GetComponent<FollowAnimationCurve>();
            comp.SetCurves(curveX, curveY, curveZ);
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("No Game Object selected for adding an animation curve");
        }
    }
}

```

This is the run-time script which animates the attached GameObject:
```
// Note that this must be FollowAnimationCurve.cs  
  
using UnityEngine;
using System.Collections;  
  
public class FollowAnimationCurve : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curveX;
    public AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curveY;
    public AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curveZ;  
  
    public void SetCurves(AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) xC, AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) yC, AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) zC)
    {
        curveX = xC;
        curveY = yC;
        curveZ = zC;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(
            curveX.Evaluate(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)),
            curveY.Evaluate(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)),
            curveZ.Evaluate(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)));
    }
}

```

* * *
## Declaration
public static void CurveField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ranges); 
## Declaration
public static void CurveField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ranges, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
property | The curve to edit.  
color | The color to show the curve with.  
ranges | Optional rectangle that the curve is restrained within.  
label | Optional label to display in front of the field. Pass [[GUIContent.none] to hide the label.  
### Description
Makes a field for editing an [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html).
* * *
