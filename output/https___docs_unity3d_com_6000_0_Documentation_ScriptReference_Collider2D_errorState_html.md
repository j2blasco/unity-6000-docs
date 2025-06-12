* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-errorState.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).errorState
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
[ColliderErrorState2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderErrorState2D.html) errorState; 
### Description
The error state that indicates the state of the physics shapes the 2D Collider tried to create. (Read Only)
The 2D Collider can sometimes encounter an issue when creating the physics shapes which it represents. This can either be that some of the physics shapes were not able to be created or in the worst case, none of them could be created.  
  
The 2D Collider may not be able to create an underlying physics shape due to the physics engine's constraints on physics shapes, such as the vertices must not be too close or collinear; or that the total physics shape area must not be too small.  
  
Additional resources: [ColliderErrorState2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderErrorState2D.html).
* * *
