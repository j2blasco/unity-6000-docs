* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationLayerMixerPlayable.SetLayerMaskFromAvatarMask.html

#  [AnimationLayerMixerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationLayerMixerPlayable.html).SetLayerMaskFromAvatarMask
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
public void SetLayerMaskFromAvatarMask(uint layerIndex, [AvatarMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.html) mask); 
### Parameters
Parameter | Description  
---|---  
layerIndex | The layer index.  
mask | The AvatarMask used to create the new LayerMask.  
### Description
Sets the mask for the current layer.
This function generates a layer mask from the specified AvatarMask, and applies it to the specified Layer index. If you change the AvatarMask, you need to call this function again to update the layer mask.
```
using System.Collections.Generic;
using UnityEngine;  
  
using UnityEngine.Playables;
using UnityEngine.Animations;  
  
public class LayerMixerPlayable : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip1;
    public AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip2;
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) leftShoulder;  
  
    PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) m_Graph;
    AnimationLayerMixerPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationLayerMixerPlayable.html) m_Mixer;  
  
    public float mixLevel = 0.5f;  
  
    AvatarMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.html) mask;  
  
    public void Start()
    {
        Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();  
  
        mask = new AvatarMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.html)();
        mask.AddTransformPath(leftShoulder, true);  
  
        m_Graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)();
        var playableOutput = AnimationPlayableOutput.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html)(m_Graph, "LayerMixer", animator);
        playableOutput.SetSourcePlayable(m_Mixer);  
  
        // Create two clip playables
        var clipPlayable1 = AnimationClipPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationClipPlayable.Create.html)(m_Graph, clip1);
        var clipPlayable2 = AnimationClipPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationClipPlayable.Create.html)(m_Graph, clip2);  
  
        // Create mixer playable
        m_Mixer = AnimationLayerMixerPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationLayerMixerPlayable.Create.html)(m_Graph, 2);  
  
        // Create two layers, second is setup to override the first layer and affect only left shoulder and childs
        m_Mixer.ConnectInput(0, clipPlayable1, 0, 1.0f);
        m_Mixer.ConnectInput(1, clipPlayable2, 0, mixLevel);  
  
        m_Mixer.SetLayerMaskFromAvatarMask(1, mask);  
  
        m_Graph.Play();
    }  
  
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        m_Mixer.SetInputWeight(1, mixLevel);
    }  
  
    public void OnDestroy()
    {
        m_Graph.Destroy();
    }
}

```

* * *
