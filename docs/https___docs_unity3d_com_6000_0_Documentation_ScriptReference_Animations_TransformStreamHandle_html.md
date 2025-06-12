* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.html

# TransformStreamHandle
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
Position, rotation and scale of an object in the [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html).
```
using UnityEngine;
using UnityEngine.Playables;
using UnityEngine.Animations;  
  
public struct TransformStreamHandleJob : IAnimationJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html)
{
    public TransformStreamHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.html) handle;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rotation;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scale;  
  
    public void ProcessRootMotion(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
        // Set the new local position.
        handle.SetLocalPosition(stream, position);  
  
        // Set the new local rotation (converted from euler).
        handle.SetLocalRotation(stream, Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(rotation));  
  
        // Set the new local scale.
        handle.SetLocalScale(stream, scale);
    }  
  
    public void ProcessAnimation(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
    }
}  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)))]
public class TransformStreamHandleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) rotation;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scale = Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html);  
  
    PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) m_Graph;
    AnimationScriptPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html) m_AnimationScriptPlayable;  
  
    void Start()
    {
        var animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();  
  
        m_Graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)("TransformStreamHandleExample");
        var output = AnimationPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html)(m_Graph, "output", animator);  
  
        var animationJob = new TransformStreamHandleJob();
        animationJob.handle = animator.BindStreamTransform(gameObject.transform);
        m_AnimationScriptPlayable = AnimationScriptPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.Create.html)(m_Graph, animationJob);  
  
        output.SetSourcePlayable(m_AnimationScriptPlayable);
        m_Graph.Play();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var animationJob = m_AnimationScriptPlayable.GetJobData<TransformStreamHandleJob>();
        animationJob.position = position;
        animationJob.rotation = rotation;
        animationJob.scale = scale;
        m_AnimationScriptPlayable.SetJobData(animationJob);
    }  
  
    void OnDisable()
    {
        m_Graph.Destroy();
    }
}

```

Additional resources: [AnimatorJobExtensions.BindStreamTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindStreamTransform.html), [PropertyStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html), [PropertySceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html), and [TransformSceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.html).
### Public Methods
Method | Description  
---|---  
[GetGlobalTR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetGlobalTR.html) | Gets the position and scaled rotation of the transform in world space.  
[GetLocalPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetLocalPosition.html) | Gets the position of the transform relative to the parent.  
[GetLocalRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetLocalRotation.html) | Gets the rotation of the transform relative to the parent.  
[GetLocalScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetLocalScale.html) | Gets the scale of the transform relative to the parent.  
[GetLocalToParentMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetLocalToParentMatrix.html) | Gets the local to parent matrix of the transform.  
[GetLocalToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetLocalToWorldMatrix.html) | Gets the local to world matrix of the transform.  
[GetLocalTRS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetLocalTRS.html) | Gets the position, rotation and scale of the transform relative to the parent.  
[GetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetPosition.html) | Gets the position of the transform in world space.  
[GetPositionReadMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetPositionReadMask.html) | Gets the position read mask of the transform.  
[GetRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetRotation.html) | Gets the rotation of the transform in world space.  
[GetRotationReadMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetRotationReadMask.html) | Gets the rotation read mask of the transform.  
[GetScaleReadMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.GetScaleReadMask.html) | Gets the scale read mask of the transform.  
[IsResolved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.IsResolved.html) | Returns whether this handle is resolved.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.IsValid.html) | Returns whether this is a valid handle.  
[Resolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.Resolve.html) | Bind this handle with an animated values from the AnimationStream.  
[SetGlobalTR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.SetGlobalTR.html) | Sets the position and rotation of the transform in world space.  
[SetLocalPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.SetLocalPosition.html) | Sets the position of the transform relative to the parent.  
[SetLocalRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.SetLocalRotation.html) | Sets the rotation of the transform relative to the parent.  
[SetLocalScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.SetLocalScale.html) | Sets the scale of the transform relative to the parent.  
[SetLocalTRS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.SetLocalTRS.html) | Sets the position, rotation and scale of the transform relative to the parent.  
[SetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.SetPosition.html) | Sets the position of the transform in world space.  
[SetRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.SetRotation.html) | Sets the rotation of the transform in world space.  
* * *
