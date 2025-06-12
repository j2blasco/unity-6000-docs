* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.CurveField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).CurveField
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
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField([AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value, params GUILayoutOption[] options); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField(string label, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value, params GUILayoutOption[] options); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value, params GUILayoutOption[] options); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField([AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ranges, params GUILayoutOption[] options); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField(string label, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ranges, params GUILayoutOption[] options); 
## Declaration
public static [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) CurveField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) value, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ranges, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label to display in front of the field.  
value | The curve to edit.  
color | The color to show the curve with.  
ranges | Optional rectangle that the curve is restrained within.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**AnimationCurve** The curve edited by the user. 
### Description
Make a field for editing an [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/FollowCurve.png)   
_Create an animation on the different axis and assign it to a GameObject._
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class FollowCurve : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curveX = AnimationCurve.Linear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Linear.html)(0, 0, 10, 10);
    AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curveY = AnimationCurve.Linear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Linear.html)(0, 0, 10, 10);
    AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curveZ = AnimationCurve.Linear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Linear.html)(0, 0, 10, 10);  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Create Curve For Object")]
    static void Init()
    {
        FollowCurve window = (FollowCurve)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(FollowCurve));
        window.Show();
    }  
  
    void OnGUI()
    {
        curveX = EditorGUILayout.CurveField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.CurveField.html)("Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) on X", curveX);
        curveY = EditorGUILayout.CurveField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.CurveField.html)("Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) on Y", curveY);
        curveZ = EditorGUILayout.CurveField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.CurveField.html)("Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) on Z", curveZ);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Generate Curve"))
            AddCurveToSelectedGameObject();
    }  
  
    void  AddCurveToSelectedGameObject()
    {
        if (Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
        {
            FollowAnimationCurve comp =
                Selection.activeGameObject.AddComponent<FollowAnimationCurve>();  
  
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
And the script that works with the example:
```
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
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(curveX.Evaluate(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)), curveY.Evaluate(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)), curveZ.Evaluate(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)));
    }
}

```

* * *
## Declaration
public static void CurveField([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ranges, params GUILayoutOption[] options); 
## Declaration
public static void CurveField([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ranges, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
property | The curve to edit.  
color | The color to show the curve with.  
ranges | Optional rectangle that the curve is restrained within.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
label | Optional label to display in front of the field. Pass [[GUIContent.none] to hide the label.  
### Description
Make a field for editing an [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html).
* * *
