* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.InsertNode.html

#  [AccessibilityHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.html).InsertNode
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
public [Accessibility.AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html) InsertNode(int childIndex, string label, [Accessibility.AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html) parent); 
### Parameters
Parameter | Description  
---|---  
childIndex | A zero-based index for positioning the inserted node in the parent's children list, or in the list of roots if the node is a root node. If the index is invalid, the inserted node will be the last child of its parent (or the last root node).  
label | A label that succinctly describes the accessibility node.  
parent | The parent of the node being added. When the value given is `null`, the created node is placed at the root level.  
### Returns
**AccessibilityNode** The node created and inserted. 
### Description
Creates and inserts a new node with the given label at the given index in this hierarchy under the given parent node. If no parent is provided, the new node is inserted at the given index as a root in the hierarchy. 
* * *
