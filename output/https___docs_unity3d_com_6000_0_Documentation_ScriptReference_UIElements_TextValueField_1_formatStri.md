* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1-formatString.html

#  [TextValueField<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1.html).formatString
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
formatString; 
### Description
The format string used to define how numeric values are displayed. The string follows standard .NET formatting conventions. 
The supported numeric formats string (using `0` as an example) are:   
- `"0.#"`: Displays the numeric value with up to one decimal place, omitting trailing zeros. For example, `3.5` becomes `3.5` and `3.0` becomes `3`.   
-`"0.00"`: Ensures the numeric value is displayed with exactly two decimal places. For example, `3.5` is displayed as `3.50` and `3` as `3.00`.   
-`"0"`: Displays only the integer part of a numeric value, rounding if necessary. For example, `3.5` becomes `4` and `3.0` becomes `3`. 
* * *
