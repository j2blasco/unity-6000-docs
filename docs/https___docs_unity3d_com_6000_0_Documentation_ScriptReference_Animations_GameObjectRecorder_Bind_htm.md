* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.Bind.html

#  [GameObjectRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html).Bind
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
public void Bind([EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html) binding); 
### Parameters
Parameter | Description  
---|---  
binding | The binding definition.  
### Description
Binds a GameObject's property as defined by [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html).
Use this function to bind a specific GameObject's property. The binding is defined in [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html). See the following example on binding the `MeshRenderer.m_Enabled` property.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Animations;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var recorder = new GameObjectRecorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html)(gameObject);  
  
        // Add a binding on the position on X axis.
        EditorCurveBinding[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html) binding = EditorCurveBinding.FloatCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.FloatCurve.html)("", typeof(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)), "m_LocalPosition.x");
        recorder.Bind(binding);  
  
        // Add a binding on the activation of the MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) component.
        binding = EditorCurveBinding.FloatCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.FloatCurve.html)("", typeof(MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)), "m_Enabled");
        recorder.Bind(binding);
    }
}

```

* * *
