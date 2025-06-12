* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.DestroyPlayable.html

#  [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).DestroyPlayable
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
public void DestroyPlayable(U playable); 
### Parameters
Parameter | Description  
---|---  
playable | The playable to destroy.  
### Description
Destroys the Playable.
Playables connected to the destroyed Playable output ports are orphaned. These orphaned Playables still exist in the PlayableGraph. Orphaned Playables are not updated until they are connected to a branch that is connected to a [PlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutput.html).
* * *
