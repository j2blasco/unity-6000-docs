* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineEditorUtility.GetDerivedTypesSupportedOnCurrentPipeline.html

#  [RenderPipelineEditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineEditorUtility.html).GetDerivedTypesSupportedOnCurrentPipeline
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
public static Type[] GetDerivedTypesSupportedOnCurrentPipeline(); 
### Returns
**Type[]** Child types of the base type supported on current pipeline. 
### Description
Returns the types that're children of `T` and have a [SupportedOnRenderPipelineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedOnRenderPipelineAttribute.html) corresponding to the render pipeline you're using. Order of the return types is arbitrary.
```
using UnityEditor.Rendering;
using UnityEngine;
using UnityEngine.Rendering;  
  
public interface IBaseClass
{
}  
  
[SupportedOnRenderPipeline]
public class SupportedOnClass : IBaseClass
{
}  
  
public class BehaviourTest : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var types = RenderPipelineEditorUtility.GetDerivedTypesSupportedOnCurrentPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineEditorUtility.GetDerivedTypesSupportedOnCurrentPipeline.html)<IBaseClass>();
        foreach (var type in types)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{type.Name} is supported on current Render Pipeline.");
        }
    }
}

```

Additional resources: [SupportedOnRenderPipelineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedOnRenderPipelineAttribute.html).
* * *
