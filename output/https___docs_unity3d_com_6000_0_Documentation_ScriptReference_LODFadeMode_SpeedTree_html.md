* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODFadeMode.SpeedTree.html

#  [LODFadeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODFadeMode.html).SpeedTree
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
By specifying this mode, your LODGroup will perform a SpeedTree-style LOD fading scheme:  

  * For all the mesh LODs other than the last (most crude) mesh LOD, the fade factor is calculated as the percentage of the object's current screen height, compared to the whole range of the LOD. It is 1, if the camera is right at the position where the previous LOD switches out and 0, if the next LOD is just about to switch in.  

  * For the last mesh LOD and the billboard LOD, the cross-fade mode is used.


* * *
