* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-requiresSrgbBlitToBackbuffer.html

#  [Display](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html).requiresSrgbBlitToBackbuffer
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
requiresSrgbBlitToBackbuffer; 
### Description
True when doing a blit to the back buffer requires manual color space conversion.
This property indicates whether the back buffer requires manual color space conversion from linear color space to sRGB in order to blit to it. The back buffer requires this if you are using linear color space and the back buffer does not support automatic conversion to sRGB.
* * *
