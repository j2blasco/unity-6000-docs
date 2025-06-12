* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementExtensions.ChangeCoordinatesTo.html

#  [VisualElementExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementExtensions.html).ChangeCoordinatesTo
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) ChangeCoordinatesTo([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) src, [UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) dest, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) point); 
### Parameters
Parameter | Description  
---|---  
src | The element to use as a reference as the source local space.  
dest | The element to use as a reference as the destination local space.  
point | The point to transform, in the local space of the source element.  
### Returns
**Vector2** A point in the local space of destination element. 
### Description
Transforms a point from the local space of an element to the local space of another element. 
The elements both need to be attached to a panel and must receive a valid [VisualElement.layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-layout.html). Otherwise, this method may return invalid results. 
* * *
## Declaration
public static [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) ChangeCoordinatesTo([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) src, [UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) dest, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect); 
### Parameters
Parameter | Description  
---|---  
src | The element to use as a reference as the source local space.  
dest | The element to use as a reference as the destination local space.  
rect | The rectangle to transform, in the local space of the source element.  
### Returns
**Rect** A rectangle in the local space of destination element. 
### Description
Transforms a rectangle from the local space of an element to the local space of another element. 
The elements both need to be attached to a panel and have received a valid [VisualElement.layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-layout.html). Otherwise, this method may return invalid results. 
* * *
