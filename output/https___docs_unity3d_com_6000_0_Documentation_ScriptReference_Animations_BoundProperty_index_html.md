* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty-index.html

#  [BoundProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html).index
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
index; 
### Description
The index of this BoundProperty to the internal list of bound properties.
The bound property index is recycled when a domain reload occurs or when either the GameObject or Component associated with a BoundProperty is destroyed. When the index is recycled, the system increments the version identifier. To represent the same BoundProperty, the Index and the Version must match. If the Index and Version differ, then the Index has been recycled.
* * *
