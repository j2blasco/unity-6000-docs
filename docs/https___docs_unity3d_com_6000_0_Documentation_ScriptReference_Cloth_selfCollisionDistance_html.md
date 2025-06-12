* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-selfCollisionDistance.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).selfCollisionDistance
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cloth.html "Go to Cloth Component in the Manual")
selfCollisionDistance; 
### Description
Minimum distance at which two cloth particles repel each other (default: 0.0).
A value larger than 0.0 enables particle versus particle collision. Self-collision distance should be smaller than the smallest distance between two particles in the rest configuration. If the distance is larger, self-collision may violate some distance constraints and result in jittering.
* * *
