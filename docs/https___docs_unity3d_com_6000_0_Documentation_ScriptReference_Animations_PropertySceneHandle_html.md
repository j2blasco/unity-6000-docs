* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html

# PropertySceneHandle
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
Handle to read a [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) property on an object in the Scene.
PropertySceneHandle are read-only.
```
using UnityEngine;
using UnityEngine.Playables;
using UnityEngine.Animations;  
  
public struct PropertySceneHandleJob : IAnimationJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html)
{
    public PropertySceneHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html) handleR;
    public PropertySceneHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html) handleG;
    public PropertySceneHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.html) handleB;  
  
    public void ProcessRootMotion(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
    }  
  
    public void ProcessAnimation(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
        // Log the light color.
        var r = handleR.GetFloat(stream);
        var g = handleG.GetFloat(stream);
        var b = handleB.GetFloat(stream);
        Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)("Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) color: (R: {0}, G: {1}, B: {2})", r, g, b);
    }
}  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)))]
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)))]
public class PropertySceneHandleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) sceneLight;  
  
    PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) m_Graph;
    AnimationScriptPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html) m_AnimationScriptPlayable;  
  
    void Start()
    {
        if (sceneLight == null)
            return;  
  
        var animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();  
  
        m_Graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)("PropertySceneHandleExample");
        var output = AnimationPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html)(m_Graph, "output", animator);  
  
        var animationJob = new PropertySceneHandleJob();
        animationJob.handleR = animator.BindSceneProperty(sceneLight.transform, typeof(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)), "m_Color.r");
        animationJob.handleG = animator.BindSceneProperty(sceneLight.transform, typeof(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)), "m_Color.g");
        animationJob.handleB = animator.BindSceneProperty(sceneLight.transform, typeof(Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)), "m_Color.b");
        m_AnimationScriptPlayable = AnimationScriptPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.Create.html)(m_Graph, animationJob);  
  
        output.SetSourcePlayable(m_AnimationScriptPlayable);
        m_Graph.Play();
    }  
  
    void OnDisable()
    {
        if (sceneLight == null)
            return;  
  
        m_Graph.Destroy();
    }
}

```

Additional resources: [AnimatorJobExtensions.BindSceneProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindSceneProperty.html), [TransformSceneHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformSceneHandle.html), [PropertyStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html), and [TransformStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransformStreamHandle.html).
### Public Methods
Method | Description  
---|---  
[GetBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.GetBool.html) | Gets the boolean property value from an object in the Scene.  
[GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.GetFloat.html) | Gets the float property value from an object in the Scene.  
[GetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.GetInt.html) | Gets the integer property value from an object in the Scene.  
[IsResolved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.IsResolved.html) | Returns whether or not the handle is resolved.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.IsValid.html) | Returns whether or not the handle is valid.  
[Resolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertySceneHandle.Resolve.html) | Resolves the handle.  
* * *
