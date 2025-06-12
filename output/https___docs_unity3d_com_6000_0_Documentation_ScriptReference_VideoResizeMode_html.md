* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoResizeMode.html

# VideoResizeMode
enumeration
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
How the video clip's images will be resized during transcoding.
When choosing a mode that may result in a change in aspect ratio, use the VideoClipImporter.keepRatio property to control the addition of padding.
### Properties
Property | Description  
---|---  
[OriginalSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoResizeMode.OriginalSize.html) | Same width and height as the source.  
[ThreeQuarterRes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoResizeMode.ThreeQuarterRes.html) | 3/4 width and height.  
[HalfRes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoResizeMode.HalfRes.html) | Half width and height.  
[QuarterRes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoResizeMode.QuarterRes.html) | Quarter width and height.  
[Square1024](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoResizeMode.Square1024.html) | Fit source in a 1024x1024 rectangle.  
[Square512](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoResizeMode.Square512.html) | Fit source in a 512x512 rectangle.  
[Square256](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoResizeMode.Square256.html) | Fit source in a 256x256 rectangle.  
[CustomSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoResizeMode.CustomSize.html) | Resulting size will be driven by VideoClipImporter.customWidth and VideoClipImporter.customHeight.  
* * *
