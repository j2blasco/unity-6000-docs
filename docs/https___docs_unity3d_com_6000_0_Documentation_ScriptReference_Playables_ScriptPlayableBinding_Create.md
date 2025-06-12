* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableBinding.Create.html

#  [ScriptPlayableBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableBinding.html).Create
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
public static [Playables.PlayableBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBinding.html) Create(string name, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) key, Type type); 
### Parameters
Parameter | Description  
---|---  
key | A reference to a UnityEngine.Object that acts as a key for this binding.  
type | The type of object that will be bound to the [ScriptPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableOutput.html).  
name | The name of the ScriptPlayableOutput.  
### Returns
**PlayableBinding** Returns a [PlayableBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBinding.html) that contains information that is used to create a [ScriptPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableOutput.html). 
### Description
Creates a [PlayableBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBinding.html) that contains information representing a [ScriptPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableOutput.html).
```
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Playables;  
  
public class CustomPlayableAsset : PlayableAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableAsset.html)
{
    public override Playable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) CreatePlayable(PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) graph, GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) owner)
    {
        return Playable.Create(graph);
    }  
  
    public override IEnumerable<PlayableBinding[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBinding.html)> outputs
    {
        get { yield return ScriptPlayableBinding.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableBinding.Create.html)("ScriptPlayableOutput[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableOutput.html)", this, typeof(Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html))); }
    }
}

```

* * *
