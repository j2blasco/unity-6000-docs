* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-deltaTime.html

#  [FrameData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData.html).deltaTime
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
deltaTime; 
### Description
The interval between this frame and the preceding frame. The interval is unscaled and expressed in seconds.
To time-scale the interval, multiple the interval by [FrameData.effectiveSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData-effectiveSpeed.html). 
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that has an Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) and set the Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) field.
using UnityEngine;
using UnityEngine.Animations;
using UnityEngine.Playables;  
  
public class MyMonoBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) m_Animator;  
  
    private PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) m_Graph;
    private void Awake()
    {
        m_Graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)();
        m_Graph.SetTimeUpdateMode(DirectorUpdateMode.GameTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.DirectorUpdateMode.GameTime.html));  
  
        var scriptPlayable = ScriptPlayable<MyPlayableBehaviour>.Create(m_Graph);  
  
        // Sets game time's scale, as well as custom playable's speed.
        Time.timeScale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) = 10f;
        scriptPlayable.SetSpeed(0.5f);  
  
        var playableOutput = AnimationPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html)(m_Graph, "MyPlayableOutput", m_Animator);
        playableOutput.SetSourcePlayable(scriptPlayable, 0);  
  
        m_Graph.Play();
    }  
  
    private void OnDestroy()
    {
        if (m_Graph.IsValid())
            m_Graph.Destroy();
    }
}  
  
public sealed class MyPlayableBehaviour : PlayableBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html)
{
    public override void PrepareFrame(Playable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) playable, FrameData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData.html) info)
    {
        base.PrepareFrame(playable, info);  
  
        // info.deltaTime is not scaled, and so is 10 times smaller than Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html)
        // info.effectiveSpeed is equal to 5 (10 * 0.5). Time.timeScale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) is accounted for because we use DirectorUpdateMode.GameTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.DirectorUpdateMode.GameTime.html).
        // If we had used DirectorUpdateMode.UnscaledGameTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.DirectorUpdateMode.UnscaledGameTime.html), info.effectiveSpeed would have been equal to 0.5.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"info.deltaTime = {info.deltaTime}, speed {info.effectiveSpeed} Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) = {Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html)}");
    }
}

```

* * *
