* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetCurveBindings.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).GetCurveBindings
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
public static EditorCurveBinding[] GetCurveBindings([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip); 
### Description
Retrieves the float curve bindings in an animation clip.
Unity has two types of animation: float curve and object reference curve. A float curve is a classic curve that animates a float property over time. An object reference curve is a construct that animates an object reference property over time.  
  
This method returns the float curve bindings. See [AnimationUtility.GetObjectReferenceCurveBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetObjectReferenceCurveBindings.html) for object reference curves.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
// Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) window for listing all float curves in an animation clip
public class ClipInfo : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    private AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Clip Info")]
    static void Init()
    {
        GetWindow(typeof(ClipInfo));
    }  
  
    public void OnGUI()
    {
        clip = EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)("Clip", clip, typeof(AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)), false) as AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html);  
  
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Curves:");
        if (clip != null)
        {
            foreach (var binding in AnimationUtility.GetCurveBindings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetCurveBindings.html)(clip))
            {
                AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve = AnimationUtility.GetEditorCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetEditorCurve.html)(clip, binding);
                EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)(binding.path + "/" + binding.propertyName + ", Keys: " + curve.keys.Length);
            }
        }
    }
}

```

* * *
