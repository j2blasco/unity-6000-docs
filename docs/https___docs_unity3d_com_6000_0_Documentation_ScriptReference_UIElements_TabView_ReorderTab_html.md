* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TabView.ReorderTab.html

#  [TabView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TabView.html).ReorderTab
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
public void ReorderTab(int from, int to); 
### Parameters
Parameter | Description  
---|---  
from | The current index of the tab to move.  
to | The target index to move the tab to.  
### Description
Moves the tab from the specified index to a new index. 
If the TabView contains a view-data-key, reorder the tab only after the view data is applied. Otherwise, the view data will override the order. 
* * *
