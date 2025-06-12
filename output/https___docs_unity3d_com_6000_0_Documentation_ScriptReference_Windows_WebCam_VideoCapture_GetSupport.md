* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.GetSupportedFrameRatesForResolution.html

#  [VideoCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html).GetSupportedFrameRatesForResolution
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
## Declaration
public static IEnumerable<float> GetSupportedFrameRatesForResolution([Resolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resolution.html) resolution); 
### Parameters
Parameter | Description  
---|---  
resolution | A recording resolution.  
### Returns
**IEnumerable <float>** The frame rates at which the video can be recorded. 
### Description
Returns the supported frame rates at which a video can be recorded given a resolution.
Use [VideoCapture.SupportedResolutions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.SupportedResolutions.html) to get the supported web camera recording resolutions.
* * *
