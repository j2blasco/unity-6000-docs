* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.IsDone.html

#  [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).IsDone
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
public bool IsDone(); 
### Returns
**bool** A boolean indicating if the graph is done playing or not. 
### Description
Indicates that a graph has completed its operations.
Returns true if a graph has [PlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutput.html)s, and the source playable on all of its outputs have completed their operations.
* * *
