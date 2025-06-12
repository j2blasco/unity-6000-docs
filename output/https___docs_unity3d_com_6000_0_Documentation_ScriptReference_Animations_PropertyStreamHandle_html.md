* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html

# PropertyStreamHandle
struct in UnityEngine.Animations
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
Handle for a [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) property on an object in the [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html).
```
using UnityEngine;
using UnityEngine.Playables;
using UnityEngine.Animations;  
  
public struct PropertyStreamHandleJob : IAnimationJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html)
{
    public PropertyStreamHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html) handleR;
    public PropertyStreamHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html) handleG;
    public PropertyStreamHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html) handleB;
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color;  
  
    public void ProcessRootMotion(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
    }  
  
    public void ProcessAnimation(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
        // Set the new light color.
        handleR.SetFloat(stream, color.r);
        handleG.SetFloat(stream, color.g);
        handleB.SetFloat(stream, color.b);
    }
}  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)))]
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)))]
public class PropertyStreamHandleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);  
  
    PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) m_Graph;
    AnimationScriptPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html) m_AnimationScriptPlayable;  
  
    void Start()
    {
        var animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();  
  
        m_Graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)("PropertyStreamHandleExample");
        var output = AnimationPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html)(m_Graph, "output", animator);  
  
        var animationJob = new PropertyStreamHandleJob();
        animationJob.handleR = animator.BindStreamProperty(gameObject.transform, typeof(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)), "m_Color.r");
        animationJob.handleG = animator.BindStreamProperty(gameObject.transform, typeof(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)), "m_Color.g");
        animationJob.handleB = animator.BindStreamProperty(gameObject.transform, typeof(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)), "m_Color.b");
        m_AnimationScriptPlayable = AnimationScriptPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.Create.html)(m_Graph, animationJob);  
  
        output.SetSourcePlayable(m_AnimationScriptPlayable);
        m_Graph.Play();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var animationJob = m_AnimationScriptPlayable.GetJobData<PropertyStreamHandleJob>();
        animationJob.color = color;
        m_AnimationScriptPlayable.SetJobData(animationJob);
    }  
  
    void OnDisable()
    {
        m_Graph.Destroy();
    }
}

```

Additional resources: [AnimatorJobExtensions.BindStreamProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindStreamProperty.html), [TransformStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.html), [PropertySceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html), and [TransformSceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.html).
### Public Methods
Method | Description  
---|---  
[GetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.GetBool.html) | Gets the boolean property value from a stream.  
[GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.GetFloat.html) | Gets the float property value from a stream.  
[GetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.GetInt.html) | Gets the integer property value from a stream.  
[GetReadMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.GetReadMask.html) | Gets the read mask of the property.  
[IsResolved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.IsResolved.html) | Returns whether or not the handle is resolved.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.IsValid.html) | Returns whether or not the handle is valid.  
[Resolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.Resolve.html) | Resolves the handle.  
[SetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.SetBool.html) | Sets the boolean property value into a stream.  
[SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.SetFloat.html) | Sets the float property value into a stream.  
[SetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.SetInt.html) | Sets the integer property value into a stream.  
* * *
