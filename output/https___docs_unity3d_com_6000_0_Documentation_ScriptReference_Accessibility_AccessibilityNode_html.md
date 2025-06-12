* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.html

# AccessibilityNode
class in UnityEngine.Accessibility
/
Implemented in:[UnityEngine.AccessibilityModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AccessibilityModule.html)
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
### Description
An instance of a node in the [AccessibilityHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.html), representing an element in the UI that the screen reader can read, focus, and execute actions on. 
### Properties
Property | Description  
---|---  
[allowsDirectInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-allowsDirectInteraction.html) |  Whether this node allows direct touch interaction for users.   
[children](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-children.html) |  The children nodes of the node.   
[frame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-frame.html) |  The Rect represents the position in screen coordinates of the node in the UI. This can be set directly but it is recommended that frameGetter is set instead, so that the value can be recalculated when necessary.   
[frameGetter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-frameGetter.html) |  Optional delegate that can be set to calculate the frame for the node instead of setting a flat value. If the frame of the node may change over time, this delegate should be set instead of giving a one time value for the frame.   
[hint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-hint.html) |  Provides additional information about the accessibility node. For example, the result of performing an action on the node.   
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-id.html) |  The ID of this node.   
[isActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-isActive.html) |  Whether this node is active in the hierarchy. The default value is true.   
[isFocused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-isFocused.html) |  Whether the node is focused by the screen reader.   
[label](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-label.html) |  A string value that succinctly describes this node. The label is the first thing read by the screen reader when a node is focused.   
[parent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-parent.html) |  The parent of the node. If the node is at the root level, the parent value is null.   
[role](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-role.html) |  The role for the node.   
[state](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-state.html) |  The state for the node.   
[value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-value.html) |  The value of this node.   
### Public Methods
Method | Description  
---|---  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.GetHashCode.html) |  A hash used for comparisons.   
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode.ToString.html) |  Provides a debugging string.   
### Events
Event | Description  
---|---  
[decremented](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-decremented.html) |  Called when the user of the screen reader decrements the content of the node.   
[dismissed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-dismissed.html) |  Called when the user of the screen reader dismisses this node.   
[focusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-focusChanged.html) |  Called when the node gains or loses screen reader focus.   
[incremented](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-incremented.html) |  Called when the user of the screen reader increments the content of the node.   
[selected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-selected.html) |  Called when the user of the screen reader selects this node.   
* * *
