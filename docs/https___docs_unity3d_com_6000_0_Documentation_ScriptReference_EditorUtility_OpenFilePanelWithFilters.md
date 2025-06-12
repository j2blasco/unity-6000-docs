* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFilePanelWithFilters.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).OpenFilePanelWithFilters
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
public static string OpenFilePanelWithFilters(string title, string directory, string[] filters); 
### Parameters
Parameter | Description  
---|---  
title | Title for dialog.  
directory | Default directory.  
filters | File extensions in form: new string[] { "Image files", "png,jpg,jpeg", "All files", "*" }.  
### Description
Displays the "open file" dialog and returns the selected path name.
* * *
