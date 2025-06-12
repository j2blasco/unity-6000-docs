* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayModeWindow.SetCustomRenderingResolution.html

#  [PlayModeWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayModeWindow.html).SetCustomRenderingResolution
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
public static void SetCustomRenderingResolution(uint width, uint height, string baseName); 
### Parameters
Parameter | Description  
---|---  
width | The custom resolution width.  
height | The custom resolution height.  
baseName | The basename for the custom resolution entry.  
### Description
Adds a new Custom resolution entry with the specified baseName. If an entry with the same baseName already exists, this method updates the resolution of this entry with the new values.
* * *
