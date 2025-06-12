* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.SearchWindow.Open.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [SearchWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.SearchWindow.html).Open
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
public static bool Open([Experimental.GraphView.SearchWindowContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.SearchWindowContext.html) context, T provider); 
### Parameters
Parameter | Description  
---|---  
context | Structure of parameters that configure the search window.  
provider | Reference to the object that provides the search results.  
### Returns
**bool** Returns true if the window opens successfully. Returns false otherwise. 
### Description
Opens the search window above the Graph.
The provider object must be of type ScriptableObject for the search window to maintain the its reference after a domain reload. For example, you can use your own instance of an EditorWindow subclass.
* * *
