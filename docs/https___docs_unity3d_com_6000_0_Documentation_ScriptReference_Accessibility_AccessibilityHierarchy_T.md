* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.TryGetNodeAt.html

#  [AccessibilityHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.html).TryGetNodeAt
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
public bool TryGetNodeAt(float horizontalPosition, float verticalPosition, out [Accessibility.AccessibilityNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html) node); 
### Parameters
Parameter | Description  
---|---  
horizontalPosition | The horizontal position on the screen.  
verticalPosition | The vertical position on the screen.  
node | The node found at that screen position, or `null` if there are no nodes at that position.  
### Returns
**bool** Returns true if a node is found and false otherwise. 
### Description
Tries to retrieve the node at the given position on the screen. 
* * *
