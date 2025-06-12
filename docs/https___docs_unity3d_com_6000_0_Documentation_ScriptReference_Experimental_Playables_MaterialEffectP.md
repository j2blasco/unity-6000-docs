* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Playables.MaterialEffectPlayable.Create.html

**Experimental** : this API is experimental and might be changed or removed in the future.
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
### Parameters
Parameter | Description  
---|---  
graph | The [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) object that will own the [MaterialEffectPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Playables.MaterialEffectPlayable.html).  
material |  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) used to modify linked texture playable inputs.  
pass | Shader pass index.(Note: -1 for all passes).  
### Returns
**MaterialEffectPlayable** A [MaterialEffectPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Playables.MaterialEffectPlayable.html) linked to the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html). 
### Description
Creates a [MaterialEffectPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Playables.MaterialEffectPlayable.html) in the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).
NOTE: Each MaterialEffectPlayable input is connected to the selected Material’s texture properties (ie. texture input 0 is connected to the Material’s first texture property, texture input 1 to the second texture property, etc.)
* * *
