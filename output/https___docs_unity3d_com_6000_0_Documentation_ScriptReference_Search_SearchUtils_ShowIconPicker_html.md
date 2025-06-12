* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.ShowIconPicker.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).ShowIconPicker
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
public static void ShowIconPicker(Action<Texture2D,bool> iconSelectedHandler); 
### Parameters
Parameter | Description  
---|---  
iconSelectedHandler | Select handler invoked if the user selects an icon.  
### Description
Opens a search picker to select an icon.
In example, this API is used to select search query icons. This API try to filter out texture that would be suitable as an icon.
* * *
