* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView-ctor.html

# TreeView Constructor
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
public TreeView(); 
### Description
Creates a [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView.html) with all default properties. 
Use BaseTreeView.SetRootItems_1 to add content. 
* * *
## Declaration
public TreeView(Func<VisualElement> makeItem, Action<VisualElement,int> bindItem); 
### Parameters
Parameter | Description  
---|---  
makeItem | The factory method to call to create a display item. The method should return a VisualElement that can be bound to a data item.  
bindItem | The method to call to bind a data item to a display item. The method receives as parameters the display item to bind, and the index of the data item to bind it to.  
### Description
Creates a [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView.html) with specified factory methods. 
Use BaseTreeView.SetRootItems_1 to add content. 
* * *
## Declaration
public TreeView(int itemHeight, Func<VisualElement> makeItem, Action<VisualElement,int> bindItem); 
### Parameters
Parameter | Description  
---|---  
itemHeight | The item height to use in FixedHeight virtualization mode.  
makeItem | The factory method to call to create a display item. The method should return a VisualElement that can be bound to a data item.  
bindItem | The method to call to bind a data item to a display item. The method receives as parameters the display item to bind, and the index of the data item to bind it to.  
### Description
Creates a [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView.html) with specified factory methods using the fixed height virtualization method. 
Use BaseTreeView.SetRootItems_1 to add content. 
* * *
