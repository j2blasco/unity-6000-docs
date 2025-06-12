* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D-offsetDistance.html

#  [CompositeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.html).offsetDistance
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
offsetDistance; 
### Description
Vertices are offset by this distance when compositing multiple physic shapes. Any vertices between shapes within this distance are combined.
Do not set the distance offset to higher than 1% of the Sprite's length, as this may result in a loss in detail when too many vertices are combined together.
* * *
