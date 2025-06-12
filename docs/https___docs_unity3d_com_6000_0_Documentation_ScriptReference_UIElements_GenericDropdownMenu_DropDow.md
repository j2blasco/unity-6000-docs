* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.DropDown.html

#  [GenericDropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.html).DropDown
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
public void DropDown([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) targetElement, bool anchored); 
### Parameters
Parameter | Description  
---|---  
position | The position in the coordinate space of the panel.  
targetElement | The element determines which root to use as the menu's parent.  
anchored | If true, the menu's width matches the width of the `position`; otherwise, the menu expands to the container's full width.  
### Description
Displays the menu at the specified position. 
The parent element that displays the menu: 
  * For Editor UI, the parent element is [EditorWindow.rootVisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-rootVisualElement.html).
  * For runtime UI, the parent element is [UIDocument.rootVisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument-rootVisualElement.html).


The `anchored` parameter determines the width of the menu. Refer to [GenericDropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.html) for example usages. 
* * *
## Declaration
public void DropDown([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) targetElement, bool anchored, bool fitContentWidthIfAnchored); 
### Parameters
Parameter | Description  
---|---  
position | The position in the coordinate space of the panel.  
targetElement | The element determines which root to use as the menu's parent.  
anchored | If true, the menu's width matches the width of the `position`; otherwise, the menu expands to the container's full width.  
fitContentWidthIfAnchored | If true and the menu is anchored, the menu's width matches its content's width; otherwise, the menu's width matches the width of the `position`. If the menu is unanchored, this parameter is ignored.  
### Description
Displays the menu at the specified position. 
The parent element that displays the menu: 
  * For Editor UI, the parent element is [EditorWindow.rootVisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-rootVisualElement.html).
  * For runtime UI, the parent element is [UIDocument.rootVisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument-rootVisualElement.html).


The `anchored` and `fitContentWidthIfAnchored` parameters determine the width of the menu. Refer to [GenericDropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.html) for example usages.  
  

* * *
