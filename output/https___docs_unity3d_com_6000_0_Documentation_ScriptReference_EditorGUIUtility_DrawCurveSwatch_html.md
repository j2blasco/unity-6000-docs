* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.DrawCurveSwatch.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).DrawCurveSwatch
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
public static void DrawCurveSwatch([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) bgColor); 
## Declaration
public static void DrawCurveSwatch([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) bgColor, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) curveRanges); 
### Parameters
Parameter | Description  
---|---  
position | The rectangle to draw the color swatch within.  
curve | The curve to draw.  
property | The curve to draw as a SerializedProperty.  
color | The color to draw the curve with.  
bgColor | The color to draw the background with.  
curveRanges | Optional parameter to specify the range of the curve which should be included in swatch.  
### Description
Draw a curve swatch.
Pass in the curve to draw either with the curve parameter or with the property parameter.
* * *
