* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.BuildRows.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).BuildRows
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
protected IList<TreeViewItem> BuildRows([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) root); 
### Parameters
Parameter | Description  
---|---  
root | Root item that was created in the BuildRoot method.  
### Returns
**IList <TreeViewItem>** The rows list shown in the TreeView. Can later be accessed using GetRows(). 
### Description
Override this method to take control of how the rows are generated.
This method is called when Reload is called and every time items are expanded or collapsed. The default implementation of BuildRows takes care of caching the expanded rows based on the full tree and the expanded state of items.  
  
For very large data-sets or for data that change often it can be desirable to only create the rows of the TreeView and not the full tree. In this situation override this method to build the rows manually. If a collapsed parent is encountered then the descendants of that parent can be omitted (since they are not visible). Set the children of that item using the CreateChildListForCollapsedParent() method.  
  
When using this approach then [BuildRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.BuildRoot.html) should just create the root TreeViewItem (and not the full tree). You will need to add your own delegate to getNewSelectionOverride in order to handle selection changes. Also ensure to override GetAncestors() and GetDescendantsThatHaveChildren() and use the model data to fetch this information, otherwise framing and expanding sub-trees will fail.  
  
When building the rows manually remember to use the search string of the TreeView to filter items.  
  
Additional resources: [BuildRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.BuildRoot.html), [SetupParentsAndChildrenFromDepths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SetupParentsAndChildrenFromDepths.html), [SetupDepthsFromParentsAndChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SetupDepthsFromParentsAndChildren.html), [TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html).
* * *
