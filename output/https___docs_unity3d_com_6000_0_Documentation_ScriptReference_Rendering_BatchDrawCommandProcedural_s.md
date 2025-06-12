* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandProcedural-splitVisibilityMask.html

#  [BatchDrawCommandProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandProcedural.html).splitVisibilityMask
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
splitVisibilityMask; 
### Description
Indicates which splits that the draw command is visible in.
Unity uses this when it culls shadow map splits simultaneously. A split refers to a shadow cascade in a directional light shadow map or a cube map face in a point light shadow map.  
  
This is an 8-bit bitfield where a value of `1` indicates that Unity should render the draw command in the split, and a value of `0` indicates that Unity shouldn't render the draw command in the split. The least significant bit corresponds to the first culling split (array index 0) and each successive bit corresponds to the next culling split up until a maximum of six bits. 
* * *
