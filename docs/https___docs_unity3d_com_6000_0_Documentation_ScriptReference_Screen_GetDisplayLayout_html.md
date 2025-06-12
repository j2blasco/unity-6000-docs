* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.GetDisplayLayout.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).GetDisplayLayout
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
public static void GetDisplayLayout(List<DisplayInfo> displayLayout); 
### Parameters
Parameter | Description  
---|---  
displayLayout | Connected display information.  
### Description
Retrieves layout information about connected displays such as names, resolutions, and refresh rates.
This API does not allocate managed memory outside of the Editor. You can call this method without generating garbage or triggering the garbage collector. It is only supported on Linux, macOS, and Windows platforms.  
  
Additional resources: [DisplayInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DisplayInfo.html)
* * *
