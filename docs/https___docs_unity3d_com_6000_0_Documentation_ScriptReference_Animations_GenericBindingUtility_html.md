* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.html

# GenericBindingUtility
class in UnityEngine.Animations
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
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
### Description
Animation utility functions for reading and writing values from Unity components.
```
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Animations;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using Unity.Collections;
using System.Linq;  
  
public class AnimationClipPlayer : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)        animationClip;
    public float                time;  
  
    List<AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)>        curves;  
  
    NativeArray<BoundProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html)>  floatProperties;
    NativeArray<BoundProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html)>  intProperties;
    NativeArray<float>          floatValues;
    NativeArray<int>            intValues;  
  
    void Start()
    {
        var editorCurveBindings = AnimationUtility.GetCurveBindings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetCurveBindings.html)(animationClip);
        editorCurveBindings = editorCurveBindings.Where(editorCurveBinding =>
            editorCurveBinding.type != typeof(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)) && !editorCurveBinding.isPPtrCurve && !editorCurveBinding.isDiscreteCurve
            ).ToArray();  
  
        curves = new List<AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)>(editorCurveBindings.Length);
        for (var i = 0; i < editorCurveBindings.Length; i++)
        {
            curves.Add(AnimationUtility.GetEditorCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetEditorCurve.html)(animationClip, editorCurveBindings[i]));
        }  
  
        var genericBindings = new NativeArray<GenericBinding[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding.html)>(AnimationUtility.EditorCurveBindingsToGenericBindings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.EditorCurveBindingsToGenericBindings.html)(editorCurveBindings), Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
        GenericBindingUtility.BindProperties[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.BindProperties.html)(gameObject, genericBindings, out floatProperties, out intProperties, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));  
  
        floatValues = new NativeArray<float>(floatProperties.Length, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
        intValues = new NativeArray<int>(intProperties.Length, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
    }  
  
    private void OnDestroy()
    {
        floatProperties.Dispose();
        floatValues.Dispose();
        intProperties.Dispose();
        intValues.Dispose();
    }  
  
    // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) is called once per frame
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        for (int i = 0; i < curves.Count; i++)
        {
            floatValues[i] = curves[i].Evaluate(time);
        }  
  
        GenericBindingUtility.SetValues[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.SetValues.html)(floatProperties, floatValues);
    }
}

```

### Static Methods
Method | Description  
---|---  
[BindProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.BindProperties.html) | Retrieves the list of BoundProperty defined by the list of GenericBinding.  
[CreateGenericBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.CreateGenericBinding.html) | Retrieves the GenericBinding that represents a specific property associated with a GameObject or one of its components.  
[GetAnimatableBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.GetAnimatableBindings.html) | Retrieves the animatable bindings for a specific GameObject.  
[GetCurveBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.GetCurveBindings.html) | Retrieves the curve bindings from an animation clip.  
[GetValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.GetValues.html) | Retrieves the float or integer value for each [[BoundProperty].  
[SetValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.SetValues.html) | Sets the float or integer value for each [[BoundProperty].  
[UnbindProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.UnbindProperties.html) | Unbinds and frees all resources used by a list of BoundProperty.  
* * *
