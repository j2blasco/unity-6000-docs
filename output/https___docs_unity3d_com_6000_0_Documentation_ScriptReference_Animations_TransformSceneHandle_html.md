* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.html

# TransformSceneHandle
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
Handle to read position, rotation and scale of an object in the Scene.
TransformSceneHandle are read-only.  
  
A TransformSceneHandle is a safe handle on a [TransformAccess](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.html). The [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) used to create this handle manages the validity of this handle.
```
using UnityEngine;
using UnityEngine.Playables;
using UnityEngine.Animations;  
  
public struct TransformSceneHandleJob : IAnimationJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html)
{
    public TransformSceneHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.html) handle;  
  
    public void ProcessRootMotion(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
        // Log the local position.
        var position = handle.GetLocalPosition(stream);
        Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)("Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html): {0}", position);  
  
        // Log the local rotation (converted from euler).
        var rotation = handle.GetLocalRotation(stream);
        Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)("Rotation: {0}", rotation.eulerAngles);  
  
        // Log the local scale.
        var scale = handle.GetLocalScale(stream);
        Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)("Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html): {0}", scale);
    }  
  
    public void ProcessAnimation(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
    }
}  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)))]
public class TransformSceneHandleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) sceneTransform;  
  
    PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) m_Graph;
    AnimationScriptPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html) m_AnimationScriptPlayable;  
  
    void Start()
    {
        if (sceneTransform == null)
            return;  
  
        var animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();  
  
        m_Graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)("TransformSceneHandleExample");
        var output = AnimationPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html)(m_Graph, "output", animator);  
  
        var animationJob = new TransformSceneHandleJob();
        animationJob.handle = animator.BindSceneTransform(sceneTransform);
        m_AnimationScriptPlayable = AnimationScriptPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.Create.html)(m_Graph, animationJob);  
  
        output.SetSourcePlayable(m_AnimationScriptPlayable);
        m_Graph.Play();
    }  
  
    void OnDisable()
    {
        if (sceneTransform == null)
            return;  
  
        m_Graph.Destroy();
    }
}

```

Additional resources: [AnimatorJobExtensions.BindSceneTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindSceneTransform.html), [PropertySceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html), [PropertyStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html), and [TransformStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.html).
### Public Methods
Method | Description  
---|---  
[GetGlobalTR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.GetGlobalTR.html) | Gets the position and scaled rotation of the transform in world space.  
[GetLocalPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.GetLocalPosition.html) | Gets the position of the transform relative to the parent.  
[GetLocalRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.GetLocalRotation.html) | Gets the rotation of the transform relative to the parent.  
[GetLocalScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.GetLocalScale.html) | Gets the scale of the transform relative to the parent.  
[GetLocalToParentMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.GetLocalToParentMatrix.html) | Gets the local to parent matrix of the transform.  
[GetLocalToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.GetLocalToWorldMatrix.html) | Gets the local to world matrix of the transform.  
[GetLocalTRS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.GetLocalTRS.html) | Gets the position, rotation and scale of the transform relative to the parent.  
[GetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.GetPosition.html) | Gets the position of the transform in world space.  
[GetRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.GetRotation.html) | Gets the rotation of the transform in world space.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.IsValid.html) | Returns whether this is a valid handle.  
* * *
