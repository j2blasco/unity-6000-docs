* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-removeConstantScaleCurves.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).removeConstantScaleCurves
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
removeConstantScaleCurves; 
### Description
Removes constant animation curves with values identical to the object initial scale value.
The FBX transform stack includes transform pivots that can be used to offset rotation and scaling transformations. When importing FBX content to Unity, transforms and animations are converted into a simpler transform stack and this operation can create additional animation curves. Enable this property to remove unnecessary scale curves.
* * *
