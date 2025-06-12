* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.AlignmentUtils.RoundToPanelPixelSize.html

#  [AlignmentUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.AlignmentUtils.html).RoundToPanelPixelSize
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
public static float RoundToPanelPixelSize([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) ve, float v); 
### Description
Round the value so that it is a whole number of pixels on the target when rendered. 
It will only work on visualElements inside a panel.  
  
Is is used to get dimensions repesenting whole pixels used for layout values, translations or in the generation of the visual Content. It does not consider the transform of the element and its ancestors.   
  
This method uses the scaling from [see cref="VisualElement.scaledPixelsPerPoint"/> and uses the same rounding thresholds as the layout engine. 
* * *
