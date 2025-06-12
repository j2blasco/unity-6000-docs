* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html

# PlayableBehaviour
class in UnityEngine.Playables
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
  

Implements interfaces:[IPlayableBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayableBehaviour.html)
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
PlayableBehaviour is the base class from which every custom playable script derives.
A PlayableBehaviour can be used to add user-defined behaviour to a [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).  
  
A PlayableBehaviour must be part of a branch of a [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) that is connected to an output to be active.  
  
In the following example, two [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) are controlled by two [AnimationClipPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationClipPlayable.html), which are blended by a [AnimationMixerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html). A custom BlenderPlayableBehaviour is modifying the inputs weigth of the [AnimationMixerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html) every frame.
```
using UnityEngine;
using UnityEngine.Animations;
using UnityEngine.Playables;  
  
public class BlenderPlayableBehaviour : PlayableBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html)
{
    public AnimationMixerPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html) mixerPlayable;  
  
    public override void PrepareFrame(Playable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) playable, FrameData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData.html) info)
    {
        float blend = Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)((float)playable.GetTime(), 1.0f);  
  
        mixerPlayable.SetInputWeight(0, blend);
        mixerPlayable.SetInputWeight(1, 1.0f - blend);  
  
        base.PrepareFrame(playable, info);
    }
}  
  
public class PlayableBehaviourSample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) m_Graph;
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clipA;
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clipB;  
  
    // Use this for initialization
    void Start()
    {
        // Create the PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).
        m_Graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)();  
  
        // Add an AnimationPlayableOutput[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html) to the graph.
        var animOutput = AnimationPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html)(m_Graph, "AnimationOutput", GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>());  
  
        // Add an AnimationMixerPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html) to the graph.
        var mixerPlayable = AnimationMixerPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.Create.html)(m_Graph, 2);  
  
        // Add two AnimationClipPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationClipPlayable.html) to the graph.
        var clipPlayableA = AnimationClipPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationClipPlayable.Create.html)(m_Graph, clipA);
        var clipPlayableB = AnimationClipPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationClipPlayable.Create.html)(m_Graph, clipB);  
  
        // Add a custom PlayableBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html) to the graph.
        // This behavior will change the weights of the mixer dynamically.
        var blenderPlayable = ScriptPlayable<BlenderPlayableBehaviour>.Create(m_Graph, 1);
        blenderPlayable.GetBehaviour().mixerPlayable = mixerPlayable;  
  
        // Create the topology, connect the AnimationClipPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationClipPlayable.html) to the
        // AnimationMixerPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html).  Also add the BlenderPlayableBehaviour.
        m_Graph.Connect(clipPlayableA, 0, mixerPlayable, 0);
        m_Graph.Connect(clipPlayableB, 0, mixerPlayable, 1);
        m_Graph.Connect(mixerPlayable, 0, blenderPlayable, 0);  
  
        // Use the ScriptPlayable as the source for the AnimationPlayableOutput[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html).
        // Since it's a ScriptPlayable, also set the source input port to make the
        // passthrough to the AnimationMixerPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html).
        animOutput.SetSourcePlayable(blenderPlayable);
        animOutput.SetSourceInputPort(0);  
  
        // Play the graph.
        m_Graph.Play();
    }  
  
    private void OnDestroy()
    {
        // Destroy the graph once done with it.
        m_Graph.Destroy();
    }
}

```

### Public Methods
Method | Description  
---|---  
[OnBehaviourPause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.OnBehaviourPause.html) | This method is invoked when one of the following situations occurs: The effective play state during traversal is changed to PlayState.Paused. This state is indicated by FrameData.effectivePlayState. The PlayableGraph is stopped while the playable play state is Playing. This state is indicated by PlayableGraph.IsPlaying returning true.  
[OnBehaviourPlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.OnBehaviourPlay.html) | This function is called when the Playable play state is changed to PlayState.Playing.  
[OnGraphStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.OnGraphStart.html) | This function is called when the PlayableGraph that owns this PlayableBehaviour starts.  
[OnGraphStop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.OnGraphStop.html) | This function is called when the PlayableGraph that owns this PlayableBehaviour stops.  
[OnPlayableCreate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.OnPlayableCreate.html) | This function is called when the Playable that owns the PlayableBehaviour is created.  
[OnPlayableDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.OnPlayableDestroy.html) | This function is called when the Playable that owns the PlayableBehaviour is destroyed.  
[PrepareData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.PrepareData.html) | This function is called during the PrepareData phase of the PlayableGraph.  
[PrepareFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.PrepareFrame.html) | This function is called during the PrepareFrame phase of the PlayableGraph.  
[ProcessFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.ProcessFrame.html) | This function is called during the ProcessFrame phase of the PlayableGraph.  
* * *
