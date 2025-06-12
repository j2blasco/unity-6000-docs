* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.GetLowestCommonAncestor.html

#  [AccessibilityHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.html).GetLowestCommonAncestor
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
public [Accessibility.AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html) GetLowestCommonAncestor([Accessibility.AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html) firstNode, [Accessibility.AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html) secondNode); 
### Parameters
Parameter | Description  
---|---  
firstNode | The first node to find the lowest common ancestor of.  
secondNode | The second node to find the lowest common ancestor of.  
### Returns
**AccessibilityNode** The lowest common ancestor of the two given nodes, or `null` if there is no common ancestor. 
### Description
Retrieves the lowest common ancestor of two nodes in the hierarchy. The lowest common ancestor is the node that is the common node that both nodes share in their path to the root node of their branch in the hierarchy. 
* * *
