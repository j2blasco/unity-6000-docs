* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.Overlaps.html

#  [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html).Overlaps
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
public bool Overlaps([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) other); 
## Declaration
public bool Overlaps([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) other, bool allowInverse); 
### Parameters
Parameter | Description  
---|---  
other | Other rectangle to test overlapping with.  
allowInverse | Does the test allow the widths and heights of the Rects to be negative?  
### Description
Returns true if the other rectangle overlaps this one. If `allowInverse` is present and true, the widths and heights of the Rects are allowed to take negative values (ie, the min value is greater than the max), and the test will still work.
* * *
