* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.AddNode.html

#  [AccessibilityHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.html).AddNode
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
public [Accessibility.AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html) AddNode(string label, [Accessibility.AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html) parent); 
### Parameters
Parameter | Description  
---|---  
label | A label that succinctly describes the accessibility node.  
parent | The parent of the node being added. When the value given is `null`, the created node is placed at the root level.  
### Returns
**AccessibilityNode** The node created and added. 
### Description
Creates and adds a new node with the given label in this hierarchy under the given parent node. If no parent is provided, the new node is added as a root in the hierarchy. 
* * *
