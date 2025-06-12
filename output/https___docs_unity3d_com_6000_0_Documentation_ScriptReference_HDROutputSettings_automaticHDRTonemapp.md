* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings-automaticHDRTonemapping.html

#  [HDROutputSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings.html).automaticHDRTonemapping
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
automaticHDRTonemapping; 
### Description
Describes whether Unity performs HDR tonemapping automatically.
Set automaticHDRTonemapping to be true to instruct Unity to perform an automatic tonemapping of your final image onto the HDR display buffer immediately before it is presented to screen. Set automaticHDRTonemapping to be false to perform your own custom HDR tonemapping onto the display buffer of the active HDR display. This could be achieved as a custom post processing stage or by using [Camera.OnRenderImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnRenderImage.html) to blit the cameras output to the HDR display buffer using your own tonemapping shader.  
  
Performing your own tonemapping gives greater flexibility over the final image, whereas using Unity's automatic tonemapping provides a simple route to achieving HDR output.  
  
Some platforms don't support automatic HDR Tonemapping (see [SystemInfo.hdrDisplaySupportFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-hdrDisplaySupportFlags.html)). In this case, the default value of automaticHDRTonemapping is false and can't be changed. If automatic tonemapping is available, it's enabled by default.  
  
The value of automaticHDRTonemapping is ignored if HDR output is not active on the display.
* * *
