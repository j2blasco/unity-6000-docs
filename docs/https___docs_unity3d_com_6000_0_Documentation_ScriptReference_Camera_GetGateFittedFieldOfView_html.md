* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetGateFittedFieldOfView.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).GetGateFittedFieldOfView
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
## Declaration
public float GetGateFittedFieldOfView(); 
### Returns
**float** Returns the effective vertical field of view. 
### Description
Retrieves the effective vertical field of view of the camera, including GateFit. Fitting the sensor gate and the resolution gate has an impact on the final field of view. If the sensor gate aspect ratio is the same as the resolution gate aspect ratio or if the camera is not in physical mode, then this method returns the same value as the fieldofview property. 
* * *
