* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.CalculateFrameTransform.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [GraphView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.html).CalculateFrameTransform
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
public static void CalculateFrameTransform([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rectToFit, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) clientRect, int border, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) frameTranslation, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) frameScaling); 
### Parameters
Parameter | Description  
---|---  
rectToFit | Rectangle to fit.  
clientRect | Parent rectangle.  
border | Border size.  
frameTranslation | Calculated translation.  
frameScaling | Calculated scaling.  
### Description
Calculate the view transform based on zoom level and the size of the window or parent.
* * *
