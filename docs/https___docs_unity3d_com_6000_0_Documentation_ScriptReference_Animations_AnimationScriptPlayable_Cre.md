* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.Create.html

#  [AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html).Create
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
public static [Animations.AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html) Create([Playables.PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) graph, T jobData, int inputCount); 
### Parameters
Parameter | Description  
---|---  
graph | The PlayableGraph object that will own the AnimationScriptPlayable.  
job | The [IAnimationJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html) to execute when processing the playable.  
inputCount | The number of inputs on the playable.  
### Returns
**AnimationScriptPlayable** A new [AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html) linked to the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html). 
### Description
Creates an [AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html) in the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).
This playable contains a job implementing an [IAnimationJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html). This interface defines two methods that will be called while processing the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).  
  
Here is an example of how to create an [AnimationScriptPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html) with a simple [IAnimationJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html):
```
using UnityEngine;
using UnityEngine.Playables;
using UnityEngine.Animations;  
  
public struct AnimationJob : IAnimationJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html)
{
    public int userData;  
  
    public void ProcessRootMotion(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
        // This method is called during the root motion process pass.
    }  
  
    public void ProcessAnimation(AnimationStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) stream)
    {
        // This method is called during the animation process pass.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(string.Format("Value of the userData: {0}", userData));
    }
}  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)))]
public class AnimationScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) m_Graph;
    AnimationScriptPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.html) m_AnimationScriptPlayable;  
  
    void OnEnable()
    {
        m_Graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)("AnimationScriptExample");
        var output = AnimationPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html)(m_Graph, "ouput", GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>());  
  
        var animationJob = new AnimationJob();
        m_AnimationScriptPlayable = AnimationScriptPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationScriptPlayable.Create.html)(m_Graph, animationJob);  
  
        output.SetSourcePlayable(m_AnimationScriptPlayable);
        m_Graph.Play();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        var animationJob = m_AnimationScriptPlayable.GetJobData<AnimationJob>();
        ++animationJob.userData;
        m_AnimationScriptPlayable.SetJobData(animationJob);
    }  
  
    void OnDisable()
    {
        m_Graph.Destroy();
    }
}

```

Additional resources: [IAnimationJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.html), [AnimatorJobExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.html).
* * *
