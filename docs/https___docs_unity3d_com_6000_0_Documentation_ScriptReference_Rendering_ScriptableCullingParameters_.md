* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableCullingParameters-maximumVisibleLights.html

#  [ScriptableCullingParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableCullingParameters.html).maximumVisibleLights
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
maximumVisibleLights; 
### Description
This parameter controls how many visible lights are allowed.
Default is set to unlimited (-1).  
  
If this parameter has a value other than -1, Unity does not render lights in excess of that value.  
  
Unity avoids culling lights that contribute significantly to the lighting result. When there are more lights in the Scene than allowed by this parameter, Unity renders Directional lights first, then the lights closest to the camera, proceeding away from the camera until it reaches the light limit. 
* * *
