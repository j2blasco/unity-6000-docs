* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1.MeasureTextSize.html

#  [TextInputBaseField<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1.html).MeasureTextSize
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
public [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) MeasureTextSize(string textToMeasure, float width, [UIElements.VisualElement.MeasureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.MeasureMode.html) widthMode, float height, [UIElements.VisualElement.MeasureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.MeasureMode.html) heightMode); 
### Parameters
Parameter | Description  
---|---  
textToMeasure | The text to measure.  
width | Suggested width. Can be zero.  
widthMode | Width restrictions.  
height | Suggested height.  
heightMode | Height restrictions.  
### Returns
**Vector2** The horizontal and vertical size needed to display the text string. 
### Description
Computes the size needed to display a text string based on element style values such as font, font-size, and word-wrap. 
* * *
