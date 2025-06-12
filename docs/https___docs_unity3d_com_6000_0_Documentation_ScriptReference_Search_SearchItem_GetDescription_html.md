* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetDescription.html

#  [SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html).GetDescription
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
public string GetDescription([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, bool stripHTML); 
### Parameters
Parameter | Description  
---|---  
context | Any search context for the item search provider.  
stripHTML | True if any HTML tags should be dropped (if the control does not support HTML).  
### Returns
**string** The search item description. 
### Description
Fetch and format description.
* * *
