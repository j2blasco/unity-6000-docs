* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshColliderCookingOptions.CookForFasterSimulation.html

#  [MeshColliderCookingOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshColliderCookingOptions.html).CookForFasterSimulation
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
### Description
Toggle between cooking for faster simulation or faster cooking time.
When set, this runs some extra steps to guarantee the resulting mesh is optimal for run-time performance. This affects performance of the physics queries as well as contacts generation. If not set, produces the result as fast as possible. Consequently, the cooked MeshCollider might not be optimal.
* * *
