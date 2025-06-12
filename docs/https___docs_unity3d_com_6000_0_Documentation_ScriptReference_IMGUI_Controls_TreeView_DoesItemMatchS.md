* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.DoesItemMatchSearch.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).DoesItemMatchSearch
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
protected bool DoesItemMatchSearch([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) item, string search); 
### Parameters
Parameter | Description  
---|---  
item | Item used for matching against the search string.  
search | The search string of the TreeView.  
### Returns
**bool** True if item matches search string, otherwise false. 
### Description
Override this function to extend or change the search behavior.
This function is called automatically for each TreeViewItem by the default BuildRows method. If true is returned then the TreeViewItem becomes part of the search result.  
  
If you are overriding BuildRows and are building only the visible rows then handle the search yourself against your backend which has all the state.  
  
By default this function is matching the search string against the name of the item.
* * *
